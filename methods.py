import numpy as np


def print_interval(a, b, iteration):
    print("INTERVAL nr" + str(iteration) + ": [" + str(a) + ", " + str(b) + "]")


def bisect(a: float, b: float, function, stop_condition, min_accuracy, max_iterations=1, iteration=1):
    print_interval(a, b, iteration)
    l_range = b - a
    x1, xm, x2 = a + l_range / 4, (a + b) / 2, b - l_range / 4
    x = np.array([x1, xm, x2])  # for eval
    f1, fm, f2 = eval(function)

    if stop_condition == "Iterations" and iteration > max_iterations:
        return xm  # we assume the extremum is the middle of the range
    if stop_condition == "Accuracy" and l_range <= 2 * min_accuracy:
        return xm

    # lewy przedział
    if f1 < fm:
        return bisect(a, xm, function, stop_condition, min_accuracy, max_iterations, iteration + 1)
    # prawy przedział
    if f2 < fm:
        return bisect(xm, b, function, stop_condition, min_accuracy, max_iterations, iteration + 1)
    # środkowy przedział
    return bisect(x1, x2, function, stop_condition, min_accuracy, max_iterations, iteration + 1)


def fibonacci(a: float, b: float, function, stop_condition, min_accuracy, max_iterations=1, iteration=1):
    print_interval(a, b, iteration)
    pass
