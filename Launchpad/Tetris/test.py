def update_value(board, row, col, newColor=[0,0]):
    row -= 1
    col -= 1
    object = board[row][col]
    raw = object["Number"]
    color = [object["Red"], object["Green"]]

    print(board[row][col])
    
    board[row][col] = {"Number": int(raw), "Red": newColor[0], "Green": newColor[1]}

    print(board[row][col])
    print("-----------------------")
    print(Board)







Board = [  #         1                                     2                                       3                                   4                                     5                                 6                                        7                                  8
    [{"Number": 0, "Red": 0, "Green": 0}, {"Number": 1, "Red": 0, "Green": 0}, {"Number": 2, "Red": 56, "Green": 19}, {"Number": 3, "Red": 0, "Green": 0}, {"Number": 4, "Red": 0, "Green": 0}, {"Number": 5, "Red": 0, "Green": 0}, {"Number": 6, "Red": 0, "Green": 0}, {"Number": 7, "Red": 0, "Green": 0}],
    [{"Number": 16, "Red": 0, "Green": 0}, {"Number": 17, "Red": 0, "Green": 0}, {"Number": 18, "Red": 0, "Green": 0}, {"Number": 19, "Red": 0, "Green": 0}, {"Number": 20, "Red": 0, "Green": 0}, {"Number": 21, "Red": 0, "Green": 0}, {"Number": 22, "Red": 0, "Green": 0}, {"Number": 23, "Red": 0, "Green": 0}],
    [{"Number": 32, "Red": 0, "Green": 0}, {"Number": 33, "Red": 0, "Green": 0}, {"Number": 34, "Red": 0, "Green": 0}, {"Number": 35, "Red": 0, "Green": 0}, {"Number": 36, "Red": 0, "Green": 0}, {"Number": 37, "Red": 0, "Green": 0}, {"Number": 38, "Red": 0, "Green": 0}, {"Number": 39, "Red": 0, "Green": 0}],
    [{"Number": 48, "Red": 0, "Green": 0}, {"Number": 49, "Red": 0, "Green": 0}, {"Number": 50, "Red": 0, "Green": 0}, {"Number": 51, "Red": 0, "Green": 0}, {"Number": 52, "Red": 0, "Green": 0}, {"Number": 53, "Red": 0, "Green": 0}, {"Number": 54, "Red": 0, "Green": 0}, {"Number": 55, "Red": 0, "Green": 0}],
    [{"Number": 64, "Red": 0, "Green": 0}, {"Number": 65, "Red": 0, "Green": 0}, {"Number": 66, "Red": 0, "Green": 0}, {"Number": 67, "Red": 0, "Green": 0}, {"Number": 68, "Red": 0, "Green": 0}, {"Number": 69, "Red": 0, "Green": 0}, {"Number": 70, "Red": 0, "Green": 0}, {"Number": 71, "Red": 0, "Green": 0}],
    [{"Number": 80, "Red": 0, "Green": 0}, {"Number": 81, "Red": 0, "Green": 0}, {"Number": 82, "Red": 0, "Green": 0}, {"Number": 83, "Red": 0, "Green": 0}, {"Number": 84, "Red": 0, "Green": 0}, {"Number": 85, "Red": 0, "Green": 0}, {"Number": 86, "Red": 0, "Green": 0}, {"Number": 87, "Red": 0, "Green": 0}],
    [{"Number": 96, "Red": 0, "Green": 0}, {"Number": 97, "Red": 0, "Green": 0}, {"Number": 98, "Red": 0, "Green": 0}, {"Number": 99, "Red": 0, "Green": 0}, {"Number": 100, "Red": 0, "Green": 0}, {"Number": 101, "Red": 0, "Green": 0}, {"Number": 102, "Red": 0, "Green": 0}, {"Number": 103, "Red": 0, "Green": 0}],
    [{"Number": 112, "Red": 0, "Green": 0}, {"Number": 113, "Red": 0, "Green": 0}, {"Number": 114, "Red": 0, "Green": 0}, {"Number": 115, "Red": 0, "Green": 0}, {"Number": 116, "Red": 0, "Green": 0}, {"Number": 117, "Red": 0, "Green": 0}, {"Number": 118, "Red": 0, "Green": 0}, {"Number": 119, "Red": 0, "Green": 0}]
]


update_value(Board, row=1, col=3, newColor=[3,0])




# print(Board)
