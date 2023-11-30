import random

dict_breakfast = {
    'Каша1': {
        'cal': 111,
        'ingrid': ['манка', 'молоко']
    },
    'Яичница1': {
        'cal': 111,
        'ingrid': ['яйца', 'лук', 'молоко']
    },
    'Бутер1': {
        'cal': 222,
        'ingrid': ['хлеб', 'сыр', 'колбаса']
    },
    'Бобовая кашица1': {
        'cal': 210,
        'ingrid': ['горох', 'фасоль', 'морковь', 'лук', 'вода']
    },
    'Рисовый сюрприз1': {
        'cal': 300,
        'ingrid': ['рис', 'молоко', 'масло', 'соль', 'корица']
    },
    'Гречневый деликатес1': {
        'cal': 250,
        'ingrid': ['гречка', 'молоко', 'сахар', 'масло', 'яблоко']
    },
    'Овсяное чудо1': {
        'cal': 180,
        'ingrid': ['овсянка', 'молоко', 'банан', 'кокосовая стружка', 'мед']
    }
}

dict_lunch = {
    'Борщ2': {
        'cal': 444,
        'ingrid': ['свекла', 'картофель', 'морковь', 'лук', 'капуста']
    },
    'Бургер2': {
        'cal': 555,
        'ingrid': ['фарш', 'булка', 'соус', 'лук', 'кетчуп']
    },
    'Цезарь2': {
        'cal': 333,
        'ingrid': ['курица', 'сухари', 'капуста']
    },
    'Куриный фарш2': {
        'cal': 320,
        'ingrid': ['курица', 'лук', 'морковь', 'перец', 'панировочные сухари']
    },
    'Тунцовый стейк2': {
        'cal': 280,
        'ingrid': ['тунец', 'соевый соус', 'лимон', 'чеснок', 'оливковое масло']
    },
    'Свиной рулет2': {
        'cal': 380,
        'ingrid': ['свинина', 'сыр', 'перчики', 'бекон', 'зелень']
    },
    'Лососевый бургер2': {
        'cal': 400,
        'ingrid': ['лосось', 'авокадо', 'томат', 'салат', 'булочка']
    }
}

dict_dinner = {
    'Шашлык3': {
        'cal': 444,
        'ingrid': ['мясо', 'лук', 'соус']
    },
    'Макарики3': {
        'cal': 555,
        'ingrid': ['макароны', 'фарш', 'соус', 'лук', 'кетчуп']
    },
    'Гречка3': {
        'cal': 333,
        'ingrid': ['гречка', 'фарш', 'морковь']
    },
    'Мексиканский чили3': {
        'cal': 350,
        'ingrid': ['фасоль', 'говядина', 'томаты', 'лук', 'перец']
    },
    'Лазанья с курицей3': {
        'cal': 420,
        'ingrid': ['лазанья', 'курица', 'сыр', 'помидоры', 'базилик']
    },
    'Овощной тефтели3': {
        'cal': 280,
        'ingrid': ['цукини', 'морковь', 'лук', 'яйцо', 'панировочные сухари']
    },
    'Тайский карри3': {
        'cal': 390,
        'ingrid': ['курица', 'кокосовое молоко', 'корень имбиря', 'бамбуковые побеги', 'перец чили']
    }
}

i = 0

while i != 7:
    breakfast = random.choice(list(dict_breakfast.keys()))
    lunch = random.choice(list(dict_lunch.keys()))
    dinner = random.choice(list(dict_dinner.keys()))
    print(breakfast, lunch, dinner)

    del dict_breakfast[breakfast]
    del dict_lunch[lunch]
    del dict_dinner[dinner]
    #print(breakfast, lunch, dinner)
    i += 1

#monday_breakfast = random.choice(list(breakfast.keys()))
#monday_lunch = random.choice(list(lunch.keys()))
#monday_dinner = random.choice(list(dinner.keys()))
#print(monday_breakfast, monday_lunch, monday_dinner)

#del breakfast[monday_breakfast]
#del lunch[monday_lunch]
#del dinner[monday_dinner]
#print(breakfast, lunch, dinner)

#tuesday_breakfast = random.choice(list(breakfast.keys()))
#tuesday_lunch = random.choice(list(lunch.keys()))
#tuesday_dinner = random.choice(list(dinner.keys()))
#print(tuesday_breakfast, tuesday_lunch, tuesday_dinner)

#del breakfast[tuesday_breakfast]
#del lunch[tuesday_lunch]
#del dinner[tuesday_dinner]
#print(breakfast, lunch, dinner)

#wednesday_breakfast = random.choice(list(breakfast.keys()))
#wednesday_lunch = random.choice(list(lunch.keys()))
#wednesday_dinner = random.choice(list(dinner.keys()))
#print(wednesday_breakfast, wednesday_lunch, wednesday_dinner)

#del breakfast[wednesday_breakfast]
#del lunch[wednesday_lunch]
#del dinner[wednesday_dinner]
#print(breakfast, lunch, dinner)

#thursday_breakfast = random.choice(list(breakfast.keys()))
#thursday_lunch = random.choice(list(lunch.keys()))
#thursday_dinner = random.choice(list(dinner.keys()))
#print(thursday_breakfast, thursday_lunch, thursday_dinner)

#del breakfast[thursday_breakfast]
#del lunch[thursday_lunch]
#del dinner[thursday_dinner]
#print(breakfast, lunch, dinner)

#friday_breakfast = random.choice(list(breakfast.keys()))
#friday_lunch = random.choice(list(lunch.keys()))
#friday_dinner = random.choice(list(dinner.keys()))
#print(friday_breakfast, friday_lunch, friday_dinner)

#del breakfast[friday_breakfast]
#del lunch[friday_lunch]
#del dinner[friday_dinner]
#print(breakfast, lunch, dinner)

#saturday_breakfast = random.choice(list(breakfast.keys()))
#saturday_lunch = random.choice(list(lunch.keys()))
#saturday_dinner = random.choice(list(dinner.keys()))
#print(saturday_breakfast, saturday_lunch, saturday_dinner)

#del breakfast[saturday_breakfast]
#del lunch[saturday_lunch]
#del dinner[saturday_dinner]
#print(breakfast, lunch, dinner)

#sunday_breakfast = random.choice(list(breakfast.keys()))
#sunday_lunch = random.choice(list(lunch.keys()))
#sunday_dinner = random.choice(list(dinner.keys()))
#print(sunday_breakfast, sunday_lunch, sunday_dinner)

#del breakfast[sunday_breakfast]
#del lunch[sunday_lunch]
#del dinner[sunday_dinner]
#print(breakfast, lunch, dinner)

# test push
# test push win
