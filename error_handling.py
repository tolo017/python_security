try:
    # The risky action: Trying to open a file that might be deleted
    with open("secret_passwords.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    # The safety net: What to do if the file is not there
    print("ALERT: The password file is missing! Did a hacker delete it?")