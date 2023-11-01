
#                      OVERVIEW
            -------------------------------

# The Simple Mail Transfer Protocol (SMTP) is an application used by mail servers to send, receive, and relay outgoing email between 
# senders and receivers. As the technology behind email communication, SMTP is the protocol that allows you to send and receive emails.
# Email SMTP is a module that comes pre-bundled with Python, the smtplib is a Python module that allows us to send emails using Python code.


#               SENDING EMAILS
          --------------------------------

import smtplib

my_email = "anyaray2016@gmail.com"                 # anyaray2016 is the identity of my email account, while gmail.com is the identity of my email provider.
my_password = "wsoi uzkm tuaw aiqm"                # The password is an app-password you create from your gmail account (and not your regular password)


connection = smtplib.SMTP("smtp.gmail.com")        # We create an object from the SMTP class and we specify the
                                                   # the location of our email provider's SMTP server

connection.starttls()                              # Transport Layer Security (TLS) provides a secure (encrypted) connection
                                                   # to our email server.

connection.login(user=my_email, password=my_password)

connection.sendmail(from_addr=my_email,
                    to_addrs="anyaraymond@yahoo.com",
                    msg="Subject: Happy New Month\n\nI am writing to wish you a happy new month this 1st November 2023. Take good care of yourself"
                    )
connection.close()                                 # We use this line of code to close the connection




#               USING THE with KEYWORD
          ---------------------------------
# Using the "with" keyword automatically closes the connection, therefore we don't need to do connection.close() 

import smtplib

my_email = "anyaray2016@gmail.com"
my_password = "wsoi uzkm tuaw aiqm"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="anyaraymond@yahoo.com",
        msg="Subject: Happy New Month\n\nI am writing to wish you a happy new month this 1st November 2023. Take good care of yourself"
        )

