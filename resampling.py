from random import random, randrange, shuffle, expovariate, gauss
from statistics import mean, median, stdev
from math import factorial as fact
from heapq import heappush, heappop

#############################################################################
# Helper functions for analysis

def combinations(n, r):
    return fact(n) // (fact(r) * fact(n-r))

def cum_binom(n, r, ph):
    total = 0.0
    for h in range(r, n+1):
        total += ph ** h * (1.0 - ph) ** (n - h) * combinations(n, h)
    return total


#############################################################################
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


#############################################################################
# Probability of the median of 5 samples being in the
# middle two quartiles of the population
trial = lambda :  2500 <= sorted(randrange(10000) for i in range(5))[2] < 7500
print(sum(trial() for i in range(10000)) / 10000.0)    # compare with the beta distribution


#############################################################################
# Hypothesis testing with an exact permutation text
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


#############################################################################
# Simulation of arrival times and service deliveries in a single server queue

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


############################################################################
# Simulation of arrival times and service deliveries for a multiserver queue

average_arrival_interval = 5.6
average_service_time = 15.0
stdev_service_time = 3.5
num_servers = 3

waits = []
arrival_time = 0.0
servers = [0.0] * num_servers  # time when each server becomes available
for i in range(100_000):
    arrival_time += expovariate(1.0 / average_arrival_interval)
    next_server_available = heappop(servers)
    wait = max(0.0, next_server_available - arrival_time)
    waits.append(wait)
    service_duration = gauss(average_service_time, stdev_service_time)
    service_completed = arrival_time + wait + service_duration
    heappush(servers, service_completed)

print(f'Mean wait: {mean(waits):.1f}.  Stdev wait: {stdev(waits):.1f}.')
print(f'Median wait: {median(waits):.1f}.  Max wait: {max(waits):.1f}.')
