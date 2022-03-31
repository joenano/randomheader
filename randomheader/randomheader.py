from random import choice, sample, shuffle
from typing import Iterator


class RandomHeader:

    def __init__(self) -> None:
        self.accepts = [*self.readlines('agents/accepts.txt')]
        self.referrers = [*self.readlines('agents/referrer.txt')]
        self.user_agents = [*self.readlines('agents/user-agents.txt')]

    def header(self) -> dict:
        random_header = {
            'Accept': choice(self.accepts),
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Referer': choice(self.referrers),
            'Dnt': choice(('0', '1')),
            'Connection': 'keep-alive',
            'X-Forwarded-For': self.random_ip(),
            'User-Agent': choice(self.user_agents),
            'Upgrade-Insecure-Requests': '1'
        }

        return self.shuffle_header(random_header)

    def random_ip(self) -> str:
        return '{}.{}.{}.{}'.format(*sample(range(0, 255), 4))

    def readlines(self, filename: str) -> Iterator[str]:
        with open(filename, 'r') as f:
            for line in f:
                yield line.strip()

    def shuffle_header(self, header: dict) -> dict:
        keys = list(header.keys())
        shuffle(keys)
        return {k:header[k] for k in keys}
