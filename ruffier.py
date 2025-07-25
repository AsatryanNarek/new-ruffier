""" Модуль для розрахунку результатів проби Руф’є.
 
Сума вимірювань пульсу у трьох спробах (до навантаження, одразу після та після короткого відпочинку)
в ідеалі має бути не більше 200 ударів на хвилину.
Ми пропонуємо дітям вимірювати свій пульс протягом 15 секунд,
і наводимо результат до ударів за хвилину множенням на 4:
    S = 4* (P1 + P2 + P3)
Що далі цей результат від ідеальних 200 ударів, то гірше.
Традиційно таблиці даються для величини, поділеної на 10.
 
Індекс Руф’є  
   IR = (S - 200) / 10
оцінюється за таблицею відповідно до віку:
           7-8             9-10             11-12          13-14                15+ 
                                                                      (тільки для підлітків!)
чуд.    6.4 і менше    4.9 і менше       3.4 і менше    1.9 і менше          0.4 і менше
доб.    6.5 - 11.9     5 - 10.4          3.5 - 8.9      2 - 7.4              0.5 - 5.9
задов.  12 - 16.9      10.5 - 15.4       9 - 13.9       7.5 - 12.4           6 - 10.9
слабкий 17 - 20.9      15.5 - 19.4       14 - 17.9      12.5 - 16.4          11 - 14.9
незад.  21 і більше    19.5 і більше     18 і більше    16.5 і більше        15 і більше
 
для будь-якого віку результат "незадовільно" віддалений від "слабкого" на 4,
той від "задовільного" на 5, а "добрий" від "чуд" - на 5.5
 
тому напишемо функцію ruffier_result(r_index, level), яка отримуватиме
розрахований індекс Руф'є та рівень "незадовільно" для віку тестованого, і віддавати результат """
# тут задаються рядки, за допомогою яких викладено результат:
txt_index = "Ваш індекс Руф’є:"
txt_workheart = "Працездатність серця:"
txt_nodata = """ Немає даних для такого віку """
txt_res = []
txt_res.append(""" Низька. Терміново зверніться до лікаря! """)
txt_res.append(""" Задовільна. Зверніться до лікаря! """)
txt_res.append(""" Середня. Можливо, варто додатково обстежитись у лікаря. """)
txt_res.append(""" Вище середнього """)
txt_res.append(""" Висока """)


def ruffier_index(P1, P2, P3):
    """повертає значення індексу за трьома показниками пульсу для звірки з таблицею"""
    return (4 * (P1 + P2 + P3) - 200) / 10


def nezad_level(age):
    """варіанти з віком менше 7 і дорослим треба обробляти окремо,
    тут підбираємо рівень "незадовільно" тільки всередині таблиці:
    у віці 7 років "незадовільно" - це індекс 21, далі кожні 2 роки він знижується на 1.5 до значення 15 в 15-16 років"""
    norm_age = (
        min(age, 15) - 7
    ) // 2  # кожні 2 роки різниці від 7 років перетворюються на одиницю - аж до 15 років
    result = (
        21 - norm_age * 1.5
    )  # множимо кожні 2 роки різниці на 1.5, так розподілені рівні у таблиці
    return result


def ruffier_result(r_index, level):
    """функція отримує індекс Руф’є і інтерпретує його,
    повертає рівень готовності: число від 0 до 4
    (що вище рівень готовності, то краще)."""
    if r_index >= level:
        return 0
    level = level - 4  # це не буде виконано, якщо ми вже повернули відповідь "незадовільно"
    if r_index >= level:
        return 1
    level = level - 5  # аналогічно, потрапляємо сюда, якщо рівень як мінімум "задовільно"
    if r_index >= level:
        return 2
    level = level - 5.5  # наступний рівень
    if r_index >= level:
        return 3
    return 4  # тут опинились, якщо індекс менше всіх проміжних рівнів, тобто із серцем все чикі-пікі


def test(P1, P2, P3, age):
    """цю функцію можна використовувати зовні модуля для підрахунків індексу Руф’є.
    Повертає готові тексти, які залишається намалювати у потрібному місці
    Використовує для текстів константи, задані на початку цього модуля."""
    if age < 7:
        return (txt_index + "0", txt_nodata) # якщо малий вік, то рахуємо по-іншому
    else:
        ruff_index = ruffier_index(P1, P2, P3)  # розрахунок
        result = txt_res[
            ruffier_result(ruff_index, nezad_level(age))
        ]  # інтерпретація, переведення числового рівня підготовки до текстових даних
        res = txt_index + str(ruff_index) + "\n" + txt_workheart + result
        return res
