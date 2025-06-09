import locale

def investment_value(start, interest_rate, tax_rate, deposit, years):
    balance = start
    for _ in range(1, years + 1):
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
    return balance

def investment_value(start, interest_rate, tax_rate, deposit, years):
    balance = start
    for _ in range(1, years + 1):
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
    return balance

def years_to_reach_goal(start, interest_rate, tax_rate, deposit, goal):
    years = 0
    balance = start
    while balance < goal:
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
        years += 1
    return years

funds = investment_value(start=10000,
                       interest_rate=0.07,
                       years=25,
                       tax_rate=0.13,
                       deposit=500)

print(years_to_reach_goal(start=10000,
                       interest_rate=0.07,
                       years=25,
                       tax_rate=0.13,
                       deposit=500))

print(years_to_reach_goal(start=10000,
                       interest_rate=0.13,
                       deposit=1000,
                       tax_rate=0.25,
                       goal=100000))

locale.setlocale(locale.LC_ALL, 'ru_RU')
print(locale.currency(3552.99315, grouping=True))
locale.setlocale(locale.LC_ALL, 'de_DE')
print(locale.currency(3552.99315, grouping=True))
locale.setlocale(locale.LC_ALL, 'en_US')
print(locale.currency(3552.99315, grouping=True))
locale.setlocale(locale.LC_ALL, 'fr_CA')
print(locale.currency(3552.99315, grouping=True))
locale.setlocale(locale.LC_ALL, 'en_GB')
print(locale.currency(3552.99315, grouping=True))