# K - матрица жесткости системы, размерность 3x3
# q - вектор-столбец неизвестных узловых перемещений
# f - вектор-столбец известных внешних нагрузок

# вызываем скрипт ввода начальных данных

from fem_input import get_input
EF1, EF2, F = get_input()

# Матрицы жесткости элементов

from fem_hardnessmatrix import matrix_priemnyi
K = matrix_priemnyi(EF1, EF2)
print("Матрица жескости до введения ГУ" + "\n" + "K:", K)

# Применяем ГУ к матрице

from fem_borderconditions import border_condition
K = border_condition(K)
print("Матрица жескости после введения ГУ" + "\n" + "K:", K)

# Вектор внешних узловых усилий:

f = [0, F, 0]

print("Вектор внешних узловых усилий:" + "\n" + "f:", f)

# Неизвестное перемещение во втром узле

from fem_unkownsecondnodedisplacement import usnd
u1, u2, u3, u = usnd(f, K)
print("Неизвестное перемещение во втром узле:" + "\n" + "u:", u)

#перемещения первого элемента

import fem_firstnodedisplacement
fem_firstnodedisplacement.fnd(u1, u2)

#перемещения второго элемента

import fem_secondnodedisplacement
fem_secondnodedisplacement.snd(u2, u3)

# Внутренние усилия в стержне:
# N = EFu'

import fem_firstnodeforce
fem_firstnodeforce.fnf(u1, u2, EF1)

import fem_secondnodeforce
fem_secondnodeforce.snf(u2, u3, EF2)