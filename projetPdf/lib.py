import PyPDF2
import os

def askUser():
    ligne = True

    print("Entrer le type de pdf (colonne ou ligne) : ", end = "")
    type=input()
    if type == "colonne" :
        ligne = False

    print("\nEntrer le nom du pdf que vous voulez examiner : ", end = "") #testpdf
    nomPdf=input()
    if len(nomPdf) == 0: 
        raise Exception("Nom de pdf invalide")

    print("\nEntrer le mot à rechercher : ", end = "") #Ligne4
    rechercheMot = input()
    if len(rechercheMot) == 0:
        raise Exception("Aucun mot fourni, veuillez rééssayer ! ")

    return ligne, nomPdf, rechercheMot

def findFile(serialNumber):
    dossier = os.getcwd()
    pdfRepo="%s/ressources/%s.pdf" % (dossier, serialNumber)
    return pdfRepo

def _extractText(pdf):

    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfText = ""

    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pdfText += pageObj.extract_text()
    textSplit=list(pdfText.split('\n'))

    # rangement du texte dans une liste 2 dimensions (lignes et mots)
    textOrdered = [[]]
    for word in textSplit:
        stripped = word.strip()
        if stripped != '':
            textOrdered[-1].append(stripped)
        else:
            textOrdered.append([])

    return textOrdered

def extractMotLigne(pdf,motRech):
    textSplit = _extractText(pdf)

    for i in range(len(textSplit)): 
        for j in range(len(textSplit[i])):
            if str(textSplit[i][j]).strip() == str(motRech).strip() :
#               print("valeur associée : ",textSplit[i+1])
                return textSplit[i][j+1]

    print("Mot introuvable")
    return None

def extractMotColonne(pdf, motRech):
    textSplit = _extractText(pdf)

    for i in range(len(textSplit)):
        for j in range(len(textSplit[i])):
            if str(textSplit[i][j]).strip() == str(motRech).strip() : 
#               print("valeur associée : ",textSplit[j+int(nbCol)+1])
                return textSplit[i+1][j]

    print("mot introuvable")
    return None 