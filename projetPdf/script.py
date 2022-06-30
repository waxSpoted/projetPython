import PyPDF2

import os
 
from fnmatch import filter
 

############
# Function #
############

def extractMot(pdf,motRech):
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfText = ""
    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pdfText += pageObj.extractText().replace('\n','')
    textSplit=list(pdfText.split())
    for mot in textSplit :
        if mot == motRech : 
            print("Mot trouvé")
            print("Mot: ",mot)    
            return mot
    print("Mot introuvable")
    print("fin")

########
# Main #
########

repTest='/home/wax/Bureau/testpdf.pdf'

extractMot(repTest,'Ligne4')