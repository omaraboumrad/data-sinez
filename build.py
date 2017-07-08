import time

import slides
import utils


pages = [
    slides.presentation,
    slides.what_is_it,
    slides.who_am_i,
    slides.how_it_works,
    slides.codename,
    slides.warning,

    # slides.mena_devs_activity,
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
    # slides.most_yells,
    # slides.most_upvotes,
    # slides.most_downvotes,

    slides.outro,
]


if __name__ == '__main__':

    print('> loading', end='')
    start = time.time()
    log = utils.load_all()
    elapsed = time.time() - start
    print('[{0:.2f}]'.format(elapsed))

    with open('stats.md', 'w') as out:
        for page in pages:
            start = time.time()
            print('> rendering: {}'.format(page.__name__), end='')

            for segment in page(log):
                out.write('\n'.join(x.strip() for x in segment.splitlines()))
                out.write('\n')

            elapsed = time.time() - start
            print('[{0:.2f}]'.format(elapsed))
