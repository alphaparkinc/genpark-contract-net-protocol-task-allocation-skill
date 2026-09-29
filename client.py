"""Contract Net Protocol (CNP) Task Allocation Engine.
100% Python Standard Library.
"""

class ContractNetProtocol:
    """FIPA Contract Net Protocol auction manager for multi-agent task distribution."""
    @staticmethod
    def run_auction(task, bids):
        if not bids:
            return None
        best_bid = min(bids, key=lambda b: b["price"] / max(b["rating"], 0.1))
        return {
            "task_id": task["id"],
            "awarded_to": best_bid["bidder"],
            "contract_price": best_bid["price"],
            "efficiency_score": round(best_bid["price"] / max(best_bid["rating"], 0.1), 4)
        }
