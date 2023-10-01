import numpy as np
from scipy import stats

# Data: Ages of offenders
data = [
    11, 14, 15, 15, 16, 16, 17, 18, 19, 21, 25, 36,
    12, 14, 15, 15, 16, 16, 17, 18, 19, 21, 25, 39,
    13, 14, 15, 15, 16, 17, 17, 18, 20, 22, 26, 43,
    13, 14, 15, 15, 16, 17, 17, 18, 20, 22, 26, 46,
    13, 14, 15, 16, 16, 17, 17, 18, 20, 22, 27, 50,
    13, 14, 15, 16, 16, 17, 17, 19, 20, 23, 27, 54,
    13, 14, 15, 16, 16, 17, 18, 19, 20, 23, 29, 59,
    13, 15, 15, 16, 16, 17, 18, 19, 20, 23, 30, 67,
    14, 15, 15, 16, 16, 17, 18, 19, 21, 24, 31, None,
    14, 15, 15, 16, 16, 17, 18, 19, 21, 24, 34, None,
]

# Remove None values if present
data = [x for x in data if x is not None]

# Calculate median
median = np.median(data)

# Calculate mode
mode = stats.mode(data).mode

# Calculate quartiles (Q1 and Q3)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

# Calculate percentiles (P10 and P95)
p10 = np.percentile(data, 10)
p95 = np.percentile(data, 95)

# Print the results
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Q1 (First Quartile): {q1}")
print(f"Q3 (Third Quartile): {q3}")
print(f"P10 (Tenth Percentile): {p10}")
print(f"P95 (Ninety-Fifth Percentile): {p95}")
