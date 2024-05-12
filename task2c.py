#The libraries using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:
#Create a normal and comprehensive list that will display only codes that are tracked by odd numbers

codes = [14, 15, 16, 17, 18, 19, 20]

#Normal list
odd_list = []
for code in codes:
    if code % 2 != 0:
        odd_list.append(code)
print("Normal list:",odd_list)

#Comprehensive list
odd = [code for code in codes if code % 2 != 0]
print("Comprehensive list:",odd)
