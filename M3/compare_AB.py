"""compare A & B"""
def is_instance(parameter):
    """returns type of a variable"""
    return type(parameter)

VARA = 123
VARB = "String"

STRING_TYPE = "string"

if is_instance(VARA) == is_instance(STRING_TYPE) or is_instance(VARB) == is_instance(STRING_TYPE):
    print("one of the variables is String")
elif VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
else:
    print("smaller")
