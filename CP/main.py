import copy
import random
import numpy
import tkinter as tk
from tkinter import messagebox, filedialog

EPS = 1e-3  # требуемая точность
MAX_ITER = 10000  # максимально допустимое число итераций

# Пробные данные для уравнения A*X = B
# x = [1.10202, 0.99091, 1.01111]

# a = [[10, 1, -1],   # 10*x1 + x2    - x3    = 11
#      [1, 10, -1],   # x1    + 10*x2 - x3    = 10
#      [-1, 1, 10]]   # -x1   + x2    + 10*x3 = 10
#
# b = [11, 10, 10]

# a = [[8, 1, 1],   # 10*x1 + x2    - x3    = 11
#      [1, 5, -1],   # x1    + 10*x2 - x3    = 10
#      [1, -1, 5]]   # -x1   + x2    + 10*x3 = 10
#
# b = [26, 7, 7]

def about_btn():
    from PIL import ImageTk, Image

    filewin = tk.Toplevel(root)
    img = ImageTk.PhotoImage(Image.open("me.png"))
    about_photo_lbl = tk.Label(filewin, image=img)
    about_photo_lbl.grid(row=0)

    about_name_lbl = tk.Label(filewin, text="Vadim Dmitriev", font='Helvetica 18 bold')
    about_name_lbl.grid(row=1)

    about_description_lbl = tk.Label(filewin, text="I spent an hour on this screen")
    about_description_lbl.grid(row=2)

    about_description_lbl = tk.Label(filewin, text="(c) 2022-2022 State University of Aerospace Instrumentation.")
    about_description_lbl.grid(row=3)

    filewin.mainloop()


def import_btn():
    filename = str()
    def open_file():
        global filename
        filename = filedialog.askopenfilename()
        file = open(filename, 'r')
        data = file.read()
        textWidget.delete(1.0, "end")
        textWidget.insert(1.0, data)
        file.close()

    def write_file(x):
        # file = open("[solved].txt"+filename, 'w')
        file = open("solved.txt", 'w')
        file.write(x)
        file.close()

    def solve_file():
        data = textWidget.get("0.0", "end")
        lines = data.split("\n")[:-1]
        a = numpy.zeros((len(lines), len(lines)))
        b = [0 for i in range(len(lines))]
        rows = 0
        try:
            for line in lines:
                nums = line.split()
                if len(lines) != len(nums)-1:
                    raise Exception("Матрица не квадратная")

                columns = 0
                for num in nums:
                    if columns == len(nums)-1:
                        b[rows] = int(num)
                    else:
                        a[rows][columns] = int(num)
                    columns += 1
                rows += 1
        except Exception as ex:
            print(type(ex).__name__, ex.args)
            messagebox.showinfo(type(ex).__name__, ex.args[0])
        else:
            # print(a, b)
            x, n = solution(a, b)
            write_file(str(x))


    newin = tk.Toplevel(root)
    textWidget = tk.Text(newin)
    textWidget.grid(row=3, column=0, columnspan=10)
    open_file()

    eps_lbl = tk.Label(newin, text="Точность решения")
    eps_lbl.grid(row=0, column=0, columnspan=2)
    eps_ent = tk.Entry(newin, width=5)
    eps_ent.insert(0, "3")
    eps_ent.grid(row=0, column=2)
    eps_lbl = tk.Label(newin, text="знаков")
    eps_lbl.grid(row=0, column=3)

    solve_btn = tk.Button(newin, text="Решить", command=solve_file)
    solve_btn.grid(row=0, column=5)

    newin.mainloop()

