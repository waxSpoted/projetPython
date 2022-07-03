import PyPDF2

############
# Function #
############

def extractMot(pdf,motRech):
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfText = ""
    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pdfText += pageObj.extractText()
    textSplit=list(pdfText.split('\n'))
    print("text split : ", textSplit)
    for phrase in textSplit :
        if phrase.startswith(motRech) : 
            print("Phrase trouvée")
            print("Phrase:",phrase)    
            return phrase
        else : 
            print("La phrase est : ",phrase)
    print("Mot introuvable")
    print("fin")


def findFile(serialNumber):
    repository="/home/wax/Bureau/pdfTest/"
    pdfRepo="%s%s.pdf" % (repository,serialNumber)
    return pdfRepo


########
# Main #
########

if __name__ == '__main__': 
    print("Entrer le nom du pdf que vous voulez examiner : ") #testpdf
    chemin=input()
    if len(chemin)>0: 
        print("Entrer le mot à rechercher : ") #Ligne4
        rechercheMot=input()
        if len(rechercheMot)>0:
            extractMot(findFile(chemin),rechercheMot)
        else: 
            print("Aucun mot fourni, veuillez rééssayer ! ")
            exit
    else: 
        print("Le nom du pdf est invalide veuillez rééssayer ! ")
        exit
     
