import PyPDF2

############
# Function #
############

def extractMotLigne(pdf,motRech):
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfText = ""
    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pdfText += pageObj.extractText()
    textSplit=list(pdfText.split('\n'))
    for i in range(len(textSplit)): 
#        print("valeur de textsplit ", i ,textSplit[i])
        if str(textSplit[i]).strip() == str(motRech).strip() :
            print('mot trouvé !')
            print("valeur associée : ",textSplit[i+1])
            print('done')
            return textSplit[i+1]
    print("Mot introuvable")
    return False

def extractMotColonne(pdf,nbCol,motRech):
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfText = ''
    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pdfText += pageObj.extractText()
    textSplit = list(pdfText.split('\n'))
    for j in range(len(textSplit)):
        if str(textSplit[j]).strip() == str(motRech).strip() : 
            print("mot trouvé !")
            print("valeur associée : ",textSplit[j+int(nbCol)+1])
            print("done")
            return textSplit[j+int(nbCol)+1]
    print("mot introuvable")
    return False   

def findFile(serialNumber):
    repository="/home/wax/Bureau/informatique/pdfTest/"
    pdfRepo="%s%s.pdf" % (repository,serialNumber)
    return pdfRepo

def execLigne():
    print('')
    print("Entrer le nom du pdf que vous voulez examiner : ") #testpdf
    chemin=input()
    if len(chemin)>0: 
        print('')
        print("Entrer le mot à rechercher : ") #Ligne4
        rechercheMot=input()
        if len(rechercheMot)>0:
            print('')
            extractMotLigne(findFile(chemin),rechercheMot)
        else: 
            print("Aucun mot fourni, veuillez rééssayer ! ")
            exit
    else: 
        print("Le nom du pdf est invalide veuillez rééssayer ! ")
        exit

def execColonne(): 
    print('') 
    print("Entrer le nom du pdf que vous voulez examiner : ") #testpdf
    chemin=input()
    if len(chemin)>0: 
        print('')
        print("Entrer le nombre de colonne : ")
        nbCol=input()
        if len(nbCol)>0:
            print('')
            print("Entrer le mot à rechercher")
            motRech=input()
            if len(motRech)>0 : 
                print('')
                extractMotColonne(findFile(chemin), nbCol, motRech)
            else : 
                print("le mot recherché est invalide ! ")
                exit
        else : 
            print("le nombre de colonne est invalide ! ")
            exit
    else : 
        print("le nom du pdf est invalide veuillez rééssayer ! ")



########
# Main #
########
  
if __name__ == '__main__': 
    print("Entrer le type de pdf : colonne / ligne ")
    type=input()
    if type == "colonne" :
        execColonne()
    else : 
        execLigne()