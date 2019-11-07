#import vimonous.vimonous as vv
from vimonous import Vimonous as v

if __name__=="__main__":
	parser=v("filetoparse.txt")

	parser.add("Gddodeleted text at bottom, added this line")
	parser.run()

	#code could also be written as follows:
	# parser + "Gddodeleted text at bottom, added this line"
	# parser()
