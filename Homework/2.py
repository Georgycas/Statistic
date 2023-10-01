import random
import math
import matplotlib.pyplot as plt

# Function to calculate the mean of a list of numbers
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Function to calculate the median of a list of numbers
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2
    else:
        median = sorted_numbers[n // 2]
    return median

# Function to calculate the standard deviation of a list of numbers
def calculate_std_deviation(numbers):
    mean = calculate_mean(numbers)
    squared_diff = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_diff) / len(numbers)
    std_deviation = math.sqrt(variance)
    return std_deviation

# Generate 500 random numbers with mean = 10 and std deviation = 0.5
random_numbers = [random.gauss(10, 0.5) for _ in range(500)]

# Calculate mean, median, and standard deviation
mean = calculate_mean(random_numbers)
median = calculate_median(random_numbers)
std_deviation = calculate_std_deviation(random_numbers)

# Plot a histogram with 10 bins
plt.hist(random_numbers, bins=10, edgecolor='black')
plt.title('Histogram of Random Numbers (Gaussian Distribution)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)

# Display the calculated statistics
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_deviation}")

# Show the histogram
plt.show()
