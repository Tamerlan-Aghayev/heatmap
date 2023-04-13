import json
import random

# create user object
user = {
    "id": 1,
    "login":"enery",
    "email": f"user{random.randint(1, 100)}@example.com",
    "password": "password",
    "Discount": 1000,
    "limit": 100,
    "RegionId": 1
}

# create months list
months = []
for i in range(1, 13):
    month = {
        "id": i,
        "name": i,
        "userId": 1
    }
    months.append(month)

# create days list
days = []
for month in months:
    for i in range(1, 32):
        day = {
            "id": len(days) + 1,
            "DayNumber": i,
            "MonthId": month["id"]
        }
        days.append(day)

# create hours list
hours = []
for day in days:
    for i in range(1, 25):
        hour = {
            "id": len(hours) + 1,
            "DayId": day["id"],
            "Consumption": random.randint(80, 240)
        }
        hours.append(hour)

# create JSON data
data = {
    "User": user,
    "Months": months,
    "Days": days,
    "Hours": hours
}

# write data to file
with open("data.json", "w") as outfile:
    json.dump(data, outfile)
