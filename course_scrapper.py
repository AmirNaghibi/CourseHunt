import requests
from bs4 import BeautifulSoup
from time import sleep
import send_mail
import datetime

'''
    User Input for
    Course Name
    Course Number
    Section Number
'''
course_name     = input("enter course name: ")
course_name     = course_name.upper()
course_number   = input("enter course number: ")
section_number  = input("enter course section (ex. 008) ")

course_info_link = "https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept="+course_name+"&course="+course_number+"&section="+section_number
page = requests.get(course_info_link)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())
sleep(2)
print("\nSUCCESS!!\n")
print(str(datetime.datetime.now())+" "+"number of general seats available: "+soup.find_all('strong')[3].get_text())
print("")
# sleep(5)
# while True:
#     if soup.find_all('strong')[3].get_text()!='0':
#         # send_mail.send_registration_email()
#         print(str(datetime.datetime.now())+" "+"number of general seats available: "+soup.find_all('strong')[3].get_text())
#         sleep(10)
