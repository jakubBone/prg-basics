# A program that prints the weekly meal plan along with the day names.

# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]


# Returns a week day name
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]


# Returns a string with day meal names separated by comma
def day_meal_plan(meal_plan, day_number):
    # ', '.join(list) joins the elements of a list into one string, with ', ' between them
    return ', '.join(meal_plan[day_number - 1])


# Prints weekly meal plan
print('WEEKLY MEAL PLAN')
print('(Breakfast, Lunch, Dinner)')
print('==========================')
for day in range(1, 8):
    print(f'{weekday(day)}: {day_meal_plan(meal_plan, day)}')
