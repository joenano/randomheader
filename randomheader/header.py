from random import choice, sample, shuffle
from typing import Iterator

import os
path = os.path.abspath(os.path.dirname(__file__))


class RandomHeader:

    def __init__(self) -> None:
        self.accepts = [*self.readlines(f'{path}/data/accepts.txt')]
        self.encodings = [*self.readlines(f'{path}/data/encodings.txt')]
        self.referers = [*self.readlines(f'{path}/data/referer.txt')]
        self.user_agents = [*self.readlines(f'{path}/data/user-agents.txt')]

    def header(self) -> dict:
        return self.shuffle_header({
            'Accept': choice(self.accepts),
            'Accept-Encoding': choice(self.encodings),
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Referer': choice(self.referers),
            'Dnt': choice(('0', '1')),
            'Connection': 'keep-alive',
            'X-Forwarded-For': self.random_ip(),
            'User-Agent': choice(self.user_agents),
            'Upgrade-Insecure-Requests': '1'
        })

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
