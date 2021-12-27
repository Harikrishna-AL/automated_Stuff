import re

passStrong = False
def passwordStrength():
    
    passwordText = input('Enter Password: ')

   
    charRegex = re.compile(r'(\w{8,})')  
    lowerRegex = re.compile(r'[a-z]+') 
    upperRegex = re.compile(r'[A-Z]+')
    digitRegex = re.compile(r'[0-9]+')


    if charRegex.findall(passwordText) == []:  
        print('Password must contain atleast 8 characters')
    elif lowerRegex.findall(passwordText)==[]: 
        print('Password must contain atleast one lowercase character')
    elif upperRegex.findall(passwordText)==[]: 
        print('Password must contain atleast one uppercase character')
    elif digitRegex.findall(passwordText)==[]: 
        print('Password must contain atleast one digit character')
    else:  
        print('Your password is strong. Good job!')
        global passStrong 
        passStrong=True
        return 
while not passStrong: 
    passwordStrength()
