"""Exercise: PowerIter
Write a Python function, iter_power(base, exp_inp), that takes in two numbers
and returns the base^(exp) of given base and exp.
This function takes in two numbers and returns one number.
"""

def iter_power(base_inp, exp_inp):
    """
    base_inp: int or float.
    exp: int >= 0
    returns: int or float, base_inp^exp
    """
    # Your code here
    power_val = 1
    while exp_inp != 0:
        power_val *= base_inp
        exp_inp -= 1
    return power_val

def main():
    """calling function"""
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
