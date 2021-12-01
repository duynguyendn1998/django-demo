1. Install djanggo: pip install Django
2. Create project: In cmd, django-admin startproject NewProject
  Note: name project avoid use "Django" or "Test"
3. Run server: 
  - Run with port default: python manage.py runserver
  - Run with port 8080:  python manage.py runserver 8080
3. Django MTV pattern
  - MTV: Model-Template-View
  - Model (M): Logical data structure
  - Template (T): Presentation layer
  - View (V): Data formatting
  - Working flow of Django framework: Template --> View --> Models --> View --> Template
4. The project structure
  - manage.py: used as a command-line utility for our projects (use for debugging, deploying and runing our web applications)
  - __init__.py: the Python interpreter
  - asgi.py: (Asynchronours server gateway interface) the same wsgi
  - setting.py: project configuration
  - urls.py: URLs of web pages to link web pages together
  - wsgi.py: (web server gateway interface)deploy project to server
  
  