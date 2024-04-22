import os
import shutil
import time

from Graph_finaly_version_2 import Graph
from Combinatorics import CombinatoricsTaskGenerator


def delete_image_folder():
    folder_path = 'C:\\Users\\user\\Downloads\\folder_tasks\\image_folder'
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
            print(f'Папка {folder_path} успешно удалена.')
        except OSError as e:
            print(f'Ошибка удаления папки {folder_path}: {e}')
    else:
        print(f'Папка {folder_path} не существует.')


def create_all_tasks_graph():
    start_time_all = time.time()

    categories = {
        "task_two": "Задание 2. Графы. Категория 1",
        "task_three": "Задание 3. Графы. Категория 2",
        "task_four": "Задание 4. Графы. Категория 3",
        "task_five_2nd_variation": "Задание 5. Графы. Категория 4",
        "task_six": "Задание 6. Графы. Категория 5",
        "task_seven": "Задание 7. Графы. Категория 6",
        "task_eight": "Задание 8. Графы. Категория 7",
        "task_nine": "Задание 9. Графы. Категория 8",
        "task_ten": "Задание 10. Графы. Категория 9",
        "task_eleven": "Задание 11. Графы. Категория 10 (макс поток)",
        "task_twelve_1": "Задание 12. Арифметика. Категория 2 (НОК)",
        "task_twelve_2": "Задание 13. Арифметика. Категория 1 (НОД)",
        "task_thirteen": "Задание 14. Арифметика. Категория 3 (Простые числа)",
        "task_fourteen": "Задание 15. Арифметика. Категория 4",
        "task_fifteen": "Задание 16. Арифметика. Категория 5",
        "part_2_task_one": "Задание 17. Исследование операций. Категория 1",
        "part_2_task_two": "Задание 18. Исследование операций. Категория 2 (Обходы)",
        "part_2_task_three": "Задание 19. Исследование операций. Категория 3",
        "part_2_task_four": "Задание 20. Исследование операций. Категория 4",
        # Добавьте другие задачи и категории по аналогии
    }

    graph = Graph(6, 2, 3)
    all_tasks_method = [graph.task_two, graph.task_three, graph.task_four, graph.task_five_2nd_variation,
                        graph.task_six, graph.task_seven, graph.task_eight, graph.task_nine, graph.task_ten,
                        graph.task_eleven, graph.task_twelve_1, graph.task_twelve_2, graph.task_thirteen,
                        graph.task_fourteen, graph.task_fifteen, graph.part_2_task_one, Graph(7, 1, 3).part_2_task_two]

    # all_tasks_method = [graph.task_twelve_2]

    categories_dict = {}
    for method in all_tasks_method:
        method_name = method.__name__
        if method_name in categories:
            categories_dict[method_name] = categories[method_name]

    file_dir_name_zipped = []
    for i, method in enumerate(all_tasks_method):
        for number_variables in [1000]:
            start_time = time.time()

            delete_image_folder()

            tasks = method(number_variables)
            file_name = categories_dict[method.__name__]
            question_name = categories_dict[method.__name__]

            if method.__name__ == graph.task_seven.__name__:
                tasks = [task for task in tasks if len(task[1]) != 1]
                graph.create_txt_file(tasks, 3, question_name, file_name)
            else:
                graph.create_txt_file(tasks, 2, question_name, file_name)

            if method.__name__ in [graph.task_two.__name__, graph.task_two.__name__, graph.task_three.__name__,
                                   graph.task_eight.__name__, graph.task_nine.__name__, graph.task_ten.__name__,
                                   graph.task_eleven.__name__, graph.part_2_task_two.__name__]:
                graph.create_zip_file(file_name, "image_folder", file_name + ".txt")
                file_dir_name_zipped.append(file_name + ".zip")
                file_path = f'C:\\Users\\user\\Downloads\\folder_tasks\\{file_name}.txt'
                if os.path.exists(file_path):
                    try:
                        os.remove(file_path)
                        print(f'Файл {file_path} успешно удален.')
                    except OSError as e:
                        print(f'Ошибка удаления файла {file_path}: {e}')
                else:
                    print(f'Файл {file_path} не существует.')
            else:
                file_dir_name_zipped.append(file_name + ".txt")

            end_time = time.time()
            print(f"Время работы программы на {number_variables} вариантах для {method.__name__}:",
                  end_time - start_time)
            print("\n\n\n")

    delete_image_folder()
    print("Запаковываю все файлы в один архив")
    graph.create_zip_file("all_tasks", *file_dir_name_zipped)
    print("Готово")
    end_time_all = time.time()
    print("\n\n\n")
    print(f"Общее время работы программы:", (end_time_all - start_time_all) / 60, "минут")
    print("\n\n\n")


