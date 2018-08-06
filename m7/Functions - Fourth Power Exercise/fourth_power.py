"""
Exercise: fourth power
Write a Python function, fourthPower, that takes in one number and returns
that value raised to the fourth power.
You should use the square procedure that you defined in an earlier exercise
exercise (you don't need to redefine square in this box;
This function takes in one number and returns one number.
"""

def square(x):
    """ square function"""
    #x: int or float.
    square_power = x**2
    return square_power

def fourthPower(x):
    """ fourth power"""
    #x: int or float.
    # fourth_Power = x**4
    return square(square(x))

def main():
    """ main program """
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourthPower(int(float(str(data)))))
    else:
        print(fourthPower(data))

if __name__ == "__main__":
    main()
