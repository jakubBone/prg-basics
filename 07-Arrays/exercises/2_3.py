# A program that calculates expenses for each category, for each week and for the whole month.

# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]

# Calculates expenses
# monthly_expenses[week][category]: the first index is the row, the second is the column
food = 0
transport = 0
utilities = 0
week_totals = [0, 0, 0, 0]
for week in range(len(monthly_expenses)):
    food += monthly_expenses[week][0]
    transport += monthly_expenses[week][1]
    utilities += monthly_expenses[week][2]
    for category in range(len(monthly_expenses[week])):
        week_totals[week] += monthly_expenses[week][category]

total = food + transport + utilities

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:', transport)
print('Utilities:', utilities)
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')
print('TOTAL:', total)
