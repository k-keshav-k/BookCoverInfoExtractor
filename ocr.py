import cv2

import pytesseract
import cv2

class Ocr_Utils:

    # initialize variables
    def __init__(self):
        self.newlist = []
        self.publisher_list = ['pearson', 'wiley', 'penguin']
        self.dict = {}

    # run pytesseract to get the extracted text
    def run_tesseract(self, image) :
    
        # convert the image to gray scale for better results
        gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_filtered = cv2.inRange(gray, 0, 70)

        # cv2.imshow('image', gray)
        # cv2.waitKey(0)

        # get the extracted string
        data = pytesseract.image_to_string(gray, lang='eng')
        print(type(pytesseract.image_to_data(gray)))

        newdata = ""

        # make a dictionary to store confidence level for each detected text
        for x in pytesseract.image_to_data(gray).splitlines():
            y = x.split('\t')
            if (y[9] == 'height'):
                continue
            if (len(y) < 12):
                continue
            self.dict[y[11].strip().lower()] = int(y[10])

        # print("Newdata ==> \n",self.dict, "\n<==")

        # make a list of all those strings that have high confidence level
        for x in pytesseract.image_to_data(gray).splitlines():
            # print("Y ==> ",y)
            y = x.split('\t')
            # print("Y ==> ",y, " ", len(y))
            if (y[9] == 'height'):
                continue
            if (len(y) < 12):
                continue
            if (y[11].strip() == ''):
                continue
            if ('|' in y[11].strip()):
                continue
            if (int(y[10]) <= 80):
                continue
            self.newlist.append([y[9], y[11].strip()])

        # print("NewList ==> \n", self.newlist)

        # print(pytesseract.image_to_data(gray))

        # print("====Tesseract data=====")
        # print(data)

        return data

    # function to check if a string has numbers
    def has_numbers(self, inputString):
        return any(char.isdigit() for char in inputString)

    # function to check if a string has a '-'
    def has_dash(self, inputString):
        return any(char == '-' for char in inputString)

    # function to get ISBN for the book
    def getISBN(self, text):
        for x in text.splitlines( ):
            if 'ISBN' in x:
                ans = ""
                for char in x:
                    if (char.isdigit() == True or char == '-'):
                        ans = ans + char
                return ans
            elif self.has_dash(x) == True and self.has_numbers(x) == True:
                ans = ""
                for char in x:
                    if (char.isdigit() == True or char == '-'):
                        ans = ans + char
                return ans
        return ''

    # get max box height
    def getMaxHeight(self):
        maxH = 0
        for x in self.newlist:
            if (int(x[0]) > maxH):
                maxH = int(x[0])
        return maxH

    # get the title for the book
    def getTitle(self):
        title = ""
        maxH = self.getMaxHeight()
        check = False
        for x in self.newlist:
            if (abs(int(x[0]) - maxH) <= 15 ):
                title = title + " " + x[1]
                check = True
        return title

    # def getPublisher(self, text):
    #     publish = ""
    #     for x in text.splitlines( ):
    #         for y in x.split(' '):
    #             if y.strip().lower() in self.publisher_list:
    #                 publish = publish + y.strip() + ", "
    #     # print("Publishers are: ", publish)
    #     return publish
    