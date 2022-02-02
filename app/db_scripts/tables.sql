CREATE TABLE IF NOT EXISTS sport (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT NOT NULL,
    active BOOLEAN NOT NULL CHECK (active IN (0, 1)),
    UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS event (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT NOT NULL,
    active BOOLEAN NOT NULL CHECK (active IN (0, 1)),
    event_type TEXT NOT NULL CHECK (event_type IN ("PREPLAY", "INPLAY")),
    sport_name TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ("PENDING", "STARTED", "ENDED", "CANCELLED")),
    scheduled_start TEXT NOT NULL,
    actual_start TEXT,
    UNIQUE(name),
    FOREIGN KEY(sport_name) REFERENCES sport(name)
);

CREATE TABLE IF NOT EXISTS selection (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    event_name TEXT NOT NULL,
    price REAL NOT NULL,
    active BOOLEAN NOT NULL CHECK (active IN (0, 1)),
    outcome TEXT NOT NULL CHECK (outcome in ("UNSETTLED", "VOID", "LOSE", "WIN")),
    UNIQUE(name),
    FOREIGN KEY(event_name) REFERENCES event(name)
);