print('3 + 4 * 5 =', 3 + 4 * 5)
print('23.45 / 1e-02 =', 23.45 / 1e-02)
print()

print('7 / 4 =', 7 / 4)
print('7 // 4 =', 7 // 4)
print()

x = 1172.5
print('x = 1172.5')
print('x.as_integer_ratio()', x.as_integer_ratio())
print('x.is_integer()', x.is_integer())
print()

y = 12345
print('y.numerator', y.numerator)
print('y.denominator', y.denominator)
print('y.bit_length()', y.bit_length())
print()

symbols = 'AAPL IBM MSFT YHOO SCO'
print('symbols = \'AAPL IBM MSFT YHOO SCO\'')
print('symbols[0] =', symbols[0])
print('symbols[1] =', symbols[1])
print('symbols[2] =', symbols[2])
print('symbols[-1] =', symbols[-1])
print('symbols[-2] =', symbols[0 - 2])
print()

print('symbols[:4] =', symbols[:4])
print('symbols[-3:] =', symbols[-3:])
print('symbols[5:8] =', symbols[5:8])
print()

symbols += ' GOOG'
print('symbols += \' GOOG\' =', symbols)
symbols = 'HPQ ' + symbols
print('symbols = \'HPQ \' + symbols =', symbols)
print()

print('\'IBM\' in symbols', 'IBM' in symbols)
print('\'AA\' in symbols', 'AA' in symbols)
print('\'CAT\' in symbols', 'CAT' in symbols)
print()

print('symbols.lower() = ', symbols.lower())
print('sumbols = ', symbols)
print()

lowersyms = symbols.lower()
print('lowersyms = symbols.lower()')
print('lowersyms =', lowersyms)
print()

print('symbols.find(\'MSFT\')', symbols.find('MSFT'))
print('symbols[13:17]', symbols[13:17])
symbols = symbols.replace('SCO', '')
print('symbols = symbols.replace(\'SCO\',\'\')', )
print('symbols =', symbols)
print()

symlist = symbols.split()
print('symlist = symbols.split()')
print('symlist =', symlist)
print('symlist[0]', symlist[0])
print('symlist[1]', symlist[1])
print('symlist[-1]', symlist[-1])
print('symlist[-2]', symlist[-2])
print()

symlist[2] = 'AIG'
print('symlist[2] = \'AIG\'')
print('symlist =', symlist)
print()

print('for s in symlist:')
for s in symlist:
    print('s =', s)
print()

print('\'AIG\' in symlist', 'AIG' in symlist)
print('\'AA\' in symlist', 'AA' in symlist)
print()

print('symlist.append(\'RHT\')')
symlist.append('RHT')
print('symlist =', symlist)
print()

print('symlist.insert(1,\'AA\')')
symlist.insert(1, 'AA')
print('symlist =', symlist)
print()

print('symlist.remove(\'MSFT\')')
symlist.remove('MSFT')
print('symlist =', symlist)
try:
    symlist.remove('MSFT')
except ValueError as e:
    print(e)
print()

print('symlist.index(\'YHOO\') =', symlist.index('YHOO'))
print('symlist[4] =', symlist[4])
print()

print('symlist.sort()')
symlist.sort()
print('symlist =', symlist)
print()

print('symlist.sort(reverse=True)')
symlist.sort(reverse=True)
print('symlist =', symlist)
print()

print('nums = [101,102,103]')
print('items = [symlist, nums]')
nums = [101, 102, 103]
items = [symlist, nums]
print('items =', items)
print()

print('items[0] =', items[0])
print('items[0][1] =', items[0][1])
print('items[0][1][2] =', items[0][1][2])
print('items[1] =', items[1])
print('items[1][1] =', items[1][1])
print()

prices = {'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
print('prices =', prices)
print()

print('prices[\'IBM\'] =', prices['IBM'])
print('>> prices[\'IBM\'] = 123.45')
print('>> prices[\'HPQ\'] = 26.15')
prices['IBM'] = 123.45
prices['HPQ'] = 26.15
print('prices =', prices)
print()

print('list(prices) =', list(prices))
print()

print('>> del prices[\'AAPL\']')
del prices['AAPL']
print('prices =', prices)
print()
