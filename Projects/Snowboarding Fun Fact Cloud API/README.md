# Snowboarding Fun Fact Cloud API

**Description:**
A Flask-based REST API deployed on an AWS EC2 instance that serves random snowboarding fun facts and request metadata. The application is hosted using Gunicorn and NGINX on an Ubuntu EC2 instance.

**Technologies Used:**
- Python 3.x
- Flask
- AWS EC2
- Gunicorn
- NGINX

**Features:**
- `/fact` endpoint returns a chosen number of random snowboarding fun facts.
- `/info` endpoint returns the current time, the requester's user agent, and the HTTP method.
- Hosted on AWS EC2 using Gunicorn and NGINX.
- Includes a Python test script for automated endpoint testing.

**How to Run:**

Using curl:
```bash
curl -H "Amount: 3" http://18.222.15.18/fact
```
```bash
curl http://18.222.15.18/info
```

Using the test script:
```bash
python test_file_pa5.py
```
This script issues GET requests to both `/fact` and `/info` and prints the JSON responses returned by the API.
