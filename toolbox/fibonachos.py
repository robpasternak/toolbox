def fibonachos(iter_num = 1):
    fibonacci = [1, 1]
    fibofunc = lambda x : f'{x} nacho' if x == 1 else f'{x} nachos'
    if iter_num <= 2:
        return [fibofunc(x) for x in fibonacci[:iter_num]]
    for i in range(iter_num - 2):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return [fibofunc(x) for x in fibonacci]
