import time

class WaitingClient:

    def __init__(self, client, choice, arrival_time=None):
        self.client = client
        self.choice = choice
        self.arrival_time = arrival_time if arrival_time is not None else time.time()
        self.patience = client.patience

    
    def to_dict(self):
        return {
            "client_id": self.client.id,
            "choice_index": self.client.choices.index(self.choice),
            "arrival_time": self.arrival_time
        }


    def is_waiting_for(self, item_name):
        return item_name in self.choice.items