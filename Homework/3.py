import matplotlib.pyplot as plt

# Assign a list of the Reason of Death 
causes = [
    "Heart Disease", "Malignant Neoplasms", "Stroke",
    "Chronic Respiratory Disease", "Accidents", "Diabetes",
    "Alzheimer’s", "Influenza/Pneumonia", "Nephritis/Nephrosis", "Septicemia"
]
# The number of death corresponding the list of resons
deaths = [63.2, 56.0, 13.7, 12.5, 12.2, 7.2, 7.2, 5.6, 4.5, 3.4]

# Sort causes and deaths in descending order of deaths
sorted_causes, sorted_deaths = zip(*sorted(zip(causes, deaths), key=lambda x: x[1], reverse=True))

# Calculate the cumulative percentage
total_deaths = sum(sorted_deaths)
cumulative_percentage = [100 * (sum(sorted_deaths[:i + 1]) / total_deaths) for i in range(len(sorted_deaths))]

# Create a Pareto chart
fig, ax1 = plt.subplots()

# Bar chart for the number of deaths
ax1.bar(sorted_causes, sorted_deaths, color='b')
ax1.set_xlabel('Causes of Death')
ax1.set_ylabel('Number of Deaths (x 10,000)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Line graph for cumulative percentage
ax2 = ax1.twinx()
ax2.plot(sorted_causes, cumulative_percentage, color='r', marker='o')
ax2.set_ylabel('Cumulative Percentage', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Title and labels
plt.title('Pareto Chart - Leading Causes of Death in 2006')
plt.tight_layout()

# Show the chart
plt.show()
