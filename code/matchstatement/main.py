def colour_picking(meal, meal_time="Dinner"):
    match meal:
        case 'spaghetti':
            return "You have picked spaghetti"
        case 'sandwich' if meal_time == "Lunch":
            return "You have picked sandwich"
        case 'pizza'|'pizza slice':
            return "You have picked pizza"
        case _:
            return "You have picked something else"
        
print(colour_picking('spaghetti'))
print(colour_picking('pizza'))
print(colour_picking('sandwich', meal_time="Lunch"))
print(colour_picking('sandwich', meal_time="Dinner"))