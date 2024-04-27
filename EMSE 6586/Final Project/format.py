import json

# Read the JSON file
with open("/Users/oscar/DataGripProjects/dbs6586/kindle_reviews.json", "r") as file:
    data = file.readlines()

# Format the JSON data
formatted_data = []
for line in data:
    formatted_data.append(json.loads(line))

# Save the formatted data to a new JSON file
with open("/Users/oscar/DataGripProjects/dbs6586/kindle_reviews_formatted.json", "w") as file:
    json.dump(formatted_data, file, indent=4)