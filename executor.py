import cv2
import os

from ner import NerUtils
from ocr import Ocr_Utils
from excel_sheet_add import Excel_Utils



class MainExecutor:

    def __init__(self):
        self.ocr_util = Ocr_Utils()
        self.title = ""
        self.author= ""
        self.pub = ""
        self.isbn = ""

    # in case of directory, get all images from the directory
    def load_images_from_folder(self, folder):
        images = []
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder,filename))
            if img is not None:
                images.append(img)
        return images

    # function to obtain all relevant meta data from the book cover
    def book_cover_extraction(self, isdir, image_name):

        # check if directory needs to be processed
        if (isdir == 1):

            # for all images in the directory
            for image in self.load_images_from_folder(image_name):

                # empty the list
                self.ocr_util.newlist = []

                # get the extracted text
                text = self.ocr_util.run_tesseract(image)

                # show all the extracted text
                print("All text recognised: \n" , text)

                # run spacy to get author and publisher
                df = NerUtils.nerSpacy(text)

                # NerUtils.ner_nltk(text)

                # process authors obtained form nlp
                df1 = df[df['Labels'].isin(['PERSON'])]
                authors = ""
                for x in set(df1['Entities']):
                    # print(self.ocr_util.getTitle().upper().strip(), " ", x)
                    if x.strip() == self.ocr_util.getTitle().upper().strip():
                        continue
                    y = ""
                    for char in x:
                        if (char.isalpha() or char == ' '):
                            y = y+char
                    authors = authors + y + ", "

                # process publishers obtained from nlp
                df2 = df[df['Labels'].isin(['ORG'])]
                pubs=""
                for x in set(df2['Entities']):
                    # print(self.ocr_util.getTitle().upper().strip(), " ", x)
                    if x.strip() == self.ocr_util.getTitle().upper().strip():
                        continue
                    if x.strip() == "ISBN":
                        continue
                    if (self.ocr_util.dict[x.strip().lower()] <= 60):
                            continue
                    pubs = pubs + x + ", "

                names = set(df['Entities'])

                publishers = set(df2['Entities'])

                print("Author: ", authors)

                print("ISBN : ", self.ocr_util.getISBN(text))

                # make a dict to add to excel file
                fields = {
                    "name": image_name,
                    "title": self.ocr_util.getTitle(),
                    "author": authors,
                    "ISBN": self.ocr_util.getISBN(text),
                    "Publisher": pubs,
                }

                self.title = self.title + self.ocr_util.getTitle() + " "
                self.author = self.author + authors + " "
                self.isbn = self.isbn + self.ocr_util.getISBN(text) + " "
                self.pub = self.pub + pubs

                print("Title: ", self.ocr_util.getTitle())

                print("Publishers: ", pubs)

                # add to excel file
                Excel_Utils.saveWorkSpace(fields)
            
            print(self.title)
            print(self.author)
            print(self.pub)
            print(self.isbn)


        else:

            # read the image
            image = cv2.imread(image_name)

            # run pytesseract to get the extracted text
            text = self.ocr_util.run_tesseract(image)

            print("All text recognised: \n" , text)

            # run spacy to get authors and publishers
            df = NerUtils.nerSpacy(text)

            # NerUtils.ner_nltk(text)

            # process the authors obtained
            df1 = df[df['Labels'].isin(['PERSON'])]
            authors = ""
            for x in set(df1['Entities']):
                # print(self.ocr_util.getTitle().upper().strip(), " ", x)
                if x.strip() == self.ocr_util.getTitle().upper().strip():
                    continue
                y = ""
                for char in x:
                    if (char.isalpha() or char == ' '):
                        y = y+char
                authors = authors + y + ", "

            # process the publishers obtained
            df2 = df[df['Labels'].isin(['ORG'])]
            pubs=""
            for x in set(df2['Entities']):
                # print(self.ocr_util.getTitle().upper().strip(), " ", x)
                if x.strip() == self.ocr_util.getTitle().upper().strip():
                    continue
                if x.strip() == "ISBN":
                    continue
                if (x.strip().lower() in self.ocr_util.dict and self.ocr_util.dict[x.strip().lower()] <= 60):
                        continue
                pubs = pubs + x + ", "

            names = set(df['Entities'])

            publishers = set(df2['Entities'])

            print("Author: ", authors)

            print("ISBN : ", self.ocr_util.getISBN(text))

            # make a dict to add to excel sheet
            fields = {
                "name": image_name,
                "title": self.ocr_util.getTitle(),
                "author": authors,
                "ISBN": self.ocr_util.getISBN(text),
                "Publisher": pubs,
            }

            self.title = self.title + self.ocr_util.getTitle() + " "
            self.author = self.author + authors + " "
            self.isbn = self.isbn + self.ocr_util.getISBN(text) + " "
            self.pub = self.pub + pubs

            print("Title: ", self.ocr_util.getTitle())

            print("Publishers: ", pubs)

            # add to excel file
            Excel_Utils.saveWorkSpace(fields)