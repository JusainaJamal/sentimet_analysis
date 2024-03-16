# import os
# import streamlit as st

# # Function to read user details from the text file
# def welcome():
#     st.title("Welcome Page")
#     st.write("Welcome to the app!")



# def read_user_details():
#     if not os.path.exists("user_details.txt"):
#         return []
#     with open("user_details.txt", "r") as file:
#         lines = file.readlines()
#         user_details = [line.strip().split(",") for line in lines]
#     return user_details

# # Function to write user details to the text file
# def write_user_details(username, password):
#     with open("user_details.txt", "a") as file:
#         file.write(f"{username},{password}\n")

# # Function to check if the username already exists
# def check_existing_username(username, user_details):
#     usernames = [user[0] for user in user_details]
#     return username in usernames

# # Function to authenticate user
# def authenticate_user(username, password, user_details):
#     for user in user_details:
#         if user[0] == username and user[1] == password:
#             return True
#     return False

# # Function to display welcome page

# # Function to clear session state and redirect to login page
# def logout():
#     st.session_state.logged_in = False

# # Streamlit app starts here
# st.title("Login and Signup Example")

# # Page state variables
# is_login_page = st.sidebar.radio("Page", ("Login", "Signup"))
# if is_login_page == "Signup":
#     st.subheader("Signup")
#     new_username = st.text_input("Enter username")
#     new_password = st.text_input("Enter password", type="password")
#     confirm_password = st.text_input("Confirm password", type="password")

#     if st.button("Signup"):
#         if new_password != confirm_password:
#             st.error("Passwords do not match!")
#         else:
#             user_details = read_user_details()
#             if check_existing_username(new_username, user_details):
#                 st.error("Username already exists!")
#             else:
#                 write_user_details(new_username, new_password)
#                 st.success("Signup successful! Please login.")

# if is_login_page == "Login":
#     st.subheader("Login")
#     username = st.text_input("Enter username")
#     password = st.text_input("Enter password", type="password")

#     if st.button("Login"):
#         user_details = read_user_details()
#         if authenticate_user(username, password, user_details):
#             st.session_state.logged_in = True
#             st.success("Login successful!")
#         else:
#             st.error("Invalid username or password!")

# # Check if user is logged in
# if st.session_state.get("logged_in"):
#     # Clear the login page content
#     st.empty()
#     # Display the welcome page
#     welcome()  
#     # Add your dashboard content here
#     # Add logout button
#     st.button("Logout", on_click=logout)





# import os
# import streamlit as st

# # Function to read user details from the text file
# def read_user_details():
#     if not os.path.exists("user_details.txt"):
#         return []
#     with open("user_details.txt", "r") as file:
#         lines = file.readlines()
#         user_details = [line.strip().split(",") for line in lines]
#     return user_details

# # Function to write user details to the text file
# def write_user_details(username, password):
#     with open("user_details.txt", "a") as file:
#         file.write(f"{username},{password}\n")

# # Function to check if the username already exists
# def check_existing_username(username, user_details):
#     usernames = [user[0] for user in user_details]
#     return username in usernames

# # Function to authenticate user
# def authenticate_user(username, password, user_details):
#     for user in user_details:
#         if user[0] == username and user[1] == password:
#             return True
#     return False

# # Function to display welcome page
# def welcome():
#     st.title("Welcome Page")
#     st.write("Welcome to the app!")

# # Function to clear session state and redirect to login page
# def logout():
#     st.session_state.logged_in = False

# # Streamlit app starts here
# st.title("Login and Signup Example")

# # Page state variables
# is_login_page = st.sidebar.radio("Page", ("Login", "Signup"))

# if st.session_state.get("logged_in"):
#     # User is logged in, show the welcome page
#     welcome()   # Display the welcome page
#     st.button("Logout", on_click=logout)  # Add logout button

# elif is_login_page == "Signup":
#     st.subheader("Signup")
#     new_username = st.text_input("Enter username")
#     new_password = st.text_input("Enter password", type="password")
#     confirm_password = st.text_input("Confirm password", type="password")

#     if st.button("Signup"):
#         if new_password != confirm_password:
#             st.error("Passwords do not match!")
#         else:
#             user_details = read_user_details()
#             if check_existing_username(new_username, user_details):
#                 st.error("Username already exists!")
#             else:
#                 write_user_details(new_username, new_password)
#                 st.success("Signup successful! Please login.")

# elif is_login_page == "Login":
#     st.subheader("Login")
#     username = st.text_input("Enter username")
#     password = st.text_input("Enter password", type="password")

#     if st.button("Login"):
#         user_details = read_user_details()
#         if authenticate_user(username, password, user_details):
#             st.session_state.logged_in = True
#         else:
#             st.error("Invalid username or password!")





import os
import streamlit as st

# Function to read user details from the text file
def read_user_details():
    if not os.path.exists("user_details.txt"):
        return []
    with open("user_details.txt", "r") as file:
        lines = file.readlines()
        user_details = [line.strip().split(",") for line in lines]
    return user_details

# Function to write user details to the text file
def write_user_details(username, password):
    with open("user_details.txt", "a") as file:
        file.write(f"{username},{password}\n")

# Function to check if the username already exists
def check_existing_username(username, user_details):
    usernames = [user[0] for user in user_details]
    return username in usernames

# Function to authenticate user
def authenticate_user(username, password, user_details):
    for user in user_details:
        if user[0] == username and user[1] == password:
            return True
    return False

# Function to display welcome page
def welcome():
    st.title("Welcome Page")
    st.write("Welcome to the app!")

# Function to clear session state and redirect to login page
def logout():
    st.session_state.logged_in = False

# Streamlit app starts here
st.title("Login and Signup Example")

# Page state variables
is_login_page = st.sidebar.radio("Page", ("Login", "Signup"))

if st.session_state.get("logged_in"):
    # User is logged in, show the welcome page
    welcome()   # Display the welcome page
    st.button("Logout", on_click=logout)  # Add logout button

elif is_login_page == "Signup":
    st.subheader("Signup")
    new_username = st.text_input("Enter username")
    new_password = st.text_input("Enter password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")

    if st.button("Signup"):
        if new_password != confirm_password:
            st.error("Passwords do not match!")
        else:
            user_details = read_user_details()
            if check_existing_username(new_username, user_details):
                st.error("Username already exists!")
            else:
                write_user_details(new_username, new_password)
                st.success("Signup successful! Please login.")

elif is_login_page == "Login":
    st.subheader("Login")
    username = st.text_input("Enter username")
    password = st.text_input("Enter password", type="password")

    if st.button("Login"):
        user_details = read_user_details()
        if authenticate_user(username, password, user_details):
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Invalid username or password!")
