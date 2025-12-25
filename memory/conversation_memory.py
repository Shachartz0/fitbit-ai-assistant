class ConversationMemory:
    def __init__(self):
        self.summary = ""

    def update(self, user, assistant):
        self.summary += f"\nUser: {user}\nAssistant: {assistant}"

    def get(self):
        return self.summary[-1000:]
