# System Architecture

```mermaid
graph TD
    Client[Web Client (Next.js)] -->|HTTPS / WSS| APIGateway[Express API Gateway]
    
    subgraph Backend Core
        APIGateway --> CoreServices[Core Services (Auth, Transactions, Budgets)]
        CoreServices --> DB[(PostgreSQL)]
        CoreServices --> Cache[(Redis)]
        CoreServices --> Celery[Background Workers]
    end
    
    subgraph AI Engine
        APIGateway -->|Internal API| AIGateway[FastAPI AI Gateway]
        AIGateway --> LangGraph[LangGraph Agents]
        AIGateway --> MLModels[ML Models]
        LangGraph --> VectorDB[(ChromaDB)]
        LangGraph --> LLM[LLM API (Gemini/OpenAI)]
    end
```
