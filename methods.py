import numpy as np
from typing import List, Union
# important for eval
sin, cos, sqrt, tan = np.sin, np.cos, np.sqrt, np.tan


def print_interval(a: float, b: float, iteration: int) -> None:
    print("INTERVAL nr" + str(iteration) + ": [" + str(a) + ", " + str(b) + "]")


def bisect(a: float, b: float, function: str, stop_condition: str, min_accuracy: float, max_iterations: int = 1,
           iteration: int = 1) -> List[Union[List[float], float]]:
    intermediate_interval = [a, b]
    print_interval(a, b, iteration)
    l_range = b - a
    x1, xm, x2 = a + l_range / 4, (a + b) / 2, b - l_range / 4
    x = np.array([x1, xm, x2])  # for eval
    f1, fm, f2 = eval(function)

    if stop_condition == "Iterations" and iteration > max_iterations:
        return [intermediate_interval, xm]  # we assume the extremum is the middle of the range
    if stop_condition == "Accuracy" and l_range <= 2 * min_accuracy:
        return [intermediate_interval, xm]

    # lewy przedział
    if f1 < fm:
        return [intermediate_interval] + \
               bisect(a, xm, function, stop_condition, min_accuracy, max_iterations, iteration + 1)
    # prawy przedział
    elif f2 < fm:
        return [intermediate_interval] + \
               bisect(xm, b, function, stop_condition, min_accuracy, max_iterations, iteration + 1)
    # środkowy przedział
    else:
        return [intermediate_interval] + \
           bisect(x1, x2, function, stop_condition, min_accuracy, max_iterations, iteration + 1)


def fibonacci(a: float, b: float, function: str, stop_condition: str, min_accuracy: float, max_iterations: int = 1,
              iteration: int = 1) -> List[Union[List[float], float]]:
    print_interval(a, b, iteration)
    intermediate_interval = [a, b]

    return [intermediate_interval]
