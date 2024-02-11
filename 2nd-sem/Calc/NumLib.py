# Модуль для обработки чисел и выражений
import re

DECIMAL_EXPR_REGEX = "^[-]?([0-9]+[.]?[0-9]*([-+*\/]([0-9]+[.]?[0-9]*)?)?)?$"
TERNAR_EXPR_REGEX = "^[-]?([10i]+[.]?[10i]*([-+*\/]([10i]+[.]?[10i]*)?)?)?$"
TERNAR_NUM_REGEX = "(^[-]?[10i]+[.]?[10i]*)?$"
DECIMAL_NUM_REGEX = "^[-]?([0-9]+[.]?[0-9]*)?$"
ACCURACY = 6


def check_expression(expr, mode="decimal"):
    if mode == "decimal":
        regex = DECIMAL_EXPR_REGEX
    elif mode == "ternar":
        regex = TERNAR_EXPR_REGEX
    else:
        return 0
    return re.match(regex, expr)


def check_number(num, mode="decimal"):
    if mode == "decimal":
        regex = DECIMAL_NUM_REGEX
    elif mode == "ternar":
        regex = TERNAR_NUM_REGEX
    else:
        return False
    return re.match(regex, num)


def ternar_to_decimal(num: str):
    if len(num) == 0:
        return ""
    decim = 0.0
    int_part, float_part, *_ = num.split(".") + [""]

    if int_part != "":
        int_part = int_part[::-1]
        accum = 1
        for i in range(len(int_part)):
            if int_part[i] == "i":
                k = -1
            else:
                k = int(int_part[i])
            decim += k * accum
            accum *= 3
    if float_part != "":
        accum = 1 / 3
        for i in range(len(float_part)):
            if float_part[i] == "i":
                k = -1
            else:
                k = int(float_part[i])
            decim += k * accum
            accum /= 3
    if float_part == "":
        return str(int(decim))
    return f"{decim:.5f}"


def decimal_to_ternar(num: str):
    if len(num) == 0:
        return ""
    ternar = ""
    tern_digits = ["0", "1", "i"]

    int_part, float_part, *_ = num.split(".") + [""]
    if int_part != "":
        int_part = int(int_part)
        if int_part < 0:
            int_part = -int_part
            tern_digits[1], tern_digits[2] = tern_digits[2], tern_digits[1]
        while int_part > 0:
            div, mod = divmod(int_part, 3)
            if mod <= 1:
                int_part = div
            else:
                int_part = div + 1
            ternar = tern_digits[mod] + ternar
    if ternar == "":
        ternar = "0"

    if float_part != "":
        float_part = float("." + float_part)
        float_digits = []
        for i in range(ACCURACY - 1):
            float_part *= 3
            float_digits.append(int(float_part // 1))
            float_part -= float_part // 1

        for i in range(ACCURACY - 2, -1, -1):
            if float_digits[i] >= 2:
                float_digits[i] -= 3
                if i == 0:
                    float_digits.insert(0, 1)
                else:
                    float_digits[i - 1] += 1
        for i in range(len(float_digits)):
            if float_digits[i] == -1:
                float_digits[i] = "i"
            else:
                float_digits[i] = str(float_digits[i])
        ternar += "." + "".join(float_digits)
    return ternar


def calc_expr(expr):
    if not re.match(DECIMAL_EXPR_REGEX, expr):
        return "error"
    if len(expr) == 0:
        return ""
    minus = False
    if expr[0] == "-":
        minus = True
        expr = expr[1:]
    for symb in expr:
        if symb in "+-/*":
            op = symb
            break
    else:
        if minus:
            expr = "-" + expr
        return expr

    expr_parts = expr.split(op)
    if minus:
        expr_parts[0] = "-" + expr_parts[0]

    for i, el in enumerate(expr_parts):
        try:
            expr_parts[i] = int(el)
        except ValueError:
            expr_parts[i] = float(el)

    if op == "+":
        res = sum(expr_parts)
    elif op == "-":
        res = expr_parts[0] - expr_parts[1]
    elif op == "*":
        res = expr_parts[0] * expr_parts[1]
    else:
        if expr_parts[1] == 0:
            return "error"
        res = expr_parts[0] / expr_parts[1]

    if isinstance(res, int) or abs((res % 1) - res) < 1:
        return str(res)
    elif abs((res // 1) - res) < (1 / 10 ** ACCURACY):
        return str(int(res))
    return f"{res:.5f}"
