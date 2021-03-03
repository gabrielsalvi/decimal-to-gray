#Algorithm to convert a decimal value, from 0 to 15, to code gray.

decimal = int(input('Decimal (0 - 15): '))

if 0 <= decimal <= 15:
    binary = ''

    if decimal == 0:
        binary = gray = '0000'

    else:
        while decimal >= 1:
            remainder = int(decimal % 2)
            decimal = decimal / 2
            binary = str(remainder) + binary

        binary_length = len(binary)

        if binary_length == 3:
            binary = '0' + binary

        elif binary_length == 2:
            binary = '00' + binary
            
        elif binary_length ==1:
            binary = '000' + binary

        a = binary[0]
        b = binary[1]
        c = binary[2]
        d = binary[3]

        gray = a

        if a == b:
            gray += '0'
        else:
            gray += '1'

        if b == c:
            gray += '0'
        else:
            gray += '1'

        if c == d:
            gray += '0'
        else:
            gray += '1'
        
    print(f'\nbinary: {binary}')
    print(f'gray: {gray}')

else:
    print('Só são aceitos números decimais de 0 a 15')