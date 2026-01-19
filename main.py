from curses import noecho
import numpy as np

matrix = np.zeros((6,6), dtype=int)
matrix[0,0] = 2
matrix[0,5] = 2
matrix[5,0] = 2
matrix[5,5] = 2
matrix[0,1] = 3
matrix[0,2] = 3
matrix[0,3] = 3
matrix[0,4] = 3
matrix[1,1] = 3
matrix[1,2] = 3
matrix[1,3] = 3
matrix[1,4] = 3
matrix[4,0] = 4
matrix[4,1] = 4
matrix[4,2] = 4
matrix[4,3] = 4
matrix[4,4] = 4
matrix[4,5] = 4
matrix[5,1] = 4
matrix[5,2] = 4
matrix[5,3] = 4
matrix[5,4] = 4
# print(matrix) 
# print(matrix[0,1])

def print_matrix(matrix):
    print("|---------------------------|")
    print("|   | A | B | C | D | E | F |")
    print("|---------------------------|")
    for i in range(6):
        print("|",i+1, end=" |")
        for j in range(6):
            # print(matrix[i,j], end="|")
            if(matrix[i,j] == 0): # 빈 칸
                print("   ", end="|") 
            elif(matrix[i,j] == 2): # 집
                print(" X ", end="|") 
            elif(matrix[i,j] == 1): # 내 돌
                print(" 𒊹 ", end="|") 
            elif(matrix[i,j] == 4): # 둘 수 있는 범위
                print(" * ", end="|")
            else:
                print(" ○ ", end="|")
        print()
        print("|---------------------------|")
        
def input_matrix(input_xy):
    input_x = input_xy[0].upper()
    input_y = int(input_xy[1])
    
    col_map = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5}
    
    col = col_map[input_x]
    row = input_y -1
    print(row, col)
    return row, col


if __name__ == "__main__":
    valid_inputs = ["A5", "B5", "C5", "D5", "E5", "F5","B6", "C7", "D7", "E7"]
    print_matrix(matrix)
    while True:
        input_xy = input(f"처음에는 *위치에만 돌을 둘 수가 있습니다. 둘 수 있는 위치 :{valid_inputs}\n")
            
        input_x = input_xy[0].upper()
        input_y = int(input_xy[1])
        
        valid_input = input_x + str(input_y)
        if valid_input not in valid_inputs:
            print(f"이곳에는 돌을 둘 수가 없습니다. 둘 수 있는 위치 :{valid_inputs}")
        else:
            row, col = input_matrix(input_xy)
            matrix[row, col] = 1
            print_matrix(matrix)
            break
    
    # print("-------------")
    # # print(" |"*6)
    # for i in range(1,7):
    #     # print("|"+"|"*6+"|")
    #     print(i,"|"+" |"*6)
    #     print("——————")
        # for j in range(6):
        #     print(i,j)
    # print("——————")
