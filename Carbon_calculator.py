# Carbon footprint calculator
def calculate_carbon_footprint(product_type, product_quantity):
    # Get the carbon footprint of the product
    carbon_footprint = get_carbon_footprint(product_type)
    
    # Calculate the total carbon footprint
    total_carbon_footprint = carbon_footprint * product_quantity
    
    return total_carbon_footprint

# Function to get the carbon footprint of a product
def get_carbon_footprint(product_type):
    # Define carbon footprint values for different products
    carbon_footprint_dict = {
        "beef": 27,
        "chicken": 6.9,
        "eggs": 4.8,
        "milk": 2,
        "tofu": 1.7,
        "beans": 0.5
    }
    
    # Return the carbon footprint value for the product type
    if product_type in carbon_footprint_dict:
        return carbon_footprint_dict[product_type]
    else:
        return None

# Example usage
product_type = "chicken"
product_quantity = 23

carbon_footprint = calculate_carbon_footprint(product_type, product_quantity)
print("The carbon footprint of", product_quantity, "kg of", product_type, "is", carbon_footprint, "kg CO2e")
