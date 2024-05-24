import random

def generateOTP():
    digits="0123456789"
    OTP=""
    for i in range(5):
        OTP=digits[random.randint(0,9)]
    return OTP

print("the 6-digits OTP is "+generateOTP())