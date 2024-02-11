PUNCTION = ",:;.!?"
END_SENTENCE_SYMB = "!&."
CONSORNANTS = "QWRTPSDFGHJKLZXCVBNMЦКНГШЩЗХЪФВПРЛДЖЧСМТБ"
POS_SYMBS_FOR_CALCULUS = "0123456789*/"


def get_word_without_punction(word): # Получение слова без знаков препинания
    if len(word) < 1:
        return word
    while word[-1] in PUNCTION:
        word = word[:-1]
    return word


def get_punction_without_word(word): # Получение знаков препинания после слова
    punc = ""
    if len(word) < 1:
        return word
    for el in word:
        if el in PUNCTION:
            punc = punc + el
    return punc


def clear_exp(exp): # Функция перевода выражения в удобный для обработки формат
    new = ""
    for i in exp:
        if i in "*/":
            new += " " + i + " "
        else:
            new += i
    return new


def calc_exp(exp): # Вычисление значения выражения
    try:
        ops = exp.split()
        res = int(ops[0])
        for i in range(1, len(ops), 2):
            op = ops[i]
            el = int(ops[i + 1])
            if op == "*":
                res *= el
            else:
                res /= el
        return f"{res:.5g}"
    except BaseException:
        return "ERROR"
