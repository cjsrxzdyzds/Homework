import mysql.connector
import pandas as pd

# Set up database connection
db_user = 'root'
db_host = 'localhost'
db_name = 'dbs'

def create_connection():
    connection = mysql.connector.connect(
        user=db_user,
        host=db_host,
        database=db_name
    )
    return connection

# Example analysis queries
def run_analysis(connection):
    # Example 1: Top 10 reviewers by number of reviews
    query_1 = '''
        SELECT reviewerID, COUNT(*) as review_count
        FROM kindle_reviews
        GROUP BY reviewerID
        ORDER BY review_count DESC
        LIMIT 10;
    '''
    result_1 = pd.read_sql(query_1, connection)
    print("Top 10 reviewers by number of reviews:")
    print(result_1)

    # Example 2: Average rating and number of reviews per product (asin)
    query_2 = '''
        SELECT asin, AVG(overall) as avg_rating, COUNT(*) as review_count
        FROM kindle_reviews
        GROUP BY asin;
    '''
    result_2 = pd.read_sql(query_2, connection)
    print("Average rating and number of reviews per product (asin):")
    print(result_2.head())

    # Example 3: Reviews with the most helpful votes
    query_3 = '''
        SELECT reviewerID, asin, helpful_positive, helpful_negative, reviewText, overall
        FROM kindle_reviews
        ORDER BY helpful_positive DESC
        LIMIT 10;
    '''
    result_3 = pd.read_sql(query_3, connection)
    print("Reviews with the most helpful votes:")
    print(result_3)

# Main execution
if __name__ == '__main__':
    connection = create_connection()

    run_analysis(connection)

    connection.close()