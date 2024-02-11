import TextFuncs as tf

# Введенного текста удалить арифм выражения, вывести слово с наиб количеством вхождений
class TextProcessor:
    def __init__(self, text: list):
        self.text = text  # Сам текст ввиде списка строк
        self.alignment = None  # Вид выравнивания на данный момент

    def __str__(self):
        return "\n".join(self.text)

    def __aling_to_left(self):  # Выравнивание по левому краю
        for ind, line in enumerate(self.text):
            was_gap = False
            new_line = ""
            for symb in line.strip():
                if symb == " " and not was_gap:
                    was_gap = True
                elif symb == " ":
                    continue
                else:
                    was_gap = False
                new_line += symb
            self.text[ind] = new_line

    def __align_to_right(self):  # Выравнивание по правому краю
        max_len = self.find_max_len()
        for ind, line in enumerate(self.text):
            was_gap = False
            new_line = ""
            for symb in line.strip():
                if symb == " " and not was_gap:
                    was_gap = True
                elif symb == " ":
                    continue
                else:
                    was_gap = False
                new_line += symb
            self.text[ind] = new_line
        for ind, line in enumerate(self.text):
            self.text[ind] = " " * (max_len - len(line)) + line

    def __align_to_width(self):  # Выравнивание по ширине
        max_len = self.find_max_len()
        for ind, line in enumerate(self.text):
            was_gap = False
            new_line = ""
            for symb in line.strip():
                if symb == " " and not was_gap:
                    was_gap = True
                elif symb == " ":
                    continue
                else:
                    was_gap = False
                new_line += symb
            self.text[ind] = new_line
        for ind, line in enumerate(self.text):
            if line.strip() == "":
                continue
            n_gaps = line.count(" ")
            gap_width, n_gap_replace = divmod(max_len - len(line) + n_gaps, n_gaps)
            self.text[ind] = self.text[ind].replace(" ", " " * gap_width).replace(" " * gap_width,
                                                                                  " " * (gap_width + 1),
                                                                                  n_gap_replace)

    def __delete_empty_lines(self):  # Метод для удаления пустых строк их текста
        i = 0
        while i < len(self.text):
            if self.text[i] == "":
                del self.text[i]
                i -= 1
            i += 1

    def find_max_len(self):  # Метод для нахождения максимальной длины строки
        return max([len(i) for i in self.text]) if len(self.text) > 0 else 0

    def align(self, alignment="self"):  # Метод для выравнивания текста
        if alignment == "self":
            if self.alignment is not None:
                self.align(self.alignment)
        elif alignment == "left":
            self.alignment = "left"
            self.__aling_to_left()
        elif alignment == "right":
            self.alignment = "right"
            self.__align_to_right()
        elif alignment == "width":
            self.alignment = "width"
            self.__align_to_width()

    def delete_word(self, word):  # Метод для удаления слова из текста
        was_deleted = False
        for ind_l, line in enumerate(self.text):
            line_split = line.split()
            for ind_w, w in enumerate(line_split):
                if tf.get_word_without_punction(w) == word:
                    punc = tf.get_punction_without_word(w)
                    if ind_w != 0:
                        line_split[ind_w - 1] = line_split[ind_w - 1] + punc
                        del line_split[ind_w]
                    elif ind_l != 0:
                        self.text[ind_l - 1] = self.text[ind_l - 1] + punc
                        del line_split[ind_w]
                    else:
                        line_split[ind_w] = punc
                    was_deleted = True
            self.text[ind_l] = " ".join(line_split)
        self.align()
        return was_deleted

    def replace_word(self, word, rep):  # Метод для замены слова на другое
        was_replaced = False
        for ind_l, line in enumerate(self.text):
            line_split = line.split()
            for ind_w, w in enumerate(line_split):
                if tf.get_word_without_punction(w) == word:
                    punc = tf.get_punction_without_word(w)
                    line_split[ind_w] = rep + punc
                    was_replaced = True
            self.text[ind_l] = " ".join(line_split)
        self.align()
        return was_replaced

    def do_calcs(self): # Метод для проведения вычислений в тексте
        done_calc = False
        for ind, line in enumerate(self.text):
            exp_ind_st = 0
            exp = ""
            now_exp = False
            ind_s = 0
            while ind_s < len(line):
                symb = line[ind_s]
                s2 = line[exp_ind_st]
                if line[ind_s] in tf.POS_SYMBS_FOR_CALCULUS:
                    if not now_exp:
                        exp_ind_st = ind_s
                    exp_ind_ed = ind_s
                    exp += line[ind_s]
                    now_exp = True
                elif line[ind_s] != " ":
                    if now_exp:
                        now_exp = False
                        res = tf.calc_exp(tf.clear_exp(exp))
                        if res != "ERROR":
                            line = line[:exp_ind_st] + res + line[exp_ind_ed + 1:]
                            exp = ""
                            ind_s = exp_ind_st + len(res)
                            done_calc = True
                ind_s += 1
            if now_exp:
                now_exp = False
                res = tf.calc_exp(tf.clear_exp(exp))
                if res != "ERROR":
                    line = line[:exp_ind_st] + res + line[exp_ind_ed + 1:]
                    exp = ""
                    ind_s = exp_ind_st + len(res)
            self.text[ind] = line
        self.align()
        return done_calc

    def pop_sentence(self): # Метод, удаляющий предложение со словом с максимальным количеством согласных
        now_sentence = [(0, 0), 0]
        max_sentence = ((0, 0), (0, 0), 0)

        for ind_l, line in enumerate(self.text):
            now_word_cons = 0
            for ind_s, symb in enumerate(line):
                if symb == " ":
                    now_sentence[1] = max(now_sentence[1], now_word_cons)
                    now_word_cons = 0
                elif symb.upper() in tf.CONSORNANTS:
                    now_word_cons += 1
                elif symb in tf.END_SENTENCE_SYMB:
                    now_sentence[1] = max(now_sentence[1], now_word_cons)
                    if now_sentence[1] > max_sentence[2]:
                        max_sentence = (now_sentence[0], (ind_l, ind_s), now_sentence[1])
                    now_sentence = [(ind_l, ind_s + 1), 0]
        if max_sentence[2] != 0:
            max_sentence_text = ""
            st_l = max_sentence[0][0]
            ed_l = max_sentence[1][0]
            for _ in range(st_l + 1, ed_l):
                max_sentence_text += self.text[st_l]
                del self.text[st_l + 1]
            self.text = self.text[:st_l + 1] + self.text[ed_l:]
            max_sentence_text = self.text[st_l][max_sentence[0][1]:]  + " " + max_sentence_text + " " + self.text[st_l + 1][
                                                                                           :max_sentence[1][1] + 1]
            self.text[st_l] = self.text[st_l][:max_sentence[0][1]]
            self.text[st_l + 1] = self.text[st_l + 1][max_sentence[1][1] + 1:]
            self.__delete_empty_lines()
            self.align()
            return max_sentence_text
        return False


if __name__ == "__main__":
    test = ["   Неделю спустя Дориан, Грей сидел lllllllllll в оранжерее",
            "5*5     своей, усадьбы СелбиРойял,   беседуя с  40 / 20 * 5  5*5   хорошенькой герцогиней Монмаут, 25*25",
            "    которая гостила у него вместе     с мужем, высохшим шестидесятилетним стариком."
            ]
    tp = TextProcessor(test)
    tp.align("width")
    print(tp)
    tp.delete_word("Дориан")
    print(tp)
