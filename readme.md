# Original Challenge:
https://github.com/NextGenVest/challenge


## Running the project
After cloning the repository and navigating to the project directory, install project requirements by running

`pip install -r requirements.txt`

Then run the Flask app with `python app.py`

### Making a request to the app
Unless you are using an app like Postman, you can make a request to the Flask app with
```
curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/max_scholarship -d '{"data":[[1,2,3,4,5], [1,1,2,3,5], [3,4,5,5,5], [3,4,5,9,5], [1,1,5,5,25]]}'
```

