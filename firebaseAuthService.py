import pyrebase # pyrebase4
from firebaseConfig import config

def getToken(email, password):
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()

    try:
        user = auth.sign_in_with_email_and_password(email, password)
    except Exception as err:
        print(f"Failed to login with error: \n {err}")
        print("attempting to create a new user")
        user = auth.create_user_with_email_and_password(email, password)

    return user['idToken']




