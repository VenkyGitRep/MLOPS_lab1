def addNums(a,b):
    print("Adding ",a," and ",b, ". Result: ",(a+b))
    return (a+b)

addNums(2,3)

#power function
def powNums(base, exponent):
        result = 1
        for _ in range(exponent):
            result *= base
        print("Power", base, "and", exponent, " Result:", result)
        return result

powNums(2,3)