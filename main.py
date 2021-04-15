#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator")
bill_total = input("what is the total bill?")
tip_amount = input("what % tip would you like to leave for your bill?")
people_total = input("How many people are splitting the bill?")

bill_convert = int(bill_total)
tip_convert = float(tip_amount) / 100
people_convert = int(people_total)

print(tip_convert)

result = (bill_convert / people_convert) * tip_convert
print(round(result, 2))