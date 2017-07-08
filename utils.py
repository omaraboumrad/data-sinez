import datetime
import itertools
import os

import pandas as pd

from ascii_graph import Pyasciigraph

DATA_ROOT = './data'
USERS = os.path.join(DATA_ROOT, 'users.json')


def grouped(frame, size):
    grouped = frame.groupby(['name'])
    aggregated = grouped.agg(['count'])['text']
    result = aggregated.sort_values('count', ascending=False)[:size]
    result.reset_index(inplace=True)
    return result[['name', 'count']].set_index('name')


def last_n_days(frame, days=30):
    since = datetime.datetime.now() - pd.to_timedelta('{}days'.format(days))
    return frame.index > since


def sieve(log, predicate, then):
    if predicate is not None:
        filtered = log[predicate]
    else:
        filtered = log

    yield plot(grouped(then(filtered), 7))
    yield '\n\nlast 30 days...\n\n '

    if predicate is not None:
        filtered = log[predicate & last_n_days(log)]
    else:
        filtered = log[last_n_days(log)]

    yield plot(grouped(then(filtered), 7))
    yield '\n------\n'


def listdir_with_path(name):
    return [os.path.join(name, x) for x in os.listdir(name)]


def plot(data):
    graph = Pyasciigraph(human_readable='si')
    return '\n'.join(graph.graph(label=None, data=data.itertuples()))


def identity(x):
    return x


def load_all():
    users = pd.read_json(USERS)

    channels_selected = [
        'general',
        'programming',
        'announcements',
    ]

    messages_per_channel = []

    for channel in channels_selected:
        channel_path = os.path.join(DATA_ROOT, channel)
        for daily in itertools.chain(listdir_with_path(channel_path)):
            channel_messages = pd.read_json(daily)
            channel_messages['channel'] = channel
            messages_per_channel.append(channel_messages)

    log = pd.concat(messages_per_channel)

    # delete the existing name column
    # we will get a fresh one from the merge
    del log['name']

    log['ts'] = pd.to_datetime(log['ts'], unit='s')

    log = pd.merge(
        log, users,
        left_on='user', right_on='id'
    )[['ts', 'name', 'text', 'channel']]

    return log.set_index('ts')
