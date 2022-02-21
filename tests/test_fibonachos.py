from toolbox.fibonachos import fibonachos

def test_fibonachos():
    assert fibonachos() == ['1 nacho']
    assert fibonachos(4) == ['1 nacho', '1 nacho', '2 nachos', '3 nachos']
