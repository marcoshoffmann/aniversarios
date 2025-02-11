from os import getenv
from DB.queries import consulta_email_birthday, consulta_aniversariantes
from dotenv import load_dotenv
load_dotenv()
from use_cases.MySQLDB import MySQLDB
from use_cases.EmailBirthday import EmailBirthday
from html import body

class VerifyEmailsBirthday:
    def __init__(self) -> None:
        self.mysqldb = MySQLDB(host=getenv("HOST"), user=getenv("USER"), password=getenv("PWD"), database=getenv("DATABASE"))
        self.destiny = [email[0] for email in self.mysqldb.ler_dados(query=consulta_email_birthday)]
        self.aniversariantes = self.mysqldb.ler_dados(query=consulta_aniversariantes)
        self.mensagem_aniversariantes = ''
        if len(self.aniversariantes).__gt__(0):
            self.mensagem_aniversariantes = body
            for aniversariante in self.aniversariantes:
                self.mensagem_aniversariantes += f'<tr><td>{aniversariante[0]}</td><td>{aniversariante[1]}</td><td>{aniversariante[-1]}</td>'
            self.mensagem_aniversariantes += '</table><br><br>Atenciosamente:<br>Equipe de TI' # Rodapé do email após a tabela

    def send_email(self) -> None:
        if len(self.aniversariantes).__gt__(0):
            emailbirthday = EmailBirthday(destiny=self.destiny, aniversariantes=self.mensagem_aniversariantes).send_email()
