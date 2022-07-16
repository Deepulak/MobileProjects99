import os

def script_directory():
	return os.path.dirname(os.path.realpath(__file__))

def current_directory():
	return os.getcwd()

if __name__ == "__main__":
	print("Script Directory: " + script_directory())
	print("Current Directory: " + current_directory())