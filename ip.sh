#!/bin/bash

# File dove è stato salvato l'IP pubblico
FILE_IP="INSERIRE/IL/PERCORSO"

# Funzione per rilevare l'IP pubblico corrente
function rileva_ip_pubblico {
    IP=$(curl -s https://api.ipify.org)
    echo $IP
}

# Legge l'IP salvato nel file
if [ -f "$FILE_IP" ]; then
    IP_SALVATO=$(cat "$FILE_IP")
else
    echo "File dell'IP pubblico non trovato: $FILE_IP"
    exit 1
fi

# Rileva l'IP pubblico corrente
IP_CORRENTE=$(rileva_ip_pubblico)

# Confronta l'IP corrente con quello salvato
if [ "$IP_CORRENTE" == "$IP_SALVATO" ]; then
    echo "L'IP pubblico non è cambiato ($IP_CORRENTE). Non viene eseguito nulla."
else
    echo "L'IP pubblico è cambiato da $IP_SALVATO a $IP_CORRENTE."
    echo "Eseguo il programma Python per inviare l'email con il nuovo IP..."

    # Esegui il programma Python per inviare l'email e eseguire un secondo controllo
    python3 /home/aliorc/programmazione/ipinvier/ipinvier.py 
    # Aggiorna il file con il nuovo IP pubblico
    echo "$IP_CORRENTE" > "$FILE_IP"
fi

