import smtplib
import sys

sender = "godzilla74@wearehackerone.com"
receiver = "godzillabounty@gmail.com"

message = """From: From g0dzilla <godzilla74@wearehackerone.com>
To: lilzilla <godzillabounty@gmail.com>
Subject: SMTP Anon relay email

This is just a test
"""

try:
    smtpObj = smtplib.SMTP(sys.argv[1])
    smtpObj.sendmail(sender, receiver, message)
    print("Successfully sent anonymous email from {}".format(sys.argv[1]))
except:
    print("Error: {}".format(sys.exc_info()[0]))
