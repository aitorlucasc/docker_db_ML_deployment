# Part 1 - ETL with containerized databases
In the part 1 folder, we have created a simple ETL workflow using different database engines. We have used docker images on MySQL and MongoDB and tabular data that comes from a csv file. The main steps are:

- Data ingestion from csv file to each containerized database.
- Connect to the current table.
- Execute a query and save it for other purposes.

Use your favorite database IDE to look the tables, in my case I have used DataGrip.


# Part 2 - Deploying ML model as a service (with Flask)

To play a bit with endpoints and a ML model, we have deployed a simple app with Flask which does:
- Model creation with a simple logistic regression.
- Model storing in pickle format.
- App that gets a test set and returns a prediction.




To run the environment:
```
python3 -m venv /path/to/new/virtual/environment
source env/bin/activate
pip install -r requirements.txt
```
