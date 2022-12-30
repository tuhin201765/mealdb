import requests
from pprint import pprint
from wp_functions import image_url,list_html,dict_list,headers,wp_h2,open_ai

mealdb_url = 'https://www.themealdb.com/api/json/v1/1/search.php?f=a'
r = requests.get(mealdb_url)
meals = r.json().get('meals')
first_meal = meals[1]
area = first_meal.get('strArea')
strMeal = first_meal.get('strMeal')
image = first_meal.get('strMealThumb')
instruction = first_meal.get('strInstructions')
Youtube = first_meal.get('strYoutube')

i = 1
ingredients = {}
while i < 21:
    ingredient = f'strIngredient{i}'
    measure = f'strMeasure{i}'
    if (first_meal.get(ingredient) != None) and (first_meal.get(ingredient) != ""):
        ingredients[first_meal.get(ingredient)] = first_meal.get(measure)

    i +=1
# pprint(ingredients)
instruction_list = instruction.split('\r\n')

title = f'{strMeal} Recipe'
intro = open_ai(f'Write about {area} {strMeal}')
image = image_url(image,title)
heading = wp_h2('Ingredients')
ingredients_list = dict_list(ingredients)
heading_second = wp_h2('Description')
description = list_html(instruction_list)

content = f'{intro}{image}{heading}{ingredients_list}{heading_second}{description}'

data = {
    'title' : title,
    'content' : content
}

headers = headers('Mjujahidultuhin','YVgM aXCo tAVr Yei6 S7eP iFJH')
endpoint = 'https://mysite.local/wp-json/wp/v2/posts'
r = requests.post(endpoint,data=data, headers=headers,verify=False)