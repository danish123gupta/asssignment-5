nameage="Abc is 18 years old"
nameage= "Xyz is 10 years old"
import re
nameage=re.findall('[A-Z],[a-z]',nameage)
print(nameage)

import re
emailid="gupta.danish236@gmail.com add.com 123"
emails=re.findall(r'[\w\.-]+@[\w\.-]+',emailid)
for email in emails:
    print("email")

    import re
    strr='sat rat cat mat'
    regex=re.compile("[m]at")
    str =regex.sub("dan",strr)
    print(strr)

