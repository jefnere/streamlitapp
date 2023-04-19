import streamlit as st

def find_largest_num(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

st.title("Find the largest among the 3 given numbers")
st.write("Enter three numbers below:")

a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
c = st.number_input("Enter the third number:")

if st.button("Find largest number"):
    largest = find_largest_num(a, b, c)
    st.write(f"The largest number is {largest}.")