def export_btn():
    # filewin = tk.Toplevel(root)
    # img = ImageTk.PhotoImage(Image.open("me.png"))
    # about_photo_lbl = tk.Label(filewin, image=img)
    # about_photo_lbl.grid(row=0)
    #
    # about_name_lbl = tk.Label(filewin, text="Vadim Dmitriev", font='Helvetica 18 bold')
    # about_name_lbl.grid(row=1)
    #
    # about_description_lbl = tk.Label(filewin, text="I spent an hour on this screen")
    # about_description_lbl.grid(row=2)
    #
    # about_description_lbl = tk.Label(filewin, text="(c) 2022-2022 State University of Aerospace Instrumentation.")
    # about_description_lbl.grid(row=3)
    #
    # filewin.mainloop()
    print("bye")

def print_SLAE(a, b):
    for row in range(0, len(a)):
        for column in range(0, len(b)):
            print(f"{abs(a[row][column]):.0f}*x{column + 1}", end=" ")
            if column != len(b) - 1:
                if a[row][column + 1] > 0:
                    print(f"+", end=" ")
                else:
                    print(f"-", end=" ")
        print(f"= {b[row]:.0f}")


def rand_gen(n):
    a = numpy.zeros((n, n))
    for row in range(0, n):
        for column in range(0, n):
            if row != column:
                a[row][column] = random.randint(-100, 100)
        a[row][row] = sum(abs(a[row])) + 1
    b = [random.randint(-100, 100) for i in range(n)]
    return a, b


# Проверка матрицы коэффициентов на корректность
def isCorrectArray(a, b):
    for row in range(0, len(a)):
        if len(a[row]) != len(b):
            print('Не соответствует размерность')
            return False

        if a[row][row] == 0:
            print('Нулевые элементы на главной диагонали')
            return False

        if a[row][row] < sum(abs(a[row])-abs(a[row][row])):
            print('Не выполнено условие сходимости')
            return False
    return True


# Условие завершения программы
def isEnough(x_old, x_new):
    for k in range(0, len(x_old)):
        dif = x_new[k] - x_old[k]
        if abs(dif) > EPS:
            return False
    return True


def toNormal(a, b):
    matrix = numpy.zeros((len(a), len(b)))
    for row in range(0, len(a)):
        j = 0
        matrix[row][j] = b[row] / a[row][row]
        j += 1
        for column in range(0, len(a[row])):
            if row != column:
                matrix[row][j] = -a[row][column] / a[row][row]
                j += 1
    return matrix


# Процедура решения
def solution(a, b):
    if not isCorrectArray(a, b):
        print('Ошибка в исходных данных')
    else:
        SLAE = toNormal(a, b)
        count = len(b)  # количество корней

        x = [SLAE[i][0] for i in range(0, count)]  # начальное приближение корней

        numberOfIter = 0  # подсчет количества итераций
        while (numberOfIter < MAX_ITER):

            x_prev = copy.deepcopy(x)

            for row in range(0, len(a)):
                j = 0
                x[row] = SLAE[row][0]
                j += 1
                for column in range(0, len(a[row])):
                    if row != column:
                        tmp = SLAE[row][j] * x_prev[column]
                        x[row] += tmp
                        j += 1

            if isEnough(x_prev, x):  # проверка на выход
                break

            numberOfIter += 1

        print('Количество итераций на решение: ', numberOfIter)

        return x, numberOfIter


def check(a, b, x):
    for row in range(0, len(a)):
        res = 0
        for column in range(0, len(a[row])):
            res += a[row][column] * x[column]
        tmp = abs(res - b[row])
        cop = EPS * sum(abs(a[row]))
        if tmp > cop:
            # print('решение не сходится')
            return False
    return True


# MAIN - блок программмы

root = tk.Tk()
root.title("Решение СЛАУ методом последовательных итераций")
# root.geometry("850x200")

root.columnconfigure(7, weight=1)
root.rowconfigure(8, weight=1)

eq1_lbl = tk.Label(root, text="Уравнение 1")
eq1_lbl.grid(row=0, column=0)
eq2_lbl = tk.Label(root, text="Уравнение 2")
eq2_lbl.grid(row=2, column=0, pady=(20, 0))
eq3_lbl = tk.Label(root, text="Уравнение 3")
eq3_lbl.grid(row=4, column=0, pady=(20, 0))

