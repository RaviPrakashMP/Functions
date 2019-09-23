def get_username():
    """
    Prompt the user to enter his name
    Input : None
    Output : Return the user input as a string
    """
    print("Hello","Ravi")

def say_hello(user):
    '''
    Greet the user by saying Hello followed by his name
    Input : User name
    Output : Greeting statement on the screen. No return value
    Example : If input string is Sam
        Then the expected output is
        Hello Sam !!!
    '''
    print("Hello","World!!!")

def main():
    '''
    Main function of the program
    '''
    name = get_username()
    say_hello(name)
main()
        
