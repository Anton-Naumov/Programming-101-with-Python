from sql_manager import SQLManager
from getpass import getpass
from exceptions import InvalidPassword, UsernameTaken, BruteForce, UserNotRegistered


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            email = input("Enter your email: ")

            try:
                SQLManager.register(username, password, email)
                print("Registration Successfull")
            except (InvalidPassword, UsernameTaken) as e:
                print(str(e))
                break

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")

            try:
                logged_user = SQLManager.login(username, password)
            except BruteForce as e:
                print(str(e))
            else:
                if logged_user:
                    logged_menu(logged_user)
                else:
                    print("Login failed")
        elif command.split(' ')[0] == 'send-reset-password':
            try:
                SQLManager.send_email_to_user(command.split(' ')[1])
                print('The email was sent!')
            except UserNotRegistered as e:
                print(str(e))
        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print('send-reset-password <username>- for sending password reset email to the user')
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass("Enter your new password: ")
            SQLManager.change_pass(new_pass, logged_user)
        elif command.split(' ')[0] == 'deposit':
            try:
                SQLManager.deposit_money(command.split(' ')[1], logged_user)
            except Exception as e:
                print(str(e))
        elif command.split(' ')[0] == 'withdraw':
            try:
                SQLManager.withdraw_money(command.split(' ')[1], logged_user)
            except Exception as e:
                print(str(e))
        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("deposit <amount> - for depositing money")
            print("withdraw <amount> - for withdrawing money")


def main():
    SQLManager.initialize_database(dbname='bank', user='anton')
    SQLManager.create_clients_table()
    main_menu()
    SQLManager.close_database()


if __name__ == '__main__':
    main()
