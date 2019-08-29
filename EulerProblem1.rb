=begin  Marcelo Zometa ©2019
        #Last edited solution 08/29/2019
        Solution to first problem of Euler problem https://projecteuler.net/problem=1
=end

#main(): driver function
def main()

    sum_ = 0;
    i = 0;

    #Loop to repeat until i equals 1000
    until i == 1000 do

        if (i % 3 == 0) or (i % 5 == 0)
            sum_ = increaseSum(sum_, i);
        end

        i += 1;
    end

    puts "The final result is ";
    puts sum_;
end

#increaseSum(sum, num): increments the running sum.
def increaseSum(sum, num)
    return sum += num;
end

main();