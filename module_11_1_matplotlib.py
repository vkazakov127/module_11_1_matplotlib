# -*- coding: utf-8 -*-
# module_11_1_matplotlib.py
"""
Пример использования matplotlib.widgets
Button — кнопки "Очистить", "Показать"
CheckButtons — Флажки, 2 шт.
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, CheckButtons


class MyPlotter():

    def __init__(self, x_min, x_max, x_num):
        self.x_min = x_min  # Минимальное значение по оси Х
        self.x_max = x_max  # Максимальное значение по оси Х
        self.x_num = x_num  # Количество точек по оси Х

    def my_plot(self, plot_axes):
        """ График на осях 'my_axes' """
        plot_axes.clear()  # Сначала очистить область графика
        global box_checked_list
        # ------------------------
        # Если отмечен "Флажок1" —> показать "Функцию №1"
        if box_checked_list[0]:
            x = np.linspace(self.x_min, self.x_max, self.x_num)
            y = my_function(x)
            plot_axes.plot(x, y, "r")   # "r" — цвет "red"
            # Нарисовать график
            plt.draw()
        # ------------------------
        # Если отмечен "Флажок2" —> показать "Функцию №2"
        if box_checked_list[1]:
            x = np.linspace(self.x_min, self.x_max, self.x_num)
            y = my_function2(x)
            plot_axes.plot(x, y, "b")   # "b" — цвет "blue"
            # Нарисовать график
            plt.draw()
        # Сетка на графике
        plot_axes.grid()
        plot_axes.set_title(axes_title)
        plt.draw()


def clear_button_clicked(event):
    """ Обработчик события для кнопки 'Очистить' """
    graph_axes.clear()
    graph_axes.set_title(axes_title)
    plt.draw()


def show_button_clicked(event):
    """ Обработчик события для кнопки 'Показать' """
    my_plt.my_plot(graph_axes)


def check_box_clicked(event):
    global box_checked_list
    box_checked_list = checkbox1.get_status()


def my_function(x):
    """ Отображаемая функция """
    return ((np.log(abs(1 / np.sin(x)))) ** np.cos(x)) * np.sin(x)


def my_function2(x):
    """ Отображаемая функция """
    return 0.5 * np.sin(x + 4)


if __name__ == "__main__":
    # Настройки графика
    x_min1 = 0.1  # Минимальное значение по оси Х
    x_max1 = 25  # Максимальное значение по оси Х
    x_num1 = 250  # Количество точек на оси Х
    box_checked_list = [True, True]  # Предустановленные флажки
    axes_title = "Пример использования matplotlib.widgets"
    # Мой экземпляр графика
    my_plt = MyPlotter(x_min1, x_max1, x_num1)
    # -------------------
    # Окно с графиком
    fig, graph_axes = plt.subplots()
    # Оси графика с сеткой
    graph_axes.grid()
    # Область графика
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.2)
    # Собственно график
    my_plt.my_plot(graph_axes)
    # ------ Виджеты из Matplotlib -------------
    # Кнопка "Очистить"
    # Оси для кнопки
    clear_button_axes = plt.axes([0.7, 0.05, 0.25, 0.075])
    clear_button = Button(clear_button_axes, 'Очистить')
    # Событие нажатия кнопки
    clear_clicked_id = clear_button.on_clicked(clear_button_clicked)
    # -------------------
    # Кнопка "Показать"
    # Оси для кнопки
    show_button_axes = plt.axes([0.4, 0.05, 0.25, 0.075])
    show_button = Button(show_button_axes, 'Показать')
    # Событие нажатия кнопки
    show_clicked_id = show_button.on_clicked(show_button_clicked)
    # -------------------
    # Флажки, 2 шт.
    # Оси для флажков
    checkbox_axes = plt.axes([0.1, 0.05, 0.25, 0.075])
    # Флажки, 2 шт.
    labels_list = ["Функция 1", "Функция 2"]
    box_checked_list = [True, True]
    checkbox1 = CheckButtons(checkbox_axes, labels_list, box_checked_list)
    # Событие Флажков
    show_clicked_id = checkbox1.on_clicked(check_box_clicked)
    # -------------------
    plt.show()
    print('----------- The End -----------')
