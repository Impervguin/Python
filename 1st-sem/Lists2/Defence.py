# Список строк, найти строку содержащую наибольшее кол-во слов(по пробелам)

n = int(input("Введите кол-во строк: "))
if n < 1:
    print("Некорректное кол-во строк")
    exit()

lst = [input(f'{i + 1}-я строка:') for i in range(n)]

m_str = [0, 0]  # Индекс строки с наибольшим кол-вом слов, и количество слов в ней
for ind, el in enumerate(lst):
    el = el.strip(" ")
    n_words = len([word for word in el.split(" ") if word != ""])
    if n_words > m_str[1]:
        m_str[0] = ind
        m_str[1] = n_words

if m_str[1] == 0:
    print("Строки не содержат ни одного слова")
else:
    print(f'Строка с наибольшим количеством строк имеет номер {m_str[0] + 1}. Количество слов в ней - {m_str[1]}:')
    print(lst[m_str[0]])
