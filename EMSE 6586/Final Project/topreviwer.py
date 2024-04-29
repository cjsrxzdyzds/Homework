import mysql.connector
import plotly.graph_objects as go

db = mysql.connector.connect(host='localhost',
                             database='dbs',
                             user='root')
cursor = db.cursor()

# Fetch reviews for September 10, 2014
query = """
    SELECT reviewerID, asin, reviewText, unixReviewTime 
    FROM kindle_reviews
    WHERE DATE(FROM_UNIXTIME(unixReviewTime)) = '2014-04-01'
"""
cursor.execute(query)

reviews = []
for row in cursor:
    reviewerID, asin, text, timestamp = row
    reviews.append((reviewerID, asin, text))

if len(reviews) == 0:
    print("No reviews found.")
    exit()

nodes = []
for i, review in enumerate(reviews):
    nodes.append({
        "review": review[2],
        "reviewerID": review[0],
        "asin": review[1],
        "x": i % 50,  # assign x coordinate based on index
        "y": i // 50  # assign y coordinate based on index
    })

node_trace = go.Scatter(x=[], y=[], text=[], mode='markers', hoverinfo='text', marker=dict(size=10))

for node in nodes:
    node_trace['x'] += tuple([node['x']])
    node_trace['y'] += tuple([node['y']])
    node_info = f"Review: {node['review']}<br>Reviewer: {node['reviewerID']}<br>Product: {node['asin']}"
    node_trace['text'] += tuple([node_info])

fig = go.Figure(data=[node_trace],
         layout=go.Layout(
             title=f"Reviews on September 10, 2014",
             showlegend=False,
             hovermode='closest',
             xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
             yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
         ))

fig.show()