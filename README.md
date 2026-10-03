# Chadbot Helpdesk Ticketing API

A RESTful API for managing helpdesk tickets, clients, priorities, and support requests.

## Status 

🟠 in progress

## Features

- Create and manage support tickets
- Track ticket IDs and request dates
- Manage clients
- Set ticket priority
- Categorize ticket types
- Retrieve ticket information through API endpoints

## Tech Stack
- Python
- FastAPI
- Jinja2
- REST API
- Git


## Project Structure

```bash
chadbot-helpdesk-ticketing-api/
├── main.py
├── templates/
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation
Clone the repository:

```bash
git clone https://github.com/your-username/chadbot-helpdesk-ticketing-api.git
cd chadbot-helpdesk-ticketing-api
```

Create and activate a virtual environment:
```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Running the Application


Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```bash
http://127.0.0.1:8000
```

API documentation:

```bash
http://127.0.0.1:8000/docs
```

```bash
Example Ticket
{
  "client": "Juan Dela Cruz",
  "ticket_id": "INC-2026-0001",
  "subject": "Unable to login",
  "priority": "High",
  "type": "Technical Support",
  "request_date": "2026-10-03"
}
```

License

This project is licensed under the MIT License. See the LICENSE file for details.