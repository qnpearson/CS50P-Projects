fruits = [
    {"Name" : "apple", "Calories" : 130},
    {"Name" : "avocado", "Calories" : 50},
    {"Name" : "banana", "Calories" : 110},
    {"Name" : "cantaloupe", "Calories" : 50},
    {"Name" : "grapefruit", "Calories" : 60},
    {"Name" : "grapes", "Calories" : 90},
    {"Name" : "honeydew melon", "Calories" : 50},
    {"Name" : "kiwifruit", "Calories" : 90},
    {"Name" : "lemon", "Calories" : 15},
    {"Name" : "lime", "Calories" : 20},
    {"Name" : "nectarine", "Calories" : 60},
    {"Name" : "orange", "Calories" : 80},
    {"Name" : "peach", "Calories" : 60},
    {"Name" : "pineapple", "Calories" : 50},
    {"Name" : "pear", "Calories" : 100},
    {"Name" : "plums", "Calories" : 70},
    {"Name" : "strawberries", "Calories" : 50},
    {"Name" : "sweet cherries", "Calories" : 100},
    {"Name" : "tangerine", "Calories" : 50},
    {"Name" : "watermelon", "Calories" : 80}
    ]

def main():
    item = input("What would you like to input?" ).lower()
    (nutrition(item))

def nutrition(i):
        if any(i in Name.values() for Name in fruits) == True:
              my_fruit = [i["Name"] for i in fruits]
              my_calories = [i["Calories"] for i in fruits]
              index = my_fruit.index(i)
              print(my_calories[index])
              #item_calories = my_fruit["Calories"]
              #item_calories = fruits[index]["Calories"]
              #print(item_calories)
              #print(my_fruit)
              #print(my_calories)

main()
