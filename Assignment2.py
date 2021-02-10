import re
from datetime import date
class AgeCalculator:

    def __init__(self,str1):
        self.str1=str1

    def check(self):
        date_pattern = "^([0-9]|[0-2][0-9]|(3)[0-1])(\/)(([1-9])|((1)[0-2]))(\/)\d{4}$"
        searchobj = re.search( date_pattern , self.str1)
        if searchobj != None:
            return "1"
        else:
            return "0"


    def findAge(self):

        if self.check()=="0":
            return "InvalidDateException"

        if self.check() == "1":
            tokens = self.str1.split('/')
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            d2 = d1.split('/')
            age = int(d2[2]) - int(tokens[2])
            if age >= 0:
                return age
            else:
                print("Future Date passed")
                return False

a=AgeCalculator("30/11/2020")

print(AgeCalculator.findAge(a))
