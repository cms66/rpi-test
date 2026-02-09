# Python entry point for main
import os

def run_bash(file, func):
	bashfile = os.path.dirname(__file__) + "/bash/" + file + ".sh"
	cmd = "source " + bashfile + "; " + func
	os.system(cmd)
	input("Command done, press enter to continue")

def get_selection(prompt):
	usropt = input(prompt)
	return usropt
	
def main():
	input("Python main start")
	usrsel = get_selection("Test prompt: ")
	print("Selection = " + usrsel)
	run_bash(main, show_vars)
	input("Python main end")

if __name__ == "__main__":
	main()
