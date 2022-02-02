# 888 Assignment

---

## Requirements

- Python 3.9.2
- pip
- venv

---

## Flask app

### Execute Flask app

- Create a virtual environment
  For Mac OS/Linux

```commandline
python -m venv venv
source venv/bin/activate
```

- Install project requirements.

```commandline
pip install -r requirements.txt
```

- Set PYTHONPATH to repository path in local filesystem.
  For Mac OS/Linux, Navigate to project path and run the following command:

```
export PYTHONPATH=`pwd`
```

- Run Flask app.

```commandline
python run_app.py
```

To see options for the script, run the following

```commandline
python run_app.py -h
usage: Parse arguments for flask server [-h] [--host HOST] [--port PORT] [--debug]

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Host/IP to use for the server
  --port PORT  Port to use for the server
  --debug      Start app in debug mode
```

### Usage and endpoint information

All responses will have one of the following forms

```
{
  data in json form
}
```

OR

```json
{
  "message": "A message containing extra details"
}
```

OR

```
Http Codes
```

#### List resources

- `GET /sports`
- `GET /events`
- `GET /selections`

#### List a specific resource

- `GET /sports/<name>`
- `GET /events/<name>`
- `GET /selections/<name>`

#### Create a resouce

- `POST /sports`

Body: application/json

```
{
	"name": "Name of sport. Whitespaces and underscores replaced by hyphen",
	"slug": "Any string",
	"active": 1 // 1 represents true and 0 represents false
}
```

example

```json
{
  "name": "football",
  "slug": "http://football",
  "active": 1
}
```

- `POST /events`

Body: application/json

```
{
    "name": "name of event. Whitespaces and underscores replaced by hyphen",
	"slug": "any string",
	"sport_name": "name of sport to associate with",
	"active": 1 // 1 represents true and 0 represents false,
	"event_type": ("preplay" or "inplay"),
	"status": ("pending", "started", "ended", "cancelled"),
	"scheduled_start": "YYYY-MM-DD HH:MM:SS"
	"actual_start": "YYYY-MM-DD HH:MM:SS" (Optional)
}
```

example

```json
{
  "name": "sl-vs-ire",
  "slug": "http://game-link",
  "sport_name": "cricket",
  "active": 0,
  "event_type": "preplay",
  "status": "pending",
  "scheduled_start": "2022-01-01 10:10:10"
}
```

- `POST /selections`

Body: application/json

```
{
    "name": "name of selection. Whitespaces and underscores replaced by hyphen",
	"event_name": "event name to associate with",
	"price": "Decimal value, to 2 decimal places",
	"active": 1 // 1 represents true and 0 represents false,
	"outcome": ("unsettled", "void", "lose", "win")),
}
```

example

```json
{
  "name": "loss",
  "event_name": "sl-vs-ire",
  "price": 10.0,
  "active": 1,
  "outcome": "unsettled"
}
```

#### Update a resource

- `PATCH /sports/<name>`
- `PATCH /events/<name>`
- `PATCH /selections/<name>`

#### Start an event

- `POST /events/<name>/started`

---

## Tree Problem

No special requirements such as venv, extra libs in requirements needed.
Run the following command:

```commandline
python tree_solution.py
```

---
