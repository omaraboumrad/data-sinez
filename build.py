#! /usr/bin/env python

import argparse
import os
import time

import pandas as pd

import slides
import utils


pages = [
    slides.presentation,
    slides.what_is_it,
    slides.who_am_i,
    slides.how_it_works,
    slides.codename,
    slides.warning,

    slides.mena_devs_activity,
    slides.early_birds,
    slides.most_active_during_day,
    slides.most_active_during_night,
    slides.night_owls,
    slides.most_active_in_programming,
    slides.most_active_in_general,
    slides.most_active_in_announcements,
    slides.total_messages_per_user,
    slides.size_of_longest_message,
    slides.most_links_posted,
    slides.most_mentioned,
    slides.most_emojis_in_messages,
    # slides.most_reacted_to,
    # slides.most_reactor,
    slides.most_dots,
    slides.jollyest,
    slides.most_profane,
    slides.greeter,
    slides.most_thankful,
    slides.karma_whore,
    slides.most_affirmative,
    slides.most_dissenting,
    slides.most_yells,
    # slides.most_upvotes,
    # slides.most_downvotes,

    slides.outro,
]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='build.py')
    parser.add_argument(
        '--outfile', default='stats.md', help='name of output file')
    parser.add_argument(
        '--cached', action='store_true', help='use cached log')
    args = parser.parse_args()

    if not os.path.exists('output'):
        os.makedirs('output')

    print('> loading ', end='')
    start = time.time()

    if args.cached:
        try:
            log = pd.read_pickle('output/all.pkl')
        except FileNotFoundError:
            print('[cache not found, rebuilding] ', end='')
            log = utils.rebuild()
            log.to_pickle('output/all.pkl')  # cache it
    else:
        log = utils.rebuild()
        log.to_pickle('output/all.pkl')  # cache it

    elapsed = time.time() - start
    print('[{0:.2f}]'.format(elapsed))

    with open(os.path.join('output', args.outfile), 'w') as out:
        for page in pages:
            start = time.time()
            print('> rendering: {} '.format(page.__name__), end='')

            for segment in page(log):
                out.write('\n'.join(x.strip() for x in segment.splitlines()))
                out.write('\n')

            elapsed = time.time() - start
            print('[{0:.2f}]'.format(elapsed))
