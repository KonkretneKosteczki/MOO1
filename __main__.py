import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, RadioButtons


function = "x ** 2"
method = "Bisection"
stop_condition = "Accuracy"
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.35, top=0.95, bottom=0.05, right=0.95)
x_min = 0
x_max = 20
x = np.arange(x_min, x_max, 0.01)
s = x ** 2
l, = plt.plot(x, s, lw=2)


def update_plot():
    global x
    x = np.arange(x_min, x_max, 0.01)
    y_data = eval(function)
    l.set_xdata(x)
    l.set_ydata(y_data)
    ax.set_ylim(np.min(y_data), np.max(y_data))
    ax.set_xlim(x_min, x_max)
    plt.draw()


def change_range_min(min_range):
    global x_min
    x_min = float(min_range)
    update_plot()


def change_range_max(max_range):
    global x_max
    x_max = float(max_range)
    update_plot()


def change_function(text):
    global function
    function = text
    update_plot()
    # y_data = eval(text)
    # # TODO: safe input
    # l.set_ydata(y_data)
    # ax.set_ylim(np.min(y_data), np.max(y_data))
    # plt.draw()


def change_method(text):
    global method
    method = text
    print(method)


def change_stop_condition(text):
    global stop_condition
    stop_condition = text
    print(stop_condition)


input_function = plt.axes([0.05, 0.9, 0.2, 0.04])
input_function_text_box = TextBox(input_function, '', initial=function)
input_function_text_box.on_submit(change_function)

method_selection = plt.axes([0.05, 0.625, 0.2, 0.25], facecolor='white')
method_selection_radio = RadioButtons(method_selection, ("Bisection", "Fibonacci"))
method_selection_radio.on_clicked(change_method)
plt.text(0.05, 0.8, "Method", fontsize=12)

stop_condition_selection = plt.axes([0.05, 0.35, 0.2, 0.25], facecolor='white')
stop_condition_selection_radio = RadioButtons(stop_condition_selection, ("Accuracy", "Iterations"))
stop_condition_selection_radio.on_clicked(change_stop_condition)
plt.text(0.05, 0.8, "Stop condition", fontsize=12)

x_min_axs = plt.axes([0.05, 0.25, 0.2, 0.04])
x_min_text_box = TextBox(x_min_axs, '', initial=str(x_min))
x_min_text_box.on_submit(change_range_min)
plt.text(0.05, 1.25, "Min X", fontsize=12)

x_max_axs = plt.axes([0.05, 0.15, 0.2, 0.04])
x_max_text_box = TextBox(x_max_axs, '', initial=str(x_max))
x_max_text_box.on_submit(change_range_max)
plt.text(0.05, 1.25, "Max X", fontsize=12)

update_plot()
plt.show()

