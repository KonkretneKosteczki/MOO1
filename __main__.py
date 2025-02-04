import numpy as np
import matplotlib.pyplot as plt
from methods import bisect, fibonacci
from matplotlib.widgets import TextBox, RadioButtons, Button, CheckButtons

# important for eval
sin, cos, sqrt, tan, ln, log10, log2 = np.sin, np.cos, np.sqrt, np.tan, np.log, np.log10, np.log2

function: str = "x ** 2"
method: str = "Bisection"
stop_condition: str = "Accuracy"
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.35, top=0.95, bottom=0.05, right=0.95)
x_min: float = -5.0
x_max: float = 5.0
x: np.ndarray = np.arange(x_min, x_max, 0.01)
s: np.ndarray = x ** 2
l, = ax.plot(x, s, lw=2)
marked_regions = []
lines = []
max_iterations = 5
min_accuracy = 0.01
unimod_check= False
unimod=10


def update_plot() -> None:
    global x, x_min
    clear_lines()
    # if ("log" in function or "ln" in function) and x_min <= 0:
    #     x_min = 0.01

    clear_marked_regions()
    clear_lines()
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


def change_accuracy(accuracy) -> None:
    global min_accuracy
    min_accuracy = float(accuracy)
    update_plot()


def change_iterations(iterations) -> None:
    global max_iterations
    max_iterations = int(iterations)
    update_plot()


def change_function(text: str) -> None:
    # TODO: safe input
    global function
    function = text
    update_plot()

def change_unimod(text: str) -> None:
    # TODO: safe input
    global unimod
    unimod = int(text)
    clear_lines()

def change_method(text: str) -> None:
    global method
    method = text
    print(method)

def change_stop_condition(text: str) -> None:
    global stop_condition
    stop_condition = text
    print(stop_condition)

def change_unimod_check(text: str) -> None:
    global unimod_check
    unimod_check = not unimod_check
    print(unimod_check)

def on_submit(button_release_event) -> None:
    if unimod_check:
        try:
            nx_min, nx_max = exhaustive_search_method(x_min, x_max, function, unimod)
            lines.append(ax.axvline(nx_min, 0, 1, color='red'))
            lines.append(ax.axvline(nx_max, 0, 1, color='red'))
        except ValueError:
            print(f"No minimum within the given range. The minimum is the endpoint: {min(x_min,x_max)}")
            return
    else:
        nx_min, nx_max = x_min,x_max

    if method == "Bisection":
        print("Running Bisection on range: [" + str(nx_min) + ", " + str(nx_max) + "] and function: " + function)
        results = bisect(nx_min, nx_max, function, stop_condition, min_accuracy, max_iterations)
        print("Result: " + str(results.pop()) + "\nIntermediate intervals: " + str(results))
        mark_regions(results)
    else:
        print("Running Fibonacci on range: [" + str(nx_min) + ", " + str(nx_max) + "] and function: " + function)
        results = fibonacci(nx_min, nx_max, nx_max-nx_min, function, stop_condition, min_accuracy, max_iterations+1)
        print("Result: " + str(results.pop()) + "\nIntermediate intervals: " + str(results))
        mark_regions(results)


def clear_marked_regions():
    global marked_regions
    for region in marked_regions:
        region.remove()
    marked_regions = []

def clear_lines():
    global lines
    for line in lines:
        line.remove()
    lines = []

def mark_regions(intervals):
    global marked_regions
    clear_marked_regions()
    for a, b in intervals:
        marked_regions.append(ax.axvspan(a, b, color='blue', alpha=1/len(intervals)))
    plt.draw()

def exhaustive_search_method(ua, ub, fun, n=10):
    clear_lines()
    ux1 = ua
    dx = (ub - ua) / n
    ux2 = ux1 + dx
    ux3 = ux2 + dx
    while True:
        x = np.array([ux1, ux2, ux3])  # for eval
        uf1, uf2, uf3 = eval(fun)
        if uf1 >= uf2 and uf2 <= uf3:
            print(f"Found unimodality bounds: [{ux1},{ux3}]")
            return ux1, ux3
        else:
            ux1 = ux2
            ux2 = ux3
            ux3 = ux2 + dx
            if ux3 <= ub:
                continue
            else:
                raise ValueError

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

x_min_axs = plt.axes([0.05, 0.25, 0.1, 0.04])
x_min_text_box = TextBox(x_min_axs, '', initial=str(x_min))
x_min_text_box.on_submit(change_range_min)
plt.text(0.05, 1.25, "Min X", fontsize=12)

x_max_axs = plt.axes([0.15, 0.25, 0.1, 0.04])
x_max_text_box = TextBox(x_max_axs, '', initial=str(x_max))
x_max_text_box.on_submit(change_range_max)
plt.text(0.05, 1.25, "Max X", fontsize=12)

accuracy_axs = plt.axes([0.05, 0.15, 0.1, 0.04])
accuracy_text_box = TextBox(accuracy_axs, '', initial=str(min_accuracy))
accuracy_text_box.on_submit(change_accuracy)
plt.text(0.05, 1.25, "Acc", fontsize=12)

iterations_axs = plt.axes([0.15, 0.15, 0.1, 0.04])
iterations_text_box = TextBox(iterations_axs, '', initial=str(max_iterations))
iterations_text_box.on_submit(change_iterations)
plt.text(0.05, 1.25, "Iter", fontsize=12)

unimod_axs1 = plt.axes([0.05, 0.06, 0.1, 0.05])
unimod_checkbox = CheckButtons(unimod_axs1, ["Check"])
unimod_checkbox.on_clicked(change_unimod_check)
plt.text(0.05, 1.25, "Unimodality on n intervals", fontsize=8)

unimod_axs2 = plt.axes([0.15, 0.06, 0.1, 0.05])
unimod_text_box = TextBox(unimod_axs2, '', initial=str(unimod))
unimod_text_box.on_submit(change_unimod)

submit_button_axs = plt.axes([0.05, 0.01, 0.2, 0.04])
submit_button = Button(submit_button_axs, "Submit")
submit_button.on_clicked(on_submit)

update_plot()
plt.show()
