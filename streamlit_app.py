import streamlit as st

# Streamlit app title
st.title('Savings Calculator💰 by Jose Cedeno')

# Input fields 
apr = st.number_input("Enter the Annual Percentage Rate (APR) as a percentage:", min_value=0.0, format='%f') / 100
years = st.number_input("Enter the number of years:", min_value=0, format='%d')
pv = st.number_input("Enter the Initial deposit:", min_value=0.0, format='%f')

# Contribution frequency dropdown (weekly, monthly, annual)
contribution_period = st.selectbox("Select contribution frequency:", ("Weekly", "Monthly", "Annually"))

# Determine appropriate label based on period:
label = "Enter the amount you contribute" if contribution_period == "Annually" else "Enter the amount for each contribution"

# Contribution input based on period
contribution_pmt = st.number_input(label + ":", min_value=0.0, format='%f')

# Set compounding and contribution terms based on user frequency choice
if contribution_period == "Weekly":
    n = 52  # Weekly compounding periods
    # Convert annual APR to weekly interest rate
    r = apr / 52
    total_periods = years * 52  # Total number of weekly payments over `t` years
elif contribution_period == "Monthly":
    n = 12  # Monthly compounding periods
    # Convert annual APR to monthly interest rate
    r = apr / 12
    total_periods = years * 12  # Total number of monthly payments 
else:
    n = 1  # Yearly compounding periods (no fraction)
    r = apr  # APR remains as is for annual contributions
    total_periods = years

# Calculate Future Value
if st.button('Calculate Future Value'):

    # Future value calculation with compound interest
    fv_with_apr = pv * (1 + r)**(n * years) + contribution_pmt * (((1 + r)**total_periods - 1) / r)

    # Calculate future value without APR (just savings)
    fv_without_apr = pv + contribution_pmt * total_periods

    # Display the results
    st.success(f"The future value of your savings with regular {contribution_period.lower()} contributions of ${contribution_pmt:,.2f} is: ${fv_with_apr:,.2f}")
    st.success(f"The future value of your savings without interest (just savings) is: ${fv_without_apr:,.2f}")
