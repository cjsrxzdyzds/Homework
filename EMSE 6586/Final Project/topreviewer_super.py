import mysql.connector
import datetime
import random
import plotly.graph_objects as go

db = mysql.connector.connect(host='localhost',
                             database='dbs',
                             user='root')
cursor = db.cursor()

query = """
    SELECT reviewerID, asin, reviewText, unixReviewTime 
    FROM kindle_reviews
    WHERE unixReviewTime BETWEEN %s AND %s
"""
start_date = datetime.datetime(2014, 1, 1).strftime('%s')
end_date = datetime.datetime(2014, 1, 8).strftime('%s')
cursor.execute(query, (start_date, end_date))

review_data = {}
for row in cursor:
    reviewerID, asin, text, timestamp = row
    date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    review_data.setdefault(date, []).append((reviewerID, asin, text))

# Randomly sample 1000 reviews
sampled_reviews = []
for date, reviews in review_data.items():
    sampled_reviews.extend(random.sample(reviews, min(1000, len(reviews))))

nodes = []
for review in sampled_reviews:
    nodes.append({
        "review": review[2],
        "reviewerID": review[0],
        "asin": review[1],
        "x": random.random(),  # assign random x coordinate
        "y": random.random()   # assign random y coordinate
    })

edges = []
for i, review1 in enumerate(sampled_reviews):
    for j, review2 in enumerate(sampled_reviews[i+1:]):
        if review1[0] == review2[0] or review1[1] == review2[1]:  # connect if same reviewer or product
            edges.append((i, i+j+1))

edge_trace = go.Scatter(x=[], y=[], line=dict(width=0.5, color='#888'), hoverinfo='none', mode='lines')
node_trace = go.Scatter(x=[], y=[], text=[], mode='markers', hoverinfo='text', marker=dict(size=10))

for edge in edges:
    x0, y0 = nodes[edge[0]]['x'], nodes[edge[0]]['y']
    x1, y1 = nodes[edge[1]]['x'], nodes[edge[1]]['y']
    edge_trace['x'] += tuple([x0, x1, None])
    edge_trace['y'] += tuple([y0, y1, None])

for node in nodes:
    node_trace['x'] += tuple([node['x']])
    node_trace['y'] += tuple([node['y']])
    node_info = f"Review: {node['review']}<br>Reviewer: {node['reviewerID']}<br>Product: {node['asin']}"
    node_trace['text'] += tuple([node_info])

fig = go.Figure(data=[edge_trace, node_trace],
         layout=go.Layout(showlegend=False, hovermode='closest',
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

fig.show()