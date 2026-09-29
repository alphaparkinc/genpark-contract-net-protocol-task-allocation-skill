from client import ContractNetProtocol

task = {"id": "task_404", "title": "Large Model Fine-Tuning"}
bids = [
    {"bidder": "Cluster_Node_A", "price": 450, "rating": 4.9},
    {"bidder": "Cluster_Node_B", "price": 400, "rating": 3.8},
    {"bidder": "Cluster_Node_C", "price": 380, "rating": 4.7}
]

award = ContractNetProtocol.run_auction(task, bids)
print(f"Contract Awarded to: {award['awarded_to']} at Price {award['contract_price']}")
