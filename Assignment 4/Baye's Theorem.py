def bayes_theorem(prior_A, prob_B_given_A, prob_B):
    return (prob_B_given_A * prior_A) / prob_B

# Example usage
prior_cancer = 0.01
prob_positive_given_cancer = 0.9
prob_positive = 0.1

prob_cancer_given_positive = bayes_theorem(prior_cancer, prob_positive_given_cancer, prob_positive)
print(f"Probability of having cancer given a positive test result: {prob_cancer_given_positive:.4f}")
