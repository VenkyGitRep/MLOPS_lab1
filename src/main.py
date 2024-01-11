def addNums(a,b):
    print("Adding ",a," and ",b, ". Result: ",(a+b))
    return (a+b)

addNums(2,3)


def multNums(a,b):
    print("Multiplying ",a," and ",b, ". Result: ",(a*b))
    return (a*b)

multNums(2,3)


def divNums(a,b):
    if b==0:
        print("Invalid division operation.")
    else:
        return(a/b)

divNums(2,3)