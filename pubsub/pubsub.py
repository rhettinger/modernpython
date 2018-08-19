'Simple message publisher/subscriber service'

import sys
assert sys.version_info[:3] >= (3, 6, 1), "Requires 3.6.1 or later"

from typing import List, Tuple, DefaultDict, Set, Optional, NamedTuple, Deque, Dict
from collections import deque, defaultdict
import hashlib
import random
import secrets
from itertools import islice
from time import time, sleep
from heapq import merge
from bisect import bisect
from sys import intern

User = str
Timestamp = float
HashAndSalt = Tuple[bytes, bytes]

Post = NamedTuple('Post', [('timestamp', float), ('user', User), ('text', str)])
UserInfo = NamedTuple('UserInfo', [('displayname', str), ('email', str),
                                   ('hashed_password', HashAndSalt), ('bio', Optional[str]),
                                   ('photo', Optional[str])])

posts = deque()                     # type: Deque[Post]     # Posts from newest to oldest
user_posts = defaultdict(deque)     # type: DefaultDict[User, Deque[Post]]
following = defaultdict(set)        # type: DefaultDict[User, Set[User]]
followers = defaultdict(set)        # type: DefaultDict[User, Set[User]]
user_info = dict()                  # type: Dict[User, UserInfo]

def post_message(user: User, text: str, timestamp: Optional[Timestamp]=None) -> None:
    user = intern(user)
    timestamp = timestamp or time()
    post = Post(timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)

def follow(user: User, followed_user: User) -> None:
    user, followed_user = intern(user), intern(followed_user)
    following[user].add(followed_user)
    followers[followed_user].add(user)

def posts_by_user(user: User, limit: Optional[int] = None) -> List[Post]:
    return list(islice(user_posts[user], limit))

def posts_for_user(user: User, limit: Optional[int] = None) -> List[Post]:
    relevant = merge(*[user_posts[u] for u in following[user]], reverse=True)
    return list(islice(relevant, limit))

def get_followers(user: User) -> List[User]:
    return sorted(followers[user])

def get_followed(user: User) -> List[User]:
    return sorted(following[user])

def search(phrase:str, limit: Optional[int] = None) -> List[Post]:
    # XXX this could benefit from caching and from preindexing
    return list(islice((post for post in posts if phrase in post.text), limit))

def hash_password(password: str, salt: Optional[bytes] = None) -> HashAndSalt:
    pepper = b'alchemists discovered that gold came from earth air fire and water'
    salt = salt or secrets.token_bytes(16)
    salted_pass = salt + password.encode('utf-8')
    return hashlib.pbkdf2_hmac('sha512', salted_pass, pepper, 100000), salt

def set_user(user: User, displayname: str, email: str, password: str, bio: Optional[str]=None, photo: Optional[str]=None) -> None:
    user = intern(user)
    hashed_password = hash_password(password)
    user_info[user] = UserInfo(displayname, email, hashed_password, bio, photo)

def check_user(user: User, password: str) -> bool:
    hashpass, salt = user_info[user].hashed_password
    target_hash_pass = hash_password(password, salt)[0]
    sleep(random.expovariate(10))
    return secrets.compare_digest(hashpass, target_hash_pass)

def get_user(user: User) -> UserInfo:
    return user_info[user]

time_unit_cuts = [60, 3600, 3600*24]                                           # type: List[int]
time_units = [(1, 'second'), (60, 'minute'), (3600, 'hour'), (24*3600, 'day')] # type: List[Tuple[int, str]]

def age(post: Post) -> str:
    seconds = time() - post.timestamp
    divisor, unit = time_units[bisect(time_unit_cuts, seconds)]
    units = seconds // divisor
    return '%d %s ago' % (units, unit + ('' if units==1 else 's'))
