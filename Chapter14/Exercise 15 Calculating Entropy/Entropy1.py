import numpy as np
distribution = [p1, p2, …, pn] // insert your distribution here
minus_distribution = [-x for x in distribution]
log_distribution = [x for x in map(np.log2,distribution)]
entropy_value = np.dot(minus_distribution, log_distribution)

entropy_value

def entropy(distribution):
 minus_distribution = [-x for x in distribution]
 logDistribution = [x for x in map( np.log2, distribution )]
 return np.dot(minusDistribution, logDistribution)

H_employed = entropy([4/7, 3/7])
H_employed

H_income = entropy([1/7, 2/7, 1/7, 2/7, 1/7])
H_income

H_loanType = entropy([3/7, 2/7, 2/7])
H_loanType

H_LoanAmount = entropy([1/7, 1/7, 3/7, 1/7, 1/7])
H_LoanAmount

H_incomeMoreThan75K = entropy([4/7, 3/7])
H_incomeMoreThan75K

H_loanMoreThan15K = entropy([6/7, 1/7])
H_loanMoreThan15K