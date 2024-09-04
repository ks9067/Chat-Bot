# Sample Python code for a basic food delivery application

class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

class FoodDeliveryApp:
    def __init__(self):
        self.restaurants = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def display_restaurants(self):
        print("Available Restaurants:")
        for idx, restaurant in enumerate(self.restaurants, start=1):
            print(f"{idx}. {restaurant.name}")

    def display_menu(self, restaurant_idx):
        if 1 <= restaurant_idx <= len(self.restaurants):
            selected_restaurant = self.restaurants[restaurant_idx - 1]
            print(f"\nMenu for {selected_restaurant.name}:")
            for item in selected_restaurant.menu:
                print(f"- {item}")
        else:
            print("Invalid restaurant index")

# Example usage
if __name__ == "__main__":
    # Create restaurants
    restaurant1 = Restaurant("Pizzeria Italia", ["Margherita Pizza", "Pasta Carbonara", "Tiramisu"])
    restaurant2 = Restaurant("Sushi Express", ["Sashimi Platter", "Dragon Roll", "Mochi Ice Cream"])

    # Create food delivery app
    food_app = FoodDeliveryApp()

    # Add restaurants to the app
    food_app.add_restaurant(restaurant1)
    food_app.add_restaurant(restaurant2)

    # Display available restaurants and their menus
    food_app.display_restaurants()

    # User selects a restaurant
    selected_restaurant_index = int(input("\nEnter the number of the restaurant you want to view: "))
    food_app.display_menu(selected_restaurant_index)
