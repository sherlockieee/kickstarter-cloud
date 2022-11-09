# kickstarter-cloud

To start the project locally:

1. Set up virtual environment

MacOS
```
$ python3 -m venv venv && source venv/bin/activate
```

2. Install the requirements
```
(venv)$ pip3 install -r requirements.txt
```

3. Initialize the database:
```
(venv)$ python init_db.py

4. Run the server:
```
(venv)$ uvicorn main:app --reload
```
Navigate to http://localhost:8000/ and http://localhost:8000/projects in your favorite web browser.