import math
user_selection = input("""Please choose from the following options...

Investment - to calculate the amount of interest you'll earn on your investment
Bond - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed: """).lower()

## Takes user's input, converts it to lowercase and stores it as user_selection

if user_selection == "investment" :
    principal = float(input("Enter the amount you are depositing: "))
    rate = float(input("Enter the interest rate as a percentage, exclude %: ")) / 100
    years = float(input("Enter the number of years you will be investing for: "))
    interest = input("Choose simple or compound interest: ").lower()

# Takes user's inputs for investment and saves user choice between simple/compound as variable 'interest'
    
    if interest == "simple" :
        investment_value = principal * (1 + rate * years)
        simple_interest = str(investment_value)
        print("Your investment value is: " + simple_interest)

    elif interest == "compound" :
        investment_value = principal * math.pow((1 + rate), years)
        compound_interest = str(investment_value)
        print("Your investment will be worth: " + compound_interest)
        
    else:
        print("Error. Input must be 'simple' or 'compound'. Re-run the programme to try again.")


# calculates and returns investment value based on user selection and returns error if selection is invalid

elif user_selection == "bond" :
    present_value = float(input("Enter the present value of the property: "))
    annual_interest_rate = float(input("Enter the annual interest rate as a percentage, exclude %: "))
    interest_rate = (annual_interest_rate / 100) / 12
    num_months = float(input("Enter the number of months it will take you to repay the bond: "))
    repayment_calculation = (interest_rate * present_value) / (1 - (1 + interest_rate) ** (-num_months))
    repayment = str(repayment_calculation)
    print("The amount you will repay each month on your bond is: " + repayment)

 # Calculates and returns repayment value if user selects "bond"









 

