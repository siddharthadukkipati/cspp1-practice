"""odd tuples"""

def oddTuples(aTup):
    """tuples function"""
    tup_a=()
    for j in range(0, len(aTup), 2):
        tup_a = tup_a +(aTup[j],)
    return tup_a
def main():
    """callling function"""
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += ((data[j]),)
    print(oddTuples(aTup))

if __name__ == "__main__":
    main()
    