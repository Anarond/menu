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

breakfast = random.choice(list(dict_breakfast.keys()))
cal_breakfast = dict_breakfast.get(breakfast)['cal']
while cal_breakfast > 200:
    breakfast = random.choice(list(dict_breakfast.keys()))
    cal_breakfast = dict_breakfast[breakfast]['cal']
print(breakfast)

lunch = random.choice(list(dict_lunch.keys()))
cal_lunch = dict_lunch.get(lunch)['cal']
while cal_lunch > 500:
    lunch = random.choice(list(dict_lunch.keys()))
    cal_lunch = dict_lunch[lunch]['cal']
print(lunch)

dinner = random.choice(list(dict_dinner.keys()))
cal_dinner = dict_dinner.get(dinner)['cal']
while cal_dinner > 400:
    dinner = random.choice(list(dict_dinner.keys()))
    cal_dinner = dict_dinner[dinner]['cal']
print(dinner)


# i = 0

# while i != 7:
#    breakfast = random.choice(list(dict_breakfast.keys()))
#    lunch = random.choice(list(dict_lunch.keys()))
#    dinner = random.choice(list(dict_dinner.keys()))
#    print(breakfast, lunch, dinner)
#        if breakfast
#        else
#            del dict_breakfast[breakfast]
#            del dict_lunch[lunch]
#            del dict_dinner[dinner]
#            #print(breakfast, lunch, dinner)
#            i += 1


