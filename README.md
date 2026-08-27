# User Management System — CLI Application

This project is a clean, layered, and structured User Management System built in Python.
Although simple in functionality, the architecture reflects a system-level engineering mindset:
deterministic flow, explicit data handling, separation of concerns, and clarity over abstraction.
It demonstrates how a developer with a C background approaches Python with discipline and structure.

--- 

## Architecture Overview

The project is organized into four distinct layers, each with a single responsibility.
This keeps the codebase maintainable, testable, and easy to reason about.

user-manager/
    main.py        → Application entry point
    loop.py        → Program controller (state machine)
    core.py        → Business logic and user interaction
    database.py    → Persistence layer (JSON storage)

---

## Layer Details

main.py — Entry Point
A minimal bootstrap that initializes the main loop.
Keeps startup logic clean and avoids mixing responsibilities.

loop.py — Program Controller
Implements the main program loop as a simple state machine:
- Displays menu options
- Receives user input
- Dispatches operations
- Saves data on exit

Ensures deterministic program flow, similar to system-level design principles.

core.py — Business Logic
Handles:
- Input validation
- Menu rendering
- User operations (add, delete, list, statistics)

Focused purely on logic and user interaction, without touching storage.

database.py — Persistence Layer
A thin abstraction over JSON storage:
- Reads and writes user data
- Provides CRUD operations
- Implements sorting
- Uses pathlib for portable file paths
- Uses TypedDict for structured user objects

Isolates all I/O operations from the rest of the system.

---

## Features

- Add new users
- Delete users by name and age
- List all registered users
- Sort users by age or name (ascending/descending)
- Calculate average age
- Display minimum and maximum ages
- Count total users
- Persistent JSON storage
- Safe input handling
- Clean multi-layer architecture
- Full type hints across the codebase

---

# Running the Program
- python3 main.py

The program will automatically create user-data.json if it does not exist.

---

# Example User Object:
```
    {
        "name": "Mustapha",
        "job": "Programmer",
        "age": 18,
        "email": "SysDevMustapha@gmail.com"
    }

```

---

## Why This Project Matters

Even though the application is simple, the engineering approach behind it is not.
It demonstrates:

- Clear separation of layers
- Predictable data flow
- Minimal side effects
- Explicit control over program state
- Clean abstractions
- Readable, maintainable code

A practical example of applying system-level thinking (C-style discipline) to Python development.

---

# License
- MIT License

---
# Author
- Mustapha, System Level Developer,
- Mashhad, Iran
