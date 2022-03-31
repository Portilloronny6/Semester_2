# Selenium with python
This is the final project to the course: https://stepik.org/course/575

The project implemented autotests based on a Page Object pattern for the [Training site](http://selenium1py.pythonanywhere.com/) 


### Requirements
```
pytest==5.1.1
selenium==3.14.0
```
### Getting started
These instructions will get you a copy of the project up and running on your local machine for testing purposes.
```
git clone https://github.com/ArtV1ctory/final_task_stepik_autotests_course.git
cd final_task_stepik_autotests_course
pip install -r requirements.txt
```
## Running tests
To run basic tests for a review:
```
pytest -v --tb=line --language=en -m need_review
```

### More tests

The project also presents autotests of two different pages for guests and authorized users:

```
pytest --tb=line test_main_page.py
pytest --tb=line test_product_page.py
pytest --tb=line -m guest_add_good_to_basket
pytest --tb=line -m login_guest
pytest --tb=line -m registered_guest_add_good
```
