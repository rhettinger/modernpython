''' Use k-means to locate voting clusters in the U.S. Congress.

    Data set:  Senate voting record on 28 passed bills for the 2016 (114th Congress)
    Source:    https://www.govtrack.us/congress/votes#chamber[]=1&category[]=3

'''

from typing import Tuple, List, Dict, DefaultDict, NamedTuple
from kmeans import k_means, assign_data
from collections import defaultdict, Counter
import csv
import glob

Senator = NamedTuple('Senator', [('name', str), ('party', str), ('state', str)])
VoteValue = float

# Load votes arranged by topic and accumulate votes by senator
vote_value = {'Nay': -1, 'Not Voting': 0, 'Yea': 1} # type: Dict[str, VoteValue]
accumulated_record = defaultdict(list)              # type: DefaultDict[Senator, List[VoteValue]]
for filename in glob.glob('congress_data/*.csv'):
    with open(filename) as f:
        reader = csv.reader(f)
        vote_topic = next(reader)
        headers = next(reader)
        for person, state, district, vote, name, party in reader:
            senator = Senator(name, party, state)
            accumulated_record[senator].append(vote_value[vote])

# Transform record into plain dict mapping a senator to a tuple of vote values
record = {senator: tuple(votes) for senator, votes in accumulated_record.items()} # type: Dict[Senator, Tuple[VoteValue, ...]]

# Use k-means to locate the cluster centroids and assign senators to the nearest cluster
centroids = k_means(record.values(), k=3, iterations=50)
clustered_votes = assign_data(centroids, record.values())

# Build a reverse mapping from a pattern of votes to senators who voted that way
votes_to_senators = defaultdict(list)   # type: DefaultDict[Tuple[VoteValue, ...], List[Senator]]
for senator, votes in record.items():
    votes_to_senators[votes].append(senator)
assert sum(map(len, clustered_votes.values())) == 100

# Display the clusters and the members of each cluster
for i, votes_in_cluster in enumerate(clustered_votes.values(), start=1):
    print(f'=========== Voting Cluster #{i} ===========')
    party_totals = Counter()            # type: Counter
    for votes in set(votes_in_cluster):
        for senator in votes_to_senators[votes]:
            party_totals[senator.party] += 1
            print(senator)
    print(party_totals)
    print()
