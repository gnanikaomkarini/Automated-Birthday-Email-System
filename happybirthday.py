import pandas, datetime, openpyxl, ssl, smtplib
from email.message import EmailMessage

path = r'file path'
studDetails = pandas.read_excel(path)
rollNos = list(studDetails.RollNumber)
names = list(studDetails.Name)
birthdays = list(studDetails.Birthday)
birthdays = [str(birthday)[:10] for birthday in birthdays]
today = str(datetime.date.today())
bornTodayNames = []
bornTodayRollNo = []
bornTodayEmail = []
for index in range(len(birthdays)):
    if today[4:] in birthdays[index]:
        bornTodayNames.append(names[index])
        bornTodayRollNo.append(rollNos[index])
print(bornTodayNames)
print(bornTodayRollNo)
# print(bornTodayEmail)
if len(bornTodayNames) == 0:
    exit()
for index in range(len(bornTodayNames)):
    sender = 'your emaid id'
    password = 'your password'
    reciever = bornTodayRollNo[index].lower() + "@bvrithyderabad.edu.in"//here we have sent the mails directly using the students roll numbers to get their college mai ids. instead of this you can have an additional column in the excel sheet for the email ids and assign the birthday gir/boy's email id to the reciever variable.
    subject = "HAPPY BIRTHDAY!!!!!!!!!"
    body = f"""
    Happy {int(today[:4]) - int(birthdays[names.index(bornTodayNames[index])][:4])}th Birthday {bornTodayNames[index]}!.
    We hope you celebrate many more such birthdays ahead and have a bright future. We love you from the bottom of our hearts and are happy to be your batchmates.
    From,
    Gnanika Omkarini Makkena
    
    P.S: Where's the cake???
    """
    em = EmailMessage()
    em['From'] = sender
    em['To'] = reciever
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, reciever, em.as_string())
