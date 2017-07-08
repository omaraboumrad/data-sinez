import pandas as pd

from utils import (
    last_n_days,
    identity,
    sieve,
    plot,
    USERS)


def presentation(log):
    yield """\
    %title: MENA Devs - Data Sinez
    %author: ♔ Omar Abou Mrad♔
    """


def what_is_it(log):
    yield """\
    -> # What is it? <-




    -> ▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜ <-
    -> ▌ Startup : Data Sinez ▐ <-
    -> ▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟ <-



    ------
    """


def who_am_i(log):
    yield """\
    -> # Who am i? <-


    -> Entreprenoonoo <-

    <br>

     CEO - Chief Executive Officer
     CFO - Chief Financial Officer
     COO - Chief Operating Officer
     CMO - Chief Marketing Officer
     CIO - Chief Information Officer
     CCO - Chief Communications Officer
     CLO - Chief Legal Officer
     CTO - Chief Technology Officer
     CRO - Chief Risk Officer
     CCO - Chief Creative Officer
     CCO - Chief Compliance Officer
     CAE - Chief Audit Executive
     CDO - Chief Diversity Officer
    CHRO - Chief Human Resources Officer
    CBDO - Chief Business Development Officer
        
    ------
    """



def how_it_works(log):
    yield """\
    -> # How does it work? <-

    It uses back propagation of the bayes theorem with bias on big data
    through binomial distribution of chi-square test for classification
    clustering with coefficient of computational linguistics through
    confidence interval of continuous variable correlation and cross
    validation zhe2to walla ba3ed given the k-means clustering of linear
    regression while singing killoun 3indoun siyyarat w jiddi 3indou
    posterior distribution of reinforcment learning.


    Do not doubt my words, i have the best words:

    http://www.datascienceglossary.org/

    ------
    """


def codename(log):
    yield """\
    -> # but you can use the codename <-

    <br>
    [D]ata
    <br>
    [A]pproximation by
    <br>
    [R]ectangular
    <br>
    [T]ableau
    <br>
    [A]bousoulazouzou
    <br>

    or just... DARTA.

    ------
    """


def warning(log):
    yield """\
    -> # WARNING! <-



    The stats in this presentation:
        - will shock you to your core.
        - took 375 hours to compute on a 1024 core machine on Fraggle.
        - on the cloud with AWSCompuLambdaLastic say me Fantastic.
        - are very accurate, no false positives whatsoever.
        - will be sold to NSA for cash.



    Feel free to talk to me to about how it was done (5 doodoo)

    ------
    """


def outro(log):
    yield """\
    -> # assert all(map(show, slides)) <-



    -> code: tiny.cc/data-sinez <-


    -> anyone.has_question?  <= lolruby <-


    -> ▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜ <-
    -> ▌ http://aboumrad.info ▐ <-
    -> ▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟ <-

    ------
    """


def mena_devs_activity(log):
    yield """\
    -> # How is MENA Devs activity throughout the years? <-

    Since 2015

    <br>
    """

    group_by_months = log.groupby([pd.TimeGrouper(freq='M')])
    aggregated = group_by_months.agg('count')[['text']]
    flattened = aggregated.reset_index()
    flattened['ts_friendly'] = flattened['ts'].dt.strftime('%Y - %b')
    del flattened['ts']
    flattened.set_index('ts_friendly', inplace=True)
    # flattened.to_csv('yearly.csv', sep='\t')

    yield plot(flattened)
    yield '\n------\n'


def total_messages_per_user(log):
    yield """\
    -> # What are the total messages per user? <-

    Wall of shame, much shame!
    <br>
    """
    predicate = None
    then = identity
    yield from sieve(log, predicate, then)


def size_of_longest_message(log):
    yield """\
    -> # What is the size of the longest message written? <-

    Yeah, some people love to raaaaaamble rumble!
    <br>
    """

    log['count'] = log['text'].str.len()
    computed = log.groupby(['name'])['count'].max()
    sorted_ = computed.sort_values(ascending=False)[:14]
    flattened = sorted_.reset_index().set_index('name')

    yield plot(flattened)
    yield '\n------\n'


def most_links_posted(log):
    yield """\
    -> # Who posts links the most? <-

    Uncontested.
    <br>
    """
    predicate = log['text'].str.contains('http', na=False)
    then = identity
    yield from sieve(log, predicate, then)


def most_active_during_day(log):
    yield """\
    -> # Who is the most active during the day? <-

    work day in, 08:00 to 18:00
    <br>
    """

    predicate = None
    then = lambda x: x.between_time('08:00', '18:00')
    yield from sieve(log, predicate, then)


