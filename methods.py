import numpy as np
from typing import List, Union

# important for eval
sin, cos, sqrt, tan = np.sin, np.cos, np.sqrt, np.tan


def print_interval(a: float, b: float, iteration: int) -> None:
    print(f"INTERVAL no {iteration}: [{a}, {b}]")


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


def fibonacci(a: float, b: float, l_range: float, function: str, stop_condition: str, min_accuracy: float,
              max_iterations: int = 1, iteration: int = 2) -> List[Union[List[float], float]]:
    print_interval(a, b, iteration)
    intermediate_interval = [a, b]

    if stop_condition == "Iterations" and iteration > max_iterations:
        x0 = (a + b) / 2
        return [intermediate_interval, x0]
    elif stop_condition == "Accuracy":
        raise NotImplementedError

    l_star = l_range * (fib_num(max_iterations - iteration+1) / fib_num(max_iterations+1))
    x1, x2 = a+l_star, b-l_star
    x = np.array([x1, x2])
    f1, f2 = eval(function)

    if f1 > f2:
        return [intermediate_interval] + \
               fibonacci(x1, b, l_range, function, stop_condition, min_accuracy, max_iterations, iteration + 1)
    else:
        return [intermediate_interval] + \
               fibonacci(a, x2, l_range, function, stop_condition, min_accuracy, max_iterations, iteration + 1)


def fib_num(n: int) -> int:
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        n1, n2 = 1, 1
        non_recursive: int = 0
        for i in range(n - 1):
            non_recursive = n1 + n2
            n1 = n2
            n2 = non_recursive
        return non_recursive
        # return fib_num(n - 1) + fib_num(n - 2)
