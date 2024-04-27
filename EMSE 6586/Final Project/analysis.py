import mysql.connector
import matplotlib.pyplot as plt

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(user='root',
                              host='localhost', database='dbs')
cursor = cnx.cursor()

# Query to retrieve the length of reviews and overall ratings
query = """
SELECT LENGTH(reviewText) AS review_length, overall
FROM kindle_reviews;
"""

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Lists to store the data
review_lengths = []
overall_ratings = []

# Extract the review lengths and overall ratings from the results
for row in results:
    review_length = row[0]
    overall_rating = row[1]
    review_lengths.append(review_length)
    overall_ratings.append(overall_rating)

# Close the database connection
cursor.close()
cnx.close()

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(review_lengths, overall_ratings, alpha=0.5)
plt.xlabel('Review Length')
plt.ylabel('Overall Rating')
plt.title('Relationship between Review Length and Overall Rating')
plt.grid(True)
plt.show()