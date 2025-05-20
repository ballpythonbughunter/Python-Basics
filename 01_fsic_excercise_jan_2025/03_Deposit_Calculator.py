# сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

# 1. Депозирана сума – реално число в интервала [100.00 … 10000.00]
deposited_amount = float(input())
# 2. Срок на депозита (в месеци) – цяло число в интервала [1…12]
deposit_period = int(input())
# 3. Годишен лихвен процент – реално число в интервала [0.00 …100.00]
annual_interest_rate = float(input())

# total_amount = deposited_amount + deposit_period * ((deposited_amount * annual_interest_rate) / 12)

annual_interest = deposited_amount * annual_interest_rate / 100

monthly_interest = annual_interest / 12

print(deposited_amount + deposit_period * monthly_interest)
