from pyscript import document, window  # Import PyScript modules to interact with HTML elements and browser

# ----------------------------
# Function: create_account
# ----------------------------
# Purpose: Validates username and password, and displays a message if an account is created or missing fields.
def create_account(event):
    # Get values from input fields
    username = document.getElementById("username").value
    password = document.getElementById("password").value

    # Check if password is empty
    if password == '':
        message = "You need a password to make an account"

    # Check if username is empty
    elif username == '':
        message = "You need a username to make an account"

    # Both fields are filled
    else:
        message = f"Your username is {username}"

    # Display the message in the HTML paragraph with id="account"
    document.getElementById("account").innerText = message


# ----------------------------
# Function: proceed
# ----------------------------
# Purpose: Checks if the user has created an account. If yes, redirect to another page; if not, show an error.
def proceed(event):
    # Get the current message displayed in the account paragraph
    account_text = document.getElementById("account").innerText

    # If no account has been created, show an error
    if account_text == "" or "Your username is" not in account_text:
        document.getElementById("account").innerText = "Make an account first"

    # If account exists, navigate to the "teamchecker.html" page
    else:
        window.location.href = "teamchecker.html"


# ----------------------------
# Function: sign
# ----------------------------
# Purpose: Determines team assignment based on the user's grade, section, and certain registration requirements.
def sign(event):
    # Get values from grade and section input fields
    grade = document.getElementById("grade").value
    section = document.getElementById("sec").value

    # Check if the user hasn't registered online
    if document.getElementById("no").checked:
        document.getElementById("result").innerHTML = "You need to register online"

    # Check if the user needs medical clearance
    elif document.getElementById("noo").checked:
        document.getElementById("result").innerHTML = "You need medical clearance"

    # ----------------------------
    # Team Assignment Logic
    # ----------------------------
    # Grade 7
    elif grade == "7" and section == "emerald":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Red Bulldogs"
    elif grade == "7" and section == "ruby":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Yellow Tigers"
    elif grade == "7" and section == "sapphire":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Green Hornets"
    elif grade == "7" and section == "topaz":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Blue Bears"

    # Grade 8
    elif grade == "8" and section == "ruby":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Red Bulldogs"
    elif grade == "8" and section == "emerald":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Yellow Tigers"
    elif grade == "8" and section == "topaz":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Green Hornets"
    elif grade == "8" and section == "sapphire":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Blue Bears"

    # Grade 9
    elif grade == "9" and section == "emerald":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Red Bulldogs"
    elif grade == "9" and section == "ruby":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Yellow Tigers"
    elif grade == "9" and section == "sapphire":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Green Hornets"
    elif grade == "9" and section == "topaz":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Blue Bears"

    # Grade 10
    elif grade == "10" and section == "ruby":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Red Bulldogs"
    elif grade == "10" and section == "emerald":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Yellow Tigers"
    elif grade == "10" and section == "topaz":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Green Hornets"
    elif grade == "10" and section == "sapphire":
        document.getElementById("result").innerHTML = "Congratulations! You are part of the Blue Bears"

    # If no conditions match (invalid input or missing requirements)
    else:
        document.getElementById("result").innerHTML = "Fill out your requirements first"