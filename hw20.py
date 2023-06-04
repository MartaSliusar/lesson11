def generate_cube_numbers(number: int) -> list:
    n = 0
    for n in range(2, number):
        n = n**3
        if n <= number:
            yield n
