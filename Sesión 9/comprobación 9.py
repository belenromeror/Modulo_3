def ejercicio(numbers):
    total_sum = sum(numbers)
    resta_result = numbers[0] - numbers[1] - numbers[2]
    result_tupla = (total_sum, resta_result)
    print(result_tupla)
    return result_tupla

ejercicio([12,6,3])