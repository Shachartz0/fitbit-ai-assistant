Fitbit Conversational AI – POC

This repository contains a proof-of-concept conversational AI assistant designed for the Fitbit app.
The assistant demonstrates how LLMs can be orchestrated to deliver personalized, data-grounded health insights while maintaining safety, trust, and an empathetic tone.

The focus of this POC is on architecture, reasoning, data grounding, and evaluation, rather than UI or production deployment.

Overview
The assistant enables users to ask natural language questions such as:
“How did I sleep last night?”
“Am I more active this week than last week?”
It responds with explicitly grounded insights based on mock Fitbit data (sleep, steps, heart rate) and offers gentle follow-up suggestions when appropriate.

Architecture
The system is implemented as a modular LangGraph pipeline:
Intent Detection – Classifies user intent
Data Selection – Retrieves relevant health data
Insight Generation – Produces structured, data-backed observations
Response Generation – Synthesizes an empathetic, non-medical response
Conversation Memory – Maintains lightweight multi-turn context
An optional LLM-as-a-judge component is used offline to evaluate grounding, tone, and relevance.

Repository Structure
agents/        # Intent, data selection, insight, and response agents
data/          # Mock Fitbit health data
memory/        # Conversation memory
evaluation/    # Automated evaluation logic
notebooks/     # Experimentation notebook
graph.py       # LangGraph definition
main.py        # CLI entry point
environment.yml

Experimentation

The notebooks/fitbit_conversational_ai_experiments.ipynb notebook documents:

- Handling Missing Data
- Factual accuracy / grounding against source data
- Automated evaluation using an LLM-as-a-judge

Running the POC
conda env create -f environment.yml
conda activate fitbit-ai


Create a .env file:
ANTHROPIC_API_KEY=your_api_key_here


Run:
python main.py

Notes
- Responses are grounded only in provided data
- Missing data results in a graceful decline
- All advice is non-medical and supportive
- Uses mock data for demonstration purposes
