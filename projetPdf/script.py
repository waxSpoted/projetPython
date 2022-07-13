import PyPDF2

#################################################
# Fonctionne avec la mise en page de 123456.pdf #
#################################################

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
#    print("text split : ", textSplit)
#    print("première val de text split : ", textSplit[1])
#    print("longueur de split : ", len(textSplit))

    for i in range(len(textSplit)): 
#        print("valeur de textsplit ", i ,textSplit[i])
        if str(textSplit[i]).strip() == str(motRech).strip() :
            print("%s : %s" % (motRech,textSplit[i+1]))
            return textSplit[i+1]
    print("Mot introuvable")
    return False

def findFile(serialNumber):
    repository="/home/wax/Bureau/Informatique/pdfTest/"
    pdfRepo="%s%s.pdf" % (repository,serialNumber)
    return pdfRepo

def findVal (phraseExtraite): 
    listPhrase=list(phraseExtraite)
    for mot in listPhrase : 
        if mot == "test":
            return True


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
     
