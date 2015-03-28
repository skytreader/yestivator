import json
import pynotify
import random
import time

class QuoteSource(object):
    """
    Hard-coded quote source.
    """
    
    def __init__(self):
        self.quotes = json.load("~/.yestivator_quotes")

    def get_quote(self):
        return choice.random(self.quotes)

class Yestivator(object):
    
    def __init__(self, quote_source, freq):
        self.quote_source = quote_source
        self.freq = freq
        pynotify.init("Basic")

    def run(self):
        time.sleep(self.freq)
        notif = pynotify.Notification("YES", self.quote_source.get_quote())
        notif.show()

if __name__ == "__main__":
    quotes = QuoteSource()
    yessarian = Yestivator(quotes, 8)
    yessarian.run()
