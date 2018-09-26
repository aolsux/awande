# taken from https://github.com/zalando/connexion/blob/master/examples/restyresolver/api/pets.py

import datetime

from connexion import NoContent
from prometheus_client import Histogram, Counter

pets = {}

histogram = Histogram('response_latency_seconds', 'Response latency (seconds)')
counter = Counter("rest_call_count", "The number of calls to the rest backend", ['method', 'endpoint'])


@histogram.time()
def post(pet):
    counter.labels('post', 'pets').inc()
    count = len(pets)
    pet['id'] = count + 1
    pet['registered'] = datetime.datetime.now()
    pets[pet['id']] = pet
    return pet, 201


def put(id, pet):
    counter.labels('put', 'pets').inc()
    id = int(id)
    if pets.get(id) is None:
        return NoContent, 404
    pets[id] = pet

    return pets[id]


def delete(id):
    counter.labels('delete', 'pets').inc()
    id = int(id)
    if pets.get(id) is None:
        return NoContent, 404
    del pets[id]
    return NoContent, 204


def get(id):
    counter.labels('get', 'pets').inc()
    id = int(id)
    if pets.get(id) is None:
        return NoContent, 404

    return pets[id]


def search():
    counter.labels('search', 'pets').inc()
    # NOTE: we need to wrap it with list for Python 3 as dict_values is not JSON serializable
    return list(pets.values())
