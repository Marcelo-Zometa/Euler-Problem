This program will give the solution to the Euler Problem number 1 
which reads:

"If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."  Source: https://projecteuler.net/problem=1

To run this program open a new terminal in VS Code (making sure to have
installed the Docker and Remote controllers modules). Then, in the terminal 
move to the folder location "workspaces/vscode-dev-containers/containers/python-3-anaconda/test-project/EulerProblem1#"

Then, type the following command: "python EulerProblem1.py" and watch the magic!

Some important functions are:

* main(): it is the driver of the program. Holds a loop to cicle through the numbers from 1 to 1000
* increaseSum(sum, num): increments the running sum of the system.

And some important variables are:

* sum_: it is the running sum of the program.
* i: counter for the while loop.