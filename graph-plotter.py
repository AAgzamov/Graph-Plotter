print('\n\t\tLoading...\n')

# IMPORTING FUNCTIONS FFORM "functions.py" FILE.
import functions as f

# MAIN PROGRAM LOOP.
while 1:
    f.clear()
    f.menu()
    user = input()
    if user == 'exit()':
        f.exit()
    elif user == '1':
        f.clear()
        f.menu_1()
        user = input()
        if user == 'exit()':
            f.exit()
        elif user == '1':
            f.clear()
            f.types_of_graphs()
            user = input()
            if user == 'exit()':
                f.exit()
            elif user == '1':
                f.clear()
                f.line_graph()
                f.clear()
            elif user == '2':
                f.clear()
                f.bar_chart()
                f.clear()
            elif user == '3':
                pass
        elif user == '2':
            f.clear()
            f.derive()
            input()
            continue
    elif user == '2':
        f.clear()
        f.menu_2()
        input()
        continue
    elif user == '3':
        f.clear()
        f.manual()
        input()
        continue
    elif user == '4':
        f.clear()
        f.credits()
        input()
        continue
    elif user == '5':
        f.exit()
