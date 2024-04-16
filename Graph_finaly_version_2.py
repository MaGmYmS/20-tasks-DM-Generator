import os
import random
import zipfile
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx
import pulp
from pulp import LpProblem, LpVariable, lpSum, LpMaximize, LpMinimize, LpStatus


#  нужен алгоритм разных типов задач + рисовать графы
#  ложные решения сделать


class Graph:
    # пример вызова:
    # graph = Graph(6, 2, 3)  Создаем объект класса граф
    # tasks = graph.task_two(5)  Генерим 5 задач из второго шаблона
    # graph.create_txt_file(tasks, 1)  Создаем txt файл и указываем что нужно рисовать графы
    # graph.create_zip_file("image_folder", "quiz.txt")  Создаем zip архив в формате gift from media formats
    def __init__(self, n=6, min_number_of_edges_from_vertex=1, max_number_of_edges_from_vertex=2):
        # конструктор
        """
        :param n число вершин:
        :param min_number_of_edges_from_vertex: минимальное количество ребер из вершины
        :param max_number_of_edges_from_vertex: максимальное количество ребер из вершины
        """

        self.vertices = [value for value in range(1, n + 1)]
        self.edges = []
        self.min_number_of_edges_from_vertex = min_number_of_edges_from_vertex
        self.max_number_of_edges_from_vertex = max_number_of_edges_from_vertex
        self.graph = dict()
        self.value = []

    # region вспомогательные функции
    def __graph_generator(self):
        """
        Метод, который создает граф с минимальным и максимальным количеством ребер из вершин
        :return:
        """
        # можно сделать проще, перебрать все возможные комбинации ребер,
        # перемешать и взять k элементов(хотя там свои проблемы)
        # идея, строить граф через матрицу инцидентности
        # строить граф на основе связности

        random_vertices_one = self.vertices.copy()
        random_vertices_two = self.vertices.copy()
        self.edges = []
        random.shuffle(random_vertices_one)
        random.shuffle(random_vertices_two)

        for i in range(len(random_vertices_one)):
            count = 0
            for j in range(len(random_vertices_two)):
                value = (random_vertices_one[i], random_vertices_two[j])
                value_reverse = (random_vertices_two[j], random_vertices_one[i])
                if count < self.min_number_of_edges_from_vertex and value not in self.edges \
                        and value_reverse not in self.edges and random_vertices_one[i] != random_vertices_two[j]:
                    self.edges.append(value)
                    self.value.append(0)
                    count += 1
                elif self.min_number_of_edges_from_vertex <= count < self.max_number_of_edges_from_vertex \
                        and value not in self.edges and value_reverse not in self.edges \
                        and random_vertices_one[i] != random_vertices_two[j]:
                    if random.random() >= 0.5:
                        break
                    self.edges.append(value)
                    self.value.append(0)
                    count += 1

        self.graph = {key: value for key, value in zip(self.edges, self.value)}

    def paintilovka(self, choice_values: bool, choice_orientation: bool):
        """
        Метод, рисующий граф
        :param choice_values: нужно ли рисовать веса на графе
        :param choice_orientation: нужна ли ориентация у графа
        :return:
        """
        plt.figure(figsize=(4, 2))
        # рисуем граф
        if choice_orientation:
            draw_graph = nx.DiGraph()
        else:
            draw_graph = nx.Graph()

        draw_graph.add_nodes_from(self.vertices)
        for key, value in self.graph.items():
            draw_graph.add_edge(key[0], key[1])

        pos = nx.spring_layout(draw_graph)
        # pos = nx.circular_layout(draw_graph)
        # print(pos)

        nx.draw(draw_graph, pos=pos, with_labels=True)
        if choice_values:
            nx.draw_networkx_edge_labels(draw_graph, pos=pos,
                                         edge_labels={(key[0], key[1]): value for key, value in self.graph.items()},
                                         font_color='red')

        # region сохранение графа
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads", "folder_tasks")
        image_folder = os.path.join(download_folder, "image_folder")
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)

        # Создаем полный путь к файлу
        path_to_img_graph = ""
        # image_folder = os.path.join(image_folder, f"graph {0}.png")
        counter_file_in_directory = -1
        while True:
            counter_file_in_directory += 1
            path_to_img_graph = os.path.join(image_folder, f"graph {counter_file_in_directory}.png")
            if not os.path.exists(path_to_img_graph):
                break

        # print(path_to_img_graph)
        plt.savefig(path_to_img_graph)
        path_to_img_graph = f"image_folder/graph {counter_file_in_directory}.png"
        plt.close()
        return path_to_img_graph
        # endregion

    @staticmethod
    def __check_unique_variable(check_unique_question_inner, task_inner, answer_inner, forbidden_answer_inner):
        length_check_unique_question = len(check_unique_question_inner)
        # Преобразование списков в кортежи
        if type(answer_inner[0]) != list:
            text_tuple = tuple(task_inner)
            answer_tuple = tuple(answer_inner)
            forbidden_answer_tuple = tuple(forbidden_answer_inner)
        else:
            text_tuple = tuple(task_inner)
            answer_tuple = tuple(tuple(pair) for pair in answer_inner)
            forbidden_answer_tuple = tuple(tuple(pair) for pair in forbidden_answer_inner)

        check_unique_question_inner.add(frozenset((text_tuple, answer_tuple, forbidden_answer_tuple)))
        if length_check_unique_question == len(check_unique_question_inner):
            return True  # Такое задние уже существует
        else:
            return False

    def create_txt_file(self, tasks_massive, type_of_response, name_of_the_questions, file_name):
        """
        Метод, создающий txt файл c задачами
        :param tasks_massive: массив задач в формате (вопрос, ответ)
        :param type_of_response: переменная, отвечающая за тип ответа
        :return:
        """
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "folder_tasks")
        if not os.path.exists(downloads_path):
            os.makedirs(downloads_path)
        file_path = os.path.join(downloads_path, file_name + ".txt")
        result_string = ""

        if len(tasks_massive[0]) == 4:
            for i, (task, answer, forbidden_answer, path_to_graph_img) in enumerate(tasks_massive):
                construction_of_the_image_output_in_gift_format = str.format('<img src\="@@PLUGINFILE@@/{0}"/>',
                                                                             path_to_graph_img)
                tasks_with_graph = task.replace("graph_img", construction_of_the_image_output_in_gift_format)
                tasks_massive[i] = (tasks_with_graph, answer, forbidden_answer)

        check_unique_question = set()
        with open(file_path, "w", encoding="utf-8") as file:
            match type_of_response:
                case 1:  # краткий ответ
                    for task, answer, forbidden_answer in tasks_massive:
                        if self.__check_unique_variable(check_unique_question, task, answer, forbidden_answer):
                            continue

                        result_answer_str = ""
                        for ans in answer:
                            result_answer_str += f"={ans}\n"
                        result_string += f"::{name_of_the_questions}::" + task + " {" + result_answer_str + "} " + "\n" + "\n"
                    file.write(result_string)

                case 2:  # множественный выбор, один ответ
                    for task, answer, forbidden_answer in tasks_massive:
                        if self.__check_unique_variable(check_unique_question, task, answer, forbidden_answer):
                            continue

                        all_answers = forbidden_answer.copy()
                        all_answers.extend(answer)
                        random.shuffle(all_answers)
                        string_answer = ""
                        for value in all_answers:
                            if value in answer:
                                string_answer += f"={value}\n"
                            else:
                                string_answer += f"~{value}\n"
                        result_string += f"::{name_of_the_questions}::" + task + " {" + string_answer + "} " + "\n" + "\n"
                    file.write(result_string)

                case 3:  # множественный выбор, несколько ответов
                    for task, answer, forbidden_answer in tasks_massive:
                        if self.__check_unique_variable(check_unique_question, task, answer, forbidden_answer):
                            continue

                        all_answers = forbidden_answer.copy()
                        all_answers.extend(answer)
                        random.shuffle(all_answers)
                        string_answer = ""
                        for value in all_answers:
                            if value in answer:
                                string_answer += f"~%{100 / len(answer)}%{value}\n"
                            else:
                                string_answer += f"~{value}\n"
                        result_string += f"::{name_of_the_questions}::" + task + " {" + string_answer + "} " + "\n" + "\n"
                    file.write(result_string)

                case 4:  # пропущенное слово
                    for task, answer, forbidden_answer in tasks_massive:
                        if self.__check_unique_variable(check_unique_question, task, answer, forbidden_answer):
                            continue

                        string_answer = ""
                        for ans in answer:
                            string_answer += f"={ans}\n"
                        split_task = task.split("__")
                        result_string += f"::{name_of_the_questions}::"
                        for i in range(len(split_task) - 1):
                            result_string += f"{split_task[i]} __________"
                        result_string += f"{split_task[len(split_task) - 1]}" + "{" + string_answer + "}" + "\n" + "\n"
                    file.write(result_string)

                case 5:  # верно\неверно
                    for task, answer, forbidden_answer in tasks_massive:
                        if self.__check_unique_variable(check_unique_question, task, answer, forbidden_answer):
                            continue

                        result_string += f"::{name_of_the_questions}::" + task + "{" + answer + "}" + "\n" + "\n"
                    file.write(result_string)

                case 6:  # на соответствие
                    for task, answer, forbidden_answer in tasks_massive:
                        if self.__check_unique_variable(check_unique_question, task, answer, forbidden_answer):
                            continue

                        string_answer = ""
                        # ::Вопрос 1:: Укажите столицы государств: {
                        # = Канада -> Оттава
                        # = Италия -> Рим
                        # = Япония -> Токио
                        # = Индия -> Нью Дели}
                        for quest, ans in answer:
                            string_answer += f"={quest} -> {ans}\n"
                        result_string += f"::{name_of_the_questions}::" + task + "{" + string_answer + "}" + "\n" + "\n"
                    file.write(result_string)

                case 7:  # эссе
                    for task, answer, forbidden_answer in tasks_massive:
                        if self.__check_unique_variable(check_unique_question, task, answer, forbidden_answer):
                            continue

                        result_string += f"::{name_of_the_questions}::" + task + "{}" + "\n" + "\n"
                    file.write(result_string)
        print("Количество уникальных вариантов:", len(check_unique_question))
        print(f"Файл {file_path} успешно создан.")

    @staticmethod
    def create_zip_file(zip_file_name, *args):
        try:
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "folder_tasks")
            zip_file_name = os.path.join(downloads_path, zip_file_name + ".zip")

            with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for item in args:
                    item_path = os.path.join(downloads_path, item)

                    if os.path.exists(item_path):
                        if os.path.isfile(item_path):
                            zipf.write(item_path, os.path.basename(item_path))
                            print(f"Файл {os.path.basename(item_path)} добавлен в архив")
                        elif os.path.isdir(item_path):
                            for root, dirs, files in os.walk(item_path):
                                for file in files:
                                    file_path = os.path.join(root, file)
                                    relative_path = os.path.relpath(file_path, item_path)
                                    zipf.write(file_path, os.path.join(os.path.basename(item_path), relative_path))
                                    print(f"Файл {file} добавлен в архив")
                        else:
                            print(f"Не удалось добавить {item} в архив. Неизвестный тип.")
                    else:
                        print(f"Файл или папка {item} не существует.")

        except Exception as e:
            print(f"Произошла ошибка: {e}")
        else:
            print(f"Архив {zip_file_name} успешно создан.")
    # endregion

    def task_two(self, number_of_tasks, drawing_graph=True, number_forbidden_answer=3):
        """
        Граф задан следующим образом: <{1,2,3,4,5,6}-множество вершин; {(1,3),
        (2,1), (2,5), (3,2), (4,3), (4,5)}-множество дуг>. Выпишите сколько «-1» будет в
        3-й строке матрицы инциденций.
        :param number_of_tasks: количество задач
        :param drawing_graph: флаг для отображения графа (по умолчанию True)
        :param number_forbidden_answer: количество запрещенных вариантов ответа (по умолчанию 3)
        :return: массив с задачами в формате (вопрос, ответ)
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            self.__graph_generator()
            incidence_matrix = [[0 for _ in range(len(self.edges))] for _ in range(len(self.vertices))]
            for i, (vertex_one, vertex_two) in enumerate(self.edges):
                incidence_matrix[vertex_one - 1][i] = 1
                incidence_matrix[vertex_two - 1][i] = -1
            row_index = random.randint(0, len(self.vertices) - 1)
            search_element = random.choice([-1, 0, 1])

            task_text = (
                f"Граф задан следующим образом: <{', '.join(map(str, self.vertices))} "
                f"-множество вершин; {', '.join(map(str, self.edges))}, -множество дуг>. "
                f"Выпишите сколько «{search_element}» будет в {row_index + 1}-й строке матрицы инциденций."
            )

            answer = incidence_matrix[row_index].count(search_element)

            error_count = 0
            while error_count < 100:
                forbidden_answer = random.sample(range(0, 10), number_forbidden_answer)
                if answer not in forbidden_answer:
                    break
                error_count += 1

            path_to_graph_img = ""
            if drawing_graph:
                task_text += "<br/>graph_img"
                path_to_graph_img = self.paintilovka(False, True)

            result_tasks_massive.append((task_text, [answer], forbidden_answer, path_to_graph_img))
        return result_tasks_massive

    def task_three(self, number_of_tasks, drawing_graph=True, number_forbidden_answer=3):
        """
        Граф задан следующим образом: <{1,2,3,4,5}-множество вершин; {(1,3), (2,1),
        (2,5), (3,2), (4,3), (4,5)}-множество дуг>. Какая из последовательностей
        соответствует столбцу номер 1 матрицы смежностей для данного графа.
            01000
            00100
            01010
        :param number_of_tasks: количество задач
        :return result_tasks_massive: массив с задачами в формате (вопрос, ответ)
        :return drawing_graph: рисуем или не рисуем граф
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            self.__graph_generator()
            adjacency_matrix = [[0 for _ in range(len(self.vertices))] for _ in range(len(self.vertices))]
            for i, (vertex_one, vertex_two) in enumerate(self.edges):
                adjacency_matrix[vertex_one - 1][vertex_two - 1] = 1
                adjacency_matrix[vertex_two - 1][vertex_one - 1] = 1

            row_index = random.randint(0, len(self.vertices) - 1)

            reversed_edges = [(v, u) for u, v in self.edges]
            task_text = "Граф задан следующим образом: <" + ", ".join(map(str, self.vertices)) + \
                        " -множество вершин; " + ", ".join(map(str, self.edges)) + ", " + ", ".join(
                map(str, reversed_edges)) + \
                        " -множество дуг>. " \
                        f"Какая из последовательностей соответствует столбцу номер {row_index + 1} матрицы " \
                        f"смежностей для данного графа. Отсчет столбцов начинается с 1."

            path_to_graph_img = ""
            if drawing_graph:
                task_text += "<br/>graph_img"
                path_to_graph_img = self.paintilovka(False, False)

            answer = "".join([str(value) for value in adjacency_matrix[row_index]])

            forbidden_answer = set()
            while len(forbidden_answer) != number_forbidden_answer:
                tmp_mas = map(str, [random.choice([0, 1]) for _ in range(len(self.vertices))])
                gen_for_ans = "".join(tmp_mas)
                forbidden_answer.add(gen_for_ans)
            forbidden_answer = list(forbidden_answer)

            result_tasks_massive.append((task_text, [answer], forbidden_answer, path_to_graph_img))
        return result_tasks_massive

    @staticmethod
    def task_four(number_of_tasks, number_forbidden_answer=3):
        """
        В однородном графе степень вершины равна 5 Число ребер равно 35. Найдите число вершин.
        :param number_of_tasks: количество задач
        :return result_tasks_massive: массив с задачами в формате (вопрос, ответ)
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            while True:
                vertex_degree = random.randint(5, 20)
                answer = random.randint(5, 30)
                count_edges = vertex_degree * answer / 2
                count_edges_int = vertex_degree * answer // 2
                if count_edges - count_edges_int == 0:
                    break
            task_text = f"В однородном графе степень вершины равна {vertex_degree}. Число ребер равно {count_edges_int}. " \
                        f"Найдите число вершин."
            forbidden_answer = [random.choice([answer + i + 1, answer - 1 - i]) for i in range(number_forbidden_answer)]

            result_tasks_massive.append((task_text, [answer], forbidden_answer))
        return result_tasks_massive

    @staticmethod
    def task_five(count_task):
        """
        Генерирует задачи типа:
        Найдите степень вершины полного графа, имеющего 91 ребро.
        :param count_task:  Количество задач
        :return:  Список с задачами в формате [(текст, ответ(ы), ложные ответы), (текст, ответ(ы), ложные ответы)]
        """
        output_list = []
        for _ in range(count_task):
            incorrect_answers = []
            right_answer = []
            # определяем сколько вершин в графе минимум 3
            answer = random.randint(3, 20)
            edges = int(answer * (answer - 1) / 2)

            if 9 > edges % 10 == 0:
                edges_word = "ребер"
            elif 1 > edges % 10 < 5:
                edges_word = "ребра"
            elif edges % 10 == 1:
                edges_word = "ребро"
            else:
                edges_word = "ребер"

            task_text = f"Найдите степень вершины полного графа, имеющего {edges} {edges_word}."
            right_answer.append(answer)
            # region НЕправильный ответы
            delta_ans = answer
            delta_ans += 1
            incorrect_answers.append(delta_ans)
            delta_ans += 1
            incorrect_answers.append(delta_ans)
            delta_ans -= 3
            incorrect_answers.append(delta_ans)

            # endregion

            tmp = (task_text, right_answer, incorrect_answers)
            output_list.append(tmp)
        return output_list

    @staticmethod
    def task_five_2nd_variation(count_task, randomleft1=3, randomright1=30):
        """
        Генерирует задачи типа:

        Найдите степень вершины полного графа, в котором количество ребер равно 91.

        Найдите степень вершины полного графа, в котором количество  вершин  равно 10.

        Найдите количество ребер в полном графе,в котором количество  вершин  равно 10.

        Найдите количество ребер в полном графе, если степень  вершины равна 6.

        Найдите количество вершин в полном графе, в котором количество ребер равно 10.

        Найдите количество вершин в полном графе, если степень вершины равна 10.

        :param random1,random2:  диапозон генерации графа

        :return:  Список с задачами в формате [(текст, ответ(ы), ложные ответы), (текст, ответ(ы), ложные ответы)]
        """
        output_list = []

        """
        в данном функции меняется кол-во вершин 
        answer=edges
        edges=answer
        """
        for type_task in range(1, 7):

            for i in range(randomleft1, randomright1):
                incorrect_answers = []
                right_answer = []
                # определяем сколько вершин в графе минимум 3
                # answer = random.randint(3, 30)
                count_nodes = i
                stepen_node = i - 1
                edges = int(count_nodes * (count_nodes - 1) / 2)

                if type_task == 1:
                    task_text = f"Найдите степень вершины полного графа, в котором количество ребер равно {edges}."
                    right_answer.append(stepen_node)
                    # НЕправильный ответы для степени вершины
                    delta_ans = stepen_node
                    delta_ans += 1
                    incorrect_answers.append(delta_ans)
                    delta_ans += 1
                    incorrect_answers.append(delta_ans)
                    delta_ans -= 3
                    incorrect_answers.append(delta_ans)


                elif type_task == 2:
                    task_text = f"Найдите степень вершины полного графа, в котором количество  вершин  равно {count_nodes}."
                    right_answer.append(stepen_node)
                    # НЕправильный ответы для степени вершины
                    delta_ans = stepen_node
                    delta_ans += 1
                    incorrect_answers.append(delta_ans)
                    delta_ans += 1
                    incorrect_answers.append(delta_ans)
                    delta_ans -= 3
                    incorrect_answers.append(delta_ans)
                elif type_task == 3:
                    task_text = f"Найдите количество ребер в полном графе,в котором количество  вершин  равно {count_nodes}."
                    right_answer.append(edges)
                    # НЕправильный ответы для количества ребер
                    delta_ans = count_nodes
                    delta_ans += 1
                    delta_edg = int(delta_ans * (delta_ans - 1) / 2)
                    incorrect_answers.append(delta_edg)
                    delta_ans += 1
                    delta_edg = int(delta_ans * (delta_ans - 1) / 2)
                    incorrect_answers.append(delta_edg)
                    delta_ans -= 3
                    delta_edg = int(delta_ans * (delta_ans - 1) / 2)
                    incorrect_answers.append(delta_edg)
                elif type_task == 4:
                    task_text = f"Найдите количество ребер в полном графе, если степень  вершины равна {stepen_node}."
                    right_answer.append(edges)
                    # НЕправильный ответы для количества ребер
                    delta_ans = count_nodes
                    delta_ans += 1
                    delta_edg = int(delta_ans * (delta_ans - 1) / 2)
                    incorrect_answers.append(delta_edg)
                    delta_ans += 1
                    delta_edg = int(delta_ans * (delta_ans - 1) / 2)
                    incorrect_answers.append(delta_edg)
                    delta_ans -= 3
                    delta_edg = int(delta_ans * (delta_ans - 1) / 2)
                    incorrect_answers.append(delta_edg)
                elif type_task == 5:
                    task_text = f"Найдите количество вершин в полном графе, в котором количество ребер равно {edges}."
                    right_answer.append(count_nodes)
                    # НЕправильный ответы для количества вершин
                    delta_ans = count_nodes
                    delta_ans += 1
                    incorrect_answers.append(delta_ans)
                    delta_ans += 1
                    incorrect_answers.append(delta_ans)
                    delta_ans -= 3
                    incorrect_answers.append(delta_ans)

                elif type_task == 6:
                    task_text = f"Найдите количество вершин в полном графе, если степень вершины равна {stepen_node}."
                    right_answer.append(count_nodes)
                    # НЕправильный ответы для количества вершин
                    delta_ans = count_nodes
                    delta_ans += 1
                    incorrect_answers.append(delta_ans)
                    delta_ans += 1
                    incorrect_answers.append(delta_ans)
                    delta_ans -= 3
                    incorrect_answers.append(delta_ans)

                else:
                    raise Exception

                tmp = (task_text, right_answer, incorrect_answers)
                output_list.append(tmp)

        return output_list

    @staticmethod
    def task_six(count_task):
        """
        Генерирует задачи типа:

        Из полного графа на 20 вершинах несколько вершин удалили. В оставшемся
        подграфе стало 66 ребер. Сколько вершин удалено?

        :param count_task:  Количество задач
        :return:  Список с задачами в формате [(текст, ответ, ложные ответы), (текст, ответ, ложные ответы)]
        """
        output_list = []
        for _ in range(count_task):
            incorrect_answers = []
            while True:
                # определяем сколько вершин в графе
                count_node = random.randint(10, 30)
                # определяем сколько вершин удалить из этого графа
                answer_deleted_nodes = random.randint(1, 10)
                if count_node - answer_deleted_nodes > 4:
                    break
            ost_node = count_node - answer_deleted_nodes
            ost_edges = int(ost_node * (ost_node - 1) / 2)

            if ost_edges % 10 == 0:
                edges_word = "ребер"
            elif 1 > ost_edges % 10 < 5:
                edges_word = "ребра"
            elif ost_edges % 10 == 1:
                edges_word = "ребро"
            else:
                edges_word = "ребер"

            if count_node % 10 == 1:
                nodes_word = "вершине"
            else:
                nodes_word = "вершинах"

            task_text = (
                f"Из полного графа на {count_node} {nodes_word} несколько вершин удалили. В оставшемся подграфе "
                f"стало {ost_edges} {edges_word}. Сколько вершин удалено?")
            # region НЕправильный ответы
            delta_ans = answer_deleted_nodes
            delta_ans += 1
            incorrect_answers.append(delta_ans)
            delta_ans += 1
            incorrect_answers.append(delta_ans)
            delta_ans -= 3
            incorrect_answers.append(delta_ans)

            # endregion

            tmp = (task_text, [answer_deleted_nodes], incorrect_answers)
            output_list.append(tmp)
        return output_list

    @staticmethod
    def __create_n_component_graph(num_vertices, num_components):
        """
        Генерирует n-компонентный граф

        :param num_vertices:  кол-во вершин
        :param num_components:  кол-во компонент, хотя бы на 1 меньше чем, кол-во вершин
        :return: список кортежей связей example: [(1,2),(3,4)]
        """
        if num_components < 1 or num_components > num_vertices:
            return []

        edges = []
        vertices = list(range(1, num_vertices + 1))

        for i in range(num_components - 1):
            component_size = num_vertices // num_components
            component_vertices = random.sample(vertices, component_size)

            for v1 in component_vertices:
                for v2 in component_vertices:
                    if v1 != v2 and (v1, v2) not in edges and (v2, v1) not in edges:
                        edges.append((v1, v2))

            vertices = [v for v in vertices if v not in component_vertices]

        # Последняя компонента соединяет оставшиеся вершины
        for v1 in vertices:
            for v2 in vertices:
                if v1 != v2 and (v1, v2) not in edges and (v2, v1) not in edges:
                    edges.append((v1, v2))

        return edges

    @staticmethod
    def __list_to_string(arr):
        """
        Список в строку
        :param arr:  list
        :return:  str
        """
        text = "["
        for i in range(len(arr)):
            if (i + 1) == len(arr):
                text += str(arr[i])
                text += "];"
                break
            text += str(arr[i])
            text += ","
        return text

    def task_seven(self, count_task):
        """
        Генерирует задачи типа:

        Ниже дан список графов, заданных множествами их ребер. Каждый граф
        содержит 6 вершин. Укажите номера трехкомпонентных графов:
        {(1, 2), (2, 6), (3, 4)};
        {(1, 2), (2, 5), (3, 6)};
        {(1, 5), (3, 5)};
        {(2, 3), (5, 6)};
        {(1, 2), (2, 3), (5, 6)};
        {(1, 2), (2, 5), (3, 4)};

        :param count_task:  Количество задач
        :return:  Список с задачами в формате [(текст, ответы, ложные ответы),(текст, ответы, ложные ответы)]
        """
        output_list = []
        for _ in range(count_task):
            while True:
                count_nodes = random.randint(4, 8)
                component_search = random.randint(3, 5)
                if count_nodes > component_search:
                    break
            match component_search:
                case 2:
                    text_components = "двухкомпонентных"
                case 3:
                    text_components = "трехкомпонентных"
                case 4:
                    text_components = "четырехкомпонентных"
                case 5:
                    text_components = "пятикомпонентных"
                case _:
                    raise Exception

            task_text = (
                f"Ниже дан список графов, заданных множествами их ребер. Каждый граф содержит {count_nodes} вершин. Укажите "
                f"номера {text_components} графов:")

            # region выбираем  сколько правильных ответов хотим нагенерить

            right_answers = []
            count_right_choices = random.randint(1, 4)
            incorrect_answers = []

            # добавляем правильные ответы
            for j in range(count_right_choices):
                list_edges = self.__create_n_component_graph(count_nodes, component_search)
                right_answers.append(list_edges)

            # добавляем НЕправильные ответы
            for j in range(6 - count_right_choices):
                while True:
                    some_num_component = random.randint(1, count_nodes - 1)
                    if some_num_component != component_search:
                        break
                list_edges = self.__create_n_component_graph(count_nodes, some_num_component)

                incorrect_answers.append(list_edges)

            # right_answers = self.__remove_duplicate_tuples(right_answers)
            # incorrect_asnwers = self.__remove_duplicate_tuples(incorrect_asnwers)

            # для свободного ответа (но он не предусмотрен)
            # random.shuffle(arr_choices)
            # k = 1
            # output_answer = ""
            # for arr_edges, acc_answer in arr_choices:
            #     task_text += "\n"
            #     task_text += str(k) + " "
            #     task_text += self.__list_to_string(arr_edges)
            #     if acc_answer:
            #         output_answer += str(k)
            #     k += 1

            tmp = (task_text, right_answers, incorrect_answers)
            output_list.append(tmp)

        return output_list

    def task_eight(self, number_of_tasks, drawing_graph=True, number_forbidden_answer=3):
        """
        Граф задан следующим образом: <{1,2,3,4,5,6}-множество вершин; {(1,3),
        (2,1), (2,5), (3,2), (4,3), (4,5)}-множество дуг>.
        Сколько ребер останется в графе после удаления вершины 2
        :param number_of_tasks: количество задач
        :return result_tasks_massive: массив с задачами в формате (вопрос, ответ)
        :return drawing_graph: рисуем или не рисуем граф
        """
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            self.__graph_generator()
            delete_vertex = random.choice(self.vertices)
            result_vertices = self.vertices.copy()
            result_vertices.remove(delete_vertex)
            result_edges = {(v1, v2) for v1, v2 in self.edges if v1 != delete_vertex and v2 != delete_vertex}

            reversed_edges = [(v, u) for u, v in self.edges]

            task_text = "Граф задан следующим образом: <" + ", ".join(map(str, self.vertices)) + \
                        " -множество вершин; " + ", ".join(map(str, self.edges)) + ", " + ", ".join(
                map(str, reversed_edges)) + \
                        " -множество дуг>." \
                        "Сколько ребер останется в графе после удаления вершины " + str(delete_vertex) + "?"

            path_to_graph_img = ""
            if drawing_graph:
                task_text += "<br/>graph_img"
                path_to_graph_img = self.paintilovka(False, False)

            answer_text = len(result_edges)
            while True:
                forbidden_answer = random.sample(range(answer_text // 2, answer_text * 2), number_forbidden_answer)
                if answer_text not in forbidden_answer:
                    break

            result_tasks_massive.append((task_text, [answer_text], forbidden_answer, path_to_graph_img))
        return result_tasks_massive

    def task_nine(self, count_task, count_edges=7, max_weight=10):
        """
        ::Теория графов::Фирма получила заказ на прокладку кабеля для кабельного телевидения в некотором городе. Узлы сети,
        приводимой ниже отражают точки, к которым должна быть проложена кабельная сеть. Известны расстояния в километрах
        между точками подвода кабеля. Предложите решение, которое позволит обеспечить доступ кабельной сети ко всем точкам,
        но при этом общая протяженность кабельных линий будет минимально возможной. В ответе указать суммарную длину всех
        линий кабельной сети.Расстояния между узлами:
        (7 и 4)=8;
        (2 и 4)=10;
        (2 и 1)=3;
        (3 и 4)=10;
        (3 и 1)=2;
        (5 и 4)=4;
        (5 и 1)=6;
        (5 и 7)=3;
        (6 и 4)=2;
        (2 и 3)=10;
        (6 и 7)=2;
        (1 и 7)=5;
        (7 и 2)=8;
        (1 и 6)=7;
        {=17}
        :param count_task: количество задач
        :param count_edges:количество узлов от 4 до бесконечности если есть необходимость
        :param max_weight: максимальный вес (расстояние между точками) задаётся целым числом
        :return: массив задач в формате

        """
        result_mas = []
        wrong_ans = []
        if count_edges < 5:
            return "error"
        for i in range(count_task):
            wrong_ans = []
            # Создаем пустой взвешенный граф
            G = nx.Graph()
            nodes = list(range(1, count_edges + 1))  # любые числа
            edges = set()
            # Добавляем узлы и ребра с весами
            while len(edges) < (count_edges + 1) * 2 - 2:
                node1, node2 = random.sample(nodes, 2)
                if (node1, node2) not in edges and (node2, node1) not in edges:
                    edges.add((node1, node2))
            edges_with_random_weights = [(node1, node2, round(random.uniform(1, max_weight))) for node1, node2 in edges]
            self.graph = {(key1, key2): value for key1, key2, value in edges_with_random_weights}
            # добавляем веса в граф
            G.add_weighted_edges_from(edges_with_random_weights)

            # Находим минимальное остовное дерево
            min_spanning_tree = nx.minimum_spanning_tree(G)

            # Вычисляем общую протяженность кабельных линий
            total_length = sum(weight for u, v, weight in min_spanning_tree.edges(data='weight'))
            string_task = str.format("Фирма получила заказ на прокладку кабеля для кабельного телевидения в некотором "
                                     "городе. Узлы сети, приводимой ниже отражают точки, к которым должна быть проложена "
                                     "кабельная сеть. Известны расстояния в километрах между точками подвода кабеля. "
                                     "Предложите решение, которое позволит обеспечить доступ кабельной сети ко всем "
                                     "точкам, но при этом общая протяженность кабельных линий будет минимально возможной. "
                                     "В ответе указать суммарную длину всех линий кабельной сети.Расстояния между узлами:") + "<br/>graph_img"
            for node1, node2, weight in edges_with_random_weights:
                string_task += f"\n ({node1} и {node2})={weight};"
            # string_task+="\n"
            string_task_results = total_length
            for som in range(3):
                random_var = random.choice([True, False])
                new_value = 0

                while True:
                    if random_var:
                        new_value = total_length - random.randint(1, 10)
                    else:
                        new_value = total_length + random.randint(1, 10)

                    # Проверка на отрицательное значение и отсутствие в массиве
                    if new_value >= 0 and new_value not in wrong_ans and new_value != total_length:
                        wrong_ans.append(new_value)
                        break

            # print(min_spanning_tree.edges(data=False))
            path_to_graph_img = self.paintilovka(True, False)
            result_mas.append((string_task, [string_task_results], wrong_ans, path_to_graph_img))
        return result_mas

    @staticmethod
    def __dijkstra(graph, start):
        """
        Алгоритм Дейкстры
        :param graph: граф который мы используем
        :param start: вершина с которой мы начинаем алгоритм
        :return: минимальное расстояние до каждой из вершин, предшественников для них
        """
        # Инициализация словарей для хранения кратчайших расстояний и предыдущих узлов
        shortest_distances = {}
        predecessors = {}
        unvisited_nodes = graph

        # Установка бесконечности для начального узла и 0 для остальных
        for node in unvisited_nodes:
            shortest_distances[node] = float('inf')
        shortest_distances[start] = 0

        while unvisited_nodes:
            # Выбор узла с наименьшим известным расстоянием
            min_node = None
            for node in unvisited_nodes:
                if min_node is None:
                    min_node = node
                elif shortest_distances[node] < shortest_distances[min_node]:
                    min_node = node

            # Находим кратчайшие расстояния до соседей
            neighbors = graph[min_node]
            for neighbor, weight in neighbors.items():
                potential = shortest_distances[min_node] + weight
                if potential < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = potential
                    predecessors[neighbor] = min_node

            # Удаляем текущий узел из непосещенных
            unvisited_nodes.pop(min_node)

        return shortest_distances, predecessors

    def task_ten(self, count_task, count_edges=6, max_weight=10):
        """
        ::Теория графов::В промышленном районе города расположены склад (узел 7) компании «Строй и пой» и строительные
        площадки компании (узлы от 1 до 6), на которых она осуществляет работы. Известны расстояния от склада до всех
        площадок как напрямую, так и через промежуточные объекты. Найти  площадку наиболее удаленую от склада. В ответ
        запишите длину минимального пути от склада до этой площадки. Расстояния между узлами:
        (7 и 4)=8;
        (7 и 1)=2;
        (7 и 6)=1;
        (7 и 2)=9;
        (7 и 5)=8;
        (4 и 7)=8;
        (4 и 3)=5;
        (4 и 5)=4;
        (4 и 6)=6;
        (4 и 1)=5;
        (6 и 2)=8;
        (6 и 1)=3;
        (6 и 4)=6;
        (6 и 7)=1;
        (6 и 3)=1;
        (2 и 6)=8;
        (2 и 7)=9;
        (1 и 7)=2;
        (1 и 3)=7;
        (1 и 6)=3;
        (1 и 5)=6;
        (1 и 4)=5;
        (3 и 4)=5;
        (3 и 1)=7;
        (3 и 6)=1;
        (5 и 4)=4;
        (5 и 1)=6;
        (5 и 7)=8;
        {=9}
        :param self:
        :param count_task:количество задач
        :param count_edges: количество узлов
        :param max_weight: максимальный вес узла
        :return:массив задач в формате
        """

        result_mas = []
        if count_edges < 5:
            return "error"

        for i in range(count_task):
            wrong_ans = []
            nodes = list(range(1, count_edges + 1))  # Например, от 1 до 8
            edges = set()
            # Добавляем ребра с весами
            # while len(edges) < (count_edges + 1) * 2 - 2:
            #     node1, node2 = random.sample(nodes, 2)
            #     if (node1, node2) not in edges and (node2, node1) not in edges:
            #         edges.add((node1, node2))

            # while len(edges) < (count_edges + 1) * 2 - 2:
            #     node1, node2 = random.sample(nodes, 2)
            #     if (node1, node2) not in edges and (node2, node1) not in edges:
            #         edges.add((node1, node2))
            #
            #     # Создаём временный граф и проверяем его связность
            #
            #     temp_digraph = nx.DiGraph(list(edges))
            #     if nx.is_strongly_connected(temp_digraph):
            #         break
            G = nx.DiGraph()

            G.add_nodes_from(nodes)
            while not nx.is_strongly_connected(G):
                start = random.choice(nodes)
                end = random.choice(nodes)
                if start != end:
                    capacity = random.randint(1, max_weight)
                    G.add_edge(start, end, capacity=capacity)

            # создаем пустой граф и заполняем его
            graph = {}
            graph_vis = ""
            for edge in G.edges(data=True):
                node1, node2, weight = edge
                if node1 not in graph:
                    graph[node1] = {}
                if node2 not in graph:
                    graph[node2] = {}
                graph[node1][node2] = weight['capacity']
                graph[node2][node1] = weight['capacity']
            # Вызываем алгоритм дейктсры
            for node1, neighbors in graph.items():
                for node2, weight in neighbors.items():
                    graph_vis += f"\n({node1} и {node2})={weight};"
            shortest_distances, predecessors = self.__dijkstra(graph, count_edges)
            self.graph = {(key1, key2): value for key1, key2, value in G.edges(data='capacity')}

            # бесполезная строчка просто чтоб была
            shortest_paths = shortest_distances
            # shortest_paths = nx.single_source_dijkstra_path_length(G, source=count_edges)
            max_shortest_paths = max(shortest_paths.values())
            # Выводим задачу и ответ
            string_task = str.format(f"В промышленном районе города расположены склад (узел {count_edges}) компании "
                                     f"«Строй и пой» и строительные площадки компании (узлы от 1 до {count_edges - 1}), "
                                     f"на которых она осуществляет работы. Известны расстояния от склада до всех площадок "
                                     f"как напрямую, так и через промежуточные объекты. Найти  площадку наиболее удаленую "
                                     f"от склада. В ответ запишите длину минимального пути от склада до этой площадки. "
                                     f"Расстояния между узлами: ",
                                     count_edges)
            string_task += graph_vis + "<br/>graph_img"
            string_task_results = max_shortest_paths
            if string_task_results > 99999:
                max_shortest_paths = 0
            for som in range(3):
                random_var = random.choice([True, False])
                new_value = 0

                while True:
                    if random_var:
                        new_value = max_shortest_paths - random.randint(1, 10)
                    else:
                        new_value = max_shortest_paths + random.randint(1, 10)
                    if max_shortest_paths == 0:
                        new_value = max_shortest_paths + random.randint(1, 10)
                    # Проверка на отрицательное значение и отсутствие в массиве
                    if new_value >= 0 and new_value not in wrong_ans and new_value != max_shortest_paths:
                        wrong_ans.append(new_value)
                        break
            # print(min_spanning_tree.edges(data=False))
            path_to_graph_img = self.paintilovka(True, False)
            result_mas.append((string_task, [string_task_results], wrong_ans, path_to_graph_img))
        return result_mas

# TODO: сделать так чтобы из города nck нельзя было попасть сразу в город E
    def task_eleven(self, count_task, max_weight=10):
        """
    ::Теория графов::Система автодорог, проходящих через N-скую область, может обеспечить следующие пропускные способности измеряемые в тыс. автомашин в час:
    из города N-ск в город A - пропускная способность равна 9
    из города N-ск в город E - пропускная способность равна 4
    из города N-ск в город C - пропускная способность равна 10
    из города N-ск в город B - пропускная способность равна 2
    из города A в город C - пропускная способность равна 7
    из города A в город N-ск - пропускная способность равна 10
    из города B в город N-ск - пропускная способность равна 3
    из города B в город E - пропускная способность равна 8
    из города B в город D - пропускная способность равна 9
    из города C в город A - пропускная способность равна 2
    из города C в город N-ск - пропускная способность равна 6
    из города D в город N-ск - пропускная способность равна 7
    из города D в город C - пропускная способность равна 5
    из города D в город E - пропускная способность равна 4
    из города E в город A - пропускная способность равна 6
    из города E в город C - пропускная способность равна 4
    Въезд в область осуществляется через город N-ск, а выезд через город Е. Каков максимальный поток через эту систему (тыс. автомашин в час)?{=6}

        :param count_task: количество задач
        :param max_weight: максимальный вес между узлами графа
        :return: массив задач в формате
        """
        result_mas = []
        for i in range(count_task):
            wrong_ans = []
            G = nx.DiGraph()

            # Список вершин
            nodes = ['N-ск', 'A', 'B', 'C', 'D', 'E']

            # Добавляем вершины в граф
            G.add_nodes_from(nodes)

            source_node = 'N-ск'
            nx.set_node_attributes(G, {source_node: {'source': True}}, 'attributes')

            # Устанавливаем вершину 'E' как сток
            sink_node = 'E'
            nx.set_node_attributes(G, {sink_node: {'sink': True}}, 'attributes')

            # Генерируем случайные пропускные способности между вершинами
            while not nx.is_strongly_connected(G):
                start = random.choice(nodes)
                end = random.choice(nodes)
                if start != end and not (start == source_node and end == sink_node):
                    capacity = random.randint(1, max_weight)
                    G.add_edge(start, end, capacity=capacity)

            # Удаляем входящие рёбра для вершины-источника
            for node in G.nodes():
                if node != source_node and G.has_edge(node, source_node):
                    G.remove_edge(node, source_node)

            # Удаляем исходящие рёбра для вершины-стока
            for node in G.nodes():
                if node != sink_node and G.has_edge(sink_node, node):
                    G.remove_edge(sink_node, node)

            # Добавляем рёбра с пропускными способностями в граф
            # Находим максимальный поток
            max_flow_value, max_flow_dict = nx.maximum_flow(G, source_node, sink_node)
            task_var = random.randint(1,4)
            match task_var:
                case 1:
                    string_task = ("Система автодорог, проходящих через N-скую область, может обеспечить следующие пропускные "
                                   "способности измеряемые в тыс. автомашин в час:")
                    for start, end, capacity in G.edges(data=True):
                        capacity_value = capacity['capacity']
                        string_task += f"\n из города {start} в город {end} - пропускная способность равна {capacity_value};"
                    self.graph = {(key1, key2): value for key1, key2, value in G.edges(data='capacity')}
                    self.vertices = ['N-ск', 'A', 'B', 'C', 'D', 'E']

                    string_task += (
                                       "\n Въезд в область осуществляется через город N-ск, а выезд через город Е. Каков максимальный "
                                       "поток через эту систему (тыс. автомашин в час)?") + "<br/>graph_img"

                    string_task_results = max_flow_value
                    # print(min_spanning_tree.edges(data=False))
                    for som in range(3):

                        while True:
                            random_var = random.choice([True, False])
                            new_value = 0
                            if random_var:

                                new_value = max_flow_value - random.randint(1, 10)
                            else:
                                new_value = max_flow_value + random.randint(1, 10)

                            # Проверка на отрицательное значение и отсутствие в массиве
                            if new_value >= 0 and new_value not in wrong_ans and new_value != max_flow_value:
                                wrong_ans.append(new_value)
                                break
                    path_to_graph_img = self.paintilovka(True, True)
                    result_mas.append((string_task, [string_task_results], wrong_ans, path_to_graph_img))
                    print(f"Максимальный поток: {max_flow_value}")
                    print("Поток по рёбрам:")
                    for start, edges in max_flow_dict.items():
                        for end, flow in edges.items():
                            print(f"Ребро ({start} -> {end}): Поток = {flow}")
                case 2:
                    string_task = ("Фирма добывает некоторое сырье в пункте, обозначенном на карте точкой N-ск. "
                                   "Его нужно доставить на завод – обозначенный на карте точкой E. Так же на "
                                   "карте обозначены возможные маршруты, по которым добытое сырье может "
                                   "быть отправлено. Для каждого участка маршрута указано сколько сырья "
                                   "можно по нему доставить.")
                    for start, end, capacity in G.edges(data=True):
                        capacity_value = capacity['capacity']
                        string_task += f"\n из участка {start} в участок {end} - пропускная способность равна {capacity_value};"
                    self.graph = {(key1, key2): value for key1, key2, value in G.edges(data='capacity')}
                    self.vertices = ['N-ск', 'A', 'B', 'C', 'D', 'E']

                    string_task += (
                                       "\n  Какое максимальное количества "
                                       "сырья может быть доставлено из пункта N-ск в пункт E?") + "<br/>graph_img"

                    string_task_results = max_flow_value
                    # print(min_spanning_tree.edges(data=False))
                    for som in range(3):

                        while True:
                            random_var = random.choice([True, False])
                            new_value = 0
                            if random_var:

                                new_value = max_flow_value - random.randint(1, 10)
                            else:
                                new_value = max_flow_value + random.randint(1, 10)

                            # Проверка на отрицательное значение и отсутствие в массиве
                            if new_value >= 0 and new_value not in wrong_ans and new_value != max_flow_value:
                                wrong_ans.append(new_value)
                                break
                    path_to_graph_img = self.paintilovka(True, True)
                    result_mas.append((string_task, [string_task_results], wrong_ans, path_to_graph_img))
                    print(f"Максимальный поток: {max_flow_value}")
                    print("Поток по рёбрам:")
                    for start, edges in max_flow_dict.items():
                        for end, flow in edges.items():
                            print(f"Ребро ({start} -> {end}): Поток = {flow}")
                case 3:
                    string_task = ("Дан участок сети труб, через который некоторое вещество с постоянной "
                                   "скоростью движется от источника N-ск к стоку E. Известна пропускная "
                                   "способность каждой трубы.")
                    for start, end, capacity in G.edges(data=True):
                        capacity_value = capacity['capacity']
                        string_task += f"\n из трубы {start} в трубу {end} - пропускная способность равна {capacity_value} тыс. литров в сутки;"
                    self.graph = {(key1, key2): value for key1, key2, value in G.edges(data='capacity')}
                    self.vertices = ['N-ск', 'A', 'B', 'C', 'D', 'E']

                    string_task += (
                                       "\n   Какое максимальное количества вещества "
                                       "может быть пропущено на данном участке сети из А в Z?") + "<br/>graph_img"

                    string_task_results = max_flow_value
                    # print(min_spanning_tree.edges(data=False))
                    for som in range(3):

                        while True:
                            random_var = random.choice([True, False])
                            new_value = 0
                            if random_var:

                                new_value = max_flow_value - random.randint(1, 10)
                            else:
                                new_value = max_flow_value + random.randint(1, 10)

                            # Проверка на отрицательное значение и отсутствие в массиве
                            if new_value >= 0 and new_value not in wrong_ans and new_value != max_flow_value:
                                wrong_ans.append(new_value)
                                break
                    path_to_graph_img = self.paintilovka(True, True)
                    result_mas.append((string_task, [string_task_results], wrong_ans, path_to_graph_img))
                    print(f"Максимальный поток: {max_flow_value}")
                    print("Поток по рёбрам:")
                    for start, edges in max_flow_dict.items():
                        for end, flow in edges.items():
                            print(f"Ребро ({start} -> {end}): Поток = {flow}")
                case 4:
                    string_task = ("Владелец некоторого завода, выпускающего «Товар», находящегося в пункте "
                                   "А, заключил контракт с фирмой, находящейся в другом городе на поставку "
                                   "товаров в их розничную сеть. Товары придется доставлять авиаперевозкой. "
                                   "При транспортировке в аэропорт, находящийся в пункте Z, есть некоторые "
                                   "ограничения: на дорогах стоят пункты досмотра груза, весового контроля, "
                                   "некоторые дороги и вовсе ремонтируются. Т. е. известна «пропускная "
                                   "способностью» дорог в день.")
                    for start, end, capacity in G.edges(data=True):
                        capacity_value = capacity['capacity']
                        string_task += f"\n для участка дороги ({start}, {end}) - {capacity_value} ящика;"
                    self.graph = {(key1, key2): value for key1, key2, value in G.edges(data='capacity')}
                    self.vertices = ['N-ск', 'A', 'B', 'C', 'D', 'E']

                    string_task += (
                                       "\n    Владельцу "
                                       "необходимо узнать: какое максимальное число ящиков он сможете "
                                       "транспортировать в аэропорт в день, учитывая пропускную способность "
                                       "дорог?") + "<br/>graph_img"

                    string_task_results = max_flow_value
                    # print(min_spanning_tree.edges(data=False))
                    for som in range(3):

                        while True:
                            random_var = random.choice([True, False])
                            new_value = 0
                            if random_var:

                                new_value = max_flow_value - random.randint(1, 10)
                            else:
                                new_value = max_flow_value + random.randint(1, 10)

                            # Проверка на отрицательное значение и отсутствие в массиве
                            if new_value >= 0 and new_value not in wrong_ans and new_value != max_flow_value:
                                wrong_ans.append(new_value)
                                break
                    path_to_graph_img = self.paintilovka(True, True)
                    result_mas.append((string_task, [string_task_results], wrong_ans, path_to_graph_img))
                    print(f"Максимальный поток: {max_flow_value}")
                    print("Поток по рёбрам:")
                    for start, edges in max_flow_dict.items():
                        for end, flow in edges.items():
                            print(f"Ребро ({start} -> {end}): Поток = {flow}")
        return result_mas

    @staticmethod
    def __check_unique_NOD_NOK_answer(answer, FalseAnswer):
        # Проверка на совпадение правильного ответа с неправильными
        if answer[0] in FalseAnswer or len(set(FalseAnswer)) < 3:
            print("Итог:", answer, FalseAnswer)
            raise ValueError("Ошибка: Правильный ответ содержится в массиве неправильных ответов "
                             "или два неправильных ответа совпадают.")

    def task_twelve_1(self, count_task):
        resArray = []
        for i in range(count_task):
            random.seed()
            a = random.randrange(50, 75)
            b = random.randrange(25, 50)
            c = random.randrange(10, 25)

            str_task = f"Найти НОК 3 чисел a, b, c при a = {a}, b = {b}, c = {c}."

            X_1 = a * b / self.__NOD_2(a, b)[0]
            Answer = int(X_1 * c / self.__NOD_2(X_1, c)[0])

            # Генерация неправильных ответов
            quarter_answer = Answer // 4
            sixth_answer = Answer // 6

            incorrect_1 = Answer + quarter_answer
            incorrect_2 = Answer - quarter_answer
            incorrect_3 = Answer + sixth_answer
            incorrect_4 = Answer - sixth_answer

            F_Answers = [incorrect_1, incorrect_2, incorrect_3, incorrect_4]

            self.__check_unique_NOD_NOK_answer([Answer], F_Answers)

            resArray.append((str_task, [Answer], F_Answers))

        return resArray

    def task_twelve_2(self, count_task):
        """
        Найти НОД 3 чисел a, b, c используя алгоритм Евклида, при a = 20, b = 56, c = 128
        :return: массив задач в формате
        """
        resArray_12 = []
        for i in range(count_task):
            random.seed()

            x = [1]
            while x == [1]:
                a = random.randrange(50, 75)
                b = random.randrange(25, 50)
                c = random.randrange(10, 25)
                result_func = self.__NOD_3(a, b, c)
                x = result_func[0]
                if x == [1]:
                    continue

                str_task = f"Найти НОД 3 чисел a, b, c используя алгоритм Евклида, при a = {a}, b = {b}, c = {c}."
                answer = x

                # Проверка уникальности неправильных ответов
                while True:
                    incorrect_1 = random.randint(1, 10)
                    incorrect_2 = random.randint(1, 10)
                    incorrect_3 = random.randint(1, 10)

                    # Проверка на уникальность
                    if len(set([answer[0], incorrect_1, incorrect_2, incorrect_3])) == 4:
                        break

                F_Answers = [incorrect_1, incorrect_2, incorrect_3]
                resArray_12.append((str_task, answer, F_Answers))

        return resArray_12

    def __NOD_3(self, a, b, c):
        """
        Нахождение НОД 3 чисел
        :param a: Первое число
        :param b: Второе число
        :param c: Третье число
        :return:
        """
        TAnswer = [self.__NOD_2(a, self.__NOD_2(b, c)[0])[0]]
        FAnswers = []
        FAnswers.append(self.__NOD_2(a, self.__NOD_2(b, c)[1][0])[1][1])
        FAnswers.append(self.__NOD_2(a, self.__NOD_2(b, c)[1][1])[1][0])
        FAnswers.append(self.__NOD_2(a, self.__NOD_2(b, c)[1][2])[1][2])
        return TAnswer, FAnswers

    @staticmethod
    def __NOD_2(a, b):
        """
        :param a: Первое число
        :param b: Второе число
        :return: НОД a и b
        """
        ost = -1
        if a < b:
            k = b
            b = a
            a = k

        # a всегда больше b
        while ost != 0:
            ost = a % b
            a = b
            b = ost
        Answers = []
        CorrectAnswer = a

        if CorrectAnswer > 2:
            Answers.append(CorrectAnswer + random.randint(1, 3))
        else:
            Answers.append(CorrectAnswer + random.randint(4, 6))

        # Генерируем дополнительные уникальные значения
        while len(Answers) < 3:
            new_value = CorrectAnswer + random.randint(7, 12)
            if new_value not in Answers:
                Answers.append(new_value)
        return CorrectAnswer, Answers

    @staticmethod
    def __CreateNumber(k):
        """
        Создание числа заданно размерности
        :param k: Система счисления создаваемого числа
        :return: Число заданной размерности
        """
        res = ""
        random.seed()
        a = random.randrange(5, 9)
        alphabet = "0123456789abcdef"
        for i in range(a):
            n = random.randrange(0, k)
            if i == 0 and n == 0:
                n += 1

            res += alphabet[n]
        return res

    @staticmethod
    def __convert_base(num, to_base, from_base):
        """
        Перевод числа из одной произвольной системы счисления в другую произвольную систему счисления
        :param num: число, которое переводится
        :param to_base: целевая система счисления
        :param from_base: исходная система счисления
        :return:
        """
        # first convert to decimal number
        n = int(num, from_base) if isinstance(num, str) else num
        # now convert decimal to 'to_base' base
        alphabet = "0123456789abcdef"
        res = ""
        while n > 0:
            n, m = divmod(n, to_base)
            res += alphabet[m]
        return res[::-1]

    @staticmethod
    def __isSimple(x):
        random.seed()
        n = x
        if n % 2 == 0:
            return False
        d = 1
        while d * d <= n:
            d += 2
            if n % d == 0:
                return False

        return True

    def task_thirteen(self, count_task):
        """
        Определить какое из чисел 51 100 131 167 является простым
        :return: Массив задач в формате
        """
        simple_List = []
        answers_simple_List = []
        i = 2
        while i < 50:
            if self.__isSimple(i):
                simple_List.append(i)
            i += 1

        i = 100
        while i < 1000:
            if self.__isSimple(i):
                answers_simple_List.append(i)
            i += 1

        resArray_13 = []
        for i in range(count_task):
            random.seed()
            x = random.randrange(0, len(answers_simple_List) - 1)
            CorrectAnswer = answers_simple_List[x]
            Answers = []
            AllAnswers = [CorrectAnswer]

            L = len(simple_List)
            L_1 = int(L / 3)
            L_2 = int(L / 3 * 2)

            x = random.randrange(0, L_1)
            y = random.randrange(0, L_1)
            x = simple_List[x] * simple_List[y]
            Answers.append(x)
            AllAnswers.append(x)

            x = random.randrange(L_1, L_2)
            y = random.randrange(L_1, L_2)
            x = simple_List[x] * simple_List[y]
            Answers.append(x)
            AllAnswers.append(x)

            x = random.randrange(L_2, L - 1)
            y = random.randrange(L_2, L - 1)
            x = simple_List[x] * simple_List[y]
            Answers.append(x)
            AllAnswers.append(x)

            random.shuffle(AllAnswers)
            str = f"Определить какое из чисел {AllAnswers[0]}, {AllAnswers[1]}, {AllAnswers[2]}, {AllAnswers[3]} является простым."
            resArray_13.append((str, [CorrectAnswer], Answers))
        return resArray_13

    @staticmethod
    def __ParseDr(n, d):
        res = []
        while d:
            n, r, d = d, *divmod(n, d)
            res.append(r)
        return res

    def task_fourteen(self, count_task):
        """
        C помощью разложения в непрерывную дробь сохратить дробь a/b. При a=4045, b=2002
        :return: Массив задач в формате
        """
        random.seed()
        result = []
        for i in range(count_task):
            n = random.randrange(10000, 50000)
            wrongN = []
            for i in range(3):
                wrongN.append(n + random.randint((i + 1) * 10, (i + 1) * 10 + random.randint(1, 5)))
            d = random.randrange(1000, 9999)
            d_1 = d
            str = f"C помощью разложения в непрерывную дробь, сохратить дробь a/b. При a={n}, b={d}."
            res = []
            TrueRes = self.__ParseDr(n, d)

            FalseAnswer = []
            wrongAnswer = []

            for i in range(3):
                FalseAnswer.append(self.__ParseDr(wrongN[i], d))

            result.append((str, [TrueRes], FalseAnswer))
            FalseAnswer = []
            wrongAnswer = []
        return result

    def task_fifteen(self, count_task):
        """
        Перевести число a из p-ичной системы счисления в q-ичную. При a = 2054,p = 6,q = 2"
        :return: Массив задач в формате
        """

        random.seed()
        resArray_15 = []
        for i in range(count_task):

            wrongAnswer = []
            a = random.randrange(2, 16)
            b = a
            res = 0
            while b == a:
                b = random.randrange(2, 16)
            n_1 = self.__CreateNumber(a)
            str = f"Перевести число a из p-ичной системы счисления в q-ичную. При a = {n_1}, p = {a}, q = {b}."
            TrueAnswer = self.__convert_base(n_1, b, a)
            x = n_1
            for i in range(3):
                while n_1 == x:
                    x = self.__CreateNumber(a)
                n_1 = x
                wrongAnswer.append(self.__convert_base(x, b, a))

            resArray_15.append((str, [TrueAnswer], wrongAnswer))

        return resArray_15

    @staticmethod
    def __color_graph(G):
        color_map = {}  # словарь для хранения цветов вершин
        available_colors = set(range(1, len(G) + 1))  # множество доступных цветов

        # Раскрашиваем вершины
        for node in G.nodes():
            # Получаем цвета соседей
            neighbor_colors = {color_map[neighbor] for neighbor in G.neighbors(node) if neighbor in color_map}

            # Находим доступные цвета
            available_colors_for_node = available_colors - neighbor_colors

            # Выбираем минимальный доступный цвет для вершины
            color_map[node] = min(available_colors_for_node)

        # Возвращаем словарь с раскраской
        return color_map

    def bron_kerbosch(self, graph, R, P, X, chromatic_number):
        if not P and not X:
            chromatic_number[0] = max(chromatic_number[0], len(R))
        for v in list(P):
            self.bron_kerbosch(graph, R.union({v}), P.intersection(graph.neighbors(v)), X.intersection(graph.neighbors(v)),
                                chromatic_number)
            P.remove(v)
            X.add(v)

    def chromatic_number_bron_kerbosch(self, graph):
        chromatic_number = [0]  # Массив для хранения хроматического числа
        self.bron_kerbosch(graph, set(), set(graph.nodes()), set(), chromatic_number)
        return chromatic_number[0]

    def part_2_task_one(self, count_task=2):
        """
        Картографу требуется раскрасить карту местности. Каким минимальным числом цветов он может это сделать, если
         никакие два объекта имеющих общую границу не должны быть раскрашены в один цвет. Известно, что граничат:
        обьект 1 и 2
        обьект 1 и 3
        обьект 1 и 4
        обьект 1 и 5
        обьект 2 и 5
        обьект 2 и 6
        обьект 2 и 7
        обьект 2 и 4
        обьект 3 и 4
        обьект 3 и 6
        обьект 4 и 5
        обьект 4 и 7
        обьект 5 и 7
        обьект 6 и 7 {=5
        }
        :param count_task: количество задач
        :return: массив задач в формате
        """
        k = 0
        result_mas = []
        ans_3 = 0
        ans_4 = 0
        ans_5 = 0

        while k < count_task:
            num_nodes = random.randint(7, 8)
            G = nx.Graph()

            # Добавляем вершины
            G.add_nodes_from(range(1, num_nodes + 1))

            # Генерируем случайные степени для каждой вершины
            degrees = [random.randint(2, 4) for _ in range(num_nodes)]

            # Добавляем ребра, удовлетворяющие заданным степеням
            for i in range(num_nodes):
                while G.degree[i + 1] < degrees[i]:
                    # Выбираем случайную вершину для создания ребра
                    j = random.randint(1, num_nodes)

                    # Убеждаемся, что не создаем петли и множественные ребра
                    if i + 1 != j and not G.has_edge(i + 1, j):
                        G.add_edge(i + 1, j)

            # Выводим информацию о графе
            # print("Список ребер в графе:")
            # print(G.edges())
            # coloring = self.__color_graph(G)
            chrom_number = self.chromatic_number_bron_kerbosch(G)

            # print("Минимальное число цветов:", max(coloring.values()))
            # print("Раскраска вершин:", coloring)
            max_degree = max(dict(G.degree()).values())
            # print("Максимальная степень вершины:", max_degree)
            # pos = nx.spring_layout(G)  # Позиции вершин для визуализации
            # nx.draw(G, pos, with_labels=True, font_weight='bold')
            # plt.show()
            # coloring = self.color_graph(G)

            if int(max_degree) <= 5:
                if (chrom_number == 3):
                    ans_3 += 1
                if (chrom_number == 4):
                    ans_4 += 1
                if (chrom_number == 5):
                    ans_5 += 1
                k += 1
                string_task = (
                    "Картографу требуется раскрасить карту местности. Каким минимальным числом цветов он может это "
                    "сделать, если никакие два объекта имеющих общую границу не должны быть раскрашены в один цвет. "
                    "Известно, что граничат:")
                for start, end, capacity in G.edges(data=True):
                    start_letter = chr(64 + start)
                    end_letter = chr(64 + end)
                    string_task += f"\n объект {start_letter} и {end_letter};"
                # self.graph = {(key1, key2): value for key1, key2, value in G.edges(data='capacity')}
                # self.vertices = ['N-ск', 'A', 'B', 'C', 'D', 'E']

                string_task_results = chrom_number
                result_mas.append((string_task, [string_task_results], []))
        print(ans_3, '+', ans_4, '+', ans_5)
        return result_mas

    # @staticmethod
    # def __dfs(matrix, start):
    #     answer = []
    #     visited = set()  # Множество посещенных вершин
    #     stack = [start]  # Стек для обхода в глубину
    #
    #     while stack:
    #         vertex = stack.pop()  # Берем вершину из вершины стека
    #         if vertex not in visited:
    #             answer.append(vertex + 1)
    #             visited.add(vertex)  # Отмечаем вершину как посещенную
    #
    #             # Добавляем все соседние вершины в стек
    #             for i in range(len(matrix)):
    #                 if matrix[vertex][i] == 1 and i not in visited:
    #                     stack.append(i)
    #     return answer

    @staticmethod
    def __dfs(matrix, start):
        answer = []
        visited = set()  # Множество посещенных вершин
        stack = []  # Список для обхода в глубину

        stack.append(start)  # Добавляем стартовую вершину

        while stack:
            # Сортируем список перед извлечением вершины
            stack.sort()
            vertex = stack.pop(0)  # Извлекаем вершину из начала списка
            if vertex not in visited:
                answer.append(vertex + 1)
                visited.add(vertex)  # Отмечаем вершину как посещенную

                # Добавляем все соседние вершины в стек
                for i in range(len(matrix)):
                    if matrix[vertex][i] == 1 and i not in visited:
                        stack.append(i)
        return answer

    @staticmethod
    def __bfs(matrix, start):
        answer = []
        visited = set()  # Множество посещенных вершин
        queue = deque([start])  # Очередь для обхода в ширину

        while queue:
            vertex = queue.popleft()  # Берем вершину из начала очереди
            if vertex not in visited:
                answer.append(vertex + 1)
                visited.add(vertex)  # Отмечаем вершину как посещенную

                # Добавляем все соседние вершины в очередь
                for i in range(len(matrix)):
                    if matrix[vertex][i] == 1 and i not in visited:
                        queue.append(i)
        return answer

    def part_2_task_two(self, number_of_tasks, drawing_graph=True):
        result_tasks_massive = []
        for _ in range(number_of_tasks):
            self.__graph_generator()
            adjacency_matrix = [[0 for _ in range(len(self.vertices))] for _ in range(len(self.vertices))]
            for i, (vertex_one, vertex_two) in enumerate(self.edges):
                adjacency_matrix[vertex_one - 1][vertex_two - 1] = 1
                adjacency_matrix[vertex_two - 1][vertex_one - 1] = 1

            reversed_edges = [(v, u) for u, v in self.edges]
            task_text = "Граф задан следующим образом: <" + ", ".join(map(str, self.vertices)) + \
                        " -множество вершин; " + ", ".join(map(str, self.edges)) + ", " + ", ".join(
                map(str, reversed_edges)) + \
                        " -множество дуг>."

            if random.choice([True, False]):
                task_text += "Для заданного графа выписать последовательность вершин (подряд, без " \
                             "пробелов), полученную в результате обхода графа в глубину, начиная с вершины 1."
                answer = self.__dfs(adjacency_matrix, 0)
            else:
                task_text += "Для заданного графа выписать последовательность вершин (подряд, без " \
                             "пробелов), полученную в результате обхода графа в ширину, начиная с вершины 1."
                answer = self.__bfs(adjacency_matrix, 0)

            # print()
            # print(*adjacency_matrix, sep="\n")
            # print()
            # print(answer)
            path_to_graph_img = ""
            if drawing_graph:
                task_text += "<br/>graph_img"
                path_to_graph_img = self.paintilovka(False, False)

            result_tasks_massive.append((task_text, ["".join(map(str, answer))], [], path_to_graph_img))
        return result_tasks_massive

    @staticmethod
    def solve_ilp_double_type(kx_1, ky_1, target_x, kx_2, ky_2, target_y, cost_i, cost_ii, maximize=False):
        # Создаем объект задачи
        prob = LpProblem("ILP", LpMaximize if maximize else LpMinimize)

        # Определяем переменные решения
        x = LpVariable("x", lowBound=0, cat='Float')
        y = LpVariable("y", lowBound=0, cat='Float')

        # f"{kx_1}*x + {kx_2}*y >= {target_x}\n"
        # f"{ky_1}*x + {ky_2}*y >= {target_y}\n"

        # Добавляем ограничения
        prob += kx_1 * x + kx_2 * y >= target_x
        prob += ky_1 * x + ky_2 * y >= target_y

        # Добавляем целевую функцию
        prob += cost_i * x + cost_ii * y

        # Устанавливаем уровень логирования на ERROR
        pulp.LpSolverDefault.msg = 0
        # Решаем задачу
        prob.solve()

        # Возвращаем результаты
        result = {
            'status': LpStatus[prob.status],
            'x': float(x.value()),
            'y': float(y.value()),
            'objective_value': float(lpSum(cost_i * x + cost_ii * y).value())
        }

        return result

    @staticmethod
    def solve_ilp(kx_1, ky_1, target_x, kx_2, ky_2, target_y, cost_i, cost_ii, maximize=True):
        # Создаем объект задачи
        prob = LpProblem("ILP", LpMaximize if maximize else LpMinimize)

        # Определяем переменные решения
        x = LpVariable("x", lowBound=0, cat='Integer')
        y = LpVariable("y", lowBound=0, cat='Integer')

        # f"{kx_1}*x + {kx_2}*y >= {target_x}\n"
        # f"{ky_1}*x + {ky_2}*y >= {target_y}\n"

        # Добавляем ограничения
        prob += kx_1 * x + kx_2 * y >= target_x
        prob += ky_1 * x + ky_2 * y >= target_y

        # Добавляем целевую функцию
        prob += cost_i * x + cost_ii * y

        # Устанавливаем уровень логирования на ERROR
        pulp.LpSolverDefault.msg = 0
        # Решаем задачу
        prob.solve()

        # Возвращаем результаты
        result = {
            'status': LpStatus[prob.status],
            'x': int(x.value()),
            'y': int(y.value()),
            'objective_value': int(lpSum(cost_i * x + cost_ii * y).value())
        }

        return result

    def generate_tasks(self, num_tasks, variation):
        tasks = []
        # 1x+2y>=10

        task_num = 1
        while len(tasks) < num_tasks:

            cost_i = random.randint(8, 20)
            cost_ii = random.randint(8, 20)
            kx_1 = random.randint(1, 8)
            kx_2 = random.randint(1, 8)
            ky_1 = random.randint(1, 8)
            ky_2 = random.randint(1, 8)

            target_x = random.randint(17, 40)
            target_y = random.randint(15, 40)

            if variation == 1:
                res = self.solve_ilp_double_type(kx_1, ky_1, target_x, kx_2, ky_2, target_y, cost_i, cost_ii,
                                                 maximize=False)
                # Выбираем какой вопрос и ответ который хотим получить
                # 0 - продукция 1,
                # 1 - продукция 2,
                # 2- значение целевой функции (цена, вес и т.п.)
                type_answer = random.randint(0, 2)

                if type_answer == 0:
                    end_answer = round(res['x'])
                elif type_answer == 1:
                    end_answer = round(res['y'])
                elif type_answer == 2:
                    end_answer = round(res['objective_value'])
                else:
                    raise Exception

            else:
                res = self.solve_ilp(kx_1, ky_1, target_x, kx_2, ky_2, target_y, cost_i, cost_ii, maximize=False)

                # Выбираем какой вопрос и ответ который хотим получить
                # 0 - продукция 1,
                # 1 - продукция 2,
                # 2- значение целевой функции (цена, вес и т.п.)
                type_answer = random.randint(0, 2)

                if type_answer == 0:
                    end_answer = res['x']
                elif type_answer == 1:
                    end_answer = res['y']
                elif type_answer == 2:
                    end_answer = res['objective_value']
                else:
                    raise Exception

            # Условия сброса, одинаковые параметры стоимости, одинаковые коэфиценты при x или при y, взят только один "класс" в итоговую выборку
            if cost_i == cost_ii:
                continue
            if kx_1 == kx_2:
                continue
            if ky_1 == ky_2:
                continue
            # if res['x'] == 0 or res['y'] == 0:
            #     continue

            # Определяем текстовую вариацию
            match variation:
                case 1:
                    task1_quastions = [
                        f"В ответе укажите количество корма I, который входит в итоговый рацион. (Ответ округлить до ближайшего целого числа)",
                        f"В ответе укажите количество корма II, который входит в итоговый рацион. (Ответ округлить до ближайшего целого числа)",
                        f"В ответе укажите итоговую стоимость рациона. (Ответ округлить до ближайшего целого числа)"
                    ]
                    task_text = (
                        f"Рацион для питания животных на ферме состоит из двух видов кормов I и II. \n"
                        f"Один килограмм корма I стоит {cost_i} ден. ед. и содержит {kx_1} ед. жиров, {ky_1} ед. белков.\n"
                        f"Один килограмм корма II стоит {cost_ii} ден. ед. и содержит {kx_2} ед. жиров, {ky_2} ед. белков.\n"
                        f"Составить наиболее дешевый рацион питания, обеспечивающий жиров не менее {target_x} ед., и белков не менее {target_y} ед.\n"
                        f"{task1_quastions[type_answer]}"
                        # f"Ограничения:\n"
                        # f"{kx_1}*x + {kx_2}*y >= {target_x}\n"
                        # f"{ky_1}*x + {ky_2}*y >= {target_y}\n"
                        # f"x >= 0, y >= 0\n"
                        # f"Целевая функция: {cost_i} * x+ {cost_ii} * y => min\n{res}"
                    )

                case 2:
                    food_names = [
                        "'Классика'",
                        "'Больше мяса, меньше теста'",
                        "'Горечь преподавателя'",
                        "'Антистресс'",
                        "'Знания в банке'",
                        "'Успех'",
                        "'Слезы студента'",
                        "'Тюменский деликатес'",
                    ]
                    # Выбираем первого персонажа
                    food1 = random.choice(food_names)

                    # Удаляем выбранного персонажа из списка
                    food_names.remove(food1)

                    # Выбираем второго персонажа
                    food2 = random.choice(food_names)

                    task2_quastions = [
                        f"В ответе укажите количество тушенки с названием {food1}, которая входит в итоговый набор.",
                        f"В ответе укажите количество тушенки с названием {food1}, которая входит в итоговый набор.",
                        f"В ответе укажите минимальный вес итогового набора."
                    ]

                    task_text = (
                        f"Турист собирается в поход. На складе ТюмГУ есть два вида тушенки:\n"
                        f"1) Тушенка {food1} с содержанием белков {kx_1} ед.  жиров {ky_1} ед. и весом {cost_i} ед.\n"
                        f"2) Тушенка {food2} с содержанием белков {kx_2} ед. и жиров {ky_2} ед. и весом {cost_ii} ед. \n"
                        f"Требуется найти минимальный по весу набор консерв, обеспечивающий нужное количество белков не менее {target_x} ед. и жиров не менее {target_y} ед.\n"
                        f"{task2_quastions[type_answer]}"
                        # f"Ограничения:\n"
                        # f"{kx_1}*x + {kx_2}*y >= {target_x}\n"
                        # f"{ky_1}*x + {ky_2}*y >= {target_y}\n"
                        # f"x >= 0, y >= 0\n"
                        # f"Целевая функция: {cost_i} * x+ {cost_ii} * y => min\n{res}"

                    )
                case 3:
                    character_names = [
                        "'Элита Приключенцев'",
                        "'Симфония Силы'",
                        "'Тайные Стражи'",
                        "'Путь Воителей'",
                        "'Виртуальные Путешественники'",
                        "'Космическая Команда'",
                        "'Магический Союз'",
                        "'Альянс Великих'",
                        "'Стражи Врат'",
                    ]

                    # Выбираем первого персонажа
                    character1 = random.choice(character_names)

                    # Удаляем выбранного персонажа из списка
                    character_names.remove(character1)

                    # Выбираем второго персонажа
                    character2 = random.choice(character_names)

                    task3_quastions = [
                        f"В ответе укажите количество представителей с названием {character1}, которые окажутся в итоговой команде",
                        f"В ответе укажите количество представителей с названием {character2}, которые окажутся в итоговой команде",
                        f"В ответе укажите минимальную сумму, которая необходима для найма команды."
                    ]
                    task_text = (
                        f"В компьютерной игре 'Жизнь' есть несколько представителей групп с разной силой удара, магическим уроном и стоимостью найма.\n"
                        f"1) {character1} Цена: {cost_i} . Сила удара: {kx_1} ед. Магический урон: {ky_1} ед.\n"
                        f"2) {character2} Цена: {cost_ii}. Сила удара: {kx_2} ед. Магический урон: {ky_2} ед.\n"
                        f"Требуется составить команду из персонажей, которая не будет уступать характеристикам главного босса: 'Cессия',\n"
                        f"с суммарной силой удара не менее {target_x} и суммарным магическим уроном не менее {target_y}.\n"
                        f"При этом стоимость найма команды должна быть минимальной.\n"
                        f"{task3_quastions[type_answer]}"
                        # f"Ограничения:\n"
                        # f"{kx_1}*x + {kx_2}*y >= {target_x}\n"
                        # f"{ky_1}*x + {ky_2}*y >= {target_y}\n"
                        # f"x >= 0, y >= 0\n"
                        # f"Целевая функция: {cost_i} * x+ {cost_ii} * y => min\n{res}"

                    )
                case _:
                    task_text = f"Неверно указан номер вариации: {variation}. Выберите от 1 до 3."

            # Записываем задачу, ответ и логи в список
            task_answer_logs_tuple = (task_text, [end_answer], [])
            tasks.append(task_answer_logs_tuple)

        return tasks

    def part_2_task_three(self, num_tasks=None):
        # Пример использования
        if num_tasks is None:
            num_tasks = 2

        for i in range(1, 4):
            task_variation = i  # Выберите вариацию задачи от 1 до 3
            print(i, "статус: Готово")
            if i == 1:
                generated_tasks = self.generate_tasks(num_tasks, task_variation)
            else:
                generated_tasks += self.generate_tasks(num_tasks, task_variation)

        return generated_tasks

    @staticmethod
    def __generate_transportation_problem_text(stations, loading_points, supply, demand, costs):
        text = f"В резерве трех железнодорожных станций {', '.join(stations)} находятся соответственно "
        text += ", ".join([f"{station} - {supply[station]} вагонов" for station in stations]) + ". "

        text += f"\nСоставить оптимальный план перегона этих вагонов к {loading_points} пунктам погрузки, если "
        text += ", ".join([f"пункту №{point} необходимо {demand[point]} вагонов" for point in loading_points]) + ". "

        text += "Стоимость перегона одного вагона:"
        for station in stations:
            text += f"\nсо станции {station} в пункты:"
            text += ", ".join(
                [f"{point} - {costs[(station, point)]} денежных единиц" for point in loading_points]) + ". "

        text += "\nКакое количество перевозок должно быть проставлено в таблице при составлении начального опорного плана."

        return text

    def __generate_transportation_problem(self, num_stations, num_loading_points, open_type=True, random_state=None):
        if random_state is not None:
            random.seed(random_state)
        # Генерация данных для задачи
        stations = ["A", "B", "C", "D", "E", "F", "G", "H"]
        stations = stations[:num_stations]
        loading_points = list(range(1, num_loading_points + 1))
        supply = {station: random.randint(50, 100) for station in stations}
        demand = {point: random.randint(40, 90) for point in loading_points}
        if open_type:
            costs = {(i, j): random.randint(1, 10) for i in stations for j in loading_points}
        else:
            costs = {(i, j): random.randint(1, 10) for i in stations for j in loading_points if random.randint(0, 1)}

        problem_text = self.__generate_transportation_problem_text(stations, loading_points, supply, demand, costs)

        return (problem_text, [num_stations + num_loading_points - 1])

    def part_2_task_four(self, num_tasks=1000):
        tasks = []
        for i in range(num_tasks):
            num_stat = random.randint(3, 6)
            num_load_point = random.randint(3, 6)

            problem_text, total_transports = self.__generate_transportation_problem(num_stat, num_load_point, True)
            tasks.append((problem_text, [total_transports], []))
        return tasks
