from scalr.factory import Factory
from scalr.model.policy import Policy

from scalr.policy.random import RandomPolicy
from scalr.policy.web import WebPolicy


class PolicyFactory(Factory):

    def __init__(self):
        self.cloud_classes = {
            'random': RandomPolicy,
            'web': WebPolicy,
        }

    def parse(self, config: dict) -> Policy:
        return Policy(**config)
