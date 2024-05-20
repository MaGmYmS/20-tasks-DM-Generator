import math
import random
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
import itertools
from sympy import symbols, expand, collect
import re


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
    def lecture_1_task_combinatorics_one(number_of_tasks):
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
    def lecture_1_task_combinatorics_two(number_of_tasks):
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
    def lecture_1_task_combinatorics_three(number_of_tasks):
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

    def lecture_1_task_combinatorics_four(self, number_of_tasks):
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
                if len(list_task) == number_of_tasks:
                    return list_task

        return list_task

    def lecture_1_task_combinatorics_five(self, number_of_tasks):
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
                if len(list_task) == number_of_tasks:
                    return list_task

        return list_task

    # endregion

    # region Тест по лекции № 2
    @staticmethod
    def lecture_2_probability_of_value(number_of_tasks):
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
    def lecture_3_expected_value(number_of_tasks):
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
    def lecture_4_task_combinatorics_one(number_of_tasks):
        """
          Плотность случайной величины f(x) математическое ожидание этой случайной величины равно (правильный ответ – с)
            a.	2
            b.	1
            c.	0,5
            d.	0,25
        Args:
            number_of_tasks (int): Количество задач для генерации.

        Returns:
            list: Список кортежей, каждый из которых содержит текст задачи,
                  правильный ответ и массив неправильных ответов.
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            lambda_x = random.randint(1, 100)

            answer = 1 / lambda_x
            answer = round(answer, 2)

            latex_equation = (r"""
            \[
            f(x) = 
            \begin\{cases\}
                0 & \text\{при \} x < \{0\} \\\
                """ + str(lambda_x) + r""" e^\{-""" + str(lambda_x) + r"""x\}  & \text\{при \} x \\ge \{0\}
            \end\{cases\}
            \]
            """)

            wrong_answers = set()
            wrong_answers.add(str(answer))
            wrong_answers.add(str(round(answer * 2, 2)))
            wrong_answers.add(str(round(answer * 4, 2)))
            wrong_answers.add(str(round(answer / 2, 2)))
            wrong_answers.remove(str(answer))

            task_text = (f"Плотность случайной величины {latex_equation} математическое ожидание этой случайной "
                         f"величины равно: ")

            result_tasks_massive.append((task_text, [answer], list(wrong_answers)))

        return result_tasks_massive

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

    @staticmethod
    def lecture_4_task_combinatorics_three(number_of_tasks):
        """
        Случайная величина Х имеет стандартное нормальное распределение,  математическое ожидание случайной величины
        У=3-2Х равно (правильный ответ – d)
        -2
        0
        1
        3
        :param number_of_tasks:
        :return: List_task
        """
        list_task = []

        for i in range(number_of_tasks):
            random_c = random.randint(3, 50)
            random_x = random.randint(1, random_c - 1)
            random_sign = random.choice(['-', '+'])

            task_text = (f"Случайная величина Х имеет стандартное нормальное распределение,"
                         f"  математическое ожидание случайной величины У={random_c}{random_sign}{random_x}Х равно ")
            answer = set()

            answer.add(f"{random_c}")

            forbidden_answer = set()
            forbidden_answer.add(f"0")
            if random_sign == '-':
                forbidden_answer.add(f"{random_sign}{random_x}")
                forbidden_answer.add(f"{random_c - random_x}")

            else:
                forbidden_answer.add(f"{random_x}")
                forbidden_answer.add(f"{random_c + random_x}")

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

    @staticmethod
    def lecture_4_task_combinatorics_five(number_of_tasks):
        """
        Случайная величина Х – время между вызовами «скорой помощи».  В среднем за один час поступает 10 вызовов.
        Математическое ожидание случайной величины Х равно  (правильный ответ – b)
        0,01
        0,1
        10
        10
        :param number_of_tasks:
        :return: List_task
        """
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

    @staticmethod
    def lecture_4_task_combinatorics_six(number_of_tasks):
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

            latex_equation = (r"""$$ 
                                   \frac\{1\}\{\sqrt\{""" + str(
                random_d) + r"""\pi\}\}\exp\{\left(-\frac\{(x - """ + str(random_a)
                              + r""")^\{2\}\}\{""" + str(random_d) + r"""\}\right)\} 
                                   $$""")

            task_text = (
                f"Плотность случайной величины {latex_equation},"
                f" дисперсия этой случайной величины равна")

            # Вычисляем математическое ожидание (среднее)
            e_x = quad(lambda x: x * pdf(x), x_min, x_max)[0]
            # Вычисляем математическое ожидание квадрата
            e_x2 = quad(lambda x: (pdf(x) * x ** 2), x_min, x_max)[0]
            # Вычисляем дисперсию
            variance = e_x2 - e_x ** 2

            answer = round(random_d / 2, 1)
            # answer.add(f"{variance:.1f}")

            forbidden_answer = set()
            forbidden_answer.add(f"{variance + 1:.1f}")
            forbidden_answer.add(f"{variance - 1:.1f}")
            forbidden_answer.add(f"{variance - 2:.1f}")

            result = (task_text, [answer], list(forbidden_answer))
            list_task.append(result)

        return list_task

    @staticmethod
    def lecture_4_task_combinatorics_seven(number_of_tasks):
        """
        Случайные величины Х, У и Z независимы и имеют нормальное распределение с параметрами  α = 1, σ = 2.
        Дисперсия суммы этих случайных величин равна (ответ d)
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
                         f"с параметрами  α = {random_alpha}, σ = {random_sigma}. "
                         f"Дисперсия суммы этих случайных величин равна")
            answer = set()

            answer.add(f"{math.pow(random_sigma, 2) * 3}")

            forbidden_answer = set()
            forbidden_answer.add(f"{math.pow(random_sigma, 2)}")
            forbidden_answer.add(f"{random_alpha}")
            forbidden_answer.add(f"{math.pow(random_sigma, 2) + random_alpha}")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    @staticmethod
    def lecture_4_task_combinatorics_eight(number_of_tasks):
        """
        Плотность случайной величины (1 / np.sqrt(8 * np.pi)) * np.exp(-((x - 3)**2) / 8),
        точка максимума графика плотности этой случайной величины равна (правильный ответ - с)
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
            random_a = random.randint(3, 15)
            random_d = random.randint(8, 15)

            def pdf(x):
                return (1 / np.sqrt(random_d * np.pi)) * np.exp(-((x - random_a) ** 2) / random_d)

            # Функция для минимизации (максимизации) - отрицательная плотность вероятности,
            # так как minimize_scalar ищет минимум функции
            def neg_pdf(x):
                return -pdf(x)

            latex_equation = (r"""$$ 
                                              \frac\{1\}\{\sqrt\{""" + str(
                random_d) + r"""\pi\}\}\exp\{\left(-\frac\{(x - """ + str(random_a)
                              + r""")^\{2\}\}\{""" + str(random_d) + r"""\}\right)\} 
                                              $$""")

            task_text = (
                f"Плотность случайной величины {latex_equation},"
                f" точка максимума графика плотности величины равна")

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
    # TODO: другой вариант ответов, может быть несколько правильных
    @staticmethod
    def control_work_task_combinatorics_dice(number_of_tasks):
        """
        Опыт состоит в одновременном бросании трех игральных кубиков. Какие события являются случайными относительно
        этого опыта? (правильный ответ – b, c)
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

    @staticmethod
    def control_work_task_combinatorics_1_2(number_of_tasks):
        """
        Из пяти участников команды выбирают организатора совместной работы и человека, который будет представлять ее
        результаты (это должны быть разные люди).  С помощью какой комбинаторной схемы можно построить множество
        способов такого выбора? (правильный ответ – b)
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

    @staticmethod
    def control_work_task_combinatorics_1_3(number_of_tasks):
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
            random_cust = random.randint(3, all_cust - 10)
            task_text = (
                f"Девушка выбирает {random_cust} платья из {all_cust}, имеющихся в магазине. С помощью какой "
                f"комбинаторной схемы можно построить множество способов такого выбора?")
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
    def control_work_task_combinatorics_moscow(number_of_tasks):

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

        for i, word in enumerate(words):
            letters = list(word)
            random.shuffle(letters)
            formatted_letters = ', '.join(str(letter) for letter in letters)
            task_text = (
                f"Буквы {formatted_letters} случайным образом располагают в ряд. Какова вероятность того, "
                f"что получится слово {word}?")
            answer = set()
            forbidden_answer = set()
            answer.add(f"1/{math.factorial(len(letters))}")

            forbidden_answer.add(f"1/{len(letters)}")
            forbidden_answer.add(f"1/{math.factorial(len(letters) - 1)}")
            forbidden_answer.add(f"{math.factorial(len(letters))}")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)
            if i + 1 == number_of_tasks:
                break

        return list_task

    @staticmethod
    def control_work_task_combinatorics_stud(number_of_tasks):
        """
        В группе 25 студентов, из них 20 человек обучаются по IT-направлениям, 5 человек обучаются по
        естественно-научным направлениям подготовки. Для ответа на вопросы преподавателя вызываются два студента.
        Событие А – «первый вызванный студент обучается по IT-направлению подготовки», событие В – «второй вызванный
        студент обучается по естественно-научному направлению подготовки». Чему равна вероятность пересечения событий
        А и В? (правильный ответ – a)
        1/6;
        4/25;
        1/5;
        12/25.
        :param number_of_tasks:
        :return: List_task
        """
        list_task = []

        for i in range(number_of_tasks):
            random_all = random.randint(3, 50)
            random_it = random.randint(1, random_all)
            another = random_all - random_it
            task_text = (
                f"В группе {random_all} студентов, из них {random_it} человек обучаются по IT-направлениям, {another} "
                f"человек обучаются по естественно-научным направлениям подготовки. Для ответа на вопросы преподавателя"
                f" вызываются два студента. Событие А – «первый вызванный студент обучается по IT-направлению "
                f"подготовки», событие В – «второй вызванный студент обучается по естественно-научному направлению "
                f"подготовки». Чему равна вероятность пересечения событий А и В?")
            answer = set()
            forbidden_answer = set()

            answer.add(f"{random_it / random_all * another / (random_all - 1):.3f}")
            forbidden_answer.add(f"{random_it / random_all * another / random_all:.3f}")
            forbidden_answer.add(f"{another / random_all:.3f}")
            forbidden_answer.add(f"{(random_it / random_all) * (another - 1) / (random_all - 1):.3f}")  # ?????

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    @staticmethod
    def control_work_task_combinatorics_man(number_of_tasks):
        """
        В отделе работают 4 мужчины и 6 женщин. Руководитель организации выбирает двух сотрудников отдела для участия в
        проекте. Событие А - "первый выбранный человек - мужчина", событие В - "второй выбранный человек - мужчина".
        Чему равна вероятность объединения событий А и В? (правильный ответ – b)
        2/15;
        2/3;
        4/5;
        11/15.
        :param number_of_tasks:
        :return: List_task
        """
        list_task = []

        for i in range(number_of_tasks):
            random_all = random.randint(4, 50)
            man = random.randint(2, random_all)
            woman = random_all - man
            # Man = 4
            # Woman = 6

            task_text = (
                f"В отделе работают {man} мужчин и {woman} женщин. Руководитель организации выбирает двух сотрудников"
                f" отдела для участия в проекте. Событие А - 'первый выбранный человек - мужчина', событие В -"
                f" 'второй выбранный человек - мужчина'. Чему равна вероятность объединения событий А и В?")
            answer = set()
            forbidden_answer = set()

            p_A = man / (woman + man)
            p_B_or_A = (man - 1) / ((woman + man) - 1)
            p_A_and_B = p_A * p_B_or_A
            p_ans = p_A * 2 - p_A_and_B

            answer.add(f"{p_ans:.3f}")
            forbidden_answer.add(f"{p_A_and_B:.3f}")
            forbidden_answer.add(f"{p_A * 2:.3f}")
            forbidden_answer.add(f"{1 - p_A_and_B * 2:.3f}")

            result = (task_text, list(answer), list(forbidden_answer))
            list_task.append(result)

        return list_task

    @staticmethod
    def control_work_task_combinatorics_dice_2(number_of_tasks):
        """
        Опыт состоит в бросании игрального кубика 5 раз. Чему равна вероятность того, что четное число очков выпадет 3
        раза? (правильный ответ – c)
        1/8;
        3/2;
        5/16;
        5/32.
        :param number_of_tasks:
        :return: List_task
        """
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

    # region Тест по лекции № 6
    @staticmethod
    def lecture_6_task_combinatorics_one(number_of_tasks):
        """
        Под выборкой в гипотетическом варианте интерпретации понимаем (правильный ответ – d)
            a.	случайную величину
            b.	набор конкретных чисел
            c.	последовательность независимых случайных величин, распределенных по нормальному закону
            d.	последовательность независимых одинаково распределенных случайных величин

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Под выборкой в гипотетическом варианте интерпретации понимаем"
            answer = set()
            forbidden_answer = set()
            answer.add("последовательность независимых одинаково распределенных случайных величин")

            forbidden_answer.add("случайную величину")
            forbidden_answer.add("набор конкретных чисел")
            forbidden_answer.add("последовательность независимых случайных величин, "
                                 "распределенных по нормальному закону")

            result = (task_text, list(answer), list(forbidden_answer))
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_6_task_combinatorics_two(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом из четырех вариантов.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Выборка будет репрезентативной, если"
            answer = set()
            forbidden_answer = set()
            answer.add("её осуществить случайным образом, при этом все объекты генеральной совокупности имеют "
                       "одинаковую вероятность попасть в выборку")

            forbidden_answer.add("её осуществить случайным образом")
            forbidden_answer.add("её объем будет больше половины объема генеральной совокупности")
            forbidden_answer.add("её объем будет больше половины объема генеральной совокупности и распределение "
                                 "выборки будет подчинено нормальному закону")

            result = (task_text, list(answer), list(forbidden_answer))
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_6_task_combinatorics_three(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом из четырех вариантов.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Число, показывающие сколько раз варианта встречалась в выборке, называется"
            answer = set()
            forbidden_answer = set()
            answer.add("частотой")

            forbidden_answer.add("модой")
            forbidden_answer.add("относительной частотой")
            forbidden_answer.add("эмпирической вероятностью")

            result = (task_text, list(answer), list(forbidden_answer))
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_6_task_combinatorics_four(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом из четырех вариантов.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = ("Совокупность всех возможных объектов данного вида, над которыми проводятся наблюдения с "
                         "целью получения конкретных значений определенной случайной величины, называется")
            answer = set()
            forbidden_answer = set()
            answer.add("генеральной совокупностью")

            forbidden_answer.add("выборкой")
            forbidden_answer.add("вариантами")
            forbidden_answer.add("выборочной совокупностью")

            result = (task_text, list(answer), list(forbidden_answer))
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_6_task_combinatorics_five(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом из четырех вариантов.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = ("Статистическая оценка, которая при любом объеме выборки дает систематически завышенную "
                         "оценку оцениваемого параметра, является")
            answer = set()
            forbidden_answer = set()
            answer.add("смещенной")

            forbidden_answer.add("несмещенной")
            forbidden_answer.add("модой")
            forbidden_answer.add("несостоятельной")

            result = (task_text, list(answer), list(forbidden_answer))
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_6_task_combinatorics_six(number_of_tasks):
        """
        Генерирует задачи с несколькими правильными ответами.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Выборочная средняя является оценкой"
            correct_answers = ["математического ожидания генеральной совокупности",
                               "параметра a нормально распределенной генеральной совокупности",
                               "абсциссы симметрии теоретической плотности нормально распределенной "
                               "генеральной совокупности",
                               "параметра λ генеральной совокупности, распределенной по закону Пуассона"]
            result = (task_text, correct_answers, [])
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_6_task_combinatorics_seven(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом из четырех вариантов.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Средние большого числа наблюдений обнаруживают свойство устойчивости на основании"
            answer = set()
            forbidden_answer = set()
            answer.add("ЗБЧ")

            forbidden_answer.add("ДСВ")
            forbidden_answer.add("НСВ")
            forbidden_answer.add("ФСБ")

            result = (task_text, list(answer), list(forbidden_answer))
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_6_task_combinatorics_eight(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом из четырех вариантов.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Требование несмещенности гарантирует"
            answer = set()
            forbidden_answer = set()
            answer.add("отсутствие систематических ошибок")

            forbidden_answer.add("состоятельность оценки")
            forbidden_answer.add("несостоятельность оценки")
            forbidden_answer.add("нормальное распределение генеральной совокупности")

            result = (task_text, list(answer), list(forbidden_answer))
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_6_task_combinatorics_nine(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом из четырех вариантов.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Если все варианты уменьшить на одно и то же число k, то выборочная дисперсия"
            answer = set()
            forbidden_answer = set()
            answer.add("не измениться")

            forbidden_answer.add("уменьшиться на то же число k")
            forbidden_answer.add("уменьшиться в k раз")
            forbidden_answer.add("уменьшиться в k^2 раз")

            result = (task_text, list(answer), list(forbidden_answer))
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_6_task_combinatorics_ten(number_of_tasks):
        """
        Генерирует задачи с несколькими правильными ответами.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильные_ответы, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Выборочная дисперсия является"
            correct_answers = ["состоятельной оценкой генеральной дисперсии", "смещенной оценкой генеральной дисперсии"]
            incorrect_answers = ["несмещенной оценкой генеральной дисперсии", "несостоятельной оценкой генеральной "
                                                                              "дисперсии"]
            result = (task_text, correct_answers, incorrect_answers)
            list_tasks.append(result)

        return list_tasks

    # endregion

    # region Тест по лекции № 7
    @staticmethod
    def lecture_7_task_combinatorics_one(number_of_tasks):
        """
        Генерирует задачи с несколькими правильными ответами.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильные_ответы, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Выберите из предложенных вариантов формулировки гипотез"
            correct_answers = ["Генеральная совокупность имеет нормальное распределение",
                               "Номинальный размер детали 15 мм"]
            incorrect_answers = ["Выборочная совокупность имеет нормальное распределение",
                                 "Варианты выборки независимы и распределены по нормальному закону"]
            result = (task_text, correct_answers, incorrect_answers)
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_7_task_combinatorics_two(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Мощность критерия является величина"
            correct_answer = "1-β"
            incorrect_answers = ["α", "β", "1-α"]
            result = (task_text, correct_answer, incorrect_answers)
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_7_task_combinatorics_three(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Уровень значимости критерия - это"
            correct_answer = "вероятность отвергнуть верную гипотезу"
            incorrect_answers = ["вероятность принять неверную гипотезу",
                                 "вероятность принять верную гипотезу",
                                 "вероятность отвергнуть неверную гипотезу"]
            result = (task_text, correct_answer, incorrect_answers)
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_7_task_combinatorics_four(number_of_tasks):
        """
        Генерирует задачи с несколькими правильными ответами.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильные_ответы, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = ("Если наблюдаемое значение критерия (критической статистики) гипотезы попадает в область "
                         "правдоподобных значений, то это означает что")
            correct_answers = ["проверяемая гипотеза не противоречит выборочным данным",
                               "возможно, существуют другие гипотезы, которые наравне с проверяемой гипотезой не "
                               "противоречат опытным данным"]
            incorrect_answers = ["только проверяемая гипотеза верна", "нулевая гипотеза отвергается"]
            result = (task_text, correct_answers, incorrect_answers)
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_7_task_combinatorics_five(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "P-value - это"
            correct_answer = "минимальный уровень значимости, на котором нулевая гипотеза отвергается"
            incorrect_answers = ["минимальный уровень значимости, на котором нулевая гипотеза принимается",
                                 "максимальный уровень значимости, на котором нулевая гипотеза принимается",
                                 "максимальный уровень значимости, на котором нулевая гипотеза отвергается"]
            result = (task_text, correct_answer, incorrect_answers)
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_7_task_combinatorics_six(number_of_tasks):
        """
        Генерирует задачи с несколькими правильными ответами.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильные_ответы, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = ("Генеральная совокупность – размер определенного изделия. Выберите формулировки "
                         "возможных гипотез")
            correct_answers = ["Генеральная совокупность имеет равномерное распределение",
                               "Размер изделия превышает номинальный",
                               "Размер изделия равен номинальному размеру"]
            incorrect_answers = ["Выборочная совокупность имеет нормальное распределение"]
            result = (task_text, correct_answers, incorrect_answers)
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_7_task_combinatorics_seven(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Если p-value > α, то"
            correct_answer = "Нулевая гипотеза не отвергается на уровне значимости α"
            incorrect_answers = ["Нулевая гипотеза отвергается на уровне значимости α",
                                 "Альтернативная гипотеза принимается на уровне значимости α",
                                 "Альтернативная гипотеза не отвергается на уровне значимости α"]
            result = (task_text, correct_answer, incorrect_answers)
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_7_task_combinatorics_eight(number_of_tasks):
        """
        Генерирует задачи с несколькими правильными ответами.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильные_ответы, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = "Критическая область зависит от"
            correct_answers = ["уровня значимости критерия", "выбора альтернативной гипотезы"]
            incorrect_answers = ["p-value", "выборки"]
            result = (task_text, correct_answers, incorrect_answers)
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_7_task_combinatorics_nine(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = ("Если наблюдаемое значение критерия (критической статистики) гипотезы попадает в "
                         "критическую область, то это означает что")
            correct_answer = "нулевая гипотеза отвергается"
            incorrect_answers = ["нулевая гипотеза не отвергается",
                                 "принимается любая альтернативная гипотеза",
                                 "генеральная совокупность не распределена по нормальному закону"]
            result = (task_text, correct_answer, incorrect_answers)
            list_tasks.append(result)

        return list_tasks

    @staticmethod
    def lecture_7_task_combinatorics_ten(number_of_tasks):
        """
        Генерирует задачи с одним правильным ответом.

        :param number_of_tasks: количество задач для генерации
        :return: список задач в формате (текст_задачи, правильный_ответ, неправильные_ответы)
        """
        list_tasks = []

        for i in range(number_of_tasks):
            task_text = ("Нулевая гипотеза – размер изделия совпадает с номинальным размером, "
                         "наблюдаемое значение критерия попало в левую одностороннюю область. "
                         "В пользу какой гипотезы следует сделать выбор?")
            correct_answer = "Размер изделия меньше номинального"
            incorrect_answers = [
                "Размер изделия меньше номинального на величину выборочного среднего квадратического отклонения",
                "Размер изделия отличается от номинального",
                "Размер изделия больше номинального"]
            result = (task_text, correct_answer, incorrect_answers)
            list_tasks.append(result)

        return list_tasks
    # endregion

    # region Задачи по комбинаторике от Володины Т.Ю
    @staticmethod
    def C(n: int, k: int):
        """
        Calculate the number of combinations C(n, k).
        """
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    @staticmethod
    def C_(n: int, k: int):
        """
               Calculate the number of combinations C(n, k). с повторениями
               """
        return math.factorial(n + k - 1) // (math.factorial(k) * math.factorial(n - 1))

    @staticmethod
    def solve_quadratic_equation(a, b, c):
        """
        Функция для решения квадратного уравнения вида ax^2 + bx + c = 0.
        Возвращает корни уравнения.
        """
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return round(root1, 2), round(root2, 2)  # Округление корней
        elif discriminant == 0:
            root = -b / (2 * a)
            return round(root, 2),  # Округление корня
        else:
            return "Уравнение не имеет действительных корней"

    @staticmethod
    def shielding(input_str: str):
        return input_str.replace("{", r"\{").replace("}", r"\}")

    def logic_1_task_combinatorics_one_binomial_newton(self, number_of_tasks):
        """
        В выражении (-a+3b)^15 раскрыли скобки и привели подобные слагаемые. Какие числовые коэффициенты будут
        у выражений a^3⋅b^12?
        :param number_of_tasks:
        :return:
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            n = random.randint(5, 15)
            k = random.randint(2, n - 1)
            a_coefficient = 0
            while a_coefficient == 0:
                a_coefficient = random.randint(-5, 5)
            b_coefficient = 0
            while b_coefficient == 0:
                b_coefficient = random.randint(-5, 5)

            if b_coefficient > 0:
                expression_1 = fr"$$ ({a_coefficient}a + {b_coefficient}b)" + r"^\{" + str(n) + r"\} $$"
            else:
                expression_1 = fr"$$ ({a_coefficient}a - {abs(b_coefficient)}b)" + r"^\{" + str(n) + r"\} $$"
            expression_2 = r"$$ a^\{" + str(n - k) + r"\} * b^\{" + str(k) + r"\} $$"
            # Generate task text
            task_text = (
                f"В выражении {expression_1} раскрыли скобки и привели подобные слагаемые. "
                f"Какие числовые коэффициенты будут у выражений {expression_2}"
            )
            c_is_n_on_k = self.C(n, k)
            answer = c_is_n_on_k * (a_coefficient ** (n - k)) * (b_coefficient ** k)
            forbidden_answer = [(a_coefficient ** (n - k)) * (b_coefficient ** k) // c_is_n_on_k * 3,
                                c_is_n_on_k * (a_coefficient ** (n - k)) // (b_coefficient ** k) * 3,
                                (a_coefficient ** (n - k)) * (b_coefficient ** k) * 3]

            result_tasks_massive.append((task_text, [answer], forbidden_answer))

        return result_tasks_massive

    def _forming_response_logic_1_task_combinatorics_two(self, root1, root2):
        sign_root = '-' if root2 < 0 else '+'
        sign_root_start = '-' if root1 < 0 else ''
        response = fr"$$ {sign_root_start}c_1 \cdot {abs(root1)}^{{n}} {sign_root} c_2 \cdot {abs(root2)}^{{n}} $$"
        response = self.shielding(response)
        return response

    def logic_1_task_combinatorics_two_recurrence_relation(self, number_of_tasks):
        """
        Найти общее решение рекуррентное соотношения a_(n+2)-8a_(n+1)+16a_n=0
        :param number_of_tasks:
        :return:
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            a = 1
            b = 0
            c = 0
            root = "Уравнение не имеет действительных корней"
            while root == "Уравнение не имеет действительных корней":
                b = 0
                c = 0
                while b == 0:
                    b = random.randint(-5, 5)
                while c == 0:
                    c = random.randint(-10, 10)
                root = self.solve_quadratic_equation(a, b, c)

            # Определение знака перед b и c
            sign_b = '-' if b < 0 else '+'
            sign_c = '-' if c < 0 else '+'

            # Формирование строки с уравнением в LaTeX
            expression = self.shielding(fr'$$ a_{{n+2}} {sign_b} {abs(b)}a_{{n+1}} {sign_c} {abs(c)}a_n = 0 $$')

            task_text = f"Найти общее решение рекуррентного соотношения {expression}"

            forbidden_answer = []
            if isinstance(root, tuple) and len(root) == 2:
                answer = self._forming_response_logic_1_task_combinatorics_two(root[0], root[1])
                forbidden_answer.append(self._forming_response_logic_1_task_combinatorics_two(root[0] * 2, root[1] * 2))
                forbidden_answer.append(self._forming_response_logic_1_task_combinatorics_two(root[0], root[0]))
                forbidden_answer.append(self._forming_response_logic_1_task_combinatorics_two(root[1], root[1]))
            else:
                root = float(root[0])
                answer = self._forming_response_logic_1_task_combinatorics_two(root, root)
                forbidden_answer.append(self._forming_response_logic_1_task_combinatorics_two(root * 2, root * 2))
                forbidden_answer.append(self._forming_response_logic_1_task_combinatorics_two(root / 2, root / 2))
                forbidden_answer.append(self._forming_response_logic_1_task_combinatorics_two(root * 2, root / 2))

            result_tasks_massive.append((task_text, [answer], forbidden_answer))

        return result_tasks_massive

    def _forming_response_logic_1_task_combinatorics_three(self, root, c1, c2):
        c1 = round(c1, 2)
        c2 = round(c2, 2)
        if isinstance(root, tuple):
            sign_root_1 = '-' if c2 < 0 else ''
            sign_root_2 = '-' if c1 < 0 else '+'
            root_0 = f"({root[0]})"
            if root[0] > 0:
                root_0 = root_0.replace("(", "").replace(")", "")
            root_1 = f"({root[1]})"
            if root[1] > 0:
                root_1 = root_1.replace("(", "").replace(")", "")
            response = fr"$$ {sign_root_1}{abs(c1)}\cdot{root_0}^{{n}} {sign_root_2} {abs(c2)}\cdot{root_1}^{{n}}$$"
        else:
            sign_c2_c1 = '-' if c2 - c1 < 0 else '+'
            sign_root_start = '-' if root < 0 else ''
            response = fr"$$ {sign_root_start}{abs(root)}^{{n}}({c1}n {sign_c2_c1} {c2 - c1}) $$"
        response = self.shielding(response)
        return response

    def logic_1_task_combinatorics_three_recurrence_relation(self, number_of_tasks):
        """
        Найти a_n, зная рекуррентное соотношение и начальные члены: a_(n+2)-4a_(n+1)+4a_n=0,a_1=2,a_2=4
        :param number_of_tasks:
        :return:
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            a = 1
            b = 0
            c = 0
            root = "Уравнение не имеет действительных корней"
            while root == "Уравнение не имеет действительных корней":
                b = 0
                c = 0
                while b == 0:
                    b = random.randint(-5, 5)
                while c == 0:
                    c = random.randint(-10, 10)
                root = self.solve_quadratic_equation(a, b, c)

            # Определение знака перед b и c
            sign_b = '-' if b < 0 else '+'
            sign_c = '-' if c < 0 else '+'

            a1 = random.randint(1, 10)
            a2 = random.randint(1 + a1, 10 + a1)
            # Формирование строки с уравнением в LaTeX
            expression = \
                fr'$$ a_{{n+2}} {sign_b} {abs(b)}a_{{n+1}} {sign_c} {abs(c)}a_n = 0, a_{{1}} = {a1}, a_{{2}} = {a2} $$'
            expression = self.shielding(expression)

            task_text = rf"Найти a_\{{n\}}, зная рекуррентное соотношение и начальные члены: {expression}"

            forbidden_answer = []
            if isinstance(root, tuple) and len(root) == 2:
                c2 = (a2 - root[0] * a1) / (root[1] ** 2 - root[0] * root[1])
                c1 = (a1 - c2 * root[1]) / root[0]
                forbidden_answer.append(
                    self._forming_response_logic_1_task_combinatorics_three(root, c1 / root[0], c2 * root[1]))
                forbidden_answer.append(
                    self._forming_response_logic_1_task_combinatorics_three(root, c1 * root[1] / root[0], c2 * root[0]))
                forbidden_answer.append(
                    self._forming_response_logic_1_task_combinatorics_three(root, c1, c2 * (a2 - root[0] * a1)))
            else:
                root = float(root[0])
                c2 = a1 / root
                c1 = a2 / root ** 2 - c2
                forbidden_answer.append(
                    self._forming_response_logic_1_task_combinatorics_three(root, c1 + c2, c2 / root))
                forbidden_answer.append(
                    self._forming_response_logic_1_task_combinatorics_three(root, (c1 + c2) * a2, c2 * a1))
                forbidden_answer.append(
                    self._forming_response_logic_1_task_combinatorics_three(root, (c1 + c2) * root, c2))

            answer = self._forming_response_logic_1_task_combinatorics_three(root, c1, c2)
            result_tasks_massive.append((task_text, [answer], forbidden_answer))

        return result_tasks_massive

    @staticmethod
    def logic_1_task_combinatorics_four_koef(number_of_tasks):
        """
                Определить коэффициенты, которые будут стоять при x^17 после раскрытия скобок и
                приведения подобных членов в выражении (1 + x^2 + x^3)^1000.
                :param number_of_tasks:
                :return:
                """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            def extract_coefficient_and_power(term):
                # Используем регулярное выражение для извлечения коэффициента и степени
                match = re.match(r"([-+]?\d+)\*x\*\*(\d+)", term)
                if match:
                    coefficient = int(match.group(1))
                    power = int(match.group(2))
                    return abs(coefficient), power  # Учитываем только абсолютное значение коэффициента
                else:
                    # Если не удалось извлечь коэффициент и степень, возвращаем None
                    return None, None

            def expand_expression(expression):
                # Преобразуем входное выражение в формат sympy
                x = symbols('x')
                expr = eval(expression)

                # Раскрываем скобки
                expanded_expr = expand(expr)

                # Собираем слагаемые по степеням x
                collected_expr = collect(expanded_expr, x)

                # Извлекаем коэффициенты перед x
                coefficients_dict = {}
                for term in collected_expr.as_ordered_terms():
                    coefficient, power = extract_coefficient_and_power(str(term))
                    # print("Коэффициент:", coefficient)
                    # print("Степень:", power)
                    coefficients_dict[str(power)] = str(coefficient)

                return coefficients_dict

            def random_value_except_none(dictionary):
                # Получаем список ключей, у которых значения не равны None
                keys_with_values = [key for key, value in dictionary.items() if value is not None]

                # Выбираем случайный ключ из списка
                random_key = random.choice(keys_with_values)

                # Возвращаем значение по выбранному ключу
                return random_key

            num_1 = random.randint(2, 10)
            num_2 = random.randint(num_1 + 1, 12)
            num_3 = random.randint(5, 15)

            expression = f"(1 + x**{num_1} - x**{num_2})**{num_3}"
            forbidden_answer = set()
            coefficients_dict = expand_expression(expression)

            random_value = random_value_except_none(coefficients_dict)

            latex_expression = r"$$ (1 + x^\{" + str(num_1) + r"\} - x^\{" + str(num_2) + r"\})^\{" + str(
                num_3) + r"\} $$"
            task_text = (f"Определить коэффициенты, которые будут стоять при x^{random_value} после раскрытия скобок"
                         f" и приведения подобных членов в выражении {latex_expression}. ")

            answer = coefficients_dict[random_value]

            forbidden_answer.add(f"{coefficients_dict[random_value_except_none(coefficients_dict)]}")
            forbidden_answer.add(f"{coefficients_dict[random_value_except_none(coefficients_dict)]}")
            forbidden_answer.add(f"{coefficients_dict[random_value_except_none(coefficients_dict)]}")

            if answer != 'None':
                result_tasks_massive.append((task_text, [answer], list(forbidden_answer)))

        return result_tasks_massive

    def logic_1_task_combinatorics_five_distribution_tickets(self, number_of_tasks):
        """
        Группе из десяти сотрудников выделено три путевки. Сколько существует способов распределения путевок,
        если все путевки одинаковы?
        :param number_of_tasks:
        :return:
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            number_of_employees = random.randint(5, 30)  # количество сотрудников
            number_of_tickets = random.randint(2, number_of_employees - 2)  # количество путевок
            task_text = f"Группе из {number_of_employees} сотрудников выделено {number_of_tickets} путевки. " \
                        f"Сколько существует способов распределения путевок, если все путевки одинаковы?"

            answer = self.C(number_of_employees, number_of_tickets)

            result_tasks_massive.append((task_text, [answer], []))

        return result_tasks_massive


    def logic_1_task_combinatorics_six_different_gender_pairs(self, number_of_tasks):
        """
        На школьном вечере присутствуют 12 девушек и 15 юношей. Сколькими способами можно выбрать из них 4
        разнополые пары для танца?
        :param number_of_tasks:
        :return:
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            number_of_girls = random.randint(8, 20)
            number_of_boys = random.randint(8, 20)
            number_pairs = random.randint(3, 8)
            task_text = f"На школьном вечере присутствуют {number_of_girls} девушек и {number_of_boys} юношей. " \
                        f"Сколькими способами можно выбрать из них {number_pairs} разнополые пары для танца?"

            # part1 = self.C(number_of_girls, number_pairs)
            # part2 = self.C(number_of_boys, number_pairs)
            # answer = part1 * part2
            answer = round((math.factorial(number_of_girls) * math.factorial(number_of_boys)) / (
                        math.factorial(number_of_girls - number_pairs) * math.factorial(
                    number_of_boys - number_pairs) * math.factorial(number_pairs)))

            result_tasks_massive.append((task_text, [answer], []))

        return result_tasks_massive

    @staticmethod
    def logic_1_task_combinatorics_seven_digits(number_of_tasks):
        """
                Найти сумму всех цифр всех шестизначных чисел полученных при перестановке цифр 1, 2, 3, 4, 5, 6.
                :param number_of_tasks:
                :return:
                """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            forbidden_answer = set()
            number_of_card = random.randint(3, 9)  # кол-во чисел
            # number_of_card_2 = random.randint(3, 9)  # кол-во чисел
            # digits_array = list(range(1, number_of_card + 1))  # массив цифр
            digits_array = random.sample(range(1, 10), number_of_card)

            task_text = f"Найти сумму всех цифр всех {number_of_card} значных чисел полученных при перестановке цифр {digits_array}. "

            total_sum = 0
            # Генерация всех перестановок
            perms = itertools.permutations(digits_array)
            for perm in perms:
                # Преобразуем перестановку в число
                num = int(''.join(map(str, perm)))
                # Вычисляем сумму цифр числа и добавляем её к общей сумме
                total_sum += sum(int(digit) for digit in str(num))

            answer = total_sum

            forbidden_answer.add(f"{math.factorial(number_of_card)}")
            forbidden_answer.add(f"{math.factorial(number_of_card) * number_of_card}")
            forbidden_answer.add(f"{total_sum - math.factorial(number_of_card)}")
            result_tasks_massive.append((task_text, [answer], list(forbidden_answer)))

        return result_tasks_massive

    def logic_1_task_combinatorics_eight_soldier(self, number_of_tasks):
        """
                Во взводе 3 сержанта и 36 солдат. Сколько существует способов выделения одного сержанта и трех
                солдат для патрулирования?
                :param number_of_tasks:
                :return:
                """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            forbidden_answer = set()
            number_of_serg = random.randint(2, 12)  # кол-во сержиков
            number_of_soldier = random.randint(number_of_serg + 1, 50)  # количество солдат
            number_of_serg_choice = random.randint(2, number_of_serg - 1)  # кол-во выбрать
            number_of_soldier_choice = random.randint(2, number_of_soldier - 1)  # количество выбрать
            task_text = (f"Во взводе есть сержанты: {number_of_serg} и солдаты: {number_of_soldier}. Сколько существует"
                         f" способов выделить {number_of_serg_choice} человек среди сержантов и "
                         f"{number_of_soldier_choice} человек среди солдат для патрулирования?. ")

            answer = self.C(number_of_serg, number_of_serg_choice) * self.C(number_of_soldier, number_of_soldier_choice)

            forbidden_answer.add(f"{self.C(number_of_serg, number_of_serg_choice)}")
            forbidden_answer.add(f"{self.C(number_of_soldier, number_of_soldier_choice)}")
            forbidden_answer.add(
                f"{self.C(number_of_serg, number_of_serg_choice) * self.C(number_of_soldier, number_of_soldier_choice) * 2}")
            result_tasks_massive.append((task_text, [answer], list(forbidden_answer)))

        return result_tasks_massive

    def logic_1_task_combinatorics_nine_alphabet(self, number_of_tasks):
        """
                Сколькими способами можно составить из 5 гласных и 9 согласных слова, в которые входят 4
                 различных согласных и не менее 3 различных гласных?
                :param number_of_tasks:
                :return:
                """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            forbidden_answer = set()
            number_of_gl = random.randint(3, 10)  # кол-во гласных
            number_of_sogl = random.randint(3, 10)  # количество согласных
            number_of_sogl_choice = random.randint(2, number_of_sogl - 1)  # количество выбрать
            random_sign = random.choice(['более', 'менее'])
            if random_sign == 'менее':
                if number_of_gl<5:
                    number_of_gl_choice = random.randint(1, number_of_gl-1)  # кол-во выбрать
                else:
                    number_of_gl_choice = random.randint(number_of_gl-4, number_of_gl-1)  # кол-во выбрать

            else:
                if number_of_gl<5:
                    number_of_gl_choice = random.randint(2, number_of_gl)  # кол-во выбрать
                else:
                    number_of_gl_choice = random.randint(2, 5)  # кол-во выбрать
            # print(number_of_gl,' ',number_of_sogl,' ',number_of_sogl_choice,' ',number_of_gl_choice)

            # number_of_gl = 10 # кол-во гласных
            # number_of_sogl = 9  # количество согласных
            # number_of_sogl_choice = 2  # количество выбрать
            # random_sign ='более'
            # number_of_gl_choice = 9  # кол-во выбрать


            task_text = (f"Сколькими способами можно составить из {number_of_gl} гласных"
                         f" и {number_of_sogl} согласных слова, в которые"
                         f" входят {number_of_sogl_choice} различных согласных"
                         f" и не {random_sign} {number_of_gl_choice} различных гласных?. ")

            # Вычисление количества способов выбрать 4 различных согласных из 9
            ways_to_choose_consonants = math.comb(number_of_sogl, number_of_sogl_choice)

            # Вычисление количества способов выбрать не менее 3 различных гласных из 5
            ways_to_choose_vowels = sum(
                math.comb(number_of_gl, i) for i in range(number_of_gl_choice, number_of_gl + 1))
            ans = 0
            w_ans = 0

            if random_sign == 'менее':
                for i in range(number_of_gl_choice, number_of_gl+1, 1):
                    ans += self.C(number_of_sogl, number_of_sogl_choice) * self.C(number_of_gl, i) * math.factorial(
                        number_of_sogl_choice+i)

                for i in range(0, number_of_gl_choice + 1, 1):
                    w_ans += self.C(number_of_sogl, number_of_sogl_choice) * self.C(number_of_gl, number_of_gl_choice-i) * math.factorial(
                        (number_of_sogl_choice+number_of_gl_choice)-i)
            else:
                for i in range(0, number_of_gl_choice+1 , 1):
                    ans += self.C(number_of_sogl, number_of_sogl_choice) * self.C(number_of_gl, number_of_gl_choice-i) * math.factorial(
                        (number_of_sogl_choice+number_of_gl_choice)-i)
                for i in range(number_of_gl_choice, number_of_gl + 1, 1):
                    w_ans += self.C(number_of_sogl, number_of_sogl_choice) * self.C(number_of_gl, i) * math.factorial(
                        number_of_sogl_choice+i)

            answer = ans

            forbidden_answer.add(
                f"{w_ans}")
            forbidden_answer.add(
                f"{round(ans/self.C(number_of_sogl, number_of_sogl_choice))}")
            forbidden_answer.add(
                f"{round(w_ans/self.C(number_of_sogl, number_of_sogl_choice))}")
            result_tasks_massive.append((task_text, [answer], list(forbidden_answer)))

        return result_tasks_massive

    @staticmethod
    def logic_1_task_combinatorics_ten_arithmetic(number_of_tasks):
        """
                Известно, что арифметические операции сложения и умножения коммутативны для конечного числа операндов.
                 Например, выражение (a+b+c+d)∙(e+f) можно записать иначе: (f+e)∙(b+a+c+d).
                  Сколько всего существует способов записи этого выражения?
                :param number_of_tasks:
                :return:
                """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            forbidden_answer = set()
            number_1 = random.randint(2, 10)  # кол-во букв
            operands_1 = [chr(ord('a') + i) for i in range(number_1)]
            expression_0_1 = "(" + "+".join(operands_1) + ")"
            random.shuffle(operands_1)  # Перемешиваем операнды
            expression_1 = "(" + "+".join(operands_1) + ")"  # Формируем строку с суммой

            number_2 = random.randint(2, 10)  # кол-во букв
            operands_2 = [chr(ord('a') + number_1 + i) for i in range(number_2)]
            expression_0_2 = "(" + "+".join(operands_2) + ")"
            random.shuffle(operands_2)  # Перемешиваем операнды
            expression_2 = "(" + "+".join(operands_2) + ")"  # Формируем строку с суммой

            task_text = (f"Известно, что арифметические операции сложения и умножения"
                         f" коммутативны для конечного числа операндов. Например,"
                         f" выражение {expression_0_2}∙{expression_0_1} можно записать иначе: "
                         f"{expression_1}∙{expression_2}."
                         f" Сколько всего существует способов записи этого выражения?")

            # # Вычисляем количество способов группировки для суммы (a+b+c+d)
            # ways_to_group_sum = sum(math.comb(number_2, i) for i in range(1, number_2 - 1))
            #
            # # Вычисляем количество способов группировки для суммы другого выражения
            # ways_to_choose_vowels = sum(math.comb(number_1, i) for i in range(1, number_1 - 1))

            ans1 = math.factorial(number_1)
            ans2 = math.factorial(number_2)
            answer = ans1 * ans2 * 2

            forbidden_answer.add(f"{ans1}")
            forbidden_answer.add(
                f"{ans1 * ans2 - ans1}")
            forbidden_answer.add(
                f"{ans1 * ans2 * 2 - ans2}")
            result_tasks_massive.append((task_text, [answer], list(forbidden_answer)))

        return result_tasks_massive

    def stirling_second(self, n, k):
        """
        Вычисляет числа Стирлинга второго рода S(n, k).

        Параметры:
        - n: количество объектов
        - k: количество непустых неразличимых множеств

        Возвращает:
        - количество способов разбиения n объектов на k непустых неразличимых множеств
        """
        # Базовый случай: если n или k равны 0, возвращаем 0
        if n == 0 or k == 0:
            return 0
        # Базовый случай: если n равно k, возвращаем 1
        if n == k:
            return 1
        # Рекурсивный случай
        return k * self.stirling_second(n - 1, k) + self.stirling_second(n - 1, k - 1)

    def logic_1_task_combinatorics_eleven_stirling(self, number_of_tasks):
        """
               Найдите S(6,3)?
                :param number_of_tasks:
                :return:
                """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            forbidden_answer = set()
            number_1 = random.randint(1, 10)  # кол-во карт
            number_2 = random.randint(0, number_1)  # количество частей
            task_text = f"Найдите число стирлинга второго рода S({number_1},{number_2})?"

            answer = self.stirling_second(number_1, number_2)
            rand = random.randint(-10, 10)
            forbidden_answer.add(f"{answer + rand}")
            forbidden_answer.add(f"{number_1 + number_2}")
            forbidden_answer.add(f"{math.pow(number_1, number_2)}")
            result_tasks_massive.append((task_text, [answer], list(forbidden_answer)))

        return result_tasks_massive

    def logic_1_task_combinatorics_twelve_cards(self, number_of_tasks):
        """
                12.	Сколькими способами колоду из 36 карт можно разделить произвольно на 2 части?
                :param number_of_tasks:
                :return:
                """

        result_tasks_massive = []
        for _ in range(number_of_tasks):
            forbidden_answer = set()
            number_of_card = random.choice([36, 52, 54, 32, 48, 30, 24, 40, 42, 44, 46, 50])  # кол-во карт

            number_of_part = random.randint(5, 20)  # количество частей
            task_text = (f"Сколькими способами колоду из {number_of_card} карт можно разделить произвольно на "
                         f"{number_of_part} частей?")

            answer = self.stirling_second(number_of_card, number_of_part)
            forbidden_answer.add(f"{self.C(number_of_card, number_of_part)}")
            forbidden_answer.add(f"{number_of_card * number_of_part}")
            forbidden_answer.add(f"{math.pow(2, number_of_part)}")
            result_tasks_massive.append((task_text, [answer], list(forbidden_answer)))

        return result_tasks_massive

    def logic_1_task_combinatorics_thirteen_biatlon(self, number_of_tasks):
        """
                13.	Биатлонист делает 5 выстрелов на рубеже. За каждую не закрытую мишень он
                 получает штрафной круг. Сколько возможных комбинаций (закрытых/не закрытых мишеней)
                 приводят к двум штрафным кругам?
                :param number_of_tasks:
                :return:
                """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            forbidden_answer = set()
            number_of_target = random.randint(5, 15)  # кол-во мишеней
            number_of_miss = random.randint(2, number_of_target - 1)  # количество штрафов
            task_text = (
                f"Биатлонист делает {number_of_target} выстрелов на рубеже. За каждую не закрытую мишень он получает "
                f"штрафной круг. Сколько возможных комбинаций (закрытых/не закрытых мишеней) "
                f"приводят к {number_of_miss} штрафным кругам?")

            answer = round(self.C(number_of_target, number_of_miss))
            forbidden_answer.add(f"{round(self.C(number_of_target - 1, number_of_miss))}")
            forbidden_answer.add(f"{round(number_of_target * number_of_miss)}")
            forbidden_answer.add(f"{round(self.C_(number_of_target, number_of_miss))}")
            result_tasks_massive.append((task_text, [answer], list(forbidden_answer)))

        return result_tasks_massive

    def logic_1_task_combinatorics_fourteen_cake(self, number_of_tasks):
        """
                14.	В кондитерской продаются пирожные четырех видов. Сколькими способами можно купить 8 пирожных?
                :param number_of_tasks:
                :return:
                """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            forbidden_answer = set()
            number_of_cake = random.randint(4, 10)  # виды пирожных
            number_of_choice = random.randint(8, 20)  # количество, что мы берем
            task_text = (f"В кондитерской продаются пирожные {number_of_cake} видов. Сколькими способами можно купить"
                         f" {number_of_choice} пирожных?")

            answer = round(self.C(number_of_cake + number_of_choice - 1, number_of_choice))
            forbidden_answer.add(f"{round(self.C(number_of_cake + number_of_choice, number_of_choice))}")
            forbidden_answer.add(f"{round(number_of_choice * number_of_cake)}")
            forbidden_answer.add(f"{round(math.pow(2, number_of_choice))}")
            result_tasks_massive.append((task_text, [answer], list(forbidden_answer)))

        return result_tasks_massive

    @staticmethod
    def logic_1_task_combinatorics_fifteen_letter(number_of_tasks):
        """
                15.	Алфавит А состоит из двух символов. Сколько существует различных слов алфавита А,
                 длины которых не превосходят 5?
                :param number_of_tasks:
                :return:
                """
        result_tasks_massive = []
        for _ in range(number_of_tasks):

            forbidden_answer = set()
            number_of_letter = random.randint(2, 20)  # кол-во букв
            number_of_words = random.randint(2, 8)  # длина слова
            task_text = (
                f"Алфавит А состоит из {number_of_letter} символов. Сколько существует различных слов алфавита А, "
                f"длины которых не превосходят {number_of_words}?")

            answer = 0
            # Перебираем длины слов от 1 до максимальной длины
            for length in range(1, number_of_words + 1):
                # Количество слов длины length равно alphabet_size в степени length
                words_count = math.pow(number_of_letter, length)
                answer += words_count

            forbidden_answer.add(f"{round(answer / number_of_words)}")
            forbidden_answer.add(f"{round((answer / number_of_words) * 1.5)}")
            forbidden_answer.add(f"{round(math.pow(2, number_of_words))}")
            result_tasks_massive.append((task_text, [round(answer)], list(forbidden_answer)))

        return result_tasks_massive

    @staticmethod
    def logic_1_task_combinatorics_sixteen_profkom(number_of_tasks):
        """
               16.	В профком выбрано 9 человек. Из них нужно выбрать председателя, его заместителя и секретаря.
                Сколькими способами это можно сделать?
                :param number_of_tasks:
                :return:
                """
        result_tasks_massive = []
        # Список возможных ролей
        roles = ["председателя", "главу", "руководителя", "президента"]
        roles2 = ["помощника", "заместителя", "ассистента"]
        roles3 = ["администратора", "канцеляра", "секретаря"]

        for _ in range(number_of_tasks):
            forbidden_answer = set()
            number_of_letter = random.randint(7, 15)  # кол-во людей
            # number_of_words = random.randint(2, 5)  # длина слова
            task_text = (
                f"В профком выбрано {number_of_letter} человек. Из них нужно выбрать {random.choice(roles)}, "
                f"{random.choice(roles2)} и {random.choice(roles3)}."
                "Сколькими способами это можно сделать?")

            answer = number_of_letter * (number_of_letter - 1) * (number_of_letter - 2)
            # Перебираем длины слов от 1 до максимальной длины

            forbidden_answer.add(f"{math.pow(number_of_letter, 2)}")
            forbidden_answer.add(f"{math.pow(2, number_of_letter)}")
            forbidden_answer.add(f"{number_of_letter * (number_of_letter - 1)}")
            result_tasks_massive.append((task_text, [answer], list(forbidden_answer)))

        return result_tasks_massive
    # endregion
