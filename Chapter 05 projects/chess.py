x= {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
i = 1
dict_val = []
compulsion = ['wking','bking']
num = []
letter = ["a","b","c","d","e","f","g","h"]
square_id = []
while(i < 9):
    num.append(i)
    i+=1


for k in range(8):
    for j in range(8):
        square_id.append(str(num[k]) + letter[j])



def isValidChessBoard(pieces):
    for keys, values in pieces.items():
        if keys in square_id:
            continue
        dict_val.append(values)
        print(values)
    print(dict_val)
    if 'wking' and 'bking' in dict_val:
        print("This is a valid chessboard")
    else:
        print("This is a not a valid chessboard")

    
isValidChessBoard(x)
