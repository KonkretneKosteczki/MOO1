import numpy as np
import matplotlib.pyplot as plt
from methods import bisect, fibonacci
from matplotlib.widgets import TextBox, RadioButtons, Button

# important for eval
sin, cos, sqrt, tan = np.sin, np.cos, np.sqrt, np.tan

function: str = "x ** 2"
method: str = "Bisection"
stop_condition: str = "Accuracy"
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.35, top=0.95, bottom=0.05, right=0.95)
x_min: float = -5.0
x_max: float = 5.0
x: np.ndarray = np.arange(x_min, x_max, 0.01)
s: np.ndarray = x ** 2
l, = plt.plot(x, s, lw=2)

max_iterations = 5
min_accuracy = 0.01


def update_plot() -> None:
    global x
    x = np.arange(x_min, x_max, 0.01)
    y_data = eval(function)
    l.set_xdata(x)
    l.set_ydata(y_data)
    ax.set_ylim(np.min(y_data), np.max(y_data))
    ax.set_xlim(x_min, x_max)
    plt.draw()


def change_range_min(min_range) -> None:
    global x_min
    x_min = float(min_range)
    update_plot()


def change_range_max(max_range) -> None:
    global x_max
    x_max = float(max_range)
    update_plot()


def change_function(text: str) -> None:
    # TODO: safe input
    global function
    function = text
    update_plot()


def change_method(text: str) -> None:
    global method
    method = text
    print(method)


def change_stop_condition(text: str) -> None:
    global stop_condition
    stop_condition = text
    print(stop_condition)


def on_submit(button_release_event) -> None:
    if method == "Bisection":
        print("Running Bisection on range: [" + str(x_min) + ", " + str(x_max) + "] and function: " + function)
        results = bisect(x_min, x_max, function, stop_condition, min_accuracy, max_iterations)
        print("Result: " + str(results.pop()) + "\nIntermediate intervals: " + str(results))
    else:
        print("Running Fibonacci on range: [" + str(x_min) + ", " + str(x_max) + "] and function: " + function)
        results = fibonacci(x_min, x_max, function, stop_condition, min_accuracy, max_iterations)
        print("Result: " + str(results.pop()) + "\nIntermediate intervals: " + str(results))


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

submit_button_axs = plt.axes([0.05, 0.05, 0.2, 0.04])
submit_button = Button(submit_button_axs, "Submit")
submit_button.on_clicked(on_submit)

update_plot()
plt.show()
