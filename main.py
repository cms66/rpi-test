# Python entry point for main
import os

def run_bash(file, func):
	os.system("source /data/current/src/git/rpi-home-pycluster/main.sh; show_vars")
	input("Command done, press enter to continue")
	
def main():
	input("Python main start")
	usrsel = get_selection("Selection from same module: ")
	print("Selection = " + usrsel)
	run_bash(main, show_vars)
	input("Python main end")

if __name__ == "__main__":
	main()