eps1_lbl = tk.Label(root, text="Точность решения")
eps1_lbl.grid(row=6, column=0, columnspan=2, pady=(20, 0))
eps_ent = tk.Entry(root, width=5)
eps_ent.insert(0, "3")
eps_ent.grid(row=6, column=2, pady=(20, 0))
eps2_lbl = tk.Label(root, text="знаков")
eps2_lbl.grid(row=6, column=3, pady=(20, 0))

eq1X_lbl = tk.Label(root, text="X +")
eq1X_lbl.grid(row=1, column=1)
eq1Y_lbl = tk.Label(root, text="Y +")
eq1Y_lbl.grid(row=1, column=3)
eq1Z_lbl = tk.Label(root, text="Z +")
eq1Z_lbl.grid(row=1, column=5)
eq1X_ent = tk.Entry(root, width=5)
eq1X_ent.grid(row=1, column=0)
eq1Y_ent = tk.Entry(root, width=5)
eq1Y_ent.grid(row=1, column=2)
eq1Z_ent = tk.Entry(root, width=5)
eq1Z_ent.grid(row=1, column=4)
eq1B_ent = tk.Entry(root, width=5)
eq1B_ent.grid(row=1, column=6)

eq2X_lbl = tk.Label(root, text="X +")
eq2X_lbl.grid(row=3, column=1)
eq2Y_lbl = tk.Label(root, text="Y +")
eq2Y_lbl.grid(row=3, column=3)
eq2Z_lbl = tk.Label(root, text="Z +")
eq2Z_lbl.grid(row=3, column=5)
eq2X_ent = tk.Entry(root, width=5)
eq2X_ent.grid(row=3, column=0)
eq2Y_ent = tk.Entry(root, width=5)
eq2Y_ent.grid(row=3, column=2)
eq2Z_ent = tk.Entry(root, width=5)
eq2Z_ent.grid(row=3, column=4)
eq2B_ent = tk.Entry(root, width=5)
eq2B_ent.grid(row=3, column=6)

eq3X_lbl = tk.Label(root, text="X +")
eq3X_lbl.grid(row=5, column=1)
eq3Y_lbl = tk.Label(root, text="Y +")
eq3Y_lbl.grid(row=5, column=3)
eq3Z_lbl = tk.Label(root, text="Z +")
eq3Z_lbl.grid(row=5, column=5)
eq3X_ent = tk.Entry(root, width=5)
eq3X_ent.grid(row=5, column=0)
eq3Y_ent = tk.Entry(root, width=5)
eq3Y_ent.grid(row=5, column=2)
eq3Z_ent = tk.Entry(root, width=5)
eq3Z_ent.grid(row=5, column=4)
eq3B_ent = tk.Entry(root, width=5)
eq3B_ent.grid(row=5, column=6)

res_lbl = tk.Label(root, text="Результаты")
res_lbl.grid(row=7, column=0)
resX_lbl = tk.Label(root, text="X =")
resX_lbl.grid(row=7, column=1)
resY_lbl = tk.Label(root, text="Y =")
resY_lbl.grid(row=7, column=3)
resZ_lbl = tk.Label(root, text="Z =")
resZ_lbl.grid(row=7, column=5)

resX_ent = tk.Label(root)
resX_ent.grid(row=7, column=2)
resY_ent = tk.Label(root)
resY_ent.grid(row=7, column=4)
resZ_ent = tk.Label(root)
resZ_ent.grid(row=7, column=6)


