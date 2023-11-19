print ('Welcome to your favourite tip calculator!')
bill = float(input('What was the total bill? R'))
tip = int(input ('What percentage tip would you like to give? 10, 12 or 15?'))
number_of_people = int(input ('How many people to split the bill?'))

percentage_tip = tip/100 
bill_with_tip = bill * percentage_tip 
total_bill = bill_with_tip + bill
bill_per_person = (total_bill/number_of_people)
final_bill_per_person = round(bill_per_person, 2)
print(f'Each person should pay:R{final_bill_per_person}')





