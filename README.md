# ABCD Bank - Credit Card Validator


To run in your machine
===================
* Make a virtualenv
* Install dependencies `pip install -r requirements.txt`
* Run migrations `python manage.py migrate`
* Collect static data `python manage.py collectstatic --noinput`
* Run the server `python manage.py runserver`

Open in your browser http://localhost:8000

A form will be displayed, with some instructions about how to input data and the format.
You can input data manually in the TextField or upload a file.

After submit, the application will output if the given card number is Valid or Invalid.
It will check in the same order as the file uploaded or in the order of the text in the TextField.

To run tests: `python manage.py test`

The live demo is hosted at https://anchorapp.herokuapp.com/