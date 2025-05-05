# README

---

## 1. What does this program do

This program extracts metadata from book‑cover images. It accepts a path (file or directory) and then:

- Runs OCR to detect all text on each cover.  
- Identifies:
  - **Title** (text box with the greatest height)  
  - **Authors** (named entities labeled PERSON)  
  - **Publishers** (named entities labeled ORG)  
  - **ISBN numbers** (strings following the keyword “ISBN”)  
- Writes the extracted information into an Excel sheet.

---

## 2. How it works (logic)

1. **Input**  
   - Read command‑line flags:  
     - `--image <path>` (file or directory)  
     - `--isdir <0|1>` (0 = single image; 1 = process all images in directory)  

2. **Preprocessing**  
   - Convert each image to grayscale.

3. **OCR**  
   - Use `pytesseract` to extract all text boxes and their bounding‑box heights.

4. **Title extraction**  
   - Select the detected text with the maximum box height.

5. **Entity recognition**  
   - Use spaCy to detect named entities:  
     - Label **PERSON** → Authors  
     - Label **ORG** → Publishers  

6. **ISBN extraction**  
   - Search the OCR text for the keyword “ISBN”  
   - Capture the subsequent sequence of digits and dashes.

7. **Output**  
   - Append one row per cover to an Excel file, with columns:  
     `Title | Authors | Publishers | ISBN`

---

## 3. How to compile & run

```bash
# Run on a single image:
python runner.py --image book2.png --isdir 0

# Process all images in a directory:
python runner.py --image path/to/dir --isdir 1

# Run unit tests:
pytest test_executor.py -p no:warnings

# Generate coverage report:
coverage run -m --omit=config.py pytest test_executor.py -p no:warnings
coverage report -m --omit=config-3.8.py
```


## Coverage:
(ve3) keshav@keshav-Lenovo-ideapad:~/Desktop/SE_assign3$ coverage report -m --omit=config-3.8.py
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
excel_sheet_add.py      16      0   100%
executor.py             98      2    98%   70, 146
ner.py                  22      0   100%
ocr.py                  69      8    88%   53, 69, 85-90
test_executor.py        14      0   100%
--------------------------------------------------
TOTAL                  219     10    95%

Note: 
To run the program, the following things need to be installed (some of the following are not needed):
attrs==21.4.0
blis==0.4.1
cachetools==5.0.0
catalogue==1.0.0
certifi==2020.6.20
chardet==3.0.4
charset-normalizer==2.0.12
click==7.1.2
coverage==6.3.2
cycler==0.10.0
cymem==2.0.3
Cython==0.29.28
easyocr==1.4.2
en-core-web-lg @ https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-2.3.0/en_core_web_lg-2.3.0.tar.gz
en-core-web-md @ https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.3.0/en_core_web_md-2.3.0.tar.gz
en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.0/en_core_web_sm-2.3.0.tar.gz
google-api-core==2.7.2
google-api-python-client==2.44.0
google-auth==2.6.4
google-auth-httplib2==0.1.0
google-auth-oauthlib==0.5.1
google-spreadsheet==0.0.6
googleapis-common-protos==1.56.0
httplib2==0.20.4
idna==2.10
imageio==2.16.2
importlib-metadata==1.7.0
imutils==0.5.3
iniconfig==1.1.1
joblib==0.16.0
kiwisolver==1.2.0
matplotlib==3.2.2
murmurhash==1.0.2
networkx==2.8
nltk==3.6.3
numpy==1.22.3
oauth2client==4.1.3
oauthlib==3.2.0
opencv-python==4.5.5.64
opencv-python-headless==4.5.4.60
packaging==21.3
pandas==1.0.5
Pillow==9.1.0
plac==1.1.3
pluggy==1.0.0
preshed==3.0.2
protobuf==3.20.0
py==1.11.0
pyasn1==0.4.8
pyasn1-modules==0.2.8
pyparsing==2.4.7
pytesseract==0.3.4
pytest==7.1.1
python-bidi==0.4.2
python-dateutil==2.8.1
pytz==2020.1
PyWavelets==1.3.0
PyYAML==6.0
regex==2020.6.8
requests==2.27.1
requests-oauthlib==1.3.1
rsa==4.8
scikit-image==0.19.2
scipy==1.8.0
six==1.15.0
spacy==2.3.0
srsly==1.0.2
tesseract==0.1.3
tesseract-ocr==0.0.1
tesserocr==2.5.2
thinc==7.4.1
tifffile==2022.4.8
tomli==2.0.1
torch==1.11.0
torchvision==0.12.0
tqdm==4.47.0
typing_extensions==4.1.1
uritemplate==4.1.1
urllib3==1.26.5
wasabi==0.7.0
wincertstore==0.2
xlrd==2.0.1
xlutils==2.0.0
xlwt==1.3.0
zipp==3.1.0

4. Provide a snapshot of a sample run
(ve3) keshav@keshav-Lenovo-ideapad:~/Desktop/SE_assign3$ python runner.py --image book2.png --isdir 0
Starting...
<class 'str'>
All text recognised: 
 ——
Clean Code

A Handbook of Agile Software Craftsmanship

 

Robert C. Martin

e et ee
2.3.0
                                     Entities       Labels  Position_Start  Position_End
0                                  CLEAN CODE          LAW               3            13
1  A HANDBOOK OF AGILE SOFTWARE CRAFTSMANSHIP  WORK_OF_ART              15            57
2                            ROBERT C. MARTIN       PERSON              62            78
Author:  ROBERT C MARTIN, 
ISBN :  
Title:   Clean Code
Publishers:  
Wrote tester1.xls
