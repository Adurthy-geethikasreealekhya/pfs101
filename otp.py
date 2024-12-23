import random
def otpgen():
    otp = ''
    for i in range(2):
        otp = otp + str(random.randint(0,9))
        otp = otp + random.choice([chr(i) for i in range(ord('A'),ord('Z')+1)])
        otp = otp + random.choice([chr(i) for i in range(ord('a'),ord('z')+1)])
    return otp