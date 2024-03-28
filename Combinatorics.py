import math
import random


# from fractions import Fraction


class CombinatoricsTaskGenerator:
    CONST_NUM_AUTO_TO_STRING = ["0", "1 автомобиль", "2 автомобиля", "3 автомобиля", "4 автомобиля", "5 автомобилей",
                                "6 автомобилей", "7 автомобилей", "8 автомобилей", "9 автомобилей", "10 автомобилей",
                                "11 автомобилей", "12 автомобилей", "13 автомобилей", "14 автомобилей",
                                "15 автомобилей",
                                "16 автомобилей", "17 автомобилей", "18 автомобилей", "19 автомобилей",
                                "20 автомобилей",
                                "21 автомобиль", "22 автомобиля", "23 автомобиля", "24 автомобиля", "25 автомобилей",
                                "26 автомобилей", "27 автомобилей", "28 автомобилей", "29 автомобилей",
                                "30 автомобилей"]

    CONST_NUMBER_TO_STRING_1ST_FORM = [
        "ноль рядов", "один ряд", "два ряда", "три ряда", "четыре ряда", "пять рядов", "шесть рядов",
        "семь рядов", "восемь рядов", "девять рядов", "десять рядов", "одиннадцать рядов", "двенадцать рядов",
        "тринадцать рядов", "четырнадцать рядов", "пятнадцать рядов", "шестнадцать рядов", "семнадцать рядов",
        "восемнадцать рядов", "девятнадцать рядов", "двадцать рядов", "двадцать один ряд", "двадцать два ряда",
        "двадцать три ряда", "двадцать четыре ряда", "двадцать пять рядов", "двадцать шесть рядов",
        "двадцать семь рядов", "двадцать восемь рядов", "двадцать девять рядов", "тридцать рядов"
    ]

    CONST_NUMBERS_TO_STRING = ["нуля", "одного", "двух", "трех", "четырех", "пяти", "шести", "семи", "восьми", "девяти",
                               "десяти",
                               "одиннадцати", "двенадцати", "тринадцати", "четырнадцати", "пятнадцати", "шестнадцати",
                               "семнадцати", "восемнадцати", "девятнадцати", "двадцати", "двадцати одного",
                               "двадцати двух",
                               "двадцати трех", "двадцати четырех", "двадцати пяти", "двадцати шести", "двадцати семи",
                               "двадцати восьми", "двадцати девяти", "тридцати"]

    @staticmethod
    def task_combinatorics_one(number_of_tasks):
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            # Generate random parameters for the combinatorial task
            n = random.randint(5, 9)  # Choose a random number
            random_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random_numbers = random_numbers[:n - 3]
            random.shuffle(random_numbers)

            answer = "размещения с повторениями"
            forbidden_answer = ["сочетания без повторений",
                                "размещения без повторений",
                                "сочетания с повторениями"]

            words = ['пятизначных', 'шестизначных', 'семизначных', 'восьмизначных', 'девяти значных']

            task_text = (
                f"С помощью какой комбинаторной схемы можно построить множество всевозможных {words[n - 5]} чисел, "
                f"в записи которых используются цифры {', '.join(map(str, random_numbers))}?"
            )

            result_tasks_massive.append((task_text, [answer], forbidden_answer))

        return result_tasks_massive

    @staticmethod
    def task_combinatorics_two(number_of_tasks):
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            # Generate random parameters for the combinatorial task
            letters = [symbol for symbol in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()]
            n = random.randint(3, len(letters))  # Choose a random number
            random_letters = random.sample(letters, n)

            answer = "размещения без повторений"
            forbidden_answer = ["сочетания без повторений",
                                "размещения с повторениями",
                                "сочетания с повторениями"]

            task_text = (
                f"С помощью какой комбинаторной схемы можно построить множество всевозможных «слов», "
                f"состоящих из {n} различных букв, если разрешается использовать буквы {', '.join(random_letters)}?"
            )

            result_tasks_massive.append((task_text, [answer], forbidden_answer))

        return result_tasks_massive

    @staticmethod
    def task_combinatorics_three(number_of_tasks):
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            # Generate random parameters for the combinatorial task
            total_chocolates = random.randint(10, 20)
            k = random.randint(2, 9)

            answer = "сочетания без повторений"
            forbidden_answer = ["размещения без повторений",
                                "сочетания с повторениями",
                                "размещения с повторениями"]

            task_text = (
                f"С помощью какой комбинаторной схемы можно построить множество всевозможных способов выбора {k} "
                f"шоколадок, если в продаже имеются {total_chocolates} видов шоколадок?"
            )

            result_tasks_massive.append((task_text, [answer], forbidden_answer))

        return result_tasks_massive

    def task_combinatorics_four(self, number_of_tasks):
        list_task = []

        for i in range(2, 30):
            for j in range(i + 2, 30):
                task_text = (f"С помощью какой комбинаторной схемы можно построить множество всевозможных"
                             f" способов выбора {self.CONST_NUMBERS_TO_STRING[i]}"
                             f" человек из {self.CONST_NUMBERS_TO_STRING[j]} для участия в мероприятии.")
                answer = "сочетания без повторений"
                forbidden_answer = ["размещение без повторений",
                                    "сочетания с повторениями",
                                    "размещения с повторениями"]

                result = (task_text, [answer], forbidden_answer)
                list_task.append(result)

        return list_task

    def task_combinatorics_five(self, number_of_tasks):
        list_task = []

        for i in range(2, 10):
            for j in range(i + 2, 30):
                task_text = (f"С помощью какой комбинаторной схемы можно построить множество всевозможных"
                             f" способов выбора расстановки в {self.CONST_NUMBER_TO_STRING_1ST_FORM[i]}"
                             f" {self.CONST_NUM_AUTO_TO_STRING[j]}.")
                answer = "размещение без повторений"
                forbidden_answer = ["сочетания без повторений",
                                    "сочетания с повторениями",
                                    "размещения с повторениями"]

                result = (task_text, [answer], forbidden_answer)
                list_task.append(result)

        return list_task

    def task_combinatorics_dice(self, number_of_tasks):
        '''
        Опыт состоит в одновременном бросании трех игральных кубиков. Какие события являются случайными относительно этого опыта? (правильный ответ – b, c)
    А – «в сумме выпало меньше 20 очков»;
    В – «в сумме выпало 18 очков;
    С – «в сумме выпало больше 10 очков»;
    D – «в сумме выпало 23 очка».
        :param number_of_tasks:
        :return: List_task
        '''
        list_task = []

        for i in range(number_of_tasks):
            dice = random.randint(2, 6)
            task_text = (f"Опыт состоит в одновременном бросании {dice} игральных кубиков. Какие события являются "
                         f"случайными относительно этого опыта? ")
            answer = set()

            first_ans = random.randint(dice, dice * 6)
            answer.add(f"В сумме выпало {first_ans}")

            forbidden_answer = set()

            while (len(answer) + len(forbidden_answer)) < 4:
                true_false = random.choice([True, False])
                if true_false:
                    type_true = random.choice([True, False])
                    if type_true:
                        generated_value = f"В сумме выпало {random.randint(dice, dice * 6)}"
                    else:
                        random_sign = random.choice(['больше', 'меньше'])
                        generated_value = f"В сумме выпало {random_sign} {random.randint(dice + 1, dice * 6 - 1)}"
                    if generated_value not in answer:
                        answer.add(generated_value)
                else:
                    type_false = random.choice([True, False])
                    if type_false:
                        random_sign_false_1 = random.choice(
                            [random.randint(1, dice - 1), random.randint(dice * 6 + 1, dice * 7)])
                        generated_value = f"В сумме выпало {random_sign_false_1}"
                    else:
                        random_sign_false_2 = random.choice(['больше', 'меньше'])
                        random_sign_false_3 = random.choice(
                            [random.randint(1, dice - 1), random.randint(dice * 6 + 1, dice * 7)])
                        generated_value = f"В сумме выпало {random_sign_false_2} {random_sign_false_3}"
                    if generated_value not in forbidden_answer:
                        forbidden_answer.add(generated_value)

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    def task_combinatorics_moscow(self, number_of_tasks):
        """
        Буквы А, В, К, М, О, С случайным образом располагают в ряд. Какова вероятность того, что получится слово МОСКВА?
         (правильный ответ – c)
        1/6;
        1/120;
        1/720;
        720.
        :param number_of_tasks:
        :return:
        """
        list_task = []
        words = [
            "ВИРАЖ", "ПУСТЫРЬ", "ФУТЛЯР", "КОФЕЙНИК", "ТРЯПЬЕ",
            "МЕШОЧЕК", "ЦИТАДЕЛЬ", "ЛАНДЫШ", "ВОЗДУШНИК", "КАРНИЗ",
            "ДЕКАБРЬ", "НАЖИМ", "СВЕЧКА", "ПАРКЕТ", "МЫЧАНИЕ", "ФОНАРИК",
            "КОЛЧАН", "ПРИТОН", "СВИТОК", "ЧЕМОДАН", "ЯЧМЕНЬ",
            "КОЗЫРЕК", "ТРОПИНКА", "РОЯЛЬ", "ЖИЛЕТКА", "КОВЕР",
            "МИШЕНЬ", "ПОТЯГ", "ШКАФЧИК", "ПРЯЖКА", "ЩЕГОЛЬ",
            "ПЕЧКА", "КОЛЕСНИЦА", "ЗОНТИК", "ПОМЕТ", "КОРЖИК",
            "ГАРПУН", "ПЕРИСКОП", "ФОНАРЬ", "КОСИЧКА",
            "ВИДОК", "КОНЮШНЯ", "КИРКА", "ХЛОПЬЯ",
            "РОЯЛЬ", "ПАРУС", "КОБРА", "ПЛАВНИК",
            "ВЬЮГА", "ВИЛКА", "КОРЗИНА", "ШЛЯПА"
        ]

        for word in words:
            letters = list(word)
            random.shuffle(letters)
            formatted_letters = ', '.join(str(letter) for letter in letters)
            task_text = (
                f"Буквы {formatted_letters} случайным образом располагают в ряд. Какова вероятность того, что получится слово"
                f" {word}?")
            answer = set()
            forbidden_answer = set()
            answer.add(f"1/{math.factorial(len(letters))}")

            forbidden_answer.add(f"1/{len(letters)}")
            forbidden_answer.add(f"1/{math.factorial(len(letters) - 1)}")
            forbidden_answer.add(f"{math.factorial(len(letters))}")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    def task_combinatorics_stud(self, number_of_tasks):
        '''
        В группе 25 студентов, из них 20 человек обучаются по IT-направлениям, 5 человек обучаются по естественно-научным
        направлениям подготовки. Для ответа на вопросы преподавателя вызываются два студента. Событие А – «первый вызванный
        студент обучается по IT-направлению подготовки», событие В – «второй вызванный студент обучается по естественно-научному
        направлению подготовки». Чему равна вероятность пересечения событий А и В? (правильный ответ – a)
        1/6;
        4/25;
        1/5;
        12/25.
        :param number_of_tasks:
        :return: List_task
        '''
        list_task = []

        for i in range(number_of_tasks):
            random_all = random.randint(3, 50)
            random_IT = random.randint(1, random_all)
            another = random_all - random_IT
            task_text = (
                f"В группе {random_all} студентов, из них {random_IT} человек обучаются по IT-направлениям, {another} человек обучаются"
                f" по естественно-научнымнаправлениям подготовки. Для ответа на вопросы преподавателя вызываются"
                f" два студента. Событие А – «первый вызванныйстудент обучается по IT-направлению подготовки», "
                f"событие В – «второй вызванный студент обучается по естественно-научномунаправлению подготовки»."
                f" Чему равна вероятность пересечения событий А и В?")
            answer = set()
            forbidden_answer = set()

            answer.add(f"{random_IT / random_all * another / (random_all - 1):.3f}")
            forbidden_answer.add(f"{random_IT / random_all * another / random_all:.3f}")
            forbidden_answer.add(f"{another / random_all:.3f}")
            forbidden_answer.add(f"{(random_IT / random_all) * (another - 1) / (random_all - 1):.3f}")  # ?????

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    def task_combinatorics_man(self, number_of_tasks):
        '''
        В отделе работают 4 мужчины и 6 женщин. Руководитель организации выбирает двух сотрудников отдела для участия в
        проекте. Событие А - "первый выбранный человек - мужчина", событие В - "второй выбранный человек - мужчина".
        Чему равна вероятность объединения событий А и В? (правильный ответ – b)
        2/15;
        2/3;
        4/5;
        11/15.
        :param number_of_tasks:
        :return: List_task
        '''
        list_task = []

        for i in range(number_of_tasks):
            random_all = random.randint(4, 50)
            Man = random.randint(2, random_all)
            Woman = random_all - Man
            # Man = 4
            # Woman = 6

            task_text = (
                f"В отделе работают {Man} мужчин и {Woman} женщин. Руководитель организации выбирает двух сотрудников"
                f" отдела для участия в проекте. Событие А - 'первый выбранный человек - мужчина', событие В -"
                f" 'второй выбранный человек - мужчина'. Чему равна вероятность объединения событий А и В?")
            answer = set()
            forbidden_answer = set()

            p_A = Man / (Woman + Man)
            p_B_or_A = (Man - 1) / ((Woman + Man) - 1)
            p_A_and_B = p_A * p_B_or_A
            p_ans = p_A * 2 - p_A_and_B

            answer.add(f"{p_ans:.3f} 1")
            forbidden_answer.add(f"{p_A_and_B:.3f} 2")
            forbidden_answer.add(f"{p_A * 2:.3f} 3")
            forbidden_answer.add(f"{1 - p_A_and_B * 2:.3f} 4")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    def task_combinatorics_dice_2(self, number_of_tasks):
        '''
        Опыт состоит в одновременном бросании трех игральных кубиков. Какие события являются случайными относительно этого опыта? (правильный ответ – b, c)
    А – «в сумме выпало меньше 20 очков»;
    В – «в сумме выпало 18 очков;
    С – «в сумме выпало больше 10 очков»;
    D – «в сумме выпало 23 очка».
        :param number_of_tasks:
        :return: List_task
        '''
        list_task = []

        for i in range(number_of_tasks):
            dice = random.randint(3, 7)
            count_dice = random.randint(2, dice - 1)
            random_sign = random.choice(['четное', 'нечетное'])
            dice = 5
            count_dice = 3
            random_sign = random.choice(['четное', 'нечетное'])

            task_text = (f"Опыт состоит в бросании игрального кубика {dice} раз."
                         f" Чему равна вероятность того, что {random_sign}"
                         f" число очков выпадет {count_dice} раза?")
            answer = set()

            answer.add(f"{math.factorial(dice) // (math.factorial(count_dice) * math.factorial(dice - count_dice)) * math.pow(1/2,dice)}")

            forbidden_answer = set()
            forbidden_answer.add(f"{math.factorial(dice) // (math.factorial(count_dice) * math.factorial(dice - count_dice)) * math.pow(1/2,dice+1)}")
            # forbidden_answer.add(f"{math.factorial(dice) // (math.factorial(count_dice) * math.factorial(dice - count_dice)) * math.pow(1/2,dice+1)}")


            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task
