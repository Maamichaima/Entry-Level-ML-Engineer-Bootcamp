import sys #est un module (function & variable) qui interagir avec l'interpréteur Python et le système d’exploitation

argv = sys.argv

for i in range(1, argv.__len__()):
	result = argv[i].swapcase()
	print (result)