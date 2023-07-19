import random

def generate_otp():
     return str(random.randint(100000,999999))

def send_otp(phone_number,otp):
     print(f"OTP sent to{phone_number}: {otp}")
     
def verify_otp(entered_otp,generated_otp):
     return entered_otp == generated_otp

def otp_verification():
     phone_number = input("Enter your number: ")
     
     generated_otp =generate_otp()
     send_otp(phone_number,generated_otp)
     
     entered_otp=input("Enter the OTP you recived:")
     
     if verify_otp(entered_otp,generated_otp):
          print("OTP verification Successfull!")
     else:
          print("OTP verification failed.")

otp_verification()
          