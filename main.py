# Import Jinja2 Templates
#--------------------------------------------------------
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


# Initialize FastAPI application and Jinja2 templates
# -------------------------------------------------------
app = FastAPI()
templates = Jinja2Templates(directory="templates")


# Ticket data list for Helpdesk 
tickets = [
    {
        "client": "Juan Dela Cruz",
        "ticket_id": "INC-2026-0001",
        "subject": "Unable to login",
        "priority": "High",
        "type": "Technical Support",
        "request_date": "2026-10-01"
    },
    {
        "client": "Maria Santos",
        "ticket_id": "INC-2026-0002",
        "subject": "Password reset request",
        "priority": "Medium",
        "type": "Account",
        "request_date": "2026-10-01"
    },
    {
        "client": "Pedro Reyes",
        "ticket_id": "INC-2026-0003",
        "subject": "System is running slowly",
        "priority": "High",
        "type": "Technical Support",
        "request_date": "2026-10-02"
    },
    {
        "client": "Ana Garcia",
        "ticket_id": "INC-2026-0004",
        "subject": "Request for new user account",
        "priority": "Low",
        "type": "Access Request",
        "request_date": "2026-10-02"
    },
    {
        "client": "Mark Flores",
        "ticket_id": "INC-2026-0005",
        "subject": "Unable to access dashboard",
        "priority": "Critical",
        "type": "Access Issue",
        "request_date": "2026-10-03"
    }
]


# Health Check Route
@app.get('/test')
def test_route():
    return {"Message":"Runnig..."}


# Retieve all tickets
#-------------------------------------------------
@app.get('/')
@app.get('/user/{id}', include_in_schema=False)
def getUsersPost(id : int):
    return tickets

# Retrive Specific Ticket by id
#-------------------------------------------------
@app.get('/chadbot/ticket/{tck_id}', include_in_schema=False)
def getPost(request : Request, tck_id : int):
    return templates.TemplateResponse(
        request, 
        "ticket.html",
        {
            "ticket" : tickets[tck_id]   
        }
    )
