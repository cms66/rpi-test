# Python entry point for main
import os
import python.functions as pf
import python.vars as pv
	
def main():
	input("Python main start")
	pf.run_bash('show_vars; test_func')
	input("Python main end")

if __name__ == "__main__":
	main()
