import streamlit as st

def find_largest(num1, num2, num3):
    # Find the largest number
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest

# Create Streamlit web app
def main():
    # Set app title and description
    st.set_page_config(page_title="Largest Number Calculator", page_icon=":1234:",
                        layout="wide", initial_sidebar_state="expanded")

    # Add app title and header
    st.title("Largest Number Calculator")
    st.header("Enter three numbers below:")

    # Set up the user input fields
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        num1 = st.number_input("Number 1", value=0.0, step=0.1)
    with col2:
        num2 = st.number_input("Number 2", value=0.0, step=0.1)
    with col3:
        num3 = st.number_input("Number 3", value=0.0, step=0.1)

    # Calculate the largest number
    largest = find_largest(num1, num2, num3)

    # Display the result
    st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
