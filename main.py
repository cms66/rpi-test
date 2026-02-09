# Python entry point for main

def get_selection(prompt):
	usropt = input(prompt)
	
def main():
	input("Python main start")
	usrsel = get_selection("Test prompt")
	print("Selection = " + usrsel)
	input("Python main end")

if __name__ == "__main__":
	main()
