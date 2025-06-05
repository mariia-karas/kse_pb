
def send_email(users, emails, sender):
    recipient = input("enter recipient: ")
    mail = input("Enter some text: ")
    if recipient not in users:
          print("Recipient is not registered")
    else:
         emails.append({"sender": sender, "recipient" : recipient, "email" : mail})
    print(emails)

     
