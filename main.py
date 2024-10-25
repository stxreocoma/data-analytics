import data
import tasks
import pandas as pd

if __name__ == '__main__':
    filepath = "Product_Gallery.xlsx"
    df = data.Open(filepath)
    if df is not None:
        task_list = [
            tasks.task1(df),
            tasks.task2(df),
            tasks.task3(df),
            tasks.task4(df),
            tasks.task5(df),
            tasks.task6(df),
            tasks.task7(df),
            tasks.task8(df),
            tasks.task9(df),
            tasks.task10(df),
            tasks.task11(df),
            tasks.task12(df),
            tasks.task13(df),
            tasks.task14(df),
            tasks.task15(df),
            tasks.task16(df),
            tasks.task17(df),
            tasks.task18(df),
            tasks.task19(df),
            tasks.task20(df),
            tasks.task21(df),
            tasks.task22(df),
            tasks.task23(df)
        ]

        for task in task_list:
            task(df)
    else:
        print("Something went wrong")