# Sequential Thinking Demo

This is a simple Flask application that demonstrates sequential thinking with Multi-Chain Programming (MCP).

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`

## API Endpoints

- GET `/`: Returns a hello world message
- GET `/greet/<name>`: Returns a personalized greeting message for the provided name

## Example Usage

```bash
# Get general greeting
curl http://localhost:5000/

# Get personalized greeting
curl http://localhost:5000/greet/John
```