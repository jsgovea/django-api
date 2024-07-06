
# Django Application Setup Guide

Welcome to the Django application setup guide! Follow the steps below to get your Django application up and running. This guide will take you through cloning the repository, setting up the virtual environment, installing dependencies, applying migrations, and running the development server.

## Prerequisites

- Python (version 3.6 or above)
- Git
- pip (Python package installer)

## Installation Steps

### 1. Clone the Repository

First, clone the repository from GitHub to your local machine using the following command:

```bash
git clone https://github.com/jsgovea/django-api && cd django-api
```

### Steps to create the virtualenv
### 1. Create the virtualenv
### Windows
```bash
python -m venv env
source env/bin/activate
```

### macOS & Linux
```bash
python3 -m venv env
source env/bin/activate
```

### 2. Install the requirements
```bash
pip install -r requirements.txt
```

### 3. Apply the migrations
```bash
python manage.py migrate
```

### 4. Run the project
```bash
python manage.py runserver
```

### Open the server
Access to http://127.0.0.1:8000/