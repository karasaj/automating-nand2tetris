#!/usr/bin/python
# Test Script Written by Austin Hamilton
# This code is currently licensed under the MIT Software License provided in this repository.
# Began with the help of a nice student

import os
import glob
import platform
import sys
from subprocess import call

oper_sys = platform.platform()	# Query the OS to figure out whether we're using Windows or something Unix/Linux based.
								# Only windows needs the .bat, everything else uses .sh

windows = 'windows' in oper_sys.lower()

debug = True

def dprint(input):
	if(debug):
		print(input)

# Current directory.
cwd = os.path.dirname(os.path.realpath(__file__))

hdl_files   = [file for file in glob.iglob('{path}/**/projects/**/*.hdl'.format(path=cwd), recursive=True)]
tst_files   = [file for file in glob.iglob('{path}/**/projects/**/*.tst'.format(path=cwd), recursive=True)]
batch_files = [file for file in glob.iglob('{path}/**/tools/*.bat'.format(path=cwd), recursive=True)]
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
end = False

while(not end):
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
		project = 'projects\\0{}'.format(str(tst_project))
	else:
		project = 'projects/0{}'.format(str(tst_project))
	
	tst_run = [f for f in tst_files if project in f.lower() ]

	if(tst_project <= 3 or tst_project == 5): # We will be testing HDL files
		for file in tst_run:
			test_file = file.replace('/', '---').replace('\\','---').split('---')[-1] # Deal with Windows and Linux/Unix Quickly
			print("Testing " + test_file + ': ', end='')
			sys.stdout.flush() # Fixing a weird buffer deal with subprocess calls
			execute = [hardware_sim, file]
			call(execute)
	elif(tst_project == 4 or tst_project == 6): # ASM Projects
		for file in tst_run:
			asm_file = file.replace('tst','asm')
			execute = [assembler, asm_file] # Need to Assemble into a Hack file
			call(execute)
			sys.stdout.flush()
			test_file = file.replace('/', '---').replace('\\','---').split('---')[-1] # Deal with Windows and Linux/Unix Quickly
			print("Testing " + test_file + ': ', end='')
			sys.stdout.flush() # Fixing a weird buffer deal with subprocess calls
			execute = [cpu_emulator, file]
			call(execute)
	elif(tst_project >= 7): # VM Tests
		pass

	print('Project Testing complete. Do you need to test another project? (y/n): ', end='')
	prompt = input().lower()
	while(prompt != 'y' and prompt != 'n'):
		print('Invalid. (y/n): ', end='')
		prompt = input().lower()
	end = (prompt != 'y')
	prj_sel = False

