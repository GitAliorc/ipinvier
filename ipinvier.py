import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def rileva_ip_pubblico():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_pubblico = response.json()['ip']
        return ip_pubblico
    except Exception as e:
        return str(e)

def invia_email(ip_pubblico, email_destinatario, email_mittente, password_mittente):
    try:
        # Configurazione del messaggio email
        msg = MIMEMultipart()
        msg['From'] = email_mittente
        msg['To'] = email_destinatario
        msg['Subject'] = "Il tuo IP pubblico"

        body = f"Il tuo IP pubblico è: {ip_pubblico}"
        msg.attach(MIMEText(body, 'plain'))

        # Configurazione del server SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_mittente, password_mittente)
        text = msg.as_string()
        server.sendmail(email_mittente, email_destinatario, text)
        server.quit()

        print(f"Email inviata con successo a {email_destinatario}")
    except Exception as e:
        print(f"Errore nell'invio dell'email: {str(e)}")
        
def salva_ip_su_file(ip_pubblico, nome_file):
    try:
        with open(nome_file, 'w') as file:
            file.write(ip_pubblico)
        print(f"IP pubblico salvato nel file '{nome_file}'")
    except Exception as e:
        print(f"Errore nel salvataggio dell'IP nel file: {str(e)}")


if __name__ == "__main__":
    ip_pubblico = rileva_ip_pubblico()
    print(f"Il tuo IP pubblico è: {ip_pubblico}")

    email_destinatario = ""
    email_mittente = ""
    password_mittente = ""
    nome_file_ip = "ip_pubblico.txt"

    invia_email(ip_pubblico, email_destinatario, email_mittente, password_mittente)
    salva_ip_su_file(ip_pubblico, nome_file_ip)
