# Amazon Kindle Reviews Analysis

This project aims to restructure and analyze the Amazon Kindle reviews dataset, transforming it from its original nested JSON format into a normalized relational schema suitable for loading into a SQL database. This will facilitate efficient querying and aggregation to derive insights from the reviews data.

## Project Type
Database Translation – Restructuring and analyzing Amazon Kindle reviews dataset

## Dataset

The dataset used is the Amazon Kindle reviews dataset in JSON format, available from Kaggle. It contains information about Kindle products, reviewers, and the reviews themselves.

## Prerequisites

- Python 3.x
- MySQL database with the `kindle_reviews` table
- Required Python libraries:
  - `mysql-connector-python`
  - `pandas`

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/your-username/kindle-reviews-analysis.git
   ```

2. Install the required Python libraries:
   ```
   pip install mysql-connector-python pandas
   ```

3. Set up the MySQL database:
   - Create a MySQL database to store the Kindle reviews data.
   - Import the `kindle_reviews` table into the database. Make sure the table schema matches the following columns:
     - `reviewerID` (VARCHAR)
     - `asin` (VARCHAR)
     - `reviewerName` (VARCHAR)
     - `helpful_positive` (INT)
     - `helpful_negative` (INT)
     - `reviewText` (TEXT)
     - `overall` (FLOAT)
     - `summary` (VARCHAR)
     - `unixReviewTime` (BIGINT)
     - `reviewTime` (VARCHAR)

  The following is a sample table format:
    ```
   CREATE TABLE kindle_reviews (
    reviewerID VARCHAR(255),
    asin VARCHAR(255),
    reviewerName VARCHAR(255),
    helpful_positive INT,
    helpful_negative INT,
    reviewText TEXT,
    overall FLOAT,
    summary VARCHAR(255),
    unixReviewTime BIGINT,
    reviewTime VARCHAR(255)
    );
   ```

   You may load the dataset to your database as follow:
   ```
    LOAD DATA INFILE '/var/lib/mysql-files/kindle_reviews_formatted.json' 
    INTO TABLE kindle_reviews
    FIELDS TERMINATED BY ',' 
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    (reviewerID, asin, reviewerName, @helpful, reviewText, overall, summary, unixReviewTime, reviewTime)
    SET helpful_positive = JSON_EXTRACT(@helpful, '$[0]'),
    helpful_negative = JSON_EXTRACT(@helpful, '$[1]');
   ```

5. Configure the database connection:
   - Open the `analysis.py` file.
   - Modify the following variables with your database connection details:
     - `db_user`: MySQL database username
     - `db_password`: MySQL database password
     - `db_host`: MySQL database host
     - `db_name`: MySQL database name

## Running the Analysis

To run the analysis, execute the `analysis.py` script:

```
python analysis.py
```

The script will establish a connection to the MySQL database, perform the analysis queries, and print the results to the console.

## Analysis Examples

The script includes the following analysis examples:

1. Top 10 reviewers by number of reviews:
   - Retrieves the top 10 reviewers based on the count of their reviews.

2. Average rating and number of reviews per product (asin):
   - Calculates the average rating and the count of reviews for each product (identified by asin).

3. Reviews with the most helpful votes:
   - Retrieves the top 10 reviews with the most helpful votes, along with the reviewer ID, asin, helpful votes (positive and negative), review text, and overall rating.

Feel free to modify the analysis queries or add new ones based on your specific requirements.


## Approach

1. Data Parsing: Use Python to parse the JSON files and extract the relevant data into separate entities:
   - Reviewers: Unique reviewer IDs and metadata
   - Products: Kindle product details
   - Reviews: Linking reviewers to the products they reviewed, along with review text, rating, helpful votes, etc.

2. Schema Design: Design a normalized schema for the extracted data, creating separate tables for Reviewers, Products, and Reviews. Establish appropriate primary and foreign key relationships between the tables.

3. Data Loading: Transform the parsed data into DataFrames matching the designed schema, and load them into a PostgreSQL database using SQLAlchemy.

4. Analysis: Utilize SQL queries to perform various analyses on the restructured data, such as:
   - Examining reviewer behavior over time
   - Aggregating ratings and reviews per product
   - Analyzing the distribution of review ratings
   - Identifying most helpful reviews and their characteristics
   - Exploring time-based trends in product popularity


## Usage

1. Clone the repository.
2. Install the required Python libraries.
3. Set up a PostgreSQL database and update the database connection details in the code.
4. Place the Amazon Kindle reviews JSON files in the designated directory.
5. Run the data parsing and loading script to process the JSON files and load the data into the database.
6. Use SQL queries to perform the desired analyses on the restructured data.

## Contributors

- Ying Liu @598790089
- Jiaye Fang @cjsrxzdyzds

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

- The Amazon Kindle reviews dataset is sourced from Kaggle.
- Thanks to the open-source community for the libraries and tools used in this project.

## Link to the Dataset
https://www.kaggle.com/datasets/bharadwaj6/kindle-reviews/data
