from vimonous import Vimonous as v

if __name__=="__main__":
	parser=v("filetoparse.txt")

	parser.add("Gddodeleted text at bottom, added this line")
	parser.run()

	exit(0) #stops from below code from running

	#code could also be written as follows:
	parser=v("filetoparse.txt")
	parser + "Gddodeleted text at bottom, added this line 1"
	parser()

	#or like:
	v("filetoparse.txt", "Gddodeleted text at bottom, added this line")
