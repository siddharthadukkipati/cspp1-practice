"""
Exercise: GCD_iter
Write a_inp Python function, gcd_iter(a_inp, b_inp), that takes in two numbers and returns
the GCD_op(a_inp,b_inp) of given a and b_inp.
This function takes in two numbers and returns one number.
"""
def gcd_iter(a_inp, b_inp):
    """
    a_inp, b_inp: positive integers
    returns: a_inp positive integer, the greatest common divisor of a_inp & b_inp.
    """
    # Your code here
    i = 1
    gcd_op = 1
    small_check = min(a_inp, b_inp)
    while i <= small_check:
        if a_inp%i == 0:
            if b_inp%i == 0:
                if i > 1:
                    gcd_op = i
        i += 1
    return gcd_op

def main():
    """ calling function"""
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
