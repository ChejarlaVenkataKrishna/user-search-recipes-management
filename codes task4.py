import requests


class RecipeSearchApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.spoonacular.com/recipes/findByIngredients"
        
    def search_recipes(self, ingredients):
        params = {
            'ingredients': ','.join(ingredients),
            'apiKey': self.api_key,
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            recipes = response.json()
            return recipes
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

    def display_recipes(self, recipes):
        if recipes:
            print("Matching Recipes:")
            for recipe in recipes:
                print(f"Title: {recipe['title']}")
                print(f"Missing Ingredients: {', '.join(recipe['missedIngredients'])}")
                print(f"Used Ingredients: {', '.join(recipe['usedIngredients'])}")
                print("------")
        else:
            print("No recipes found.")

# Example usage
api_key = "https://spoonacular.com/profile/venkata%20krishna%20chejarla/settings"
app = RecipeSearchApp(api_key)

# Get user input for ingredients
user_ingredients = input("Enter ingredients (comma-separated): ").split(',')

# Search for recipes
recipes = app.search_recipes(user_ingredients)

# Display the results
app.display_recipes(recipes)
