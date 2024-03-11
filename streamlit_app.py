import streamlit as st

# Streamlit app title
st.title('Savings Calculator by Jose Cedeno')

# Input fields
apr = st.number_input("Enter the Annual Percentage Rate (APR) as a percentage:", min_value=0.0, format='%f') / 100
years = st.number_input("Enter the number of years:", min_value=0, format='%d')
weekly_pmt = st.number_input("Enter the weekly deposit:", min_value=0.0, format='%f')
pv = st.number_input("Enter the Initial deposit:", min_value=0.0, format='%f')

n = 12  # Compounded monthly for interest calculation
t = years
r = apr

if st.button('Calculate Future Value'):
    # Calculate total monthly deposit from weekly deposits
    monthly_pmt = weekly_pmt * 4.33

    # Calculate future value with APR using compound interest formula
    fv_with_apr = pv * (1 + r/n)**(n*t) + monthly_pmt * (((1 + r/n)**(n*t) - 1) / (r/n))

    # Calculate future value without APR (just savings)
    total_weeks = years * 52  # Total number of weeks over the period
    fv_without_apr = pv + weekly_pmt * total_weeks

    # Display the results
    st.success(f"The future value of your savings with an initial deposit of $ {pv:,.2f } after { years} years with an APR of { apr:.2%} and a weekly deposit of $ { weekly_pmt:,.2f} is: $ { fv_with_apr:,.2f}")
    st.success(f"The future value of your savings without any APR, just the initial deposit and weekly deposits, is: ${ fv_without_apr:,.2f}")
