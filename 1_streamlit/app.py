import streamlit as st

# Define example

st.title("Example Streamlit App")

st.markdown("""
### Assorted Inputs
""")

name = st.text_input("Name", "John Doe")
age = st.number_input("Age", 18, 100, 25)
email = st.text_input("Email")

# Define a button

if st.button("Submit"):
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Email: {email}")

    # Show some green text
    st.success("Form submitted successfully.")

# Two columns
cols = st.columns(2)

cols[0].warning("This is a warning in the first column.")
cols[1].info("This is an info message in the second column.")