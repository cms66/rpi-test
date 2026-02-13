# Python entry point for main
import os
import python.functions as pf
import python.vars as pv

#bashfile = "/home/multipi/rpi-test/bash/main.sh"

#def run_bash(func):
#	strcmd = "source " + pv.bashfile + "; source_bash; " + func
#	os.system(strcmd)
#	input("Command done, press enter to continue")
	
def main():
	input("Python main start")
	pf.run_bash('show_vars; test_func')
	input("Python main end")

if __name__ == "__main__":
	main()
