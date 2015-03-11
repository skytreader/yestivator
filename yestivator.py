import json
import random

class QuoteSource(object):
    """
    Hard-coded quote source.
    """
    
    def __init__(self):
        self.quotes = json.load("~/.yestivator_quotes")

    def get_quote(self):
        return choice.random(self.quotes)
