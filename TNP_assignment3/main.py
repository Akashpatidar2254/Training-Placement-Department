import quiz as qz
import question_bank as qb

logged_user = ""
is_logged = False
import pandas as pd

df = pd.read_excel(r"C:\Users\HP\OneDrive\Documents\TNP_assignment3_dataSheet.xlsx")


def register():
    global df

    print("______Register new user__________")
    new_username = input("Enter your username: ").strip()

    if new_username in df["username"].values:
        print("Username already registered")
    else:
        name = input("Enter your full name: ")
        password = input("Enter your password: ").strip()
        email = input("Enter your email address: ").strip()

        if df.empty:
            next_s_no = 1
        else:
            next_s_no = int(df['s.no'].max()) + 1

        new_row_data_dic = {
            "s.no": [next_s_no],
            "username": [new_username],
            "name": [name],
            "email": [email],
            "password": [password]
        }

        new_row_df = pd.DataFrame(new_row_data_dic)
        updated_df = pd.concat([df, new_row_df], ignore_index=True)

        updated_df.to_excel(r"C:\Users\HP\OneDrive\Documents\TNP_assignment3_dataSheet.xlsx", index=False)
        df = updated_df

        print(f"Registration successful for {new_username}!")
    main()


def login():
    global logged_user
    global is_logged

    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if username not in df["username"].values:
        print("Username not found")
    else:
        user_row = df[df["username"] == username]
        stored_password = user_row["password"].values[0]
        if str(stored_password) == password:
            logged_user = username
            is_logged = True
            print("Login successful")
        else:
            print("incorrect password")
    main()


def show_profile():
    if is_logged:
        user_row = df[df["username"] == logged_user]
        username = user_row["username"].values[0]
        name = user_row["name"].values[0]
        email = user_row["email"].values[0]

        print(f"Username: {username}")
        print(f"Name: {name}")
        print(f"Email: {email}")
    else:
        print("you must be logged in to show profile")
    main()


def update_profile():
    if is_logged:
        new_name = input("Enter new full name (or press Enter to skip): ")
        new_email = input("Enter new email (or press Enter to skip): ")
        new_password = input("Enter new password (or press Enter to skip): ")
        if new_name:
            df.loc[df["username"] == logged_user, "name"] = new_name
            print("Name updated.")

        if new_email:
            df.loc[df["username"] == logged_user, "email"] = new_email
            print("Email updated.")

        if new_password:
            df.loc[df["username"] == logged_user, "password"] = new_password
            print("Password updated.")
        df.to_excel(r"C:\Users\HP\OneDrive\Documents\TNP_assignment3_dataSheet.xlsx", index=False)
    else:
        print("you must be logged in to update profile")
    main()


def logout():
    global logged_user
    global is_logged
    if is_logged:
        print(f"Logout successful for {logged_user}")
        logged_user = ""
        is_logged = False
    else:
        print("you must be logged in first to logout")
    main()


def terminate():
    print("exiting..")
    exit()


def attempt_quiz():
    if is_logged:
        choice = int(input("""
        choose 1:PYTHON
        choose 2:DBMS
        choose 3:DSA
        Enter choice: """).strip())

        if choice == '1':
            qz.start_quiz(qb.python_quiz)
        elif choice == '2':
            qz.start_quiz(qb.dbms_quiz)
        elif choice == '3':
            qz.start_quiz(qb.dsa_quiz)
        else:
            print("Invalid choice.")
    main()


def main():
    print('')
    print(".....Welcome to LNCT Portal....")
    response = input("""Choose option:

1. Registration
2. Login
3. Profile
4. Update profile
5. Logout
6. Main Menu
7. Exit
8. attempt Quiz

Select option (1/2/3/4/5/6/7/8): """).strip()

    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        logout()
    elif response == '6':
        print("\n--- Returning to Main Menu ---")
        main()
    elif response == '7':
        terminate()
    elif response == '8':
        attempt_quiz()
    else:
        print("Invalid choice. Please try again.")
        main()

main()