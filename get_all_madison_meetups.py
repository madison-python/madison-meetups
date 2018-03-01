#!/usr/bin/env python
import os
import pandas
import meetup.api

key = os.environ['MEETUP_API_KEY']
client = meetup.api.Client(key)

def get_madison_tech_groups():
    return client.GetGroups(zip=53703, category_id=34).results

def get_group_events(i):
    return pandas.DataFrame.from_records(client.GetEvents(group_id=i, status='past').results)

# madison_tech = get_madison_tech_groups()
# tech_data = pandas.DataFrame.from_records(madison_tech)
# group_events = tech_data.id.apply(get_group_events)
# group_events2 = pandas.concat(group_events, ignore_index=True)
