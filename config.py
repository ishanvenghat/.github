from os import getenv

class Config(object):
      API_HASH = getenv("10dab55bfc1510dd1aef4f6c83b3e9e4")
      API_ID = int(getenv("29760783", 0))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("6224525172:AAHb759YC2EkymTQfcDnXfj6ytB9XkNi9aM", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "@lootdhamaka7").replace("\n", " ").split(' '))
