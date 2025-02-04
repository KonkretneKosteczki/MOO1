import numpy as np
from typing import List, Union

# important for eval
sin, cos, sqrt, tan, ln, log10, log2 = np.sin, np.cos, np.sqrt, np.tan, np.log, np.log10, np.log2

eval_number = 0
def print_interval(a: float, b: float, iteration: int) -> None:
    print(f"INTERVAL no {iteration}: [{a}, {b}]")


def bisect(a: float, b: float, function: str, stop_condition: str, min_accuracy: float, max_iterations: int = 1,
           iteration: int = 1, fm: float = None) -> List[Union[List[float], float]]:
    global eval_number
    intermediate_interval = [a, b]
    print_interval(a, b, iteration)
    l_range = b - a
    x1, xm, x2 = a + l_range / 4, (a + b) / 2, b - l_range / 4

    if stop_condition == "Iterations" and iteration > max_iterations:
        print(f"optimized function was evaluated {eval_number} times")
        eval_number=0
        return [intermediate_interval, xm]  # we assume the extremum is the middle of the range
    if stop_condition == "Accuracy" and l_range <= 2 * min_accuracy:
        print(f"optimized function was evaluated {eval_number} times")
        eval_number = 0
        return [intermediate_interval, xm]

    # first iteration also calculates fm
    if fm is None:
        x = np.array([x1, xm, x2])
        f1, fm, f2 = eval(function)
        eval_number+=3
    # all other iterations get fm from the last one
    else:
        x = np.array([x1, x2])
        f1, f2 = eval(function)
        eval_number+=2

    # lewy przedział
    if f1 < fm:
        return [intermediate_interval] + \
               bisect(a, xm, function, stop_condition, min_accuracy, max_iterations, iteration + 1, fm=f1)
    # prawy przedział
    elif f2 < fm:
        return [intermediate_interval] + \
               bisect(xm, b, function, stop_condition, min_accuracy, max_iterations, iteration + 1, fm=f2)
    # środkowy przedział
    else:
        return [intermediate_interval] + \
               bisect(x1, x2, function, stop_condition, min_accuracy, max_iterations, iteration + 1, fm=fm)


def acc_to_max_iter(l_range: float, min_accuracy: float) -> int:
    i = 0
    while True:
        # when max_iterations == iteration then fib_num(max_iterations - iteration+1) = 1
        l_star = l_range / fib_num(i + 1)
        if l_star <= min_accuracy:
            return i
        else:
            i += 1


def fibonacci(a: float, b: float, l_range: float, function: str, stop_condition: str, min_accuracy: float,
              max_iterations: int = 1, iteration: int = 2, f1:float = None, f2: float = None) -> List[Union[List[float], float]]:
    global eval_number
    print_interval(a, b, iteration - 1)
    intermediate_interval = [a, b]

    if stop_condition == "Iterations" and iteration > max_iterations:
        print(f"optimized function was evaluated {eval_number} times")
        eval_number=0
        x0 = (a + b) / 2
        return [intermediate_interval, x0]
    elif stop_condition == "Accuracy":
        max_iterations = acc_to_max_iter(l_range, min_accuracy)
        return fibonacci(a, b, l_range, function, "Iterations", min_accuracy, max_iterations)

    l_star = l_range * (fib_num(max_iterations - iteration + 1) / fib_num(max_iterations + 1))
    x1, x2 = a + l_star, b - l_star

    if f1 is None:
        x=x1
        f1=eval(function)
        eval_number+=1
    if f2 is None:
        x=x2
        f2=eval(function)
        eval_number+=1

    if f1 > f2:
        return [intermediate_interval] + \
               fibonacci(x1, b, l_range, function, stop_condition, min_accuracy, max_iterations, iteration + 1,f1=f2)
    else:
        return [intermediate_interval] + \
               fibonacci(a, x2, l_range, function, stop_condition, min_accuracy, max_iterations, iteration + 1,f2=f1)


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
