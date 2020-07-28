#Scrivere un programma che gestisca i pdf
#Versione 1.3

import PyPDF2
import os
import shutil

#----------------  OGGETTI  CON VALORE DI RITORNO LE FOLDERS ---------------- 

cartellainputmerge = os.path.join(os.getcwd(), "inputfile/daunire/")
cartellainputsplit = os.path.join(os.getcwd(), 'inputfile/dadividere/')

cartellaoutputmerge = os.path.join(os.getcwd(), 'outputfile/uniti/')
cartellaoutputsplit = os.path.join(os.getcwd(),'outputfile/divisi/')

cartellainputselect = os.path.join(os.getcwd(), "inputfile/daselezionare/")
cartellaoutputselect = os.path.join(os.getcwd(),'outputfile/selezionati/')

#----------------  OGGETTI  CON VALORE DI RITORNO LE FOLDERS ---------------- 

#-------------------------------------- FUNZIONI --------------------------------------

def controllodir():

        if not os.path.exists(cartellainputmerge):
            os.makedirs(cartellainputmerge)

        if not os.path.exists(cartellaoutputmerge):
            os.makedirs(cartellaoutputmerge)

        if not os.path.exists(cartellainputsplit):
            os.makedirs(cartellainputsplit)

        if not os.path.exists(cartellaoutputsplit):
            os.makedirs(cartellaoutputsplit)

        if not os.path.exists(cartellainputselect):
            os.makedirs(cartellainputselect)

        if not os.path.exists(cartellaoutputselect):
            os.makedirs(cartellaoutputselect)


def unionepdf(nomefiles):
        listafiles = os.listdir("./inputfile/daunire/")
        print(listafiles)
        pdfoutput = open((cartellaoutputmerge + nomefiles),"wb")
        merger = PyPDF2.PdfFileMerger()

        for nomeFile in listafiles:
            if nomeFile.endswith(".pdf"):
                PdfFile = open((cartellainputmerge + nomeFile),"rb")
                readerPDF = PyPDF2.PdfFileReader(PdfFile)
                print(f"Lettura del file:  {nomeFile}")
                merger.append(readerPDF)
                PdfFile.close()
        print(f"Scrittura del file:   {nomefiles}   \n")
        merger.write(pdfoutput)
        merger.close()
        
        print("Unione completata con successo!")

def  divisionepdf():
    listafiles = os.listdir("./inputfile/dadividere/")
    print(listafiles)
    for nomeFile in listafiles:
        if nomeFile.endswith(".pdf"):
            filebase = nomeFile.replace(".pdf","")
            letturapdf = PyPDF2.PdfFileReader((cartellainputsplit + nomeFile))
            for numeropagine in range(letturapdf.numPages):
                writer = PyPDF2.PdfFileWriter()
                writer.addPage(letturapdf.getPage(numeropagine))
                if not os.path.exists(cartellaoutputsplit + filebase):
                    print(f"Creazione della cartella: {(filebase)} \n")
                    os.makedirs(cartellaoutputsplit + filebase)
                with open(os.path.join(cartellaoutputsplit + filebase, "{0}_Pagina{1}.pdf".format(filebase,numeropagine + 1)),'wb') as f:
                    print("Scrittura del file: " + "{0}_Pagina{1}.pdf".format(filebase,numeropagine + 1) + " in corso...")
                    writer.write(f)
                    f.close()
    print("Divisione PDF completata con successo!!!")

