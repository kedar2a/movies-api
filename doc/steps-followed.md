# RESTful API for movies

## 1. Create folder structure, virtualenv and activate env
- `$ mkdir fynd && cd fynd`
- `$ python3.6 -m venv venv-fynd`
- `$ source venv-fynd/bin/activate`

## 2. Installation, Initialization:
- `$ pip install django djangorestframework`
- `$ django-admin startproject data_gallery_project`
- `$ cd data_gallery_project/`
- `$ django-admin startapp movies`
- `$ pip freeze > requirements.txt`
- `$ python manage.py runserver`  <!-- to check installation -->
- `$ python manage.py migrate`
- `$ python manage.py createsuperuser --email admin@example.com --username admin`

## 3. Django routine:
- Added entry in main `urls.py` file.
- Defined your `models.py` DB classes.
- Registered `Movie` class to Django's admin.
- `$ python manage.py makemigrations`
- `$ python manage.py migrate`

## 4. DRF:
- Adding `serializers` corresponding to model classes.
- Creating views, urls w.r.t DRF.
- Testing initial list, retrieve and create operation

## 5. Importing sample data:
- Added new command to import sample json data

## 6. Heroku Deployment:
- Create an app on Heroku.
- Install heroku toolbelt on local system
- Auto deployment strategy on update of: repo + branch
- Add necessary code/files:
    + `Procfile`
    + `runtime.txt`
    + Some changes in `settings.py`
    + Defining env vars in heroku for application.
- DB addon
- Creating superuser: `createsuperuser`
- Uploading data from JSON file: `bulk_upload` 


---

## Pending:
- Search functionality
- Patch/Update, delete implementation
- Documenting APIs with swagger
- Proper response after POST, PUT, PATCH operation.
- Documenting future scalability use cases
- Returning reply with proper HTTP status codes

## Verify:
- Read through DRF and check for optimal implementation.