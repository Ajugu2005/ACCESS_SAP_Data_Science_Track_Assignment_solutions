# Assignment: Python Function & Data Handling
#Task: Write a function that takes a list of transaction amounts and prints the following:

import numpy as np
list_of_trans_amounts = [
    150.50, 200.00, 45.00, 1200.75, 89.99, 340.00, 15.25, 670.00, 25.00, 110.00,
    950.00, 45.50, 30.00, 1500.00, 210.40, 55.00, 12.99, 88.00, 430.25, 75.00,
    120.00, 18.50, 99.99, 2200.50, 65.00, 310.00, 14.00, 580.00, 40.00, 105.00,
    890.00, 38.50, 25.00, 1350.00, 205.10, 60.00, 11.50, 92.00, 415.75, 80.00,
    130.00, 22.50, 85.99, 2100.00, 55.00, 325.00, 16.00, 600.00, 42.00, 115.00
]

np_array = np.array(list_of_trans_amounts)

#Total sum: The addition of all transaction values in the list.

total_sum = np.sum(list_of_trans_amounts)
print(f"Total Sum: {total_sum}")


#Average: The mean value of the transactions.

average = np.mean(list_of_trans_amounts)
print(f"Average: {average}")

#Number of transactions: The total count of items present in the list.

count_in_list = np.size(list_of_trans_amounts)
print(f"Number of Transactions: {count_in_list}")