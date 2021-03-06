#!/usr/bin/env python
import sys
import os
import pandas
import meetup.api

MADISON_ZIP = 53703
TECH_MEETUP_CATEGORY_ID = 34


def connect(meetup_api_key=None):
    """Return a connection to the Meetup.com API.

    Requires your personal Meetup API key, which you can obtain from here:
    https://secure.meetup.com/meetup_api/key/

    Parameters
    ----------
    meetup_api_key: str
        If no API key is passed, an environment variable named MEETUP_API_KEY is
        expected.
    """
    if meetup_api_key is None:
        try:
            meetup_api_key = os.environ['MEETUP_API_KEY']
        except KeyError:
            print('Error! MEETUP_API_KEY is not defined')
            sys.exit(1)

    return meetup.api.Client(meetup_api_key)


def get_madison_tech_groups(client=None):
    """Return a pandas.DataFrame of Madison-area tech meetup groups."""
    if client is None:
        client = connect()
    search_kwargs = dict(zip=MADISON_ZIP, category_id=TECH_MEETUP_CATEGORY_ID)
    response = client.GetGroups(**search_kwargs)
    return pandas.DataFrame.from_records(response.results)


def get_past_group_events(group_id, client=None):
    """Get past events for a Meetup group.

    Parameters
    ----------
    group_id : int
        Group id to get events for.

    Returns
    -------
    group_events = pandas.DataFrame
    """
    if client is None:
        client = connect()
    search_kwargs = dict(group_id=group_id, status='past')
    response = client.GetEvents(**search_kwargs)
    group_events = pandas.DataFrame.from_records(response.results)

    if len(group_events) > 0:
        # extract group name from group column of dicts
        group_events['group_name'] = group_events.group.apply(lambda d: d['name'])

    return group_events


def get_all_group_events(groups, client=None):
    """Get past events for a pandas.DataFrame of Meetup groups."""
    if client is None:
        client = connect()
    group_events = groups.id.apply(get_past_group_events, client=client)
    return pandas.concat(list(group_events), ignore_index=True)


if __name__ == '__main__':
    client = connect()
    groups = get_madison_tech_groups(client)
    events = get_all_group_events(groups)
