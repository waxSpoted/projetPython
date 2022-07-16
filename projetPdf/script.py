import lib

#########################################
# Le type colonne est le pdf 654321.pdf #
# Le type ligne est le pdf 123456.pdf   #
#########################################
  
if __name__ == '__main__': 

    ligne, nomPdf, rechercheMot = lib.askUser()

    pdf = lib.findFile(nomPdf)
    if ligne:
        res = lib.extractMotLigne(pdf, rechercheMot)
    else:
        res = lib.extractMotColonne(pdf, rechercheMot)

    if res is not None:
        print("le resultat est : ", res )