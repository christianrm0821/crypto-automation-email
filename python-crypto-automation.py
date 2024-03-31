import requests  #http requests
from bs4 import BeautifulSoup # web scraping
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime


now = datetime.datetime.now()
content = ''

#Getting email content
def Top_CoinDesk_Stories(url):
    print("\n" + "*"*100)
    cnt = ''
    cnt += ("Top CoinDesk Stories\n"+"*"*100 + "\n")
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('div', attrs={"class":"card-title"})):
        cnt+=((str(i+1)+ ". "+ tag.text + "\n") )
        if(i >23):
            break

    cnt+=("*"*100+"\n")
    print(cnt)
    return(cnt)
    
content = Top_CoinDesk_Stories('https://www.coindesk.com/')



#Sending Email
my_email = "christianrm0821@gmail.com"

mail = MIMEMultipart()
mail["subject"] = "Top Crypto Stories " + str(now.day) + "-" +str(now.year)
mail["From"] = my_email
mail["To"]=my_email

mail.attach(MIMEText(content,"plain"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(my_email,"ajxi sjfk sgln cgrr")
server.sendmail(my_email,my_email,mail.as_string())
print("List sent")
server.quit()