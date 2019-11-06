def calculate_year_of_centenary(current_year, current_age):

    if current_year < 0:
        raise Exception(f'Bad input {current_year} < 0')

    if current_age < 0:
        raise Exception(f'Bad input {current_age} < 0')

    if current_age == 0:
        return current_year + 100
    else:
        birth_year = current_year - current_age
        return birth_year + 100 - 1
