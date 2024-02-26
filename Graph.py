import os
import random
import zipfile

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


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

    def __graph_generator(self):
        """
        Метод, который создает граф с минимальным и максимальным количеством ребер из вершин
        :return:
        """
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

    @staticmethod
    def dijkstra(graph, start):
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
        count = 0
        # for edge in draw_graph.edges():
        #     node1, node2 = edge
        #     point1, point2 = pos[node1], pos[node2]
        #     for edge2 in draw_graph.edges():
        #         if edge2 != edge:
        #             node3, node4 = edge2
        #             point3, point4 = pos[node3], pos[node4]
        #             print(node1, node2, node3, self.are_points_collinear(point1, point2, point3))
        #             count += 1
        # print(count, len(draw_graph.edges()))

        # for node1, point1 in pos.items():
        #     for node2, point2 in pos.items():
        #         for node3, point3 in pos.items():
        #             node_set = {node1, node2, node3}
        #             if len(node_set) == 3:
        #                 x_mean = (point1[0] + point2[0] + point3[0]) / 3
        #                 y_mean = (point1[1] + point2[1] + point3[1]) / 3
        #                 if abs(x_mean) < 0.1 or abs(y_mean) < 0.1:
        #                     print(node1, node2, node3, x_mean, y_mean)

        # for node1, (x_coord1, y_coord1) in pos.items():
        #     for node2, (x_coord2, y_coord2) in pos.items():
        #         for node3, (x_coord3, y_coord3) in pos.items():
        #             node_set = {node1, node2, node3}
        #             if len(node_set) == 3:
        #                 left_fraction = (y_coord1 - y_coord2) / (y_coord2 - y_coord3)
        #                 right_fraction = (x_coord1 - x_coord2) / (x_coord2 - x_coord3)
        #                 if abs(left_fraction - right_fraction) < 0.2:
        #                     # print(node1, node2, node3, left_fraction - right_fraction)
        #                     plt.close()
        #                     self.paintilovka(choice_values, choice_orientation)

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
    def create_txt_file(tasks_massive, type_of_response, name_of_the_questions, file_name):
        """
        Метод, создающий txt файл c задачами
        :param tasks_massive: массив задач в формате (вопрос, ответ)
        :param type_of_response: переменная, отвечающая за тип ответа
        :return:
        """
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "folder_tasks")
        file_path = os.path.join(downloads_path, file_name + ".txt")
        result_string = ""

        if len(tasks_massive[0]) == 4:
            for i, (task, answer, forbidden_answer, path_to_graph_img) in enumerate(tasks_massive):
                construction_of_the_image_output_in_gift_format = str.format('<img src\="@@PLUGINFILE@@/{0}"/>',
                                                                             path_to_graph_img)
                tasks_with_graph = task.replace("graph_img", construction_of_the_image_output_in_gift_format)
                tasks_massive[i] = (tasks_with_graph, answer, forbidden_answer)
            # tasks_massive = [row[:2] for row in tasks_massive]

        with open(file_path, "w", encoding="utf-8") as file:
            match type_of_response:
                case 1:  # краткий ответ
                    for task, answer, forbidden_answer in tasks_massive:
                        result_answer_str = ""
                        for ans in answer:
                            result_answer_str += f"={ans}\n"
                        result_string += f"::{name_of_the_questions}::" + task + " {" + result_answer_str + "} " + "\n" + "\n"
                    file.write(result_string)

                case 2:  # множественный выбор, один ответ
                    for task, answer, forbidden_answer in tasks_massive:
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
                        all_answers = forbidden_answer.copy()
                        all_answers.append(answer)
                        random.shuffle(all_answers)
                        string_answer = ""
                        for value in all_answers:
                            if value == answer:
                                string_answer += f"={value}\n"
                            else:
                                string_answer += f"~{value}\n"
                        result_string += f"::{name_of_the_questions}::" + task[0] + " {" + string_answer + "} " + task[
                            1] + "\n" + "\n"
                    file.write(result_string)

                case 5:  # На соответствие
                    pass

        print(f"Файл {file_path} успешно создан.")

    @staticmethod
    def create_zip_file(file_name, *args):
        """
        Метод, создающий zip файл в формате Gift from media formats
        :param args: это расширяемая переменная, содержащая добавляемые в zip файлы
        :return:
        """
        folder_path = os.path.join(os.path.expanduser("~"), "Downloads")
        # Имя архива, который вы хотите создать
        zip_file_name = os.path.join(folder_path, file_name + ".zip")

        # Создаем zip-архив
        with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file in args:
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, relative_path)
                        print(f"Файл {file} добавлен в архив")
                for dir_name in dirs:
                    if dir_name in args:
                        for dir_file in os.listdir(os.path.join(root, dir_name)):
                            file_path = os.path.join(root, dir_name, dir_file)
                            relative_path = os.path.relpath(file_path, folder_path)
                            zipf.write(file_path, relative_path)
                            print(f"Файл {dir_file} добавлен в архив")
        print(f"Архив {zip_file_name} успешно создан.")

    # useless
    def __task_one(self, number_of_tasks, drawing_graph):
        """
        Граф задан следующим образом: <{1,2,3,4,5,6}-множество вершин; {(1,3),
        (2,1), (2,5), (3,2), (4,3), (4,5)}-множество дуг>. Запишите в аналогичной форме
        граф, полученный после удаления вершины 2
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

            task_text = "Граф задан следующим образом: <" + ", ".join(map(str, self.vertices)) + \
                        " -множество вершин; " + ", ".join(map(str, self.edges)) + " -множество дуг>. Запишите в " \
                                                                                   "аналогичной форме граф, полученный после удаления вершины " + str(
                delete_vertex)
            if drawing_graph:
                task_text += "<br/>graph_img"

            answer_text = ", ".join(map(str, result_vertices)) + "-множество вершин; " + \
                          ", ".join(map(str, result_edges)) + "-множество дуг"

            path_to_graph_img = self.paintilovka(False, False)
            result_tasks_massive.append((task_text, answer_text, path_to_graph_img))
        return result_tasks_massive

    def task_two(self, number_of_tasks, drawing_graph, number_forbidden_answer=3):
        """
        Граф задан следующим образом: <{1,2,3,4,5,6}-множество вершин; {(1,3),
        (2,1), (2,5), (3,2), (4,3), (4,5)}-множество дуг>. Выпишите сколько «-1» будет в
        3-й строке матрицы инциденций.
        :param number_of_tasks: количество задач
        :return result_tasks_massive: массив с задачами в формате (вопрос, ответ)
        :return drawing_graph: рисуем или не рисуем граф
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
            task_text = "Граф задан следующим образом: <" + ", ".join(map(str, self.vertices)) + \
                        " -множество вершин; " + ", ".join(map(str, self.edges)) + " -множество дуг>. " \
                                                                                   f"Выпишите сколько «{search_element}» будет в {row_index + 1}-й строке матрицы инциденций."
            answer = incidence_matrix[row_index].count(search_element)

            error_count = 0
            while True:
                forbidden_answer = random.sample(range(0, 10), number_forbidden_answer)
                if answer not in forbidden_answer:
                    break
                error_count += 1
                if error_count % 100 == 0:
                    print(error_count)

            if drawing_graph:
                task_text += "<br/>graph_img"

            path_to_graph_img = self.paintilovka(False, True)
            result_tasks_massive.append((task_text, [answer], forbidden_answer, path_to_graph_img))
        return result_tasks_massive

    def task_three(self, number_of_tasks, drawing_graph, number_forbidden_answer=3):
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
            task_text = "Граф задан следующим образом: <" + ", ".join(map(str, self.vertices)) + \
                        " -множество вершин; " + ", ".join(map(str, self.edges)) + " -множество дуг>. " \
                                                                                   f"Какая из последовательностей соответствует столбцу номер {row_index} матрицы " \
                                                                                   f"смежностей для данного графа. Отсчет стобцов начинается с 0."
            if drawing_graph:
                task_text += "<br/>graph_img"

            answer = "".join([str(value) for value in adjacency_matrix[row_index]])

            forbidden_answer = set()
            while len(forbidden_answer) != number_forbidden_answer:
                tmp_mas = map(str, [random.choice([0, 1]) for _ in range(len(self.vertices))])
                gen_for_ans = "".join(tmp_mas)
                forbidden_answer.add(gen_for_ans)
            forbidden_answer = list(forbidden_answer)

            path_to_graph_img = self.paintilovka(False, False)
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
            vertex_degree = random.randint(5, 10)
            answer = random.randint(5, 15)
            count_edges = vertex_degree * answer
            task_text = f"В однородном графе степень вершины равна {vertex_degree} Число ребер равно {count_edges}. " \
                        f"Найдите число вершин."
            forbidden_answer = [random.choice([answer + i + 1, answer - 1 - i]) for i in range(number_forbidden_answer)]

            result_tasks_massive.append((task_text, [answer], forbidden_answer))
        return result_tasks_massive

    @staticmethod
    def task_five(count_task):
        output_list = []
        for _ in range(count_task):
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
            tmp = (task_text, answer)
            output_list.append(tmp)
        return output_list

    @staticmethod
    def task_six(count_task):
        output_list = []
        for _ in range(count_task):
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
            tmp = (task_text, answer_deleted_nodes)
            output_list.append(tmp)
        return output_list

    @staticmethod
    def __create_n_component_graph(num_vertices, num_components):
        """
        :param num_vertices:  кол-во вершин
        :param num_components:  кол-во компонент, хотя бы на 1 меньше чем  кол-во вершин
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
    def __remove_duplicate_tuples(data):
        """

        :param data:  данные в виде [ ([(1,2), (3,4)],True),([(1,2), (3,4)],False),([(1,2), (3,4)],True), ]
        :return: убираем повторяющиеся  [(1,2), (3,4)] и возвращаем этот же массив
        """
        unique_data = set()
        new_data = []

        for item, flag in data:
            tuple_item = tuple(item)
            if tuple_item not in unique_data:
                unique_data.add(tuple_item)
                new_data.append((list(tuple_item), flag))

        return new_data

    @staticmethod
    def __list_to_string(arr):
        """
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
                f"номера {text_components} графов (в порядке возрастания без пробелов):")

            # region выбираем  сколько правильных ответов хотим негенерить

            arr_choices = []
            count_right_choices = random.randint(1, 4)

            # добавляем правильные ответы
            for j in range(count_right_choices):
                list_edges = self.__create_n_component_graph(count_nodes, component_search)
                tmp = (list_edges, True)
                arr_choices.append(tmp)

            # добавляем НЕправильные ответы
            for j in range(6 - count_right_choices):
                while True:
                    some_num_component = random.randint(1, count_nodes - 1)
                    if some_num_component != component_search:
                        break
                list_edges = self.__create_n_component_graph(count_nodes, some_num_component)
                tmp = (list_edges, False)
                arr_choices.append(tmp)

            arr_choices = self.__remove_duplicate_tuples(arr_choices)
            random.shuffle(arr_choices)
            k = 1
            output_answer = ""
            for arr_edges, acc_answer in arr_choices:
                task_text += "\n"
                task_text += str(k) + " "
                task_text += self.__list_to_string(arr_edges)
                if acc_answer:
                    output_answer += str(k)
                k += 1

            tmp = (task_text, output_answer)
            output_list.append(tmp)

        return output_list

    def task_eight(self, number_of_tasks, drawing_graph: bool, number_forbidden_answer=3):
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

            task_text = "Граф задан следующим образом: <" + ", ".join(map(str, self.vertices)) + \
                        " -множество вершин; " + ", ".join(map(str, self.edges)) + " -множество дуг>. Запишите в " \
                                                                                   "Сколько ребер останется в графе после удаления вершины " + str(
                delete_vertex)
            if drawing_graph:
                task_text += "<br/>graph_img"

            answer_text = len(result_edges)
            while True:
                forbidden_answer = random.sample(range(answer_text // 2, answer_text * 2), number_forbidden_answer)
                if answer_text not in forbidden_answer:
                    break

            path_to_graph_img = self.paintilovka(False, False)
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
        if count_edges < 5:
            return "error"
        for i in range(count_task):
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
            string_task_results = str.format("{0}", total_length)
            # print(min_spanning_tree.edges(data=False))
            path_to_graph_img = self.paintilovka(True, False)
            result_mas.append((string_task, string_task_results, path_to_graph_img))
        return result_mas

    def task_ten(self, count_task, count_edges=7, max_weight=10):
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

            nodes = list(range(1, count_edges + 1))  # Например, от 1 до 8
            edges = set()
            # Добавляем ребра с весами
            # while len(edges) < (count_edges + 1) * 2 - 2:
            #     node1, node2 = random.sample(nodes, 2)
            #     if (node1, node2) not in edges and (node2, node1) not in edges:
            #         edges.add((node1, node2))

            while len(edges) < (count_edges + 1) * 2 - 2:
                node1, node2 = random.sample(nodes, 2)
                if (node1, node2) not in edges and (node2, node1) not in edges:
                    edges.add((node1, node2))

                # Создаём временный граф и проверяем его связность

                temp_digraph = nx.DiGraph(list(edges))
                if nx.is_strongly_connected(temp_digraph):
                    break

            edges_with_random_weights = [(node1, node2, round(random.uniform(1, max_weight))) for node1, node2 in edges]
            self.graph = {(key1, key2): value for key1, key2, value in edges_with_random_weights}
            # создаем пустой граф и заполняем его
            graph = {}
            graph_vis = ""
            for edge in edges_with_random_weights:
                node1, node2, weight = edge
                if node1 not in graph:
                    graph[node1] = {}
                if node2 not in graph:
                    graph[node2] = {}
                graph[node1][node2] = weight
                graph[node2][node1] = weight
            # Вызываем алгоритм дейктсры
            for node1, neighbors in graph.items():
                for node2, weight in neighbors.items():
                    graph_vis += f"\n({node1} и {node2})={weight};"
            shortest_distances, predecessors = self.dijkstra(graph, count_edges)

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
            string_task_results = "{}".format(max_shortest_paths)
            # print(min_spanning_tree.edges(data=False))
            path_to_graph_img = self.paintilovka(True, True)
            result_mas.append((string_task, string_task_results, path_to_graph_img))
        return result_mas

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
            G = nx.DiGraph()

            # Список вершин
            nodes = ['N-ск', 'A', 'B', 'C', 'D', 'E']

            # Добавляем вершины в граф
            G.add_nodes_from(nodes)

            # Генерируем случайные пропускные способности между вершинами
            while not nx.is_strongly_connected(G):
                start = random.choice(nodes)
                end = random.choice(nodes)
                if start != end:
                    capacity = random.randint(1, max_weight)
                    G.add_edge(start, end, capacity=capacity)

            # Добавляем рёбра с пропускными способностями в граф
            # Находим максимальный поток
            max_flow_value, max_flow = nx.maximum_flow(G, 'N-ск', 'E')
            string_task = ("Система автодорог, проходящих через N-скую область, может обеспечить следующие пропускные "
                           "способности измеряемые в тыс. автомашин в час:")
            for start, end, capacity in G.edges(data=True):
                capacity_value = capacity['capacity']
                string_task += f"\nиз города {start} в город {end} - пропускная способность равна {capacity_value}"
            self.graph = {(key1, key2): value for key1, key2, value in G.edges(data='capacity')}
            self.vertices = ['N-ск', 'A', 'B', 'C', 'D', 'E']

            string_task += (
                               "\nВъезд в область осуществляется через город N-ск, а выезд через город Е. Каков максимальный "
                               "поток через эту систему (тыс. автомашин в час)?") + "<br/>graph_img"

            string_task_results = "{}".format(max_flow_value)
            # print(min_spanning_tree.edges(data=False))
            path_to_graph_img = self.paintilovka(True, True)
            result_mas.append((string_task, string_task_results, path_to_graph_img))
        return result_mas

    def task_twelve(self):
        """
        Найти НОД 3 чисел a, b, c используя алгоритм Евклида, при a = 20, b = 56, c = 128
        :return:  массив задач в формате
        """
        resArray_12 = []
        random.seed()

        for i in range(20):
            a = random.randrange(50, 75)
            b = random.randrange(25, 50)
            c = random.randrange(10, 25)
            str = f"Найти НОД 3 чисел a, b, c используя алгоритм Евклида, при a = {a}, b = {b}, c = {c}"
            resArray_12.append([str, self.__NOD_3(a, b, c)])
            # print(resArray_12[i])
        return resArray_12

    def __NOD_3(self, a, b, c):
        """
        Нахождение НОД 3 чисел
        :param a: Первое число
        :param b: Второе число
        :param c: Третье число
        :return:
        """
        return (self.__NOD_2(a, self.__NOD_2(b, c)))

    # return res
    @staticmethod
    def __NOD_2(a, b):
        """
        :param a: Первое число
        :param b: Второе число
        :return: НОД a и b
        """
        ost = -1
        if (a < b):
            k = b
            b = a
            a = k

        # a всегда больше b
        while (ost != 0):
            ost = a % b
            a = b
            b = ost
        return a

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
    def task_thirteen():
        """
        Опреелить является ли число a = 1034 простым
        :return: Массив задач в формате
        """
        resArray_13 = []
        random.seed()
        for i in range(20):
            n = random.randrange(50, 150)
            str = f"Опреелить является ли число a = {n} простым"

            if n % 2 == 0:
                resArray_13.append([str, False])
                continue
            d = 3
            while d * d <= n and n % d != 0:
                d += 2
                if (d * d > n):
                    resArray_13.append([str, True])
                    break
                else:
                    resArray_13.append([str, False])
                    break
        return resArray_13

    @staticmethod
    def task_fourteen():
        """
        C помощью разложения в непрерывную дробь сохратить дробь a/b. При a=4045, b=2002
        :return: Массив задач в формате
        """
        random.seed()
        result = []
        for i in range(20):
            n = random.randrange(10000, 50000)
            d = random.randrange(1000, 9999)
            str = f"C помощью разложения в непрерывную дробь сохратить дробь a/b. При a={n}, b={d}"
            res = []
            while d:
                n, r, d = d, *divmod(n, d)
                res.append(r)
            result.append([str, res])
        return result

    def task_fifteen(self):
        """
        Перевести число a из p-ичной системы счисления в q-ичную. При a = 2054,p = 6,q = 2"
        :return: Массив задач в формате
        """
        resArray_15 = []
        random.seed()
        for i in range(20):
            a = random.randrange(2, 16)
            b = a
            res = 0
            while b == a:
                b = random.randrange(2, 16)
            n_1 = self.__CreateNumber(a)
            str = f"Перевести число a из p-ичной системы счисления в q-ичную. При a = {n_1},p = {a},q = {b}"
            resArray_15.append([str, self.__convert_base(n_1, b, a)])

        return resArray_15
