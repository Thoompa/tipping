import pprint
from api import standings

year = "2022"
round = "final"
try:
    ladder = standings.getLadder(year, round)
except Exception as e:
    raise Exception("Error when calling get ladder:" + str(e))
pprint.pprint(ladder)
