#The libraries using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:
#Create a normal and comprehensive list that will add the codes together for auditing purpose.

codes = [14, 15, 16, 17, 18, 19, 20]
total = 0

#Normal list
for code in codes:
    total += code
print("Normal list:",total)

#Comprehensive list
#sum() function to sum up all codes
#Note that I'll return each code and each one is added
result = sum([code for code in codes])
print("Comprehensive list:",result)