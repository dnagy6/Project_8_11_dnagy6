# Hybrid Training & Pace Calculator V2

**Project Video Presentation:** [Link to Unlisted YouTube Video](https://youtu.be/8AOz2H_EG-Q)  
**Project Slide Deck:** [Link to Google Slides](https://docs.google.com/presentation/d/1fs5lQFq-5wVeypMbBFbSkCRuFw7UbPtuIqM0wSUT5IE/edit?usp=sharing)

---

## Project Overview

The **Hybrid Training & Pace Calculator V2** is a terminal-based utility designed to calculate barbell percentages for strength training and endurance pacing splits. This project serves as a comprehensive refactor of a monolithic Python script into a fully modular, object-oriented software architecture. 

Designed by an Orangetheory Fitness coach and Pre-ISE student at The Ohio State University, this tool brings physiological precision and software engineering best practices together.

## Core Features 

This project demonstrates core competencies in software development (Chapters 8-11), including:

* **Modular Architecture:** Core logic is decoupled into distinct calculation engines (`LiftingCalculator` and `PacingCalculator`) for strict separation of concerns.
* **Object-Oriented Programming (OOP):** Utilizes a flat class structure to encapsulate mathematical logic, stateful training templates, and data formatting.
* **JSON Data Persistence:** Automatically saves and loads athlete PRs across sessions using Python's `json` module, preventing data loss when the terminal closes.
* **Graceful Exception Handling:** Implements `try/except` blocks to catch user input errors without crashing the application.
* **Automated Unit Testing:** Includes a robust test suite using Python's `unittest` framework to mathematically verify floating-point precision and formula accuracy prior to execution.

## Installation & Execution

To run this application locally, follow these steps:

1. Clone this repository to your local machine:
   ```bash
   git clone <your-repository-url>
