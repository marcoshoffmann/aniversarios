from os import getenv
from dotenv import load_dotenv # Carrega o arquivo .env de configuração
load_dotenv()                  # .
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from use_cases.MySQLDB import MySQLDB
from resources.TimeConsult import TimeConsult

# Configurações do servidor e porta
class EmailBirthday:
    def __init__(self, destiny: list[str], aniversariantes: str) -> None:
        self.mysqldb = MySQLDB(host=getenv("HOST"), user=getenv("USER"), password=getenv("PWD"), database=getenv("DATABASE"))
        self.timeconsult = TimeConsult()
        self.destiny = destiny
        self.aniversariantes = aniversariantes
        self.smtp_server = getenv("SMTP_SERVER")
        self.port = getenv("PORT")

        self.sender_email = getenv("SENDER")
        self.password = getenv("PASSWORD")

        # Configurar a mensagem
        self.message = MIMEMultipart()
        self.message["From"] = self.sender_email
        self.message["To"] = ", ".join(self.destiny) # Junta os e-mails em uma string separada por vírgulas
        self.message["Subject"] = f"!!!ANIVERSARIANTES DO DIA - MÊS {self.timeconsult.updated_month}/{self.timeconsult.updated_year}!!!"
        body = aniversariantes

        self.message.attach(MIMEText(body, "html"))

    def send_email(self) -> None:
        server = smtplib.SMTP(self.smtp_server, self.port)
        recipients = self.destiny
        server.starttls()  # Iniciar TLS
        server.login(self.sender_email, self.password)
        server.sendmail(self.sender_email, recipients, self.message.as_string())
        print('E-mail enviado com sucesso!')
        server.quit()
