import smtplib
from email.mime.text import MIMEText

me='pensirara@gmail.com'
you='pensirara@naver.com'
contents='hello world'
msg= MIMEText(contents,_charset='euc-kr')
msg['Subject']='mail'
msg['From']=me
msg['To']=you

server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()

server.login("pensirara@gmail.com","dlaskdud7")
server.sendmail(me,you,msg.as_string())
server.quit()
