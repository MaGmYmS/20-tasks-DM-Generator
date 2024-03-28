import random


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

    # region Тест по лекции № 1
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

    # endregion

    # region Тест по лекции № 2
    @staticmethod
    def probability_of_value(number_of_tasks):
        """
        3	Случайная величина Х принимает три возможных значения х1, х2, х3. Значение х1 она принимает с вероятностью
        0,4, значение х2 – с вероятностью 0,5. С какой вероятностью случайная величина Х принимает значение х3?
        (правильный ответ – a)
            a.	0,1;
            b.	0,9;
            c.	0,45;
            d.	невозможно определить вероятность.
        :return: list: Список кортежей, каждый из которых содержит текст задачи,
                  правильный ответ и массив неправильных ответов.
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            p1 = round(random.uniform(0.1, 0.5), 1)
            p2 = round(random.uniform(0.1, 0.9 - p1), 1)

            # Вычисляем вероятность для x3
            p3 = round(1 - p1 - p2, 1)

            # Генерируем неправильные ответы
            wrong_answers = set()
            while len(wrong_answers) < 3:
                wrong_p = round(random.uniform(0.1, 0.9), 1)
                if wrong_p != p3:
                    wrong_answers.add(wrong_p)

            # Составляем текст задачи
            task_text = (
                f"Случайная величина X принимает три возможных значения x1, x2, x3. "
                f"Значение x1 она принимает с вероятностью {p1}, значение x2 – с вероятностью {p2}. "
                f"С какой вероятностью случайная величина X принимает значение x3?"
            )

            result_tasks_massive.append((task_text, [p3], list(wrong_answers)))

        return result_tasks_massive

    # endregion

    # region Тест по лекции № 3
    @staticmethod
    def expected_value(number_of_tasks):
        """
        Генерирует задачу по определению математического ожидания случайной величины.

        Args:
            number_of_tasks (int): Количество задач для генерации.

        Returns:
            list: Список кортежей, каждый из которых содержит текст задачи,
                  правильный ответ и массив неправильных ответов.
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            # Генерируем случайные вероятности p1, p2, p3 так, чтобы их сумма была равна 1
            p1 = round(random.uniform(0.1, 0.5), 1)
            p2 = round(random.uniform(0.1, 0.1 + p1), 1)
            p3 = round(1 - p1 - p2, 1)

            random_variables = [random.randint(-5, 5) for _ in range(3)]

            expected_value = random_variables[0] * p1 + random_variables[1] * p2 + random_variables[2] * p3

            expected_value_str = "{:.1f}".format(expected_value)

            wrong_answers = set()
            while len(wrong_answers) < 3:
                wrong_ev = round(random.uniform(-5, 5), 1)  # Генерация случайного значения в диапазоне от -5 до 5
                if wrong_ev != round(expected_value, 1):
                    wrong_answers.add(str(wrong_ev))

            # Составляем текст задачи
            task_text = (
                f"Случайная величина принимает значения {random_variables[0]}, {random_variables[1]} и "
                f"{random_variables[2]} с вероятностями {p1}, {p2} и {p3} соответственно. "
                f"Математическое ожидание этой случайной величины равно:"
            )

            result_tasks_massive.append((task_text, [expected_value_str], list(wrong_answers)))

        return result_tasks_massive

    # endregion

    # region Тест по лекции № 4
    @staticmethod
    def lecture_4_task_combinatorics_two(number_of_tasks):
        """
          Плотность случайной величины f(x) математическое ожидание этой случайной величины равно (правильный ответ – с)
            a.	4
            b.	6
            c.	7
            d.	10
        Args:
            number_of_tasks (int): Количество задач для генерации.

        Returns:
            list: Список кортежей, каждый из которых содержит текст задачи,
                  правильный ответ и массив неправильных ответов.
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            x1 = random.randint(1, 9)
            x2 = random.randint(10, 20)
            
            numerator = random.randint(1, 9)
            denominator = random.randint(10, 20)

            answer = (x2 ** 2 - x1 ** 2) * numerator / (2 * denominator)
            answer = round(answer, 1)

            latex_equation = (r"""
            \[
            f(x) = 
            \begin\{cases\}
                0 & \text\{при \} x \\le \{""" + str(x1) + r"""\} \\\
                \frac\{""" + str(numerator) + r"""\}\{""" + str(denominator) + r"""\} & \text\{при \} \{""" + str(x1)
                              + r"""\} < x < \{""" + str(x2) + r"""\} \\\
                0 & \text\{при \} x \\ge \{""" + str(x2) + r"""\}
            \end\{cases\}
            \]
            """)

            wrong_answers = set()
            while len(wrong_answers) < 3:
                wrong_ev = round(random.uniform(answer - 5, answer + 5), 1)  # Генерация случайного значения в диапазоне от -5 до 5
                if abs(wrong_ev - answer) > 0.3:
                    wrong_answers.add(str(wrong_ev))

            task_text = (f"Плотность случайной величины {latex_equation} математическое ожидание этой случайной "
                         f"величины равно: ")

            result_tasks_massive.append((task_text, [answer], list(wrong_answers)))

        return result_tasks_massive
    # endregion

    # region КР № 1

    # endregion
