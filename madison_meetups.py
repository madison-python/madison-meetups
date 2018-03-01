#!/usr/bin/env python

import os
import pandas as pd
import meetup.api

if os.getenv('MEETUP_API_KEY') is not None:
    key = os.getenv('MEETUP_API_KEY')
else:
    raise OSError('Missing "MEETUP_API_KEY" environment variable.')
    
client = meetup.api.Client(key)


def get_madison_tech_groups(category_id=34):
    """Uses meetup api to get information about tech meetup groups in Madison, WI
    
    Parameters
    ----------
    category_id : int, optional
        Meetup category to groups belong to (default is 34, which correspond to 
        tech meetups).
    
    Returns
    -------
    groups : pandas.DataFrame
    """
    groups = client.GetGroups(zip=53703, category_id=category_id).results
    # Want to return a nice DataFrame instead of a list of dictionaries 
    groups = pd.DataFrame.from_records(groups)
    return groups


def get_group_events(group_id):
    """Uses meetup api to get event related information for a meetup group
    
    Parameters
    ----------
    group_id : int
        Group id to get events for.
        
    Returns
    -------
    group_events = pandas.DataFrame
    """
    group_events = client.GetEvents(group_id=group_id, status='past').results
    # Want to return a nice DataFrame instead of a list of dictionaries 
    group_events = pd.DataFrame.from_records(group_events)
    
    return group_events

