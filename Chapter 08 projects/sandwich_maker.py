import pyinputplus as pyp


menu = True


prices = {'wheat': 2, 'white': 1, 'sour dough': 3, 'chicken': 2, 'turkey': 3, 'ham': 2, 'tofu': 1,
          'cheddar': 1, 'swiss': 2, 'mozzarella': 3, 'mayo': 1, 'mustard': 1, 'lettuce': 1,
          'ketchup': 1}
while menu:
    bread = pyp.inputMenu(['wheat', 'white', 'sour dough'],
                          prompt='Please select the type of bread you want for your sandwich: \n',
                          numbered=True)

    protein = pyp.inputMenu(['chicken', 'Turkey', 'Ham', 'Tofu'],
                            prompt='Which type of protein you would like: \n',
                            numbered=True)

    cheese = pyp.inputYesNo('Do you want Cheese in your sandwich?(Y/N)\n')
    cheese_type = ''
    if cheese == 'yes':
        cheese_type = pyp.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered=True)

    mayo = pyp.inputYesNo('Do you want mayo?(Y/N) \n')
    mustard = pyp.inputYesNo('Do you want mustard?(Y/N) \n')
    lettuce = pyp.inputYesNo('Do you want lettuce?(Y/N) \n')
    ketchup = pyp.inputYesNo('Do you want tomato ketchup?(Y/N) \n')

 
    sandwichQT = pyp.inputInt('How much sandwiches you would like to order?\n',
                              blockRegexes=['[0|-|.]'])

    total_amount = 0

    for item, price in prices.items():
        if bread == item:
            print(f'Your sandwich ingredients and prices are as follows: \n'
                  f'{item}= {price}')
            total_amount += price

        if protein == item:
            print(f'{item}= {price}')
            total_amount += price

        if cheese_type == item:
            print(f'{item}= {price}')
            total_amount += price

    if mayo == 'yes':
        print(f"mayo = {prices['mayo']}")
        total_amount += prices['mayo']

    if mustard == 'yes':
        print(f"mustard = {prices['mustard']}")
        total_amount += prices['mustard']

    if lettuce == 'yes':
        print(f"lettuce = {prices['lettuce']}")
        total_amount += prices['lettuce']

    if ketchup == 'yes':
        print(f"ketchup = {prices['ketchup']}")
        total_amount += prices['ketchup']

    print(f"sandwich cost x sandwich Qt ordered = {total_amount}x{sandwichQT} = "
          f"{total_amount*sandwichQT}")

    order_confirm = pyp.inputYesNo('Please confirm your order: (Y/N)\n')
    if order_confirm == 'yes':
        print('Please take your order number from the machine and you will be notified when '
              'its ready')
        menu = False