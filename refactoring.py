def enter_evaluation():
    while True:
        print('Please enter a rating on a scale of 1 to 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                print('Enter your comments')
                comment = input()
                post = f'point: {point} comment: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
            else:
                print('Please enter a value between 1 and 5')
        else:
            print('Please enter the number of evaluation points')

def check_results():
    print('Results so far:')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def main_menu():
    while True:
        print('Please select the process you wish to perform')
        print('1: Enter evaluation points and comments')
        print('2: Check the results so far')
        print('3: Terminate')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                enter_evaluation()
            elif num == 2:
                check_results()
            elif num == 3:
                print('Termination.')
                break
            else:
                print('Please enter 1 to 3')
        else:
            print('Please enter 1 to 3')

if __name__ == "__main__":
    main_menu()
