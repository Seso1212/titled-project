import random
numb1 = str(random.randrange(1, 10))
numb2 = str(random.randrange(1, 10))
numb3 = str(random.randrange(1, 10))
numb4 = str(random.randrange(1, 10))
so = 0
while so == 0:
    if numb2 == numb1:
        numb2 = str(random.randrange(1, 10))
        so = 0
    else:
        so = 1
while so == 1:
    if numb3 == numb2 or numb3 == numb1:
        numb3 = str(random.randrange(1, 10))
        so = 1
    else:
        so = 2
while so == 2:
    if numb4 == numb1 or numb4 == numb2 or numb4 == numb3:
        numb4 = str(random.randrange(1, 10))
        so = 2
    else:
        so = 3
valid_input = numb1+numb2+numb3+numb4
def get_step1_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            int(user_input)
            return user_input
        except ValueError:
            print("Oops! Please enter a valid number.")
while True:
    step_1 = (get_step1_input("let's findout what is the guess: ")) #1223
    step_1 = int(step_1)
    if step_1 >= 1000 and step_1 <= 9999:
        step_1 = str(step_1)            #step1 = string
        valid_input = str(valid_input)  #guesser = string
        box = []
        box.append(step_1[0])
        box.append(step_1[1])
        box.append(step_1[2])
        box.append(step_1[3])
        unique_list = []
        for item in box:
            if item not in unique_list:
                unique_list.append(item)
        if len(unique_list) == 4 and unique_list[0] != "0" and unique_list[1] != "0" and unique_list[2] != "0" and unique_list[3] != "0":
            f = step_1[0]
            if f == valid_input[0] or f == valid_input[1] or f == valid_input[2] or f == valid_input[3]:
                f = 1
            else:
                f = 0
            g = step_1[1]
            if g == valid_input[0] or g == valid_input[1] or g == valid_input[2] or g == valid_input[3]:
                g = 1
            else:
                g = 0
            h = step_1[2]
            if h == valid_input[0] or h == valid_input[1] or h == valid_input[2] or h == valid_input[3]:
                h = 1
            else:
                h = 0
            i = step_1[3]
            if i == valid_input[0] or i == valid_input[1] or i == valid_input[2] or i == valid_input[3]:
                i = 1
            else:
                i = 0
            z = f + g + h + i
            print(f"{z} Number")
            a = valid_input[0] == step_1[0]
            if a:
                a = 1
            else:
                a = 0
            b = valid_input[1] == step_1[1]
            if b:
                b = 1
            else:
                b = 0
            c = valid_input[2] == step_1[2]
            if c:
                c = 1
            else:
                c = 0
            d = valid_input[3] == step_1[3]
            if d:
                d = 1
            else:
                d = 0
            e = a + b + c + d
            if e == 0:
                print(f"{e} set")
            if e > 0:
                n = e
                print(f"{n} set")
                if n == 4:
                    print("Congrats: You Won The Game!!")
                    break
            step_1 = int(step_1)
            valid_input = int(valid_input)
        else:
            print("please write 4 uniqui digit numbers between 1-9!!")
            unique_list == False
            step_1 = int(step_1)
            valid_input = int(valid_input)
        step_1 = int(step_1)
        valid_input = int(valid_input)
    else:
        print("please write 4 uniqui digit numbers between 1-9!!")
        step_1 = int(step_1)
        valid_input = int(valid_input)
        False