def  estraipdf(filedestinazione):
    listafiles = os.listdir("./inputfile/daselezionare/")
    for nomeFile in listafiles:
        print(listafiles)
        filebase = nomeFile.replace(".pdf" , "")
        print("Per uscire scrivere esci()")
        nomepdf = str(input("Selezionare il pdf dalla lista:  "))
        if nomepdf == 'esci()' or nomepdf == "ESCI()":
            break
        leggipdf = PyPDF2.PdfFileReader(cartellainputselect + nomepdf)
        quantita = int(input(f"Quante pagine vorresti estrarre <{leggipdf.numPages}? "))
        x = 0
        for numeropagine in range(quantita):
            numeropag = int(input("Scrivi ial numero della pagina: "))
            writer = PyPDF2.PdfFileWriter()
            writer.addPage(leggipdf.getPage(numeropag - 1))
            if not os.path.exists(cartellaoutputselect + filebase):
                os.makedirs(cartellaoutputselect + filebase)
            with open(os.path.join(cartellaoutputselect + filebase,"{0}_Pagina{1}.pdf".format(filebase,numeropag)), "wb") as f:
                writer.write(f)
                f.close
                x +=1

            if not os.path.exists(cartellaoutputselect + filebase + "/uniti/"):
                os.makedirs(cartellaoutputselect + filebase + "/uniti/")
            listafiles2 = os.listdir(cartellaoutputselect + filebase)
            print(listafiles2)
            pdfoutput = open((cartellaoutputselect + filebase + "/uniti/" + filedestinazione),"wb")
            merger = PyPDF2.PdfFileMerger()
            for nomeFile2 in listafiles2:
                if nomeFile2.endswith(".pdf"):
                    pdfFile = open((cartellaoutputselect + filebase + "/" + nomeFile2 ),"rb")
                    readerPDF = PyPDF2.PdfFileReader(pdfFile)
                    print(f"Lettura del file:  {nomeFile2}")
                    merger.append(readerPDF)
                    pdfFile.close()
            print(f"Scrittura del file:   {filedestinazione}   \n")
            merger.write(pdfoutput)
            merger.close()
            print("Unione completata con successo!")
        if x == quantita:
            ciclo = input("Vuoi continuare (y or n)? ")
            if ciclo == "y" or ciclo == "Y":
                continue
            elif ciclo == "n" or ciclo == "N":
                break


#-------------------------------------- FUNZIONI --------------------------------------

#-------------------------------------- MAIN PROGRAM--------------------------------------

if os.path.exists(cartellainputmerge) and os.path.exists(cartellaoutputmerge) and os.path.exists(cartellaoutputsplit) and os.path.exists(cartellainputsplit) and os.path.exists(cartellainputselect) and os.path.exists(cartellaoutputselect):
    print("Le cartelle necessarie al funzionamento del programma sono presenti!")
    while True:
        scelta = int(input("Scegli la modalita': \n \
            1: Unire due o piu' PDF \n \
            2: Estrarre tutte le pagine e convertirle in file  \n \
            3: Estrarre e unire le pagine desiderate  \n \
            4 o superiore: Esci dal programma \n \
            Fai la tua scelta:  "))
            
        if scelta == 1:
            file = str(input("Controlla se nella cartella sono presenti i file(y or n):  "))
            if file == "y"or file == "Y":
                if os.listdir("./inputfile/daunire/") == []:
                    print("Non e' presente nessun file compatibile... Riprova!")
                    continue
                else:   
                    varnome = str(input("Scrivi il nome con cui vorresti salvare il file: "))
                    unionepdf((varnome + ".pdf"))
                    scelta2 = int(input("Vuoi utilizzare ancora il programma o vuoi uscire? (y or n): "))
                    if scelta2 == "y" or scelta2 == "Y":
                        continue
                    else:
                        break

        elif scelta == 2:
            file1 =  str(input("Controlla se nella cartella sono presenti i file(y or n): " ))
            if file1 == "y" or file1 =="Y":
                if os.listdir("./inputfile/dadividere/") == []:
                    print("Non e' presente nessun file compatibile... Riprova!")
                    continue
                divisionepdf()
                scelta2 = int(input("Vuoi utilizzare ancora il programma o vuoi uscire? (y or n): "))
                if scelta2 == "y" or  scelta2=="Y":
                    continue
                else:
                    break

            elif file1 == "n" or file1 == "N":
                    continue

        if scelta == 3:
            file2 =  str(input("Controlla se nella cartella sono presenti i file(y or n): " ))
            if file2 == "y"or file2 == "Y":
                if os.listdir("./inputfile/daselezionare/") == []:
                    print("Non e' presente nessun file compatibile... Riprova!")
                    continue
                else:   
                    varnome1 = str(input("Scrivi il nome con cui vorresti salvare il file: "))
                    estraipdf((varnome1 + ".pdf"))

        if scelta >=4:
            break
else:
    controllodir()
    print("Le cartelle necessarie al funzionamento del programma sono state create con successo. Riavvia il programma!")


#-------------------------------------- MAIN PROGRAM--------------------------------------
