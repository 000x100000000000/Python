# The following is used as a global constant
# the contribution rate.
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input("Enter your gross pay: "))
    bonus = float(input("Enter the amount of bonuses: "))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

# The show_pay_contrib function accepts the gross
# pay as an argument and displays the retirement
# contribution for that amount of pay.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print("Contribution for gross pay: $", \
          format(contrib, ',.2f'), \
          sep='')

# The show_bonus_contrib function accepts the
# bonus amount as an argument and displays the
# retirement contribution for that amount of pay.
def show_bonus_contrib(bouns):
    contrib = bouns * CONTRIBUTION_RATE
    print("Contribution for bonuses: $", \
          format(contrib, ',.2f'), \
          sep='')

# Call the main function.
main()
