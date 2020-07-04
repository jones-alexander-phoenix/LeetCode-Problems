from itertools import permutations
import re

#Problem 2

def clean_matrix(matrix):
    p = re.compile('0*(0*1{1}0*2{1}0*)*0*')
    print(matrix)
    buy_string = ''.join(str(i) for i in matrix)
    m = p.fullmatch(buy_string)
    if m:
        if len(m.group(0)) != len(buy_string):
            return False
        else:
            return True

def create_frameworks(values):
    matrix_length = len(values)
    matrix_values = ["0","1","2"]
    max_count = int(round(matrix_length/3))
    zero_count = matrix_length % 3
    matrix_frameworks = []
    matrices = []
    for i in range(0, max_count):
        if i == 0:
            pass
        elif i > 1:
            max_possible_values = matrix_values + ((i)*matrix_values)
            if len(max_possible_values) < matrix_length:
                max_possible_values = max_possible_values + (["0"] * (matrix_length - len(max_possible_values)))
            matrix_frameworks.append(max_possible_values)
    for i in matrix_frameworks:
        all_permutations = permutations(i)
        for matrix in set(all_permutations):
            if clean_matrix(matrix):
                matrices.append(matrix)
    return matrices


def max_profit(prices):
    #init vars
    profit = []
    buy_sell_matrices = create_frameworks(prices)
    #Step through matrices
    for matrix in buy_sell_matrices:
        iprofit = 0
        zipped = list(zip(matrix, prices))
        for action, price in zipped:
            if action == "1":
                iprofit = iprofit - price
            if action == "2":
                iprofit = iprofit + price
        profit.append(iprofit)
    try:
        if max(profit) < 0:
            return 0
        else:
            return max(profit)
    except ValueError:
        return 0

prices =[1,4,2]
print(max_profit(prices))





