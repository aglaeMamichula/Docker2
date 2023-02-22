###task1###
###import math###

#this si the first variables i need to define tot ellt he suer his debt and moeny situation

import math

print("choose either 'investment' or 'bond' fromt the menu, then we will continue")
print("investment: this is to calculate the amoutn of interest you will earn on your investmens")
print("bond: this is to calculate the amount of money you need to pay on your hoem loan")

choice = int(input("""please shoose Choose option:

1) Investment
2) Bond\n"""))



if choice == 2 or choice == 1:
    if choice == 1:
   
        #asking user for the details
        investment = float(input("that is great,please enter how much money you are depositing today in number: "))
        percentage = float(input("please enter your percentage of interest given: "))
        years = float(input("how many years this will be: "))
        
        investment_calculator = int(input("""great please tell me is the calculation:
        1compound interest
        2simple interes"""))
        
        #compound interest option
        if investment_calculator == 1:
#            years = float(input("how many years are you plannign to invest: ")# this line is redundant as i have this infor in line 22

            print("that is great {} years is a good plan".format(years))
            p = investment
            t = years
            r = percentage/100

            A = p* math.pow((1+r),t)
            print("great your total interest will be {}".format(A))

            print(A)
        
        #simple itnerest option
        if investment_calculator == 2:
            p = investment
            t = years
            r = percentage/100
            simple =p*(1+r*t)
            print(simple)

 
        
    elif choice == 2:
      
        p = float(input("that is great lets now calculate how much is the value of the property"))
        i = float(input("please enter your number of interest deal"))
        n = float(input("please enter the number of months this deal is going for"))       
        i = i/12
        x=(i*p)/(1-(1+i)**(-n))
        print("great your total interes will be {}".format(x))
#sorry i got the names of the values all mixed up, this is corrected now
        #those are all the variables from input and the total interest for the user

else:
    print("input is wrooong")
    #if the user dont ge tit we will give th eintruction again
    print("choose either 'investment' or 'bond' fromt the menu, then we will continue")
    print("investment: this is to calculate the amoutn of interest you will earn on your investmens")
    print("bond: this is to calculate the amount of money you need to pay on your hoem loan")





 
