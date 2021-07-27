# IMPORTING NECESSARY MODULES.
import os
import matplotlib.pyplot as plt

# DECLARING VARIABLES OF COLORS.
# these colors are based on Linux escape sequence symbols. they are for Linux.
WHITE = '\033[1;37;40m'
GREEN = '\033[1;32;40m'
RED = '\033[1;31;40m'
YELLOW = '\033[1;33;40m'
CYAN = '\033[1;36;40m'

# FUNCTIONS.
# function for printing out instructions.
def manual():
    print(f'''

    Supported commands:
        exit() - stop execution and quit the program.

    ''')

# function for printing out the creators of a program.
def credits():
    print(f'''

    Creators:
                AAgzamov

    ''')

# function for printing out beautiful logo.
def logo():
    print(f'''
        Not supported yet.

    ''')

# main menu function.
def menu():
    print(f'''
    Menu:

    [1] Plot a graph.
    [2] See stylesheets.
    [3] Manual.
    [4] Credits.
    [5] Quit.

    ''')

# graph plotting menu.
def menu_1():
    print(f'''

    [1] Input data manually.
    [2] Derive data from a file (csv or excel).

    ''')

# function of plotting a graph based on a already prepared data.
def derive():
    print(f'''

    Not supported yet!

    ''')

# function for printing out existing stylesheets.
def menu_2():
    print(f'''

    Available style sheets:
        1. classic                  6. fast
        2. Solarize_Light2          7. fivethirtyeight
        3. _classic_test_patch      8. ggplot
        4. bmh                      9. grayscale
        5. dark_background          10. seaborn

    ''')

# clear screen function for Unix-based operating systems.
def clear():
    os.system('clear')

# exit program.
def exit():
    quit()

# print error function.
def error_output():
    print(f'[Error]: Something went wrong! Please try again.')

# types of graphs menu function.
def types_of_graphs():
    print(f'''

    [1] Line graph.
    [2] Bar chart.
    [3] Pie chart.

    ''')

# function for plotting a line graph.
def line_graph():
    print('[Info]: Inputs marked by an asterisk are compulsory. Others are optional. Press Enter to skip optional inputs\nor type exit() to stop execution.\n')
    # title input.
    graph_name = input('How to do you want to name your line graph? ')
    if graph_name == 'exit()':
        exit()
    # 'x' label input.
    x_label = input('Label X-axis: ')
    if x_label == 'exit()':
        exit()
    # 'y' label input.
    y_label = input('Label Y-axis: ')
    if y_label == 'exit()':
        exit()
    # figure size input.
    while 1:

        try:
            size = input('Enter the size of a figure (width and height separated by comma): ')
            if size == 'exit()':
                break
            elif size == '':
                size = None
                break
            else:
                size = size.split(', ')
                figsize = [int(n) for n in size]
                figsize = tuple(figsize) # converting list 'figsize' to a tuple.
                break
        except:
            error_output()
    if size == 'exit()':
        exit()
    # graph dimension input.
    while 1:

        try:
            dimension = input('Enter the dimension of a line graph (a single number):* ')
            if dimension == 'exit()':
                break
            else:
                dimension = int(dimension)
            break
        except:
            error_output()
    if dimension == 'exit()':
        exit()
    # X and Y coordinates input.
    while 1:

        try:
            print(f'Enter the intersection coordinates of X-axis and Y-axis accordingly (two numbers separated by comma).')
            # creating lists for keeping 'X' and 'Y' values.
            x = list()
            y = list()
            # a loop for user input of coordinates.
            for i in range(dimension):
                user = input('x, y:* ')
                if user == 'exit()':
                    break
                else:
                    user = user.split(', ')
                x_coordinate = int(user[0])
                y_coordinate = int(user[1])
                x.append(x_coordinate)
                y.append(y_coordinate)
            if user == 'exit()':
                exit()
            break
        except:
            error_output()
    # stylesheet input.
    stylesheet = input('Enter the name of a stylesheet: ')
    if stylesheet == 'exit()':
        exit()
    # linewidth input.
    while 1:

        try:
            line_width = input('Enter the line width (a single number): ')
            if line_width == 'exit()':
                break
            elif line_width == '':
                line_width = None
            else:
                line_width = int(line_width)
            break
        except:
            error_output()
    if line_width == 'exit()':
        exit()
    # color input.
    line_color = input('Enter the color of a line (color name or in HEX format): ')
    if line_color == 'exit()':
        exit()
    # line style input.
    line_style = input('Enter the style of a line: ')
    if line_style == 'exit()':
        exit()
    # 'x' ticks values.
    while 1:
        try:
            x_ticks = list()
            print('Enter values to be shown on X-axis.')
            print('If finished, just press Enter.')
            while 1:
                user = input('')
                if user == 'exit()':
                    break
                elif user == '':
                    break
                else:
                    user = int(user)
                    x_ticks.append(user)
            if user == '':
                break
            if user == 'exit()':
                break
        except:
            error_output()
    if user == 'exit()':
        exit()
    # 'y' ticks values.
    while 1:
        try:
            y_ticks = list()
            print('Enter values to be shown on Y-axis.')
            print('If finished, just press Enter.')
            while 1:
                user = input('')
                if user == 'exit()':
                    break
                elif user == '':
                    break
                else:
                    user = int(user)
                    y_ticks.append(user)
            if user == '':
                break
            if user == 'exit':
                break
        except:
            error_output()
    if user == 'exit()':
        exit()



    # checking if some values should have default value.
    if stylesheet == '':
        stylesheet = 'default'
    if line_color == '':
        line_color = None
    if line_style == '':
        line_style = 'solid'
    if len(x_ticks) < 1:
        x_ticks = None
    if len(y_ticks) < 1:
        y_ticks = None




    # plotting a line graph.
    try:
        plt.style.use(stylesheet)
    except:
        print(f'[Warning]: Cannot define a style sheet! Instead using default stylesheet!')
    plt.figure(figsize = figsize)
    plt.title(graph_name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.plot(x, y, color = line_color, linestyle = line_style, linewidth = line_width)




    print('[Info]: Done! A line graph is plotted.')
    print('\n[Info]: Need to save a line graph as a file.\n')
    while 1:
        try:
            name = input('Enter the name of a file with an extension: ')
            if name == 'exit()':
                break
            dpi = int(input('Define quality in \'DPI\': '))
            if dpi == 'exit()':
                break
            else:
                dpi = int(dpi)
            plt.savefig(f'{name}', dpi = dpi)
            print(f'\n[Info]: A line graph is saved as {name} in the same directory with the program.\n')
            break
        except:
            error_output()
    if name == 'exit()':
        exit()
    if dpi == 'exit()':
        exit()


    # print('Do you want to save it as a file? [y/n]')
    # user = input().lower()
    # if user == 'y': # if user wants to save a line graph.
    #     name = input('Enter the name of a file with an extension: ')
    #     dpi = int(input('Define quality in \'DPI\': '))
    #     plt.savefig(f'{name}', dpi = dpi)
    #     print(f'A line graph is saved as {name} in the same directory with the program.')
    # elif user == 'n':
    #     pass

    print(f'\n[Info]: Plotting process is complete!\n')
    print(f'...Press any key to go back to the main menu...')
    input()

# function for plotting a bar chart.
def bar_chart():
    pass

# function for plotting a pie chart.
def pie_chart():
    pass
