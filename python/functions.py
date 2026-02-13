# Python functions
def run_bash(func):
	strcmd = "source " + pv.bashfile + "; source_bash; " + func
	os.system(strcmd)
	input("Command done, press enter to continue")
