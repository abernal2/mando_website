import streamlit as st

st.markdown(
    """
    # Approximate Profit Calculation
"""
)

loan_amount = st.number_input("Loan Amount", value=0.0, step=0.01, format="%.2f")
sale_price = st.number_input("Sale Price", value=0.0, step=0.01, format="%.2f")
commission = st.number_input("Commission", value=4.5, step=0.01, format="%.2f")
commission = commission/100.0

closing_pct = st.number_input("Closing Costs", value=2.0, step=0.01, format="%.2f")
closing_pct = closing_pct/100.0
holding_cost_per_month = st.number_input("Holding Cost Per Month", value=0.0, step=0.01, format="%.2f")
holding_months = st.number_input("Months Holding", value=1, step=1)

heloc = st.number_input("HELOC Interest", value=0.0, step=0.01, format="%.2f")
electrical = st.number_input("Electrical", value=0.0, step=0.01, format="%.2f")
hvac = st.number_input("HVAC", value=0.0, step=0.01, format="%.2f")
plumbing = st.number_input("Plumbing", value=0.0, step=0.01, format="%.2f")
extra = electrical = st.number_input("Extra Construction", value=0.0, step=0.01, format="%.2f")

if st.button('Compute'):
    equity_amount = sale_price - loan_amount
    st.write(f'Equity Amount = ${equity_amount:,.02f}')
    equity = (1 - (loan_amount/sale_price)) * 100.0
    st.write(f'Equity = {equity:.02f}%')
    closing_cost = sale_price * closing_pct
    st.write(f'Closing costs = ${closing_cost:,.02f}')
    commission_cost = sale_price * commission
    st.write(f'Commission costs = ${closing_cost:,.02f}')

    total_fees = commission_cost + \
                closing_cost + \
                extra + plumbing +\
                hvac + electrical +\
                heloc + \
                holding_months * holding_cost_per_month
    
    st.write(f'Profit = ${equity_amount - total_fees:,.02f}')
