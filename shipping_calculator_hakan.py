# Express Shipping Rate Calculator
# Programmer: Robert Wilson
# Date: March 2024

# Display welcome screen
print("Welcome to Package Express. Please follow the instructions below.")

# Get package weight from user
weight_kg = float(input("Please enter the package weight:\n"))

# Check maximum weight limit
if weight_kg > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Input package dimensions
dimension_x = float(input("Please enter the package width:\n"))
dimension_y = float(input("Please enter the package height:\n"))
dimension_z = float(input("Please enter the package length:\n"))

# Calculate total package dimensions
package_volume = dimension_x + dimension_y + dimension_z

# Validate package size
if package_volume > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate shipping rate
# Rate = (width * height * length * weight) / 100
shipping_amount = (dimension_x * dimension_y * dimension_z * weight_kg) / 100

# Show shipping cost
print(f"Your estimated total for shipping this package is: ${shipping_amount:.2f}")
print("Thank you!") 