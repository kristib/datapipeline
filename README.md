# datapipeline
Sample project for building a datapipeline that requests posts from the Programming subreddit and outputs a report that lists how many days each post was in the top 100 

To run this Data Pipeline:

1. Log in to Reddit and go to www.reddit.com/prefs/apps and create an app. Then update the code/fetch_to_s3.py script with the client id and secret.
2. Go to AWS DataPipeline and create a new Pipeline
3. Import the full_pipeline.json definition (or just use the json definition as a guide as you are building your pipeline)
4. Edit the Data Pipeline in architect and update the fields as necessary (such as s3 locations, keypair, etc)
