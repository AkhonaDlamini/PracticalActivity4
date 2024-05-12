#The libraries using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:
#Create a normal and comprehensive list that will display the codes.

#Normal list
codes = [14, 15, 16, 17, 18, 19, 20]
#for code in codes:
#    print(code)

#OR
new_c = []
for code in codes:
   new_c.append(code)
print("Normal list:",new_c)

#Comprehensive list

new_codes = [code for code in codes]
print("Comprehensive list:",new_codes)