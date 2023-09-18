
def bank(cash_deposit, deposit_term):
    year = 0
    while year < deposit_term:
        cash_deposit += (cash_deposit * 0.1)
        year += 1
    return cash_deposit

print(bank(100, 10))
        
        