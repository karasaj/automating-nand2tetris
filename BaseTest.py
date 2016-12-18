#!/usr/bin/python

# Began with the help of a nice student
# Script for testing the assembler.
# Run it without any arguments to test everything in a predefined list, 
# or pass -f<filename> and, by default, it will expect a .tst file which it will run in the CPUEmulator.

import os
import argparse
import glob
import platform

###########
# GLOBALS #
###########

oper_sys = platform.platform()

windows = 'windows' in oper_sys.lower()

# Current directory.
cwd = os.path.dirname(os.path.realpath(__file__))

print('Hello');

hdl_files   = [file for file in glob.iglob(cwd + '/**/projects/**/*.hdl', recursive=True)]
tst_files   = [file for file in glob.iglob(cwd + '/**/projects/**/*.tst', recursive=True)]
batch_files = [file for file in glob.iglob(cwd + '/**/tools/*.bat')]
sh_files    = [file for file in glob.iglob(cwd + '/**/tools/*.sh')]

vm_emulator  = ''
cpu_emulator = ''
assembler    = ''
hardware_sim = ''
jack_cmpiler = ''

for f in tst_files:
	if('VM' in f):
		vm_emulator = f
	else if('CPU' in f):
		cpu_emulator = f
	else if('Assembler' in f):
		assembler = f
	else if('Hardware' in f):
		hardware_sim = f
	else if('Jack' in f):
		jack_cmpiler = f




########################
# COMMAND LINE OPTIONS #
########################

# Configure command line options.
# http://stackoverflow.com/a/7427376/5415895

parser = argparse.ArgumentParser(description='Test the virtual machine.')
parser.add_argument('-f','--filename', help='The file to translate. If none is given, every file in the tests list will be tested.', required=False)
parser.add_argument('-v','--vm_dir', help='Directory for vm emulator.', required=False)
parser.add_argument('-c','--cpu_dir', help='Directory for cpu emulator.', required=False)
args = vars(parser.parse_args())


###################
# PARSE ARGUMENTS #
###################

# file = args['filename']

# if args['vm_dir']:
# 	vm_emulator = args['vm_dir']
# if args['cpu_dir']:
# 	cpu_emulator = args['cpu_dir']

# if args['filename']:
# 	# Run test scripts.
# 	else:
# 		print("Testing " + file + " with the CPUEmulator.")
# 		os.system("bash " + cpu_emulator + " " + file)
# else:
# 	for test in tests:
# 		print("Testing " + test + " with the CPUEmulator.")
# 		os.system('bash ' + cpu_emulator + " " + test)
# 		print("\n")
