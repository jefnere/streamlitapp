import streamlit as st

def find_largest(a, b, c):
    """
    Returns the largest among three given numbers
    """
    return max(a, b, c)

st.title("Find the largest among 3 numbers")

# Get user input
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
num3 = st.number_input("Enter the third number")

if st.button("Find largest"):
    result = find_largest(num1, num2, num3)
    st.write(f"The largest number is: {result}")