def start():
    global EPS
    try:
        a = numpy.zeros((3, 3))
        b = [0 for i in range(3)]
        a[0][0] = int(eq1X_ent.get())
        a[0][1] = int(eq1Y_ent.get())
        a[0][2] = int(eq1Z_ent.get())
        b[0] = int(eq1B_ent.get())

        a[1][0] = int(eq2X_ent.get())
        a[1][1] = int(eq2Y_ent.get())
        a[1][2] = int(eq2Z_ent.get())
        b[1] = int(eq2B_ent.get())

        a[2][0] = int(eq3X_ent.get())
        a[2][1] = int(eq3Y_ent.get())
        a[2][2] = int(eq3Z_ent.get())
        b[2] = int(eq3B_ent.get())

        EPS = int(eps_ent.get())
        if EPS <= 0:
            raise Exception("Точность — положительное целое число")
        if EPS > 15:
            raise Exception("Точность — слишком высокая(>= 15)")
        EPS = 10 ** -EPS
    except Exception as ex:
        print(type(ex).__name__, ex.args)
        if type(ex).__name__ == "ValueError" and "invalid literal for int() with base 10" in ex.args[0]:
            if "\'\'" in ex.args[0]:
                messagebox.showinfo("Ошибка", "Заполните все поля!")
            elif "." in ex.args[0]:
                messagebox.showinfo("Ошибка", "Заполните все поля целыми числами!")
            else:
                messagebox.showinfo("Ошибка", "Заполните все поля числами!")
        elif "Точность" in ex.args[0]:
            if "положительное целое число" in ex.args[0]:
                messagebox.showinfo("Ошибка", "Точность должна быть целым положительным числом!")
            elif "слишком высокая" in ex.args[0]:
                messagebox.showinfo("Ошибка", "Точность не должна быть больше 15 знаков!")

        else:
            messagebox.showinfo("Ошибка", "Заполните поля правильно!")
    else:
        x, num = solution(a, b)

        resX_ent.config(text=str(round(x[0], 3)))
        resY_ent.config(text=str(round(x[1], 3)))
        resZ_ent.config(text=str(round(x[2], 3)))

        if check(a, b, x):
            check_lbl.config(text="✅  Сходится")
        else:
            check_lbl.config(text="❌ Не сходится")

        if num % 10 == 0 or num % 10 > 4:
            iter_lbl.config(text=f"({num} итераций)")
        elif num % 10 == 1:
            iter_lbl.config(text=f"({num} итерация)")
        elif num % 10 <= 4:
            iter_lbl.config(text=f"({num} итерации)")


def fill():
    def change_text(text):
        text.delete(0, tk.END)
        text.insert(0, random.randint(-100, 100))

    def change_diagonal_text(text, value):
        text.delete(0, tk.END)
        text.insert(0, value)

    check_lbl.config(text="")
    iter_lbl.config(text="")

    change_text(eq1Y_ent)
    change_text(eq1Z_ent)
    change_text(eq1B_ent)
    change_diagonal_text(eq1X_ent, abs(int(eq1Y_ent.get())) + abs(int(eq1Z_ent.get())) + 1)

    change_text(eq2X_ent)
    change_text(eq2Z_ent)
    change_text(eq2B_ent)
    change_diagonal_text(eq2Y_ent, abs(int(eq2X_ent.get())) + abs(int(eq2Z_ent.get())) + 1)

    change_text(eq3X_ent)
    change_text(eq3Y_ent)
    change_text(eq3B_ent)
    change_diagonal_text(eq3Z_ent, abs(int(eq3X_ent.get())) + abs(int(eq3Y_ent.get())) + 1)


fill_btn = tk.Button(root, text="Заполнить", command=fill)
fill_btn.grid(row=5, column=7)
solve_btn = tk.Button(root, text="Решить", command=start)
solve_btn.grid(row=7, column=7)
check_lbl = tk.Label(root)
check_lbl.grid(row=0, column=7)
iter_lbl = tk.Label(root)
iter_lbl.grid(row=1, column=7)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Импорт", command=import_btn)
filemenu.add_command(label="Экспорт", command=export_btn)
filemenu.add_separator()
filemenu.add_command(label="О программе", command=about_btn)
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="Файл", menu=filemenu)

root.config(menu=menubar)

root.mainloop()
