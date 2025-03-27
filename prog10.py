weights = [9, 5, 8, 7, 4, 6]
values = [12, 9, 14, 10, 16, 8]
capacity = 20

max_profit = 0
A = [0] * 6
optimal = " "

while A [0] * weights [0] <= capacity :
    A [1] = 0
    profit = A [0] * values [0]
    while A [1] * weights [1] <= capacity - A [0] * weights [0]:
        A [2] = 0
        while ( A [2] * weights [2] <= capacity - A [0] * weights [0] - A [1] * weights [1]) :
            A [3] = 0
            while ( A [3] * weights [3] <= capacity - A [0] * weights [0] - A [1] * weights [1] - A [2] * weights [2]) :
                A [4] = 0
                while ( A [4] * weights [4] <= capacity - A [0] * weights [0] - A [1] * weights [1] - A [2] * weights [2] - A [3] * weights [3]) :
                    A [5] = 0
                    while ( A [5] * weights [5] <= capacity - A [0] * weights [0] - A [1] * weights [1] - A [2] * weights [2] - A [3] * weights [3] - A [4] * weights [4]) :
                        profit = A [0] * values [0]
                        profit += A [1] * values [1]
                        profit += A [2] * values [2]
                        profit += A [3] * values [3]
                        profit += A [4] * values [4]
                        profit += A [5] * values [5]
                        if profit > max_profit :
                            max_profit = profit
                            optimal = str ( A [0]) + " , "
                            optimal += str ( A [1]) + " , "
                            optimal += str ( A [2]) + " , "
                            optimal += str ( A [3]) + " , "
                            optimal += str ( A [4]) + " , "
                            optimal += str ( A [5])
                        A [5] += 1
                    A [4] += 1
                A [3] += 1
            A [2] += 1
        A [1] += 1
    A [0] += 1


print ( " Max cost : " + str ( max_profit ) )
print ( " x1 x2 x3 x4 x5 x6 " )
print ( optimal )