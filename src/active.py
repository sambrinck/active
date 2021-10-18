#!/bin/env python
from church_of_jesus_christ_api import ChurchOfJesusChristAPI
# import church_of_jesus_christ_api 
from os import environ
import datetime
import json


# church_of_jesus_christ_api.church_of_jesus_christ_api.ChurchOfJesusChristAPI.get_attendance()

username = environ.get('CHURCH_USERNAME', "sambrinck")
password = environ.get('CHURCH_PASSWORD', "oEqa8t3T1NWyJIWWcpQY")

api = ChurchOfJesusChristAPI(username, password)

# Same as api.get_birthdays(unit=api.user_details['homeUnits'][0])
# birthday_list = api.get_birthdays()

# for month in birthday_list:
#     for member in month['birthdays']:
#         birthdate = datetime.datetime.strptime(member['birthDayFormatted'], '%d %b').date()
#         if birthdate.month == today.month and birthdate.day == today.day:
#             print(f"It's {member['spokenName']}'s birthday today!")

#             # Use email or phone to automate sending a birthday message here if desired...

# # Same as api.get_moved_in(unit=api.user_details['homeUnits'][0])

# moved_in_list = api.get_moved_in()
# print(json.dumps(moved_in_list[0],indent=3))
# for record in moved_in_list:
#     move_date = birthdate = datetime.datetime.strptime(record['moveDate'], '%d %b %Y').date()
#     if (today - move_date) < datetime.timedelta(days=31):
#         print(f"Records for {record['name']} arrived to the unit this month")

# #         # Use email or phone to automate sending a message to welcome them to the unit...

# moved_out = api.get_moved_out()
# print(json.dumps(moved_out[0],indent=3))
# for member in moved_out:
#     move_date = datetime.datetime.strptime(member['moveDate'], '%Y%m%d').date()
#     # moveDate = datetime.datetime.strptime(member['birthDayFormatted'], '%d %b').date()
#     # print(f" Member: {member['name']} moved out  {datetime.datetime.fromtimestamp(int(member['moveDate'])).date()}")# datetime.timedelta(member['birthDayFormatted'])

#     if (today - move_date) < datetime.timedelta(days=31):
#         print(f" {member['name']} moved out  {move_date}")# datetime.timedelta(member['birthDayFormatted'])

adults = {}
members = api.get_member_list()
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
for member in active: #type: int
    member: str
    name=member.split(', ')
    print(f'{name[1]} {name[0]}')
# print('\n'.join(active))
print (f"{len(active)} Memebers have come at least 1 times in the last month")
 