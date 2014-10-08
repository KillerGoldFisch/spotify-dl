#!/usr/bin/env python

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def header(txt):
    print(bcolors.HEADER + txt + bcolors.ENDC)

def okblue(txt):
    print(bcolors.OKBLUE + txt + bcolors.ENDC)

def okgreen(txt):
    print(bcolors.OKGREEN + txt + bcolors.ENDC)

def warning(txt):
    print(bcolors.WARNING + txt + bcolors.ENDC)

def fail(txt):
    print(bcolors.FAIL + txt + bcolors.ENDC)