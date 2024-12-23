#  Практика 1.1

nums = [5, 6, 2, 1, 3, 4]

# def bubble_sort(ls):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(ls) - 1):
#             if ls[i] > ls[i +1]:
#                 ls[i], ls[i +1] = ls[i + 1], ls[i]
#                 swapped = True
#
#
# # bubble_sort(nums)
# # print(nums)
#
# def selection_sort(ls):
#     for i in range(len(ls)):
#         lowest = i
#         for j in range(i + 1, len(ls)):
#             if ls[j] < ls[lowest]:
#                 lowest = j
#         ls[i], ls[lowest] = ls[lowest], ls[i]
#
# selection_sort(nums)
# print(nums)
def bubble_sort(ls):
    # чтобы цикл сработал хотя бы один раз, задаем значение переменной True
    swap = True
    while swap:
        swap = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                # меняем элементы местами
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                # меняем значение переменной swap для следующего повтора цикла
                swap = True


def selection_sort(ls):
    # i - количество отсортированных элементов
    for i in range(len(ls)):
        # изначально считаем минимальным первый элемент
        low = i
        # цикл для перебора неотсортированных элементов
        for j in range(i+1, len(ls)):
            if ls[j] < ls[low]:
                low = j
        # самый минимальный элемент меняем с первым элементом
        ls[i],  ls[low] = ls[low], ls[i]


def insertion_sort(ls):
    # Начинаем сортировать со второго элемента, т.к. первый элемент считается отсортированным
    for i in range(1, len(ls)):
        item = ls[i]
        # берем элемент для вставки и сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # отсортированный кусок списка двигаем вперед, если он больше элемента для всавки
        while j >= 0 and ls[j] > item:
            ls[j + 1] = ls[j]
            j -= 1
        # вставляем элемент
        ls[j + 1] = item







import names
from time import time

def decor(func,*args):
    ls = args[0]
    print('получил', ls)
    start = time()
    func(*args)
    stop = time()
    print('отдал', ls)
    print('время', stop-start)

#0.2
def bubble_sort(ls, reverse = False):
    compare = (lambda x,y : x > y) if not reverse else (lambda x,y : x < y)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls)-1):
            if compare(ls[i], ls[i+1]):
                ls[i], ls[i + 1] = ls[i+1], ls[i]
                swapped = True


# 0.03
def selection_sort(ls):
    for i in range(len(ls)): # i - кол уже проверенных
        low = i
        for j in range(i+1,len(ls)):
            if ls[low] > ls[j]:
                low = j
        ls[low],ls[i] = ls[i],ls[low]

# 0.001
def quick_sort(ls):
    if len(ls) <= 1:
        return ls
    el = ls[len(ls)//2]
    l = [i for i in ls if i< el]
    m = [i for i in ls if i == el]
    r = [i for i in ls if i > el]
    return quick_sort(l) + m +  quick_sort(r)



ls = [names.get_first_name() for i in range(1000)]
#decor(quick_sort, ls)
print(ls)
ls = quick_sort(ls)
print(ls)