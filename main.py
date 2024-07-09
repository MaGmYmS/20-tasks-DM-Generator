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


def merge_text_files(input_folder, output_folder, output_filename):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Initialize an empty string to hold the combined contents
    combined_contents = ""

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Construct the full file path
        file_path = os.path.join(input_folder, filename)

        # Check if the file is a text file
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            # Read the contents of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                combined_contents += file.read() + '\n\n\n'

    # Construct the full output file path
    output_file_path = os.path.join(output_folder, output_filename)

    # Write the combined contents to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(combined_contents)


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
        "lecture_1_task_combinatorics_one": "Задание 1. ТерВер 1. Лекция 1",
        "lecture_1_task_combinatorics_two": "Задание 2. ТерВер 2. Лекция 1",
        "lecture_1_task_combinatorics_three": "Задание 3. ТерВер 3. Лекция 1",
        "lecture_1_task_combinatorics_four": "Задание 4. ТерВер 4. Лекция 1",
        "lecture_1_task_combinatorics_five": "Задание 5. ТерВер 5. Лекция 1",
        "lecture_2_probability_of_value": "Задание 6. ТерВер 6. Лекция 2",
        "lecture_3_expected_value": "Задание 7. ТерВер 7. Лекция 3",

        "lecture_4_task_combinatorics_one": "Задание 8. ТерВер 8. Лекция 4",
        "lecture_4_task_combinatorics_two": "Задание 9. ТерВер 9. Лекция 4",
        "lecture_4_task_combinatorics_three": "Задание 10. ТерВер 10. Лекция 4",
        "lecture_4_task_combinatorics_four": "Задание 11. ТерВер 11. Лекция 4",
        "lecture_4_task_combinatorics_five": "Задание 12. ТерВер 12. Лекция 4",
        "lecture_4_task_combinatorics_six": "Задание 13. ТерВер 13. Лекция 4",
        "lecture_4_task_combinatorics_seven": "Задание 14. ТерВер 14. Лекция 4",
        "lecture_4_task_combinatorics_eight": "Задание 15. ТерВер 15. Лекция 4",
        "lecture_4_task_combinatorics_ten": "Задание 16. ТерВер 16. Лекция 4",

        "control_work_task_combinatorics_dice": "Задание 17. ТерВер 17. Контрольная работа 5",
        "control_work_task_combinatorics_1_2": "Задание 18. ТерВер 18. Контрольная работа 5",
        "control_work_task_combinatorics_1_3": "Задание 19. ТерВер 19. Контрольная работа 5",
        "control_work_task_combinatorics_moscow": "Задание 20. ТерВер 20. Контрольная работа 5",
        "control_work_task_combinatorics_stud": "Задание 21. ТерВер 21. Контрольная работа 5",
        "control_work_task_combinatorics_man": "Задание 22. ТерВер 22. Контрольная работа 5",
        "control_work_task_combinatorics_dice_2": "Задание 23. ТерВер 23. Контрольная работа 5",

        "lecture_6_task_combinatorics_one": "Задание 24. Выборка и генеральная совокупность 24. Лекция 6",
        "lecture_6_task_combinatorics_two": "Задание 25. Выборка и генеральная совокупность 24. Лекция 6",
        "lecture_6_task_combinatorics_three": "Задание 26. Выборка и генеральная совокупность 24. Лекция 6",
        "lecture_6_task_combinatorics_four": "Задание 27. Выборка и генеральная совокупность 24. Лекция 6",
        "lecture_6_task_combinatorics_five": "Задание 28. Свойства статистических оценок 25. Лекция 7",
        "lecture_6_task_combinatorics_six": "Задание 29. Свойства статистических оценок 25. Лекция 7",
        "lecture_6_task_combinatorics_seven": "Задание 30. Свойства статистических оценок 25. Лекция 7",
        "lecture_6_task_combinatorics_eight": "Задание 31. Свойства статистических оценок 25. Лекция 7",
        "lecture_6_task_combinatorics_nine": "Задание 32. Числовые характеристики выборки 26. Лекция 7",
        "lecture_6_task_combinatorics_ten": "Задание 33. Числовые характеристики выборки 26. Лекция 7",

        "lecture_7_task_combinatorics_one": "Задание 34. Проверка статистических гипотез 27. Лекция 8",
        "lecture_7_task_combinatorics_two": "Задание 35. Проверка статистических гипотез 27. Лекция 8",
        "lecture_7_task_combinatorics_three": "Задание 36. Проверка статистических гипотез 27. Лекция 8",
        "lecture_7_task_combinatorics_four": "Задание 37. Проверка статистических гипотез 27. Лекция 8",
        "lecture_7_task_combinatorics_five": "Задание 38. Проверка статистических гипотез 27. Лекция 8",
        "lecture_7_task_combinatorics_six": "Задание 39. Проверка статистических гипотез 27. Лекция 8",
        "lecture_7_task_combinatorics_seven": "Задание 40. Проверка статистических гипотез 27. Лекция 8",
        "lecture_7_task_combinatorics_eight": "Задание 41. Проверка статистических гипотез 27. Лекция 8",
        "lecture_7_task_combinatorics_nine": "Задание 42. Проверка статистических гипотез 27. Лекция 8",
        "lecture_7_task_combinatorics_ten": "Задание 43. Проверка статистических гипотез 27. Лекция 8",

        "file_1_task_1_generate_bernoulli_variance_tasks": "Задание 44. ТерВер 28. Файл 1_1.",
        "file_1_task_2_generate_binomial_expectation_tasks": "Задание 45. ТерВер 28. Файл 1_2.",
        "file_1_task_3_generate_binomial_variance_tasks": "Задание 46. ТерВер 28. Файл 1_3.",
        "file_1_task_4_generate_binomial_probability_tasks": "Задание 47. ТерВер 28. Файл 1_4.",
        "file_1_task_5_generate_poisson_probability_tasks": "Задание 48. ТерВер 29. Файл 1_5.",
        "file_1_task_6_generate_geometric_expectation_tasks": "Задание 49. ТерВер 29. Файл 1_6.",
        "file_1_task_7_generate_geometric_variance_tasks": "Задание 50. ТерВер 29. Файл 1_7.",
        "file_1_task_8_generate_geometric_variance_tasks": "Задание 51. ТерВер 29. Файл 1_8.",

        "file_2_task_1_generate_sample_mode_tasks": "Задание 52. ТерВер 30. Файл 2_1.",
        "file_2_task_2_generate_sample_median_tasks": "Задание 53. ТерВер 30. Файл 2_2.",
        "file_2_task_3_generate_sample_variance_tasks": "Задание 53. ТерВер 30. Файл 2_3.",
        "file_2_task_4_generate_corrected_standard_deviation_tasks": "Задание 54. ТерВер 30. Файл 2_4.",
        "file_2_task_5_generate_sample_variance_tasks": "Задание 55. ТерВер 30. Файл 2_5.",

        "file_3_task_1": "Задание 56. ТерВер 31. Файл 3_1.",
        "file_3_task_2": "Задание 57. ТерВер 31. Файл 3_2.",
        "file_3_task_3": "Задание 58. ТерВер 31. Файл 3_3.",
        "file_3_task_4": "Задание 59. ТерВер 31. Файл 3_4.",
        "file_3_task_5": "Задание 60. ТерВер 31. Файл 3_5.",
        "file_3_task_6": "Задание 61. ТерВер 31. Файл 3_6.",
        "file_3_task_7": "Задание 62. ТерВер 31. Файл 3_7.",
        "file_3_task_8": "Задание 63. ТерВер 31. Файл 3_8.",
        "file_3_task_9": "Задание 64. ТерВер 31. Файл 3_9.",
        "file_3_task_10": "Задание 65. ТерВер 31. Файл 3_10.",
        "file_3_task_11": "Задание 66. ТерВер 31. Файл 3_11.",
        "file_3_task_12": "Задание 67. ТерВер 31. Файл 3_12.",
        "file_3_task_13": "Задание 68. ТерВер 31. Файл 3_13.",
        "file_3_task_14": "Задание 69. ТерВер 31. Файл 3_14.",
        "file_3_task_15": "Задание 70. ТерВер 31. Файл 3_15.",
        "file_3_task_16": "Задание 71. ТерВер 31. Файл 3_16.",

        "file_4_task_1": "Задание 72. ТерВер 32. Файл 4_1.",
        "file_4_task_2": "Задание 73. ТерВер 32. Файл 4_2.",
        "file_4_task_3": "Задание 74. ТерВер 32. Файл 4_3.",
        "file_4_task_4": "Задание 75. ТерВер 32. Файл 4_4.",
        "file_4_task_5": "Задание 76. ТерВер 32. Файл 4_5.",
        "file_4_task_6": "Задание 77. ТерВер 32. Файл 4_6.",
        "file_4_task_7": "Задание 78. ТерВер 32. Файл 4_7.",
        "file_4_task_8": "Задание 79. ТерВер 32. Файл 4_8.",
        "file_4_task_9": "Задание 80. ТерВер 32. Файл 4_9.",
        "file_4_task_10": "Задание 81. ТерВер 32. Файл 4_10.",
        "file_4_task_11": "Задание 82. ТерВер 32. Файл 4_11.",
        "file_4_task_12": "Задание 83. ТерВер 32. Файл 4_12.",
        "file_4_task_13": "Задание 84. ТерВер 32. Файл 4_13.",
        "file_4_task_14": "Задание 85. ТерВер 32. Файл 4_14.",
        "file_4_task_15": "Задание 86. ТерВер 32. Файл 4_15.",
        "file_4_task_16": "Задание 87. ТерВер 32. Файл 4_16.",

        "file_specific_task_star": "Задание 88. ТерВер 33. Задача со звездочкой.",

        # "logic_1_task_combinatorics_one_binomial_newton": "Задание 101. Комбинаторика 1. Бином Ньютона",
        # "logic_1_task_combinatorics_two_recurrence_relation": "Задание 102. Комбинаторика 2. Рекуррентные соотношения.",
        # "logic_1_task_combinatorics_three_recurrence_relation": "Задание 103. Комбинаторика 2. "
        #                                                         "Рекуррентные соотношения.",
        # "logic_1_task_combinatorics_four_koef": "Задание 104. Комбинаторика 3.",
        # "logic_1_task_combinatorics_five_distribution_tickets": "Задание 105. Комбинаторика 4.",
        # "logic_1_task_combinatorics_six_different_gender_pairs": "Задание 106. Комбинаторика 5.",
        # "logic_1_task_combinatorics_seven_digits": "Задание 107. Комбинаторика 6.",
        # "logic_1_task_combinatorics_eight_soldier": "Задание 108. Комбинаторика 7.",
        # "logic_1_task_combinatorics_nine_alphabet": "Задание 109. Комбинаторика 8.",
        # "logic_1_task_combinatorics_ten_arithmetic": "Задание 110. Комбинаторика 9.",
        # "logic_1_task_combinatorics_eleven_stirling": "Задание 111. Комбинаторика 10.",
        # "logic_1_task_combinatorics_twelve_cards": "Задание 112. Комбинаторика -1.",
        # "logic_1_task_combinatorics_thirteen_biatlon": "Задание 113. Комбинаторика 11.",
        # "logic_1_task_combinatorics_fourteen_cake": "Задание 114. Комбинаторика 12.",
        # "logic_1_task_combinatorics_fifteen_letter": "Задание 115. Комбинаторика 13.",
        # "logic_1_task_combinatorics_sixteen_profkom": "Задание 116. Комбинаторика 14.",

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

                        combinatorics_gen.lecture_6_task_combinatorics_one,
                        combinatorics_gen.lecture_6_task_combinatorics_two,
                        combinatorics_gen.lecture_6_task_combinatorics_three,
                        combinatorics_gen.lecture_6_task_combinatorics_four,
                        combinatorics_gen.lecture_6_task_combinatorics_five,
                        combinatorics_gen.lecture_6_task_combinatorics_six,
                        combinatorics_gen.lecture_6_task_combinatorics_seven,
                        combinatorics_gen.lecture_6_task_combinatorics_eight,
                        combinatorics_gen.lecture_6_task_combinatorics_nine,
                        combinatorics_gen.lecture_6_task_combinatorics_ten,

                        combinatorics_gen.lecture_7_task_combinatorics_one,
                        combinatorics_gen.lecture_7_task_combinatorics_two,
                        combinatorics_gen.lecture_7_task_combinatorics_three,
                        combinatorics_gen.lecture_7_task_combinatorics_four,
                        combinatorics_gen.lecture_7_task_combinatorics_five,
                        combinatorics_gen.lecture_7_task_combinatorics_six,
                        combinatorics_gen.lecture_7_task_combinatorics_seven,
                        combinatorics_gen.lecture_7_task_combinatorics_eight,
                        combinatorics_gen.lecture_7_task_combinatorics_nine,
                        combinatorics_gen.lecture_7_task_combinatorics_ten,

                        combinatorics_gen.file_1_task_1_generate_bernoulli_variance_tasks,
                        combinatorics_gen.file_1_task_2_generate_binomial_expectation_tasks,
                        combinatorics_gen.file_1_task_3_generate_binomial_variance_tasks,
                        combinatorics_gen.file_1_task_4_generate_binomial_probability_tasks,
                        combinatorics_gen.file_1_task_5_generate_poisson_probability_tasks,
                        combinatorics_gen.file_1_task_6_generate_geometric_expectation_tasks,
                        combinatorics_gen.file_1_task_7_generate_geometric_variance_tasks,
                        combinatorics_gen.file_1_task_8_generate_geometric_variance_tasks,

                        combinatorics_gen.file_2_task_1_generate_sample_mode_tasks,
                        combinatorics_gen.file_2_task_2_generate_sample_median_tasks,
                        combinatorics_gen.file_2_task_3_generate_sample_variance_tasks,
                        combinatorics_gen.file_2_task_4_generate_corrected_standard_deviation_tasks,
                        combinatorics_gen.file_2_task_5_generate_sample_variance_tasks,

                        combinatorics_gen.file_3_task_1,
                        combinatorics_gen.file_3_task_2,
                        combinatorics_gen.file_3_task_3,
                        combinatorics_gen.file_3_task_4,
                        combinatorics_gen.file_3_task_5,
                        combinatorics_gen.file_3_task_6,
                        combinatorics_gen.file_3_task_7,
                        combinatorics_gen.file_3_task_8,
                        combinatorics_gen.file_3_task_9,
                        combinatorics_gen.file_3_task_10,
                        combinatorics_gen.file_3_task_11,
                        combinatorics_gen.file_3_task_12,
                        combinatorics_gen.file_3_task_13,
                        combinatorics_gen.file_3_task_14,
                        combinatorics_gen.file_3_task_15,
                        combinatorics_gen.file_3_task_16,

                        combinatorics_gen.file_4_task_1,
                        combinatorics_gen.file_4_task_2,
                        combinatorics_gen.file_4_task_3,
                        combinatorics_gen.file_4_task_4,
                        combinatorics_gen.file_4_task_5,
                        combinatorics_gen.file_4_task_6,
                        combinatorics_gen.file_4_task_7,
                        combinatorics_gen.file_4_task_8,
                        combinatorics_gen.file_4_task_9,
                        combinatorics_gen.file_4_task_10,
                        combinatorics_gen.file_4_task_11,
                        combinatorics_gen.file_4_task_12,
                        combinatorics_gen.file_4_task_13,
                        combinatorics_gen.file_4_task_14,
                        combinatorics_gen.file_4_task_15,
                        combinatorics_gen.file_4_task_16,

                        combinatorics_gen.file_specific_task_star,

                        # combinatorics_gen.logic_1_task_combinatorics_one_binomial_newton,
                        # combinatorics_gen.logic_1_task_combinatorics_two_recurrence_relation,
                        # combinatorics_gen.logic_1_task_combinatorics_three_recurrence_relation,
                        # combinatorics_gen.logic_1_task_combinatorics_four_koef,
                        # combinatorics_gen.logic_1_task_combinatorics_five_distribution_tickets,
                        # combinatorics_gen.logic_1_task_combinatorics_six_different_gender_pairs,
                        # combinatorics_gen.logic_1_task_combinatorics_seven_digits,
                        # combinatorics_gen.logic_1_task_combinatorics_eight_soldier,
                        # combinatorics_gen.logic_1_task_combinatorics_nine_alphabet,
                        # combinatorics_gen.logic_1_task_combinatorics_ten_arithmetic,
                        # combinatorics_gen.logic_1_task_combinatorics_eleven_stirling,
                        # # combinatorics_gen.logic_1_task_combinatorics_twelve_cards,
                        # combinatorics_gen.logic_1_task_combinatorics_thirteen_biatlon,
                        # combinatorics_gen.logic_1_task_combinatorics_fourteen_cake,
                        # combinatorics_gen.logic_1_task_combinatorics_fifteen_letter,
                        # combinatorics_gen.logic_1_task_combinatorics_sixteen_profkom,
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


# create_all_tasks_combinatorics()
input_files = r"D:\я у мамы программист\Проект ТП\graph_generator_tasks_1_15\input_combined_file"
output_files = r"D:\я у мамы программист\Проект ТП\graph_generator_tasks_1_15\output_combined_file"
merge_text_files(input_files, output_files, 'Категория 16.txt')
