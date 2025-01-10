import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""

for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]

msg = f"Your OTP is {OTP}"

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("Your Gmail Account", "Your App Password")

emailid = input("Enter your email: ")

s.sendmail('Your Gmail Account', emailid, msg)

a = input("Enter Your OTP >>: ")

if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")

s.quit()
