"""
File: babygraphics.py
Name: Sean Wang
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + (width-GRAPH_MARGIN_SIZE*2)/len(YEARS)*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT, text=YEARS[i], anchor=tkinter.SW, font='times 12')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color_loop = 0
    for i in range(len(lookup_names)):
        if lookup_names[i] in name_data:
            name = lookup_names[i]
            j = 0
            point_y_lst = []
            # point_y_lst for recording the prior point of y-axis
            c = i
            if c % len(COLORS) == 0:
                color_loop += 1
            if c >= len(COLORS):
                c = i - len(COLORS) * color_loop
            # when the length of lookup_names is larger than the length of color, let color start from red again
            for year, rank in sorted(name_data[name].items()):
                while YEARS[j] != int(year):
                    # Begin: avoid len(name_data) < len(YEAR)
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       text=name + ' *', anchor=tkinter.SW, font='times 10', fill=COLORS[c])
                    point_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    point_y_lst.append(point_y)
                    if j > 0:
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j - 1), point_y_lst[j - 1],
                                           get_x_coordinate(CANVAS_WIDTH, j), point_y_lst[j], width=LINE_WIDTH, fill=COLORS[c])
                    j += 1
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX,
                                   GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK*int(rank),
                                   text=name + ' ' + name_data[name][year], anchor=tkinter.SW, font='times 10',
                                   fill=COLORS[c])
                point_y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK*int(rank)
                point_y_lst.append(point_y)
                if j > 0:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j-1), point_y_lst[j-1],
                                       get_x_coordinate(CANVAS_WIDTH, j), point_y_lst[j], width=LINE_WIDTH, fill=COLORS[c])
                j += 1
            while j < len(YEARS):
                # avoid len(name_data) < len(YEAR) : End
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                   text=name + ' *', anchor=tkinter.SW, font='times 10', fill=COLORS[c])
                point_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                point_y_lst.append(point_y)
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j - 1), point_y_lst[j - 1],
                                   get_x_coordinate(CANVAS_WIDTH, j), point_y_lst[j], width=LINE_WIDTH, fill=COLORS[c])
                j += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
