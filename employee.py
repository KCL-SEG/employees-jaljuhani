"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name,salary,type,commision,commisionPay,commisionTime,bonus):
        self.name = name
        self.salary=salary
        self.type=type
        self.commision=commision
        self.commisionPay=commisionPay
        self.commisionTime=commisionTime
        self.bonus=bonus

    def get_pay(self):
        if(self.commision or self.type=='contract'):
            return self.salary+self.commisionPay*self.commisionTime+self.bonus
        else:
            return self.salary+self.commisionPay

        return self.pay

    def __str__(self):
        value=f'{self.name} works on a {self.type}';
        if((self.type=='monthly') and (self.commision==False)):
         value+= f' salary of {self.salary}.'
        elif (self.type == 'contract' and self.commision == False and self.bonus > 0):
         value += f' of {self.commisionTime} hours at {self.commisionPay}/hour and receives a commission for 3 contract(s) at 220/contract.'
        elif(self.type=='contract' and self.commision==False):
         value+=f' of {self.commisionTime} hours at {self.commisionPay}/hour.'
        elif (self.type == 'monthly' and self.bonus > 0):
         value += f' salary of {self.salary} and receives a bonus commission of {self.bonus}.'
        elif (self.type == 'contract' and self.bonus > 0):
         value += f' of {self.commisionTime} hours at {self.commisionPay}/hour and receives a bonus commission of {self.bonus}.'
        elif((self.type=='monthly' and self.commision==True)):
          value+=f' salary of {self.salary} and receives a commission for {self.commisionTime} contract(s) at {self.commisionPay}/contract.'


        value+= f'  Their total pay is {self.get_pay()}.'

        return value



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000,'monthly',False,0,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',0,'contract',False,25,100,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,'monthly',True,200,4,0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',0,'contract',False,25,150,660)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,'monthly',True,0,0,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',0,'contract',True,30,120,600)
