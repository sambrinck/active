#!/usr/bin/env python
from church_of_jesus_christ_api import ChurchOfJesusChristAPI
# import church_of_jesus_christ_api 
from os import environ
import datetime
import json

def getActiveMembers() -> list[str]:
    # church_of_jesus_christ_api.church_of_jesus_christ_api.ChurchOfJesusChristAPI.get_attendance()

    username = environ.get('CHURCH_USERNAME', "sambrinck")
    password = environ.get('CHURCH_PASSWORD', "oEqa8t3T1NWyJIWWcpQY")

    api = ChurchOfJesusChristAPI(username, password)

    adults = {}
    members = api.get_member_list()
    print(f"Got {len(members)} Members")
    for member in members:
        if member["age"] >= 18:
            adults[member['uuid']] = {
                'age': member['age'],
                'name': member['nameFormats']['listPreferredLocal']
            }
    # print(json.dumps(adults,indent=3))
    attendance = api.get_attendance()
    # print(json.dumps(attendance,indent=3))
    active = []
    for member in attendance['attendees']:
        if member['uuid'] in adults:
            try:
                attended = len([True for week in member['entries'] if week['markedAttended']]) 
                if attended >= 1: 
                    active.append(member['displayName'])
            except:
                print(f"{member['displayName']} didn't work" )
            # print(f"{attended} / {total} - {member['displayName']}")
    # print(active)
    active.sort()
    return [" ".join(n.split(", ")[::-1]) for n in active]

if __name__ == "__main__": 
    active = getActiveMembers()
    for member in active: #type: int
        member: str
        name=member.split(', ')
        print(f'{name[1]} {name[0]}')
    # print('\n'.join(active))
    print (f"{len(active)} Memebers have come at least 1 times in the last month")
    