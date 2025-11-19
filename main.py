import math


def cubic_solve(a, b, c, d):
    # приводим уравнение к приведённому виду: y^3 + p*y + q = 0
    # подстановка: x = y - b/(3a)
    if a == 0:
        return ["ошибка, уравнение не кубической, первый параметр не может быть 0"]

    # коэффициенты приведённого уравнения
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)

    # решаем приведённое уравнение y^3 + p*y + q = 0
    if p == 0:
        y = math.pow(-q, 1 / 3)
        roots = [y - b / (3 * a)]

    elif q == 0:
        roots = [-b / (3 * a)]

        if p < 0:
            roots.extend([
                -b / (3 * a) + math.sqrt(-p),
                -b / (3 * a) - math.sqrt(-p)
            ])
    else:
        # используем тригонометрическую формулу виета
        if p > 0:
            Q = (p / 3) ** 3 + (q / 2) ** 2
            if Q >= 0:
                A = math.pow(-q / 2 + math.sqrt(Q), 1 / 3)
                B = math.pow(-q / 2 - math.sqrt(Q), 1 / 3)
                y1 = A + B
            else:
                r = 2 * math.sqrt(-p / 3)
                alpha = math.acos(3 * q / (p * r)) / 3
                y1 = r * math.cos(alpha)

            roots = [y1 - b / (3 * a)]

        else:
            r = 2 * math.sqrt(-p / 3)
            alpha = math.acos(3 * q / (p * r)) / 3
            y1 = r * math.cos(alpha)
            y2 = r * math.cos(alpha + 2 * math.pi / 3)
            y3 = r * math.cos(alpha + 4 * math.pi / 3)

            roots = [
                y1 - b / (3 * a),
                y2 - b / (3 * a),
                y3 - b / (3 * a)
            ]

    return [round(root, 5) for root in roots]


# тестовые примеры
test_cases = [
    (1, -6, 11, -6),
    (1, 0, 0, -8),
    (1, 0, -3, 0),
    (2, -4, -22, 24)
]

for i, (a, b, c, d) in enumerate(test_cases, 1):
    roots = cubic_solve(a, b, c, d)
    print(f"уравнение: {a}x^3 + {b}x^2 + {c}x + {d} = 0")
    print(f"корни: {roots}\n")
