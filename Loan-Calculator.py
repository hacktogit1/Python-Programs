#This program is to calculate the number of payments you have to give each month for you to be loan free!
#M = monthly payement
#L = Loan amount
#i = interest rate(for an intrest of 6%, i = 0.06)

L = input('Enter the loan amount: ')

i = input('Enter interest rate: ')

n = input('Enter number of years: ')
numberOfmonths = float(n)*12
LoanAmount = float(L)
InterestRate = float(i)
M = LoanAmount*(InterestRate*(1+InterestRate)*numberOfmonths)/((1+InterestRate)*numberOfmonths - 1)
print('You must give INR {0:.2f} every month'.format(float(M)))
