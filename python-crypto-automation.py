import requests  #http requests
from bs4 import BeautifulSoup # web scraping
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import time

def send_email():
    now = datetime.datetime.now()
    content = ''

    #Getting email content
    def Top_Stories(url, class_name, curr_tag, title):
        print("\n" + "*"*100)
        cnt = ''
        cnt += (title + "\n" + "*"*100 + "\n")
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content,'html.parser')
        for i,tag in enumerate(soup.find_all(curr_tag, attrs={"class":class_name})):
            cnt+=((str(i+1)+ ". "+ tag.text + "\n") )
            if(i > 3):
                break

        cnt+=("*"*100+"\n")
        print(cnt)
        return(cnt)
    
    content = Top_Stories('https://www.coindesk.com/', "card-title","div","Top CoinDesk Stories")
    content += Top_Stories("https://www.nytimes.com/section/business/dealbook","css-1j88qqx e15t083i0","h3","Top NYT Business Stories")
    content += Top_Stories("https://www.ft.com/cryptofinance","js-teaser-heading-link","a","Top Financial Times Stories")

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
    server.login(my_email,"[my_password]")
    server.sendmail(my_email,my_email,mail.as_string())
    print("List sent")
    server.quit()

send_email()
