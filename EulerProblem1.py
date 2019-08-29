#Marcelo Zometa ©2019
#Last edited solution 08/28/2019
#Solution to first problem of Euler problem https://projecteuler.net/problem=1

#main(): driver function
def main():    
    sum_ = 0
    i = 0

    #Loop for cicling through 1 to 1000
    while (i < 1000):
        if (i % 3 == 0) or (i % 5 == 0):
            #Increasing the running sum.
            sum_ = increaseSum(sum_, i)
        i += 1

    print("The sum equals ", sum_)

#increaseSum(sum, num): increases the running sum.
def increaseSum(sum, num):
    sum += num
    return sum

#Calling of main to run.
main()