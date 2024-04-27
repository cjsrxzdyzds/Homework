import json
import mysql.connector

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(user='root',
                              host='localhost', database='dbs')
cursor = cnx.cursor()

# Read the formatted JSON file
with open('/Users/oscar/DataGripProjects/dbs6586/kindle_reviews_formatted.json', 'r') as file:
    data = json.load(file)

# Iterate over each row in the JSON data and insert it into the table
for row in data:
    query = "INSERT INTO kindle_reviews (reviewerID, asin, reviewerName, helpful_positive, helpful_negative, reviewText, overall, summary, unixReviewTime, reviewTime) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (row.get('reviewerID', ''), row.get('asin', ''), row.get('reviewerName', ''),
              row.get('helpful', [0, 0])[0], row.get('helpful', [0, 0])[1],
              row.get('reviewText', ''), row.get('overall', 0.0), row.get('summary', ''),
              row.get('unixReviewTime', 0), row.get('reviewTime', ''))
    cursor.execute(query, values)

# Commit the changes and close the connection
cnx.commit()
cursor.close()
cnx.close()