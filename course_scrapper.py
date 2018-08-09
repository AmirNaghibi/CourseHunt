import requests
from bs4 import BeautifulSoup
from time import sleep
import send_mail

ubc_econ_102 = "https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=ECON&course=102&section=008"
page = requests.get(ubc_econ_102)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())
while True:
    if soup.find_all('strong')[4].get_text()!='0':
        send_mail.send_registration_email()
    #print(soup.find_all('strong'))
    print(soup.find_all('strong')[4].get_text())
    sleep(30)