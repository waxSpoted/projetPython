import PyPDF2

############
# Function #
############

def extractText(pdf):
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfText = ""
    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pdfText += pageObj.extractText().replace('\n','')
    print(pdfText)
    return pdfText

def recupText(text,motRech):
    textSplit=list(text.split())
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

textExtrait=extractText('testpdf.pdf')
recupText(textExtrait,"Ligne4")