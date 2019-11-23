# Eportfolio2
Rayner's eportfolio
Test Case Coverage Screenshot:EPORTFOLIO/Test Coverage Screenshot.PNG
Test Case Document: EPORTFOLIO2/CA Test Document.docx
Pytest file: EPORTFOLIO2/test_functions.py

Note: Should the blog not show images when you run 'python manage.py runserver', use 'python manage.py runserver --insecure'


Justification 

26 Test cases passed and 8 failed. The 8 failed test cases are justified below. Unfortunately, testing such as latency/ load testing could not be done with selenium. 

Test Case 19
Results: Failed
Reason of Failure: I tried testing inputting Emojis but Selenium couldn’t accept it as input.
Error Message:
selenium.common.exceptions.WebDriverException: Message: unknown error: ChromeDriver only supports characters in the BMP
E(Session info: chrome=78.0.3904.108)

Test Case 26
Results: Failed
Reason of Failure:  Selenium couldn’t accept it as input.
Error Message:
selenium.common.exceptions.WebDriverException: Message: unknown error: ChromeDriver only supports characters in the BMP
E(Session info: chrome=78.0.3904.108)
Test Case 5
Results: Failed
Reason of Failure:  Environment error. Spent 1 day searching for solution. Seen a video an Indian guy on youtube trying to fix the error but to no avail.
Error Message:
% (desc, ENVIRONMENT_VARIABLE))
E   django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.

Test Case 6
Results: Failed
Reason of Failure:  Environment error. Spent 1 day searching for solution. Seen a video an Indian guy on youtube trying to fix the error but to no avail.
Error Message:
% (desc, ENVIRONMENT_VARIABLE))
E   django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
Test Case 7
Results: Failed
Reason of Failure:  Environment error. Spent 1 day searching for solution. Seen a video an Indian guy on youtube trying to fix the error but to no avail.
Error Message:
% (desc, ENVIRONMENT_VARIABLE))
E   django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.


Test Case 8
Results: Failed
Reason of Failure:  Environment error. Spent 1 day searching for solution. Seen a video an Indian guy on youtube trying to fix the error but to no avail.
Error Message:
% (desc, ENVIRONMENT_VARIABLE))
E   django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
Test Case 12
Results: Failed
Reason of Failure:  Environment error. Spent 1 day searching for solution. Seen a video an Indian guy on youtube trying to fix the error but to no avail.
Error Message:
% (desc, ENVIRONMENT_VARIABLE))
E   django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
Test Case 13
Results: Failed
Reason of Failure:  Environment error. Spent 1 day searching for solution. Seen a video an Indian guy on youtube trying to fix the error but to no avail.
Error Message:
% (desc, ENVIRONMENT_VARIABLE))
E   django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.


