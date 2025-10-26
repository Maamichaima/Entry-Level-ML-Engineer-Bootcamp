import sys

if(sys.argv.__len__() > 2):
	print("AssertionError: argument is not an integer")
	sys.exit(1)

try:
	argv = int(sys.argv[1])
	if (argv == 0):
		print("I'm Zero.")
	elif (argv % 2 == 0):
		print("I'm Even.")
	else:
		print("I'm Old.")
except:
	print("AssertionError: more than one argument is provided");