def create_all_tasks_combinatorics():
    start_time_all = time.time()
    graph_2 = Graph()

    categories = {
        "lecture_1_task_combinatorics_one": "Задание 1. Комбинаторика. Категория 1",
        "lecture_1_task_combinatorics_two": "Задание 2. Комбинаторика. Категория 1",
        "lecture_1_task_combinatorics_three": "Задание 3. Комбинаторика. Категория 1",
        "lecture_1_task_combinatorics_four": "Задание 4. Комбинаторика. Категория 1",
        "lecture_1_task_combinatorics_five": "Задание 5. Комбинаторика. Категория 1",
        "lecture_2_probability_of_value": "Задание 6. Комбинаторика. Категория 2",
        "lecture_3_expected_value": "Задание 7. Комбинаторика. Категория 3",

        "lecture_4_task_combinatorics_one": "Задание 8. Комбинаторика. Категория 4",
        "lecture_4_task_combinatorics_two": "Задание 9. Комбинаторика. Категория 4",
        "lecture_4_task_combinatorics_three": "Задание 10. Комбинаторика. Категория 4",
        "lecture_4_task_combinatorics_four": "Задание 11. Комбинаторика. Категория 4",
        "lecture_4_task_combinatorics_five": "Задание 12. Комбинаторика. Категория 4",
        "lecture_4_task_combinatorics_six": "Задание 13. Комбинаторика. Категория 4",
        "lecture_4_task_combinatorics_seven": "Задание 14. Комбинаторика. Категория 4",
        "lecture_4_task_combinatorics_eight": "Задание 15. Комбинаторика. Категория 4",
        "lecture_4_task_combinatorics_ten": "Задание 16. Комбинаторика. Категория 4",

        "control_work_task_combinatorics_dice": "Задание 17. Комбинаторика. Категория 5",
        "control_work_task_combinatorics_1_2": "Задание 18. Комбинаторика. Категория 5",
        "control_work_task_combinatorics_1_3": "Задание 19. Комбинаторика. Категория 5",
        "control_work_task_combinatorics_moscow": "Задание 20. Комбинаторика. Категория 5",
        "control_work_task_combinatorics_stud": "Задание 21. Комбинаторика. Категория 5",
        "control_work_task_combinatorics_man": "Задание 22. Комбинаторика. Категория 5",
        "control_work_task_combinatorics_dice_2": "Задание 23. Комбинаторика. Категория 5",

        "logic_1_task_combinatorics_one_binomial_newton": "Задание 101. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_two_recurrence_relation": "Задание 102. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_three_recurrence_relation": "Задание 103. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_four_koef": "Задание 104. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_five_distribution_tickets": "Задание 105. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_six_different_gender_pairs": "Задание 106. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_seven_digits": "Задание 107. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_eight_soldier": "Задание 108. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_nine_alphabet": "Задание 109. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_ten_arithmetic": "Задание 110. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_eleven_stirling": "Задание 111. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_twelve_cards": "Задание 112. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_thirteen_biatlon": "Задание 113. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_fourteen_cake": "Задание 114. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_fifteen_letter": "Задание 115. Комбинаторика. Категория 11",
        "logic_1_task_combinatorics_sixteen_profkom": "Задание 116. Комбинаторика. Категория 11",

    }

    combinatorics_gen = CombinatoricsTaskGenerator()
    all_tasks_method = [combinatorics_gen.lecture_1_task_combinatorics_one,
                        combinatorics_gen.lecture_1_task_combinatorics_two,
                        combinatorics_gen.lecture_1_task_combinatorics_three,
                        combinatorics_gen.lecture_1_task_combinatorics_four,
                        combinatorics_gen.lecture_1_task_combinatorics_five,
                        combinatorics_gen.lecture_2_probability_of_value,
                        combinatorics_gen.lecture_3_expected_value,

                        combinatorics_gen.lecture_4_task_combinatorics_one,
                        combinatorics_gen.lecture_4_task_combinatorics_two,
                        combinatorics_gen.lecture_4_task_combinatorics_three,
                        combinatorics_gen.lecture_4_task_combinatorics_four,
                        combinatorics_gen.lecture_4_task_combinatorics_five,
                        combinatorics_gen.lecture_4_task_combinatorics_six,
                        combinatorics_gen.lecture_4_task_combinatorics_seven,
                        combinatorics_gen.lecture_4_task_combinatorics_eight,
                        combinatorics_gen.lecture_4_task_combinatorics_ten,

                        combinatorics_gen.control_work_task_combinatorics_dice,
                        combinatorics_gen.control_work_task_combinatorics_1_2,
                        combinatorics_gen.control_work_task_combinatorics_1_3,
                        combinatorics_gen.control_work_task_combinatorics_moscow,
                        combinatorics_gen.control_work_task_combinatorics_stud,
                        combinatorics_gen.control_work_task_combinatorics_man,
                        combinatorics_gen.control_work_task_combinatorics_dice_2,

                        combinatorics_gen.logic_1_task_combinatorics_one_binomial_newton,
                        combinatorics_gen.logic_1_task_combinatorics_two_recurrence_relation,
                        combinatorics_gen.logic_1_task_combinatorics_three_recurrence_relation,
                        combinatorics_gen.logic_1_task_combinatorics_four_koef,
                        combinatorics_gen.logic_1_task_combinatorics_five_distribution_tickets,
                        combinatorics_gen.logic_1_task_combinatorics_six_different_gender_pairs,
                        combinatorics_gen.logic_1_task_combinatorics_seven_digits,
                        combinatorics_gen.logic_1_task_combinatorics_eight_soldier,
                        combinatorics_gen.logic_1_task_combinatorics_nine_alphabet,
                        combinatorics_gen.logic_1_task_combinatorics_ten_arithmetic,
                        combinatorics_gen.logic_1_task_combinatorics_eleven_stirling,
                        combinatorics_gen.logic_1_task_combinatorics_twelve_cards,
                        combinatorics_gen.logic_1_task_combinatorics_thirteen_biatlon,
                        combinatorics_gen.logic_1_task_combinatorics_fourteen_cake,
                        combinatorics_gen.logic_1_task_combinatorics_fifteen_letter,
                        combinatorics_gen.logic_1_task_combinatorics_sixteen_profkom,
                        ]

    categories_dict = {}
    for method in all_tasks_method:
        method_name = method.__name__
        if method_name in categories:
            categories_dict[method_name] = categories[method_name]

    for i, method in enumerate(all_tasks_method):
        for number_variables in [100]:
            start_time = time.time()

            tasks = method(number_variables)
            file_name = categories_dict[method.__name__]
            question_name = categories_dict[method.__name__]

            graph_2.create_txt_file(tasks, 2, question_name, file_name)

            end_time = time.time()
            print(f"Время работы программы на {number_variables} вариантах для {method.__name__}:",
                  end_time - start_time)
            print("\n\n\n")

    print("Готово")
    end_time_all = time.time()
    print("\n\n\n")
    print(f"Общее время работы программы:", (end_time_all - start_time_all) / 60, "минут")
    print("\n\n\n")


create_all_tasks_combinatorics()
