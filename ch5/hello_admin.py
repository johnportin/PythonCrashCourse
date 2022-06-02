usernames = ['jack', 'jill', 'pickle', 'hill', 'admin']

greeting_admin = "Hello, admin, would you like to see a status report"

for username in usernames:
    if username == 'admin':
        print("Hello, admin, would you like to see a status report")
    else:
        print(f"Hello, {username}. Thank you for loggin in today.")
