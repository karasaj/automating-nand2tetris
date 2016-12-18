#!/usr/bin/python
# Test Script Written by Austin Hamilton
# This code is currently licensed under the MIT Software License
# Began with the help of a nice student
# Script for testing the assembler.
# Run it without any arguments to test everything in a predefined list, 
# or pass -f<filename> and, by default, it will expect a .tst file which it will run in the CPUEmulator.

import os
import argparse
import glob
import platform
import sys
from subprocess import call

###########
# GLOBALS #
###########

oper_sys = platform.platform()	# Query the OS to figure out whether we're using Windows or something Unix/Linux based.
								# Only windows needs the .bat, everything else uses .sh

windows = 'windows' in oper_sys.lower()

debug = True

def dprint(input):
	if(debug):
		print(input)

# Current directory.
cwd = os.path.dirname(os.path.realpath(__file__))

hdl_files   = [file for file in glob.iglob(cwd + '/**/projects/**/*.hdl', recursive=True)]
tst_files   = [file for file in glob.iglob(cwd + '/**/projects/**/*.tst', recursive=True)]
batch_files = [file for file in glob.iglob(cwd + '/**/tools/*.bat', recursive=True)]
sh_files    = ['sh ' + file for file in glob.iglob(cwd + '/**/tools/*.sh', recursive=True)]

if(windows):
	emulators = batch_files
else:
	emulators = sh_files

for f in emulators:
	# Duplicate .lower() function call so that we don't butcher the file path
	if('vm' in f.lower()):
		vm_emulator = f
	elif('cpu' in f.lower()):
		cpu_emulator = f
	elif('assembler' in f.lower()):
		assembler = f
	elif('hardware' in f.lower()):
		hardware_sim = f
	elif('jack' in f.lower()):
		jack_cmpiler = f

dprint('VM Emulator: ' + vm_emulator)
dprint('CPU Emulator: ' + cpu_emulator)
dprint('Assembler: ' + assembler)
dprint('Hardware Simulator: ' + hardware_sim)
dprint('Jack Compiler: ' + jack_cmpiler)

print()

print('This is the Nand2Tetris Automated Test Suite. It can be used to test any solutions for' 
	+ 'Nand2Tetris. \nThe projects provided in this repository are tailored to Texas A&M\'s '
	+ 'CSCE 312 class.\n')

prj_sel = False
while (not prj_sel):
	try:
		print('Test Project: ', end='')
		tst_project = int(input())
		if(tst_project <= 0 or tst_project > 8):
			print('Current support for Projects 1 to 8 only.')
		else:
			prj_sel = True
	except ValueError:
		print('Please provide a valid integer input.')

if(windows):
		project = 'projects\\0' + str(tst_project)
	else:
		project = 'projects/0' + str(tst_project)

if(tst_project <= 3): # We will be testing HDL files only
	tst_run = [f for f in tst_files if project in f.lower() ]
	for file in tst_run:
		test_name = file.replace('/', '---').replace('\\','---').split('---')[-1] # Deal with Windows and Linux/Unix Quickly
		print("Testing " + test_name + ': ', end='')
		sys.stdout.flush() # Fixing a weird buffer deal with subprocess calls
		execute = [hardware_sim, file]
		call(execute)
elif(tst_project == 5): # Test of the CPU Emulator
	pass
elif(tst_project == 4 or tst_project == 6): # ASM Projects
	pass
elif(tst_project >= 7): # VM Tests
	pass