#!/usr/bin/python

# Began with the help of a nice student
# Script for testing the assembler.
# Run it without any arguments to test everything in a predefined list, 
# or pass -f<filename> and, by default, it will expect a .tst file which it will run in the CPUEmulator.

import os
import argparse


###########
# GLOBALS #
###########

# List of test scripts for the CPUEmulator.
tests = {
	
}
# Current directory.
cwd = os.path.dirname(os.path.realpath(__file__))
# Paths to virtual machine emulator and cpu emulator, respectively.
# Obviously, this path will be different on different machines.
vm_emulator = ''
cpu_emulator = ''


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

file = args['filename']

if args['vm_dir']:
	vm_emulator = args['vm_dir']
if args['cpu_dir']:
	cpu_emulator = args['cpu_dir']

if args['filename']:
	# Run test scripts.
	else:
		print("Testing " + file + " with the CPUEmulator.")
		os.system("bash " + cpu_emulator + " " + file)
else:
	for test in tests:
		print("Testing " + test + " with the CPUEmulator.")
		os.system('bash ' + cpu_emulator + " " + test)
		print("\n")
