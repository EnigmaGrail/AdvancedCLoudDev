def savings():
    monthlyIncome = int(input (f' Please enter your monthly income: '))
    monthlyExpenses = int(input (f' Please enter your monthly expenses: '))
    monthlySavings = int(input (f' Please enter the amount of money you want to save monthly: '))
    savings = (monthlySavings/monthlyIncome) *100
    if monthlyExpenses > monthlySavings:
        print('You need to reduce monthly expenses')
    elif monthlyExpenses < monthlySavings:
        print('You will be saving ' + str(int(savings)) + '% per month')
    else:
        print('You are breaking even')
        
savings()
