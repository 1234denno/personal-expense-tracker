import streamlit as st
import db
import pandas as pd

st.set_page_config(page_title="Expense Tracker", layout="wide")

st.title("💸 Personal Expense Tracker")

# Sidebar form
st.sidebar.header("Add New Expense")
with st.sidebar.form("expense_form"):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Bills", "Entertainment", "Other"])
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    description = st.text_area("Description")
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        db.add_expense(date, category, amount, description)
        st.sidebar.success("Expense added!")

# Display expenses
st.header("All Expenses")
expenses = db.get_expenses()
df = pd.DataFrame(expenses, columns=["ID", "Date", "Category", "Amount", "Description"])
st.dataframe(df)

# Summary
st.header("Summary by Category")
summary = df.groupby("Category")["Amount"].sum().reset_index()
st.bar_chart(summary.set_index("Category"))

