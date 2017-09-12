from math import factorial as fact
from random import random, randrange, shuffle
from statistics import mean

def combinations(n, r):
    return fact(n) / fact(r) / fact(n-r)

def cum_binom(n, r, ph):
    total = 0.0
    for h in range(r, n+1):
        total += ph ** h * (1.0 - ph) ** (n - h) * combinations(n, h)
    return total

# Estimate the probability of getting 42500 or more heads
# from 70000 spins of biased coin (60% heads and 40% tails)    

# Estimate the probability of getting 5 or more heads
# from 7 spins of biased coin (60% heads and 40% tails)
print(cum_binom(7, 5, 0.60))

def trial():
    nh = 0
    for i in range(7):
        nh += random() < 0.60
    return nh >= 5

cases = 0
for i in range(10000):
    cases += trial()
print(cases / 10000.0)

trial = lambda : sum(random() < 0.60 for i in range(7)) >= 5
print(sum(trial() for i in range(10000)) / 10000.0)

# Probability of the median of 5 samples being in the
# middle two quartiles of the population
trial = lambda :  2500 <= sorted(randrange(10000) for i in range(5))[2] < 7500
print(sum(trial() for i in range(10000)) / 10000.0)    # compare with the beta distribution

# An exact permutation text
# Hypothesis testing
drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]
obs_diff = mean(drug) - mean(placebo)

# Null hypothesis is that there is no real difference between the drug
# and the placebo.  Which means that any observed difference was just
# due to chance and noise.

comb = drug + placebo

cases = 0
for i in range(10000):
    shuffle(comb)
    new_diff = mean(comb[:len(drug)]) - mean(comb[len(drug):])
    cases += new_diff >= obs_diff
print(cases / 10000, '<-- The p-value')
print('Accordlingly, we reject the null hypothesis')
print('and conclude the observed difference was not due to chance')
