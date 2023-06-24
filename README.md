# Question : Minimum number of denominations
Logic:
   
* The logic of this code is to calculate the minimum number of denominations required to provide change for a given amount of money using a dynamic programming approach.
* The available denominations are stored in the list denominations.
* The dynamic programming array dp is initialized with infinity values except for dp[0] which is set to 0.
* A 2D matrix coins is created to store the number of coins for each denomination.
* The code then iterates through the dynamic programming loop, considering each amount from 1 to the given amount.
* For each amount, it checks all denominations to find the minimum number of coins required.
* If a smaller number of coins is found, it updates the dp array and coins matrix accordingly.
* Finally, it returns the minimum number of denominations and the matrix coin_count containing the number of coins for each denomination.
* The function is tested by taking user input for the amount and then printing the minimum number of denominations and the number of coins for each denomination.
Commands:
    To run the code we have to run the following commands:
    1. Go to terminal and type python3 main.py
Miscellaneous:
    Description of almost every command used is given in comments of my python code.