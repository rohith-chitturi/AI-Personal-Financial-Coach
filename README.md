# AI-Personal-Financial-Coach

**Enterprise AI Financial Intelligence & Personal Wealth Management Platform**

An intelligent financial advisor, budgeting assistant, investment mentor, spending analyzer, and financial planning platform. 

## Features
- **AI Financial Coach**: Conversational AI for financial Q&A, personalized advice, and spending explanation.
- **Financial Dashboard**: Complete overview of net worth, cash flow, goals, and risk score.
- **Expense Tracking**: OCR receipt scanner, auto-categorization, and smart filters.
- **Budget Management**: Smart budget suggestions, alerts, and savings planner.
- **Investment & Debt Management**: Portfolio overview, loan tracker, debt snowball/avalanche calculators.
- **AI Recommendations & Forecasting**: Predictive spending, budget utilization, and personalized investment strategies.
- **Fraud Detection**: AI-powered anomaly detection for suspicious transactions and duplicate payments.

## Tech Stack
- **Frontend**: Next.js 15, React 19, TypeScript, Tailwind CSS, Shadcn UI
- **Backend Core**: Node.js, Express.js, TypeScript, PostgreSQL, Prisma, Redis
- **AI Backend**: FastAPI, Python, LangGraph, LangChain, Scikit-Learn
- **Infrastructure**: Docker, ChromaDB

## Quick Start (Docker)
1. Copy `.env.example` to `.env` and fill in the values.
2. Run `docker-compose up -d` to start the infrastructure (PostgreSQL, Redis, ChromaDB).
3. Follow individual service READMEs to start the frontend, backend, and AI backend.
