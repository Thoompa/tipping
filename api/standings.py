import constants
import requests

def getLadder(year, round):
    response = requests.get("{0}?q=standings;year={1};round={2}".format(constants.SQUIGGLE_API, year, round))
    if response.status_code == 200:
        return response.json()
    raise Exception("API Error: " + response.status_code)