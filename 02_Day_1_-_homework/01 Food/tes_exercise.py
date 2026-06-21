class Ingredient:
    def __init__(self, name, protein, carbohydrates, fats):
        self.name = name
        self.protein = float(protein)
        self.carbohydrates = float(carbohydrates)
        self.fats = float(fats)

    def values_for(self, grams):
        factor = grams / 100
        protein = self.protein * factor
        carbohydrates = self.carbohydrates * factor
        fats = self.fats * factor
        kcal = protein * 4 + carbohydrates * 4 + fats * 9.4
        return protein, carbohydrates, fats, kcal


class Meal:
    def __init__(self, name):
        self.name = name
        self.ingredients = []  # list of (ingredient, grams)

    def add_ingredient(self, ingredient, grams):
        self.ingredients.append((ingredient, grams))

    def summary(self):
        total_protein = total_carbs = total_fats = total_kcal = 0

        lines = [f"Meal: {self.name}"]
        for ingredient, grams in self.ingredients:
            protein, carbs, fats, kcal = ingredient.values_for(grams)

            total_protein += protein
            total_carbs += carbs
            total_fats += fats
            total_kcal += kcal

            lines.append(
                f"- {grams}g {ingredient.name} "
                f"({protein:.2f}g protein, {carbs:.2f}g carbohydrates, "
                f"{fats:.2f}g fats, {kcal:.1f} kcal)"
            )

        lines.append(
            f"Total: {total_protein:.2f}g protein, "
            f"{total_carbs:.2f}g carbohydrates, "
            f"{total_fats:.2f}g fats, "
            f"{total_kcal:.1f} kcal"
        )

        return lines, total_protein, total_carbs, total_fats, total_kcal


class DailyPlan:
    def __init__(self, name):
        self.name = name
        self.meals = []

    def add_meal(self, meal):
        self.meals.append(meal)

    def print_summary(self):
        print(self.name)
        print()

        total_protein = total_carbs = total_fats = total_kcal = 0

        for meal in self.meals:
            lines, p, c, f, k = meal.summary()
            for line in lines:
                print(line)
            print()

            total_protein += p
            total_carbs += c
            total_fats += f
            total_kcal += k

        print(
            f"TOTAL: {total_protein:.2f}g protein, "
            f"{total_carbs:.2f}g carbohydrates, "
            f"{total_fats:.0f}g fats, "
            f"{total_kcal:.0f} kcal"
        )

egg = Ingredient("Egg", 13, 1.1, 11)
tomato = Ingredient("Tomato", 0.9, 3.9, 0.2)
bread = Ingredient("Bread", 9, 49, 3.2)

scrambled_eggs = Meal("Scrambled Eggs")
scrambled_eggs.add_ingredient(egg, 200)
scrambled_eggs.add_ingredient(tomato, 50)

sandwich = Meal("Sandwich")
sandwich.add_ingredient(bread, 25)
sandwich.add_ingredient(tomato, 50)

plan = DailyPlan("Minimal")
plan.add_meal(scrambled_eggs)
plan.add_meal(sandwich)

plan.print_summary()