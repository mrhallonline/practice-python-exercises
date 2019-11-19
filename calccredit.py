# payment = 425
interest = 70
startingBalance = 2800

def balance_over_time(months, payment):
    pay_per_month = (payment-interest)
    amount_deducted = (pay_per_month * months)
    print("Total Paid: " + str(amount_deducted))
    ending_balance = (startingBalance-amount_deducted)
    print("Balance left: " + str(ending_balance))
    months_to_payoff = (startingBalance/pay_per_month)
    print("Months to PayOff: " + str(months_to_payoff))
    
balance_over_time(12, 200)