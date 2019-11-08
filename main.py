from vimonous import Vimonous as v
import sys

#main.py is mainly for use in scripts

HELP_MSG="""Vimonous -> github.com/dosisod/vimonous

Usage: main.py FILENAME "normal mode commands"

FILENAME is automatically saved after commands are typed"""

if __name__=="__main__":
	if len(sys.argv)>1:	
		parser=v(
			sys.argv[1], #file name for file
			" ".join(sys.argv[2:]) #data to put into file
		)

	else:
		print(HELP_MSG)
