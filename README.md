# Real-Time Streaming News Intelligence System

## Overview
This project implements a real-time streaming AI system that automatically ingests live news data from the internet and processes it without any manual or user-triggered input.

---

## Problem
Traditional AI systems rely on static datasets which become outdated quickly. This project addresses the need for continuous and automated data ingestion.

---

## Solution
A push-based streaming architecture that automatically fetches live news and updates the system in real time.

---

## Architecture
News API  
→ Automated Ingestion Script  
→ news.txt (Live Data Store)  
→ Pathway Streaming Engine  
→ AI Processing Layer  

---

## Tech Stack
- Python
- Pathway
- NewsAPI

---

## Project Structure
hackathon/
|__ .gitignore
|__ .env
├── app.py
├── ingest_news.py
├── requirements.txt
├── README.md
└── data/
└── news.txt
|__ venv


---

## Setup & Execution

### Step 1: Install dependencies

pip install -r requirements.txt

---

## Step 2: Start live news ingestion

python ingest_news.py

---


## Step 3: Run the streaming AI system

python app.py

---

## Environment Setup

This project requires an external News API key.

Create a `.env` file in the root directory and add:

GNEWS_API_KEY=your_api_key_here

For security reasons, this file is excluded from version control.


## Key Features
Fully automated data ingestion
Real-time streaming updates
No user-triggered input required

---


## Use Cases
News monitoring
Market intelligence
Alerting systems

---


## Conclusion
This project demonstrates how streaming architectures and AI systems can be combined to build always-on, real-time intelligence solutions, making it highly suitable for modern data-driven applications and hackathon use cases.# realtime-streaming-news-ai
