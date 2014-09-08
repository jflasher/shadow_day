# Shadow for a Day
A simple Django project utilizing DRF and a frontend to prototype out what a mentor/shadow match system might look like. Based on initial conversations at a 2014 OSTP Data Jam.


## Backend API
You will need [Python 2.7.x](https://www.python.org/) installed, I am using 2.7.5.

I'd recommend using [virtualenv](https://pypi.python.org/pypi/virtualenv) to isolate project requirements but it's not necessary.

For local development, from the root directory, run the following command to install requirements (first time only)

    pip install -r requirements/development.txt
    
To create the database initially, run the below (first time only)
    
    python manage.py syncdb --settings=shadow_day.settings.development

Once installation is complete, you can start the server with the following command

    python manage.py runserver --settings=shadow_day.settings.development

This will give you access to a url like http://localhost:8000/mentors


## Frontend Beautifulness
To see the frontend, you will need to serve the pages in the gh_pages branch via a local file server or by opening locally. I utilize two working directories on my computer, one pointed to the frontend branch and one pointed backend branch to make it easiest to work on them simultaneously.

*Feel free to fork and submit PRs, I will review them as quickly as I can. If there are any questions, just let me know!*
