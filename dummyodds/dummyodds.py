import os
import requests
import json

class DummyOdds:
    def __init__(self):
        self.__server_url = os.environ['DUMMY_ODDS_URL']

    @classmethod
    def __generate_query_tansyo(cls, id):
        query = '{ "race_id": { "year":"%s", "monthday":"%s", "jyocd":"%s", "kaiji":"%s", "nichiji":"%s", "racenum":"%s" } }' % (id)
        return query.strip()

    # @param id [ 'year', 'monthday', 'jyocd', 'kaiji', 'nichiji', 'racenum']
    def odds_tansyo(self, id):

        query = DummyOdds.__generate_query_tansyo(id)
        r = requests.post(self.__server_url, query)

        if r.status_code == 200:
            body = json.loads(r.text)
            return body['tansyo']

        else:
            body = json.loads(r.text)
            raise RuntimeError("DummyOdds server says: %s" % (body["error"],))
