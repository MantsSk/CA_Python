import logging

# Configure logger
logging.basicConfig(
    filename="rectangle.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# Function to calculate the area and perimeter of a rectangle
def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)

    # Log the calculations
    logging.info(f"Rectangle - Length: {length}, Width: {width}")
    logging.info(f"Area: {area}, Perimeter: {perimeter}")

    return area, perimeter


# Prompt user for the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area and perimeter of the rectangle
area, perimeter = calculate_rectangle_properties(length, width)

# Print the calculated results
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
