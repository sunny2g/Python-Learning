

"""
import json
from datetime import datetime

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


# Specify the path where the file will be saved
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = f"data/Sample_{current_datetime}.json"

# Open the file in write mode ('w') and use json.dump() to write data
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)  # 'indent=4' formats the JSON data for better readability

print(f"Data has been written to {file_path}")

"""






