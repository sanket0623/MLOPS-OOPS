class Chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedIn = False

        self.menu()

    def menu(self):
        user_input = input("""
            Welcome to chatbook. Now you would like to proceed:
            1. Press 1 to signup
            2. Press 2 to login
            3. Press 3 to write a post
            4. Press 4 to send a message
            Please any other key to quit.
            -> 
            """)

        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.post()
        elif user_input == '4':
            self.send_message()
        else:
            print('Existing chat menu....')
            exit()

    def signup(self):
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        self.username = email
        self.password = password
        print("you have been signed up successfully! \n")

        self.show_menu()

    def signin(self):
        if self.username == '' or self.password == '':
            print('Please signup first by pressing 1!')
        else:
            print('Please share below details')
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            if self.username == email and self.password == password:
                self.loggedIn = True
                print('Login successfully!')
            else:
                print('Wrong username or password. Please try again by pressing 2!')

        self.show_menu()

    def post(self):
        if not self.loggedIn:
            print('You are not logged in. Please login first!')
        else:
            post = input('Enter your message: ')
            print('Your post is:', post)

        self.show_menu()

    def send_message(self):
        if not self.loggedIn:
            print('You are not logged in. Please login first!')
        else:
            message = input('Enter your message: ')
            print('Your message ' + message + ', has been sent successfully')

        self.show_menu()


    def show_menu(self):
        self.menu()
