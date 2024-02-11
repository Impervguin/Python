def pos_int_input(input_mes: str, negative_mes: str) -> int:
    while True:
        try:
            n = int(input(input_mes))
            if n <= 0:
                print(negative_mes)
                continue
            break
        except Exception:
            print("Неккоректный ввод")
    return n


def float_input(input_mes: str) -> float:
    while True:
        try:
            x = float(input(input_mes))
            break
        except Exception:
            print("Некорректный ввод")
    return x
