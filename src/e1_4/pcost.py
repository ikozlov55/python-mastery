def portfolio_cost(file_name):
    total_price = 0
    with open(file_name, 'r') as file:
        for line in file:
            cols = line.split()
            try:
                number_of_shares = int(cols[1])
                price = float(cols[2])
                total_price += number_of_shares * price
            except ValueError:
                print(f'Couldn\'t parse: \'{line.strip()}\'')
    return total_price


if __name__ == '__main__':
    for file_name in ['Data/portfolio.dat', 'Data/portfolio3.dat']:
        print(f'portfolio_cost(\'{file_name}\') =', portfolio_cost(file_name))
        print()
