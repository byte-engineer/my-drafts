print("")
print("")
value = input("Enter the weight in bounds / kilograms with unit ?   " )
if float(value[:-3]) < 0:
    print('Please enter a valied number.  '.upper())
else :
    detirmin_lbs = 'lbs' in value
    detirmin_kg = 'kg' in value
    if detirmin_lbs == True :
        kilograme_value = float(float(value[:-3])) * 0.45359237
        output = (f'the weight in kilograms = {kilograme_value} kg')
    elif detirmin_kg == True :
        pound_value = float(float(value[:-3])) / 0.45359237
        output = (f'the weight in pounds = {pound_value} lbs')
    else :
          print("write the value a gain with the unit")
        
number_char = len(output)
final = f'{output}                                                ( {number_char} Character(s) )'
print(str(final) )


