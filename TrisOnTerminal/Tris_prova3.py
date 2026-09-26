import os
import msvcrt
import time

#####VALORI GLOBALI##################################
giocatore = 1     
vincita = 1    
pareggio = -1    
continuo = 0    
giocare_ancora = True
gioco = continuo    
marchio = 'X'

###########LISTA######################################
casella = ['-','-','-','-','-','-','-','-','-','-'] 

#######FUNZIONE CREAZIONE TABELLA######################
def tabella(posizione_cursore):
    os.system('cls')    
    valore_originale = casella[posizione_cursore]
    casella[posizione_cursore] = "*"
    print(
        "         |     |   ""\n""1-   ",
        casella[1]," | ",casella[2]," | ", casella[3],
        "\n""   ______|_____|______""\n""         |     |   ""\n""2-   ",
        casella[4]," | ",casella[5]," | ",casella[6],
        "\n""   ______|_____|______""\n""         |     |   ""\n""3-   ",
        casella[7]," | ",casella[8]," | ",casella[9],
        "\n""         |     |   ""\n""     1      2      3"
        )
    casella[posizione_cursore] = valore_originale

############FUNZIONE VERIFICA CONDIZIONI DI VINCITA############  
def controllo_vincita():    
    global gioco    
      
    if(casella[1] == casella[2] == casella[3] != '-'):    
        gioco = vincita    
    elif(casella[4] == casella[5] == casella[6] != '-'):    
        gioco = vincita    
    elif(casella[7] == casella[8] == casella[9] != '-'):    
        gioco = vincita    
    elif(casella[1] == casella[4] == casella[7]  != '-'):
        gioco = vincita    
    elif(casella[2] == casella[5] == casella[8] != '-'): 
        gioco = vincita    
    elif(casella[3] == casella[6] == casella[9]  != '-'):
        gioco=vincita    
    elif(casella[1] == casella[5] == casella[9] != '-'):    
        gioco = vincita    
    elif(casella[3] == casella[5]  == casella[7] != '-'):
        gioco=vincita    

    elif(casella[1]!='-' and casella[2]!='-' and casella[3]!='-' and casella[4]!='-' and casella[5]!='-' and casella[6]!='-' and casella[7]!='-' and casella[8]!='-' and casella[9]!='-'):    
        gioco=pareggio
        
    else:            
        gioco=continuo

#######CONTROLLO RANGE DELLE CASELLE#############################(Non obbligatorio)
def controllo_posizione(x):
    if(x <=9 and x >= 1):
        if(casella[x] == '-'):
            return True
        else:    
            return False
        
########CONTROLLO RANGE DELLE CASELLE E MOVIMENTI(O,X oppure "-")####################       
def controllo_cursore(x):
    if(x <=9 and x>=1):
        return True
    else:
        return False

#########MAIN E TITOLI##########################################################
if __name__ == "__main__":
    while giocare_ancora: 
        casella = ['-','-','-','-','-','-','-','-','-','-']   
        gioco = continuo
        print("\n")
        print("Benvenuti al gioco del TRIS") 
        print()
        time.sleep(2)
        nome_giocatore1= input("Inserisci il tuo nome Giocatore 1: ")
        print()
        nome_giocatore2= input("Inserisci il tuo nome Giocatore 2: ")
        
        
########INTANTO CHE IL GIOCO CONTINUA, INIZIA IL GIOCATORE 1 E POI IL 2###############
        while(gioco == continuo):    
            numero_casella_corrente = 5
            
            tabella(numero_casella_corrente)    
            if(giocatore %2!= 0):    
                
                print("Tocca a",nome_giocatore1,"[X]")
                marchio = 'X'
            else:    
                print("Tocca a",nome_giocatore2,"[O]")    
                marchio = 'O'

########COMANDI PER LA SELEZIONE WASD OPPURE CON LE FRECCE#######(nota. il comando ord(msvcrt.getch())serve per trasformare in numero un valore(tasto),in questo delle frecce)
            arrow_key = 0
            while arrow_key != 32:
                arrow_key = ord(msvcrt.getch())            

                valore_casella_corrente = casella[numero_casella_corrente]

                if arrow_key == 119 or arrow_key == 72:  #(W o freccia  in su)
                    if controllo_cursore(numero_casella_corrente -3):
                        numero_casella_corrente -= 3
                elif arrow_key == 75 or arrow_key == 97: #(A o freccia a sinistra)
                    if controllo_cursore(numero_casella_corrente -1):
                        numero_casella_corrente -= 1
                elif arrow_key == 115 or arrow_key == 80: #(S o freccia in giù)
                    if controllo_cursore(numero_casella_corrente +3):
                        numero_casella_corrente += 3
                elif arrow_key == 100 or arrow_key == 77: #(D o feccia a destra)
                    if controllo_cursore(numero_casella_corrente +1):      
                        numero_casella_corrente += 1 
                    
                tabella(numero_casella_corrente)    

            scelta = numero_casella_corrente

######VERIFICA SE IL NUMERO INSERITO E' CORRETTO O NO(es. NO parole al posto dei numeri)################################### 
            try:
                scelta = int(scelta)
            except:
                pass
                # print('Il valore che hai inserito non è valido, devi inserire un valore tra 1 e 9!')
            else:
                if(controllo_posizione(scelta)):    
                    casella[scelta] = marchio    
                    giocatore+=1    
                    controllo_vincita()  

#####REFRESH E CONTROLLO DELE CONDIZIONI DI VINCITA#########################################################################           
        os.system('cls')    
        tabella(numero_casella_corrente)    
        if(gioco==pareggio):    
            print("Esito partita: Parità")    
        elif(gioco==vincita):    
            giocatore-=1    
            if(giocatore%2!=0):    
                print("Esito partita:",nome_giocatore1,"vince")    
            else:    
                print("Esito partita:",nome_giocatore2, "vince") 
########CONTINUA? (RICORDA: i dati della partita precedente rimangono invariati affinché la casella sia svuotata)#########
        ancora=str(input("Volete giocare ancora, digita si o no: "))
        if ancora == "no":
            giocare_ancora = False
    


