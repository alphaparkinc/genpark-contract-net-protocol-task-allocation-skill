# genpark-contract-net-protocol-task-allocation-skill

Agent Skill implementing the **FIPA Contract Net Protocol (CNP) Market Mechanism** in 100% Python standard library.

## Architectural Flow
```mermaid
flowchart TD
    Manager["Manager Agent"] -->|Call for Proposals (CFP)| Swarm["Agent Worker Swarm"]
    Swarm --> Bid1["Worker 1 (Bid: Price, Quality)"]
    Swarm --> Bid2["Worker 2 (Bid: Price, Quality)"]
    Swarm --> Bid3["Worker 3 (Bid: Price, Quality)"]
    Bid1 & Bid2 & Bid3 --> Eval["Multi-Criteria Utility Evaluation"]
    Eval --> Award["Award Contract to Optimal Worker"]
```
