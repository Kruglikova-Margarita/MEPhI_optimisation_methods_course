resourse = [[0, 0, 0, 0, 0, 0],
            [3, 1, 2, 4, 6, 5],
            [4, 5, 8, 1, 4, 4],
            [6, 4, 3, 7, 7, 3],
            [2, 7, 1, 2, 3, 2],
            [5, 3, 5, 9, 5, 1],
            [6, 1, 7, 4, 2, 4]]

max_profit = 0
optimal = ""

for a_1 in range(7):
    for a_2 in range(7-a_1):
        for a_3 in range(7-a_1-a_2):
            for a_4 in range(7-a_1-a_2-a_3):
                for a_5 in range(7-a_1-a_2-a_3-a_4):
                    for a_6 in range(7-a_1-a_2-a_3-a_4-a_5):
                        profit = resourse[a_1][0] + resourse[a_2][1]
                        profit += resourse[a_3][2] + resourse[a_4][3]
                        profit += resourse[a_5][4] + resourse[a_6][5]
                        if profit > max_profit:
                            max_profit = profit
                            optimal = str(a_1) + ", " + str(a_2) + ", "
                            optimal += str(a_3) + ", " + str(a_4) + ", "
                            optimal += str(a_5) + ", " + str(a_6)

print("profit: " + str(max_profit))
print("x1 x2 x3 x4 x5 x6")
print(optimal)