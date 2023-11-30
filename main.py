import random

breakfast = {
    'Каша': {
        'cal': 111,
        'ingrid': ['манка', 'молоко']
    },
    'Яичница': {
        'cal': 111,
        'ingrid': ['яйца', 'лук', 'молоко']
    },
    'Бутер': {
        'cal': 222,
        'ingrid': ['хлеб', 'сыр', 'колбаса']
    }
}

lunch = {
    'Борщ': {
        'cal': 444,
        'ingrid': ['свекла', 'картофель', 'морковь', 'лук', 'капуста']
    },
    'Бургер': {
        'cal': 555,
        'ingrid': ['фарш', 'булка', 'соус', 'лук', 'кетчуп']
    },
    'Цезарь': {
        'cal': 333,
        'ingrid': ['курица', 'сухари', 'капуста']
    }
}

dinner = {
    'Шашлык': {
        'cal': 444,
        'ingrid': ['мясо', 'лук', 'соус']
    },
    'Макарики': {
        'cal': 555,
        'ingrid': ['макароны', 'фарш', 'соус', 'лук', 'кетчуп']
    },
    'Гречка': {
        'cal': 333,
        'ingrid': ['гречка', 'фарш', 'морковь']
    }
}

monday_breakfast = random.choice(list(breakfast.keys()))
monday_lunch = random.choice(list(lunch.keys()))
monday_dinner = random.choice(list(dinner.keys()))
print(monday_breakfast, monday_lunch, monday_dinner)

del breakfast[monday_breakfast]
del lunch[monday_lunch]
del dinner[monday_dinner]
print(breakfast, lunch, dinner)

tuesday_breakfast = random.choice(list(breakfast.keys()))
tuesday_lunch = random.choice(list(lunch.keys()))
tuesday_dinner = random.choice(list(dinner.keys()))
print(tuesday_breakfast, tuesday_lunch, tuesday_dinner)

del breakfast[tuesday_breakfast]
del lunch[tuesday_lunch]
del dinner[tuesday_dinner]
print(breakfast, lunch, dinner)

wednesday_breakfast = random.choice(list(breakfast.keys()))
wednesday_lunch = random.choice(list(lunch.keys()))
wednesday_dinner = random.choice(list(dinner.keys()))
print(wednesday_breakfast, wednesday_lunch, wednesday_dinner)

del breakfast[wednesday_breakfast]
del lunch[wednesday_lunch]
del dinner[wednesday_dinner]
print(breakfast, lunch, dinner)

thursday_breakfast = random.choice(list(breakfast.keys()))
thursday_lunch = random.choice(list(lunch.keys()))
thursday_dinner = random.choice(list(dinner.keys()))
print(thursday_breakfast, thursday_lunch, thursday_dinner)

del breakfast[thursday_breakfast]
del lunch[thursday_lunch]
del dinner[thursday_dinner]
print(breakfast, lunch, dinner)

friday_breakfast = random.choice(list(breakfast.keys()))
friday_lunch = random.choice(list(lunch.keys()))
friday_dinner = random.choice(list(dinner.keys()))
print(friday_breakfast, friday_lunch, friday_dinner)

del breakfast[friday_breakfast]
del lunch[friday_lunch]
del dinner[friday_dinner]
print(breakfast, lunch, dinner)

saturday_breakfast = random.choice(list(breakfast.keys()))
saturday_lunch = random.choice(list(lunch.keys()))
saturday_dinner = random.choice(list(dinner.keys()))
print(saturday_breakfast, saturday_lunch, saturday_dinner)

del breakfast[saturday_breakfast]
del lunch[saturday_lunch]
del dinner[saturday_dinner]
print(breakfast, lunch, dinner)

sunday_breakfast = random.choice(list(breakfast.keys()))
sunday_lunch = random.choice(list(lunch.keys()))
sunday_dinner = random.choice(list(dinner.keys()))
print(sunday_breakfast, sunday_lunch, sunday_dinner)

del breakfast[sunday_breakfast]
del lunch[sunday_lunch]
del dinner[sunday_dinner]
print(breakfast, lunch, dinner)

#test push
#test push win