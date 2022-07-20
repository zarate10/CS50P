def fuel():

    slash = 0
    num1 = []
    num2 = []

    while True: 
        try:
            
            user_fraction = input('Fraction: ')
            user_fraction = list(user_fraction)

            for i in range(len(user_fraction)):
                if user_fraction[i] == '/':
                    slash = i

            for i in range(slash + 1, len(user_fraction)):
                num2.append(user_fraction[i])        

            for i in range(0, slash):
                num1.append(user_fraction[i])

            num1, num2 = int(''.join(num1)), int(''.join(num2))
            
            if num1 > num2: 
                fuel()

            result = num1 / num2 * 100
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

    if result <= 1:
        print('E')
    elif result >= 99:
        print('F')
    else:
        print(f'{round(result)}%')

fuel()