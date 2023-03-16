import json
import pandas as pd

with open("./ec2-describe-instances.json", "r") as f:
    data = json.load(f)
    data = data["Reservations"]


InstanceId = []

def transfer_time(date_time):
    date_time = date_time.replace("T", " ")
    date_time = pd.to_datetime(date_time)
    date_time = int(date_time.strftime("%Y%m%d%H%M%S"))
    return date_time

orgin_time = "2022-04-12T13:00:00"
orgin_time = transfer_time(orgin_time)


for row in data:
    time = row["Instances"][0]["LaunchTime"]
    time = transfer_time(time)
    if time <= orgin_time:
        InstanceId.append(row["Instances"][0]["InstanceId"])

print (InstanceId)