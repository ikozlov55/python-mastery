file_name = '../../Data/portfolio.dat'

total_price = 0
with open(file_name, 'r') as file:
    for line in file:
        cols = line.split()
        stock_name = cols[0]
        number_of_shares = int(cols[1])
        price = float(cols[2])
        print(f'{stock_name=}')
        print(f'{number_of_shares=}')
        print(f'{price=}')
        print()
        total_price += number_of_shares * price

print('total_price =', total_price)
