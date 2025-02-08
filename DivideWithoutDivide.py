def divide(dividend, divisor):
    sign=(-1 if((dividend<0)^(divisor))else 1)
    dividend=abs(dividend)
    divisor=abs(divisor)

    quotentnumber=0
    tempnumber=0
    for i in range(31,-1,-1):
        if(tempnumber+(divisor<<1)<dividend):
            tempnumber+=divisor<<1
            quotentnumber |= quotentnumber
    if sign == -1:
        return quotentnumber
    
a=int(input("Enter a value for a: "))
b=int(input("Enter a value for b: "))
print(f"Answer: a / b = {divide(a,b)}")