#Sort Hackathons by Alphabetical Order
hackathons = ['Test Hackathon', 'Local Hack Day: Build Day 3', 'UTD Hack Reason', 'PyJaC', 'Rose 18', 'Cruz 16', 'Orion Hacks']
hackathons.sort()
print(hackathons)
#Sort Hackathons by Dates
hackathons = [
  {'name': 'Test Hackathon', 'date_of_birth': 2020},
  {'name': 'UTD Hack Reason', 'date_of_birth': 2017},
  {'name': 'PyJaC', 'date_of_birth': 2019},
  {'name': 'Rose 18', 'date_of_birth': 2018},
  {'name': 'Cruz 16', 'date_of_birth': 2016},
  {'name': 'Local Hack Day: Build Day 3', 'date_of_birth': 2021},
  {'name': 'Orion Hacks', 'date_of_birth': 2015},
]
hackathons.sort(reverse=False, key=lambda e: e['date_of_birth']) 
print(hackathons)
