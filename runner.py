# import argparse to parse the arguments
import argparse

# main executor is responsible for executing ocr
from executor import MainExecutor

# get the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
	help="path to input image")
ap.add_argument("-d", "--isdir", type=int,
help = "ath to input dir")

args = vars(ap.parse_args())

# print(args["image"])
# print(args["isdir"])

# check if correct parameters are given are not
if (('.jpg' in args["image"]) or ('.jpeg' in args["image"]) or ('.png' in args["image"])):
	if (args["isdir"] == 1):
		print("Please enter correct parameters")
		exit(0)

if (('.jpg' not in args["image"]) and ('.jpeg' not in args["image"]) and ('.png' not in args["image"])):
	if (args["isdir"] == 0):
		print("Please enter correct parameters")
		exit(0)


print('Starting...')
mainexe = MainExecutor()

# main executor is called
mainexe.book_cover_extraction(args["isdir"], args["image"])