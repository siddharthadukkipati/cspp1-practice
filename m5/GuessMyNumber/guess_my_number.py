"""Guess My Number Exercise"""

def main():
    """
    To check the secret number
    """
    print("Please select a number between 0 to 100")
    least_a = 0
    higher_a = 100
    guess_a = (least_a+higher_a)//2
    for _ in range(0, 100):
        print("Is your secret number " +str(guess_a))
        inp_a = input("enter 'h' if number is lower, enter 'l' if higher else enter 'c'")
        if inp_a == 'h':
            higher_a = guess_a
        elif inp_a == 'l':
            least_a = guess_a
        elif inp_a == 'c':
            break
        guess_a = (least_a + higher_a)//2
    print("Your secret number is: " +str(guess_a))
if __name__ == "__main__":
    main()
