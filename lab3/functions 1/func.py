def grams(gram):
    ounces = 0.03527396 * gram
    return ounces
gram=float(input("gram:"))
print("ounces=",grams(gram))


def temperature(F):
    C =  (5 / 9) * (F - 32) 
    return C
F=float( input ("Fahrenheit: ") )
print( "celcie:", temperature(F) )

def histogram(lst):
    for num in lst:
        print("*" * num)

histogram([4, 9, 7])
