# python3 item-to-age checker

print('Welcome to Vinmonopolet.')

age = int(input('What is your age?: '))

if age < 18: # guard clause
    print('You are under the legal age limit for alcohol or tobacco products.')
else:
    item_type = input('What would you like to purchase?: ')

 # categories
    light_spirits = ['wine','beer','cider']
    heavy_spirits = ['vodka','whiskey','tequila']
    tobacco = ['cigarettes','snus','rolling paper']
 # conditions
    if age >= 18 and item_type in light_spirits:
        print(f'You may purchase {item_type}.')
    elif age >= 18 and item_type in tobacco:
        print(f'You may purchase {item_type}.')
    elif age >= 20 and item_type in heavy_spirits:
        print(f'You may purchase {item_type}.')
    elif age < 20 and item_type in heavy_spirits:
        print(f'You may not purchase {item_type}.')
    elif (
    item_type not in light_spirits
    and item_type not in heavy_spirits
    and item_type not in tobacco
):
        print('Selected item is not sold here.')

# result
print('-')
print('Code executed successfully.')