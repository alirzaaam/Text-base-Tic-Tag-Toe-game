import random

ROW1 = [1, 2, 3]
ROW2 =  [4, 5, 6]
ROW3 =  [7, 8, 9]

USER_CHOICES = []
PC_CHOICES = []

# Draw the table
def table(list1, list2, list3):
    for i in list1:
        print(f"|{i}| ", end="")
    print()
    for i in list2:
        print(f"|{i}| ", end="")
    print()
    for i in list3:
        print(f"|{i}| ", end="")
    print()



def user_move():
    user = int(input("Choose Your Number: "))
    if user > 9 or user < 1:
        user_move()
    elif user in USER_CHOICES or user in PC_CHOICES:
        user_move()
    else:
        if 1 <= user <= 3:
            ROW1[user - 1] = 'X'
        elif 4 <= user <= 6:
            ROW2[user - 4] = 'X'
        else:
            ROW3[user - 7] = 'X'
        USER_CHOICES.append(user)


def pc_move():
    pc = random.randint(1, 9)
    if len(PC_CHOICES) + len(USER_CHOICES) == 9:
        return 
    if pc in USER_CHOICES or pc in PC_CHOICES:
        pc_move()
    else:
        PC_CHOICES.append(pc)
        if 1 <= pc <= 3:
            ROW1[pc - 1] = "O" 
        elif 4 <= pc <= 6:
            ROW2[pc - 4] = "O" 
        else:
            ROW3[pc - 7] = "O" 


def game():
    # USER
    if ROW1[0] == "X" and ROW1[1]  == "X" and ROW1[2] == "X":
        return 1
    elif ROW2[0] == "X" and ROW2[1]  == "X" and ROW2[2] == "X":
        return 1
    elif ROW3[0] == "X" and ROW3[1]  == "X" and ROW3[2] == "X":
        return 1
    elif ROW1[0] == "X" and ROW2[0]  == "X" and ROW3[0] == "X":
        return 1
    elif ROW1[1] == "X" and ROW2[1]  == "X" and ROW3[1] == "X":
        return 1
    elif ROW1[2] == "X" and ROW2[2]  == "X" and ROW3[2] == "X":
        return 1
    elif ROW1[0] == "X" and ROW2[1]  == "X" and ROW3[2] == "X":
        return 1
    elif ROW1[2] == "X" and ROW2[1]  == "X" and ROW3[0] == "X":
        return 1
    # PC
    if ROW1[0] == "O" and ROW1[1]  == "O" and ROW1[2] == "O":
        return 2
    elif ROW2[0] == "O" and ROW2[1]  == "O" and ROW2[2] == "O":
        return 2
    elif ROW3[0] == "O" and ROW3[1]  == "O" and ROW3[2] == "O":
        return 2
    elif ROW1[0] == "O" and ROW2[0]  == "O" and ROW3[0] == "O":
        return 2
    elif ROW1[1] == "O" and ROW2[1]  == "O" and ROW3[1] == "O":
        return 2
    elif ROW1[2] == "O" and ROW2[2]  == "O" and ROW3[2] == "O":
        return 2
    elif ROW1[0] == "O" and ROW2[1]  == "O" and ROW3[3] == "O":
        return 2
    elif ROW1[2] == "O" and ROW2[1]  == "O" and ROW3[0] == "O":
        return 2
    if len(PC_CHOICES) + len(USER_CHOICES) == 9:
        return 3

print("  ..:: Welcome to the Tic Tag Toe game ::..  ")
print()
print(" You Are: X")
print(" PC is: O ")
print()
table(ROW1, ROW2, ROW3)
while True:        
    if game() == 1:
        print()
        print("YOU WIN !!!!!")
        break
    if game() == 2:
        print()
        print("PC WIN !!!")
        break
    if game() == 3:
        print()
        print("DRAW !!!")
        break
    user_move()
    pc_move()
    table(ROW1, ROW2, ROW3)
