# Amazon Kindle Reviews Analysis

This project aims to restructure and analyze the Amazon Kindle reviews dataset, transforming it from its original nested JSON format into a normalized relational schema suitable for loading into a SQL database. This will facilitate efficient querying and aggregation to derive insights from the reviews data.

## Project Type
Database Translation – Restructuring and analyzing Amazon Kindle reviews dataset

## Dataset

The dataset used is the Amazon Kindle reviews dataset in JSON format, available from Kaggle. It contains information about Kindle products, reviewers, and the reviews themselves.

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

## Requirements

- Python 3.x
- PostgreSQL
- Python libraries: json, pandas, sqlalchemy

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
