import os
import shutil
import time

from Graph_finaly_version_2 import Graph


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


def create_all_tasks():
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


create_all_tasks()

