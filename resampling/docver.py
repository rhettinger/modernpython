import collections
from statistics import mean, median, stdev
from random import sample, choices, shuffle, expovariate, gauss

# Six roulette wheel spins (weighted sampling with replacement)
choices(['red', 'black', 'green'], [18, 18, 2], k=6)


# Deal 20 cards without replacement from a deck of 52 playing cards
# and determine the proportion of cards with a ten-value
# (a ten, jack, queen, or king).
deck = collections.Counter(tens=16, low_cards=36)
seen = sample(list(deck.elements()), k=20)
seen.count('tens') / 20


# Estimate the probability of getting 5 or more heads from 7 spins
# of a biased coin that settles on heads 60% of the time.
trial = lambda: choices('HT', cum_weights=(0.60, 1.00), k=7).count('H') >= 5
sum(trial() for i in range(10000)) / 10000


# Probability of the median of 5 samples being in middle two quartiles
trial = lambda : 2500 <= sorted(choices(range(10000), k=5))[2]  < 7500
sum(trial() for i in range(10000)) / 10000

# http://statistics.about.com/od/Applications/a/Example-Of-Bootstrapping.htm
data = 1, 2, 4, 4, 10
means = sorted(mean(choices(data, k=5)) for i in range(20))
print(f'The sample mean of {mean(data):.1f} has a 90% confidence '
      f'interval from {means[1]:.1f} to {means[-2]:.1f}')

# Example from "Statistics is Easy" by Dennis Shasha and Manda Wilson
drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]
observed_diff = mean(drug) - mean(placebo)

n = 10000
count = 0
combined = drug + placebo
for i in range(n):
    shuffle(combined)
    new_diff = mean(combined[:len(drug)]) - mean(combined[len(drug):])
    count += (new_diff >= observed_diff)

print(f'{n} label reshufflings produced only {count} instances with a difference')
print(f'at least as extreme as the observed difference of {observed_diff:.1f}.')
print(f'The one-sided p-value of {count / n:.4f} leads us to reject the null')
print(f'hypothesis that there is no difference between the drug and the placebo.')


# Single server queuse ##############################################

average_arrival_interval = 5.6
average_service_time = 5.0
stdev_service_time = 0.5

num_waiting = 0
arrivals = []
starts = []
arrival = service_end = 0.0
for i in range(20000):
    if arrival <= service_end:
        num_waiting += 1
        arrival += expovariate(1.0 / average_arrival_interval)
        arrivals.append(arrival)
    else:
        num_waiting -= 1
        service_start = service_end if num_waiting else arrival
        service_time = gauss(average_service_time, stdev_service_time)
        service_end = service_start + service_time
        starts.append(service_start)

waits = [start - arrival for arrival, start in zip(arrivals, starts)]
print(f'Mean wait: {mean(waits):.1f}.  Stdev wait: {stdev(waits):.1f}.')
print(f'Median wait: {median(waits):.1f}.  Max wait: {max(waits):.1f}.')
