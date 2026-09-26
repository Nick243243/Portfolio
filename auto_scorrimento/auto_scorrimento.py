import cv2
import sys

def main():
    #Inizializziamo l'oggetto VideoCapture, '0' è la fotocamera predefinita normalmente quella integrata
    cap = cv2.VideoCapture(0)

    #Controlliamo se la fotocamera è accessa
    if not cap.isOpened():
        print("Errore: impossibile accedere alla webcam")
        sys.exit()

    try:
        while True:
            success, frame = cap.read() #legge un fotogramma e salva lo stato Tre/False in success 

            if not success: #esempio webcam separato
                print("Errore: fotogramma non leggibile o saltato") 
                break

            frame = cv2.flip(frame, 1) #specchio orizzontalmente il frame catturato, dove '0' permette di specciare verticalmente mentre '1' orizzontalmente

            cv2.imshow('Controllo Testa', frame) #genera la finestra di output a schermo

            if cv2.waitKey(1) & 0xFF == ord('q'):  #waitKey fa aspettare per 1 ms in risposta ad un tasto e restituisce un valore il ricevuto. NOTA: il valore ricevuto non è detto che abbia solo 8 bit
                                                   #Allora facciamo un AND con una maschera di 0xFF (255) così eliminiamo tutti i valori superfli e infine lo confronto con la lettera q convertito in ASCII
              break

    except Exception as e:
        print(f"Errore imprevisto: {e}")

    finally:
        cap.release()   #rilascia la webcam
        cv2.destroyAllWindows()  #distrugge tutte le finestre di output a schermo
              



if __name__ == '__main__':
    main()