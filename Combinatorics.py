import math
import random
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

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

            numerator = 1
            denominator = x2 - x1

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
                wrong_ev = round(random.uniform(answer - 5, answer + 5),
                                 1)  # Генерация случайного значения в диапазоне от -5 до 5
                if abs(wrong_ev - answer) > 0.3:
                    wrong_answers.add(str(wrong_ev))

            task_text = (f"Плотность случайной величины {latex_equation} математическое ожидание этой случайной "
                         f"величины равно: ")

            result_tasks_massive.append((task_text, [answer], list(wrong_answers)))

        return result_tasks_massive

    '''поиграться с величинами fix'''

    @staticmethod
    def task_combinatorics_normal_distribution(number_of_tasks):
        '''
        Случайная величина Х имеет стандартное нормальное распределение,  математическое ожидание случайной величины У=3-2Х равно (правильный ответ – d)
        -2
        0
        1
        3
        :param number_of_tasks:
        :return: List_task
        '''
        list_task = []

        for i in range(number_of_tasks):
            random_C = random.randint(3, 50)
            random_x = random.randint(1, random_C - 1)
            random_sign = random.choice(['-', '+'])

            task_text = (f"Случайная величина Х имеет стандартное нормальное распределение,"
                         f"  математическое ожидание случайной величины У={random_C}{random_sign}{random_x}Х равно ")
            answer = set()

            answer.add(f"{random_C}")

            forbidden_answer = set()
            forbidden_answer.add(f"0")
            if random_sign == '-':
                forbidden_answer.add(f"{random_sign}{random_x}")
                forbidden_answer.add(f"{random_C - random_x}")

            else:
                forbidden_answer.add(f"{random_x}")
                forbidden_answer.add(f"{random_C + random_x}")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    @staticmethod
    def lecture_4_task_combinatorics_four(number_of_tasks):
        """
            Случайная величина распределена по равномерному закону, значение плотности f(3) = 1 / 2.
            Значение дисперсии этой случайной величины равно (правильный ответ – а)
                a.	1/3
                b.	1/2
                c.	1
                d.	2

        Args:
            number_of_tasks (int): Количество задач для генерации.

        Returns:
            list: Список кортежей, каждый из которых содержит текст задачи,
                  правильный ответ и массив неправильных ответов.
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            x1 = random.randint(0, 7)
            x2 = random.randint(8, 15)
            point = random.randint(x1 + 1, x2)

            # Формируем дробь
            numerator = 1
            denominator = x2 - x1

            # Формируем ответ
            answer = denominator ** 2 / 12
            answer = round(answer, 2)

            latex_equation = (r"""$$ 
            f(""" + str(point) + r""") = \frac\{""" + str(numerator) + r"""\}\{""" + str(denominator) + r"""\} 
            $$""")

            wrong_answers = set()
            wrong_answers.add(str(answer))
            wrong_answers.add(str(round(denominator ** 2 / 6, 2)))
            wrong_answers.add(str(round(denominator / 6, 2)))
            wrong_answers.add(str(round(denominator / 12, 2)))
            wrong_answers.remove(str(answer))

            task_text = (f"Случайная величина распределена по равномерному закону, значение плотности  "
                         f"{latex_equation} Значение дисперсии этой случайной величины равно: ")

            result_tasks_massive.append((task_text, [answer], list(wrong_answers)))

        return result_tasks_massive

    '''проверить формулу, ну уж очень я в ней не уверен fix'''

    @staticmethod
    def task_combinatorics_math_expectation(number_of_tasks):
        '''
        Случайная величина Х – время между вызовами «скорой помощи».  В среднем за один час поступает 10 вызовов.  Математическое ожидание случайной величины Х равно  (правильный ответ – b)
        0,01
        0,1
        10
        10
        :param number_of_tasks:
        :return: List_task
        '''
        list_task = []

        for i in range(number_of_tasks):
            random_t = random.randint(1, 60)

            task_text = (f" Случайная величина Х – время между вызовами «скорой помощи».  В среднем за один час"
                         f" поступает {random_t} вызовов.  Математическое ожидание случайной величины Х равно ")
            answer = set()

            answer.add(f"{1 / random_t:.3f}")

            forbidden_answer = set()
            forbidden_answer.add(f"{1 / math.pow(random_t, 2):.3f}")

            forbidden_answer.add(f"{random_t}")
            forbidden_answer.add(f"{math.pow(random_t, 2)}")
            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    '''жесть че за формула жоская надо уточнять fix'''

    @staticmethod
    def task_combinatorics_normal_distribution_2(number_of_tasks):
        """
        Случайные величины Х, У и Z независимы и имеют нормальное распределение с параметрами  α = 1, σ = 2. Дисперсия суммы этих случайных величин равна (ответ d)
        a.	3
        b.	6
        c.	9
        d.	12

        :param number_of_tasks:
        :return: List_task
        """
        list_task = []

        for i in range(number_of_tasks):
            random_alpha = random.randint(1, 60)
            random_sigma = random.randint(1, 3)

            task_text = (f" Случайные величины Х, У и Z независимы и имеют нормальное распределение "
                         f"с параметрами  α = {random_alpha}, σ = {random_sigma}. Дисперсия суммы этих случайных величин равна")
            answer = set()

            answer.add(f"{math.pow(random_sigma, 2) * 3}")

            forbidden_answer = set()
            forbidden_answer.add(f"{math.pow(random_sigma, 2)}")
            forbidden_answer.add(f"{random_alpha}")
            forbidden_answer.add(f"{math.pow(random_sigma, 2) + random_alpha}")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    '''по хорошему, спросить формулу и подправить вариативность, ложные ответы fix'''
    @staticmethod
    def task_combinatorics_random_distribution(number_of_tasks):
        """
        Плотность случайной величины (1 / np.sqrt(8 * np.pi)) * np.exp(-((x - 3)**2) / 8), дисперсия этой случайной
         величины равна (правильный ответ - d)
        a.	1
        b.	2
        c.	3
        d.	4
        :param number_of_tasks:
        :return: List_task
        """
        list_task = []

        # Формула плотности вероятности

        for i in range(number_of_tasks):
            # random_alpha = random.randint(1, 60)
            # random_sigma = random.randint(1, 3)
            x_min = -10  # Минимальное значение X для интегрирования
            x_max = 10  # Максимальное значение X для интегрирования
            random_a = random.randint(3, 15)
            random_d = random.randint(8, 15)
            def pdf(x):
                return (1 / np.sqrt(random_d * np.pi)) * np.exp(-((x - random_a) ** 2) / random_d)

            task_text = (f"Плотность случайной величины (1 / np.sqrt({ random_d} * np.pi)) * np.exp(-((x - {random_a})**2) / { random_d}),"
                         f" дисперсия этой случайной величины равна")

            # Вычисляем математическое ожидание (среднее)
            e_x = quad(lambda x: x * pdf(x), x_min, x_max)[0]
            # Вычисляем математическое ожидание квадрата
            e_x2 = quad(lambda x: (pdf(x) * x ** 2), x_min, x_max)[0]
            # Вычисляем дисперсию
            variance = e_x2 - e_x ** 2

            answer = set()
            answer.add(f"{variance:.1f}")

            forbidden_answer = set()
            forbidden_answer.add(f"{variance+1:.1f}")
            forbidden_answer.add(f"{variance-1:.1f}")
            forbidden_answer.add(f"{variance-2:.1f}")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task
    '''формула думаю верная, подправить ложные ответы и вариативность рандома fix'''
    @staticmethod
    def task_combinatorics_max_random_distribution(number_of_tasks):
        """
        Плотность случайной величины (1 / np.sqrt(8 * np.pi)) * np.exp(-((x - 3)**2) / 8), точка максимума графика плотности этой случайной величины равна   (правильный ответ - с)
        a.	-3
        b.	0
        c.	3
        d.	4

        :param number_of_tasks:
        :return: List_task
        """
        list_task = []

        # Формула плотности вероятности

        for i in range(number_of_tasks):
            # random_alpha = random.randint(1, 60)
            # random_sigma = random.randint(1, 3)
            x_min = -10  # Минимальное значение X для интегрирования
            x_max = 10  # Максимальное значение X для интегрирования
            random_a = random.randint(3, 15)
            random_d = random.randint(8, 15)

            def pdf(x):
                return (1 / np.sqrt(random_d * np.pi)) * np.exp(-((x - random_a) ** 2) / random_d)

            # Функция для минимизации (максимизации) - отрицательная плотность вероятности,
            # так как minimize_scalar ищет минимум функции
            def neg_pdf(x):
                return -pdf(x)


            task_text = (
                f"Плотность случайной величины (1 / np.sqrt({random_d} * np.pi)) * np.exp(-((x - {random_a})**2) / {random_d}),"
                f" дисперсия этой случайной величины равна")

            result = minimize_scalar(neg_pdf)
            maximum_point = result.x

            answer = set()
            answer.add(f"{maximum_point:.1f}")

            forbidden_answer = set()
            forbidden_answer.add(f"{maximum_point + 1:.1f}")
            forbidden_answer.add(f"{maximum_point - 1:.1f}")
            forbidden_answer.add(f"{maximum_point - 2:.1f}")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    @staticmethod
    def lecture_4_task_combinatorics_ten(number_of_tasks):
        """
          Плотность случайной величины f(x) функция распределения этой случайной величины в точке  2 равна
          (правильный ответ –b )
            a.	0,125
            b.	0,25
            c.	0,5
            d.	0,75

        Args:
            number_of_tasks (int): Количество задач для генерации.

        Returns:
            list: Список кортежей, каждый из которых содержит текст задачи,
                  правильный ответ и массив неправильных ответов.
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            x1 = random.randint(0, 9)
            x2 = random.randint(10, 20)
            point = random.randint(x1 + 1, x2)

            # Формируем дробь
            numerator = 1
            denominator = x2 - x1
            fraction = numerator / denominator

            # Формируем ответ
            answer = fraction * (point - x1)
            answer = round(answer, 3)

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
                wrong_ev = round(random.uniform(0, 1), 3)
                if abs(wrong_ev - answer) > 0.2:
                    wrong_answers.add(str(wrong_ev))

            task_text = (f"Плотность случайной величины {latex_equation} функция распределения этой случайной "
                         f"величины в точке {point} равна: ")

            result_tasks_massive.append((task_text, [answer], list(wrong_answers)))

        return result_tasks_massive

    # endregion

    # region КР № 1
    @staticmethod
    def task_combinatorics_dice(number_of_tasks):
        """
        Опыт состоит в одновременном бросании трех игральных кубиков. Какие события являются случайными относительно этого опыта? (правильный ответ – b, c)
            А – «в сумме выпало меньше 20 очков»;
            В – «в сумме выпало 18 очков;
            С – «в сумме выпало больше 10 очков»;
            D – «в сумме выпало 23 очка».
        :param number_of_tasks:
        :return: List_task
        """
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

    '''требуется проверка fix'''

    @staticmethod
    def task_combinatorics_1_2(number_of_tasks):
        """
        Из пяти участников команды выбирают организатора совместной работы и человека, который будет представлять ее результаты (это должны быть разные люди).  С помощью какой комбинаторной схемы можно построить множество способов такого выбора? (правильный ответ – b)
        сочетания без повторений;
        размещения без повторений;
        сочетания с повторениями;
        размещения с повторениями.
        :param number_of_tasks:
        :return:
        """
        list_task = []

        for i in range(number_of_tasks):
            random_people = random.randint(5, 100)
            task_text = (
                f"Из {random_people} участников команды выбирают организатора совместной работы и человека, который"
                f" будет представлять ее результаты (это должны быть разные люди).  С помощью какой комбинаторной схемы"
                f" можно построить множество способов такого выбора?")
            answer = set()
            forbidden_answer = set()
            answer.add("размещения без повторений")

            forbidden_answer.add("сочетания без повторений")
            forbidden_answer.add("сочетания с повторениями")
            forbidden_answer.add("размещения с повторениями")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    '''требуется проверка fix'''

    @staticmethod
    def task_combinatorics_1_3(number_of_tasks):
        """
        Девушка выбирает 3 платья из 14, имеющихся в магазине. С помощью какой комбинаторной схемы можно построить
         множество способов такого выбора? (правильный ответ – a)
        сочетания без повторений;
        размещения без повторений;
        сочетания с повторениями;
        размещения с повторениями.
        :param number_of_tasks:
        :return:
        """
        list_task = []

        for i in range(number_of_tasks):
            all_cust = random.randint(14, 1000)
            random_cust = random.randint(3, all_cust - 15)
            task_text = (
                f"Девушка выбирает 3 платья из 14, имеющихся в магазине. С помощью какой комбинаторной схемы можно"
                f" построить множество способов такого выбора?")
            answer = set()
            forbidden_answer = set()
            answer.add("размещения без повторений")

            forbidden_answer.add("сочетания без повторений")
            forbidden_answer.add("сочетания с повторениями")
            forbidden_answer.add("размещения с повторениями")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    @staticmethod
    def task_combinatorics_moscow(number_of_tasks):

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

    @staticmethod
    def task_combinatorics_stud(number_of_tasks):
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

    '''может быть косяк с тем как считается надо уточнить этот момент fix'''

    @staticmethod
    def task_combinatorics_man(number_of_tasks):
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

            answer.add(f"{p_ans:.3f}")
            forbidden_answer.add(f"{p_A_and_B:.3f}")
            forbidden_answer.add(f"{p_A * 2:.3f}")
            forbidden_answer.add(f"{1 - p_A_and_B * 2:.3f}")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    '''требуется проверка формулы плюсом поиграть с разбросом fix'''

    @staticmethod
    def task_combinatorics_dice_2(number_of_tasks):
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
            dice = random.randint(5, 7)
            count_dice = random.randint(2, dice - 2)
            random_sign = random.choice(['четное', 'нечетное'])
            # dice = 5
            # count_dice = 3
            # random_sign = random.choice(['четное', 'нечетное'])

            task_text = (f"Опыт состоит в бросании игрального кубика {dice} раз."
                         f" Чему равна вероятность того, что {random_sign}"
                         f" число очков выпадет {count_dice} раза?")
            answer = set()

            answer.add(
                f"{math.factorial(dice) // (math.factorial(count_dice) * math.factorial(dice - count_dice)) * math.pow(1 / 2, dice):.3f}")

            forbidden_answer = set()
            forbidden_answer.add(
                f"{math.factorial(dice) // (math.factorial(count_dice) * math.factorial(dice - count_dice)) * math.pow(1 / 2, dice + 1):.3f}")
            forbidden_answer.add(
                f"{math.pow(1 / 2, count_dice):.3f}")
            forbidden_answer.add(
                f"{(1 / 2) * count_dice}")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    # endregion
