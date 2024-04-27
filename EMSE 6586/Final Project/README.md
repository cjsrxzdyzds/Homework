# Amazon Kindle Reviews Analysis

This project aims to restructure and analyze the Amazon Kindle reviews dataset, transforming it from its original nested JSON format into a normalized relational schema suitable for loading into a MySQL database running in a Docker container. This will facilitate efficient querying and aggregation to derive insights from the reviews data.

## Project Type
Database Translation – Restructuring and analyzing Amazon Kindle reviews dataset

## Dataset
The dataset used is the Amazon Kindle reviews dataset in JSON format, available from Kaggle. It contains information about Kindle products, reviewers, and the reviews themselves.

## Prerequisites
- Docker
- Docker Compose
- Python 3.x
- Required Python libraries:
  - `mysql-connector-python`
  - `pandas`

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/cjsrxzdyzds/Homework/tree/main/EMSE%206586/Final%20Project.git
   cd kindle-reviews-analysis
   ```

2. Install the required Python libraries:
   ```
   pip install mysql-connector-python pandas
   ```

3. Build and start the MySQL database using Docker Compose:
   ```
   docker-compose up -d
   ```

   This will start a MySQL container with the necessary configurations.

4. Connect to the MySQL container:
   ```
   docker exec -it mysql-container bash
   ```

   Replace `mysql-container` with the actual name of your MySQL container.

5. Inside the container, connect to the MySQL database:
   ```
   mysql -u root -p
   ```

   Enter the root password when prompted.

6. Create the `kindle_reviews` database:
   ```sql
   CREATE DATABASE kindle_reviews;
   USE kindle_reviews;
   ```

7. Create the `kindle_reviews` table:
   ```sql
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

8. Preprocess the JSON file:
   - Download the Kindle reviews JSON file from Kaggle and place it in the project directory.
   - Run the preprocessing script to format the JSON file:
     ```
     python format.py
     ```

     This script will clean and format the JSON file, fixing any formatting errors and creating a new file named `kindle_reviews_formatted.json`.

9. Load the preprocessed JSON file into the MySQL database:
   ```sql
   LOAD DATA INFILE '/var/lib/mysql-files/kindle_reviews_formatted.json'
   INTO TABLE kindle_reviews
   FIELDS TERMINATED BY ',' 
   ENCLOSED BY '"'
   LINES TERMINATED BY '\n'
   (reviewerID, asin, reviewerName, @helpful, reviewText, overall, summary, unixReviewTime, reviewTime)
   SET helpful_positive = JSON_EXTRACT(@helpful, '$[0]'),
       helpful_negative = JSON_EXTRACT(@helpful, '$[1]');
   ```

   Make sure the `kindle_reviews_formatted.json` file is accessible to the MySQL container.

   ```
   python load_json.py
   ```

   It can also help you load data into MySQL if the above query doesn't work.

11. Configure the database connection in the `analysis.py` script:
    - Open the `analysis.py` file.
    - Modify the following variables with your database connection details:
      - `db_user`: MySQL database username
      - `db_password`: MySQL database password
      - `db_host`: MySQL database host (use the container name)
      - `db_name`: MySQL database name

12. Run the analysis script:
    ```
    python proposed_analysis.py
    ```

    This script will connect to the MySQL database, perform the analysis queries, and print the results.

## Analysis Examples

The `proposed_analysis.py` script includes the following analysis examples:

1. Top 10 reviewers by number of reviews:
   - Retrieves the top 10 reviewers based on the count of their reviews.

2. Average rating and number of reviews per product (asin):
   - Calculates the average rating and the count of reviews for each product (identified by asin).

3. Reviews with the most helpful votes:
   - Retrieves the top 10 reviews with the most helpful votes, along with the reviewer ID, asin, helpful votes (positive and negative), review text, and overall rating.

Feel free to modify the analysis queries or add new ones based on your specific requirements.

## Contributing

Main Contributor: 
- Ying Liu @598790089
- Jiaye Fang @cjsrxzdyzds
- 
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

- The Amazon Kindle reviews dataset is sourced from Kaggle.
- Thanks to the open-source community for the libraries and tools used in this project.

## Link to the Dataset

https://www.kaggle.com/datasets/bharadwaj6/kindle-reviews/data
