def is_even(number: int) -> bool:
    while True:
        number = str(number)
        t = ['0', '2', '4', '6', '8']
        for el in t:
            if number[-1] == el:
                return True
        else:
            return False