def most_active_during_night(log):
    yield """\
    -> # Who is the most active during the night? <-

    as in after work, 18:00 to 02:00
    <br>
    """

    predicate = None
    then = lambda x: x.between_time('18:00', '02:00')
    yield from sieve(log, predicate, then)


def early_birds(log):
    yield """\
    -> # Who are the early birds? <-

    as in, 04:30 to 08:00
    <br>
    """

    predicate = None
    then = lambda x: x.between_time('05:00', '08:00')
    yield from sieve(log, predicate, then)


def night_owls(log):
    yield """\
    -> # Who are the night owls? <-

    02:00 to 05:00
    <br>
    """

    predicate = None
    then = lambda x: x.between_time('02:00', '05:00')
    yield from sieve(log, predicate, then)


def most_mentioned(log):
    yield """\
    -> # Who is the most mentioned? <-

    Cannnn you feel the love tonight...
    <br>
    """

    def group(what):
        users = pd.read_json(USERS)
        result = what['text'].str.extract(
            '<@([A-Z0-9]{9})', expand=True).dropna()
        result.columns = ['name']
        result.reset_index(inplace=True)
        grouped_by_name = result.groupby('name')
        aggregated = grouped_by_name.agg(['count'])['ts']
        sorted_ = aggregated.sort_values(['count'], ascending=False)
        sorted_.reset_index(inplace=True)

        return pd.merge(
            sorted_, users,
            left_on='name', right_on='id'
        )[['name_y', 'count']].set_index('name_y')

    yield plot(group(log)[:7])

    yield '\n\nlast 30 days...\n\n'

    yield plot(group(log[last_n_days(log)])[:7])
    yield '\n------\n'


# Who is the most reacted to?
pass


def most_emojis_in_messages(log):
    yield """\
    -> # Who uses the most emojis in messages? <-

    emojibuse!
    <br>
    """

    predicate = log.text.str.match(':\S+:', na=False)
    then = identity
    yield from sieve(log, predicate, then)


# Who reacts the most with emojis?
pass


def most_dots(log):
    yield """\
    -> # Who ends their lines the most with dots? <-

    hello. how. are. you. mmmkay?
    <br>
    """

    predicate = log.text.str.endswith('.', na=False)
    then = identity
    yield from sieve(log, predicate, then)


def jollyest(log):
    yield """\
    -> # Who's the jollyest of em all? <-

    lol-y or haha-y
    <br>
    """

    predicate = log.text.str.match('haha|lol', na=False)
    then = identity
    yield from sieve(log, predicate, then)


def most_profane(log):
    yield """\
    -> # Who's the most profane? <-

    shit, fsck, btch, slt...
    <br>
    """
    negatives = [
        'shit',
        'fuck',
        'bitch',
        'slut',
    ]

    predicate = log.text.str.match('|'.join(negatives), na=False)
    then = identity
    yield from sieve(log, predicate, then)


def greeter(log):
    yield """\
    -> # Who's the greeter? <-

    mar7abaaaaa
    <br>
    """

    greetings = (
        'hello',
        'hi',
        'hey',
        'good morning',
        'good evening',
    )

    predicate = log.text.str.startswith(greetings, na=False)
    then = identity
    yield from sieve(log, predicate, then)


def most_thankful(log):
    yield """\
    -> # Who's the most thankful? <-

    dido is, dido.
    <br>
    """

    predicate = log.text.str.contains('thanks', na=False)
    then = identity
    yield from sieve(log, predicate, then)


def karma_whore(log):
    yield """\
    -> # Who's the karma whore? (oops!) <-

    take a guess
    <br>
    """

    predicate = log.text.str.contains('karma', na=False)
    then = identity
    yield from sieve(log, predicate, then)


def most_affirmative(log):
    yield """\
    -> # Who's the most affirmative? <-

    Right.
    <br>
    """

    predicate = log.text.str.contains('right', na=False)
    then = identity
    yield from sieve(log, predicate, then)


def most_dissenting(log):
    yield """\
    -> # Who's the most dissenting? (wat?) <-

    Wrong?
    <br>
    """

    predicate = log.text.str.contains('wrong', na=False)
    then = identity
    yield from sieve(log, predicate, then)


def most_active_in_programming(log):
    yield """\
    -> # Who's the most active in programming? <-

    develo2errr
    <br>
    """

    predicate = log['channel'] == 'programming'
    then = identity
    yield from sieve(log, predicate, then)


def most_active_in_announcements(log):
    yield """\
    -> # Who's the most active in announcements? <-

    rooster
    """

    predicate = log['channel'] == 'announcements'
    then = identity
    yield from sieve(log, predicate, then)


def most_active_in_general(log):
    yield """\
    -> # Who's the most active in general? <-

    Der General
    """

    predicate = log['channel'] == 'general'
    then = identity
    yield from sieve(log, predicate, then)
