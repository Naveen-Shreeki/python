import math
import random
snum="0123456789"
length=len(snum)
otp=""
for i in range(4):
    otp+=str(math.floor(random.random()*length))
print("Generating your otp")
print("Your OTP is ",otp) 