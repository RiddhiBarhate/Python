import scipy.stats as stats

def normal_distribution_properties(mean, std_dev):
    distribution = stats.norm(mean, std_dev)
    return distribution

def calculate_probability(distribution, value):
    return distribution.cdf(value)

# Example usage
mean = 0
std_dev = 1
value = 1.96

distribution = normal_distribution_properties(mean, std_dev)
probability = calculate_probability(distribution, value)

print(f"Probability of a value less than {value}: {probability:.4f}")
