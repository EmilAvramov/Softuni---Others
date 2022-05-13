class Receive:
    def __init__(self, _receiver: str, _rec_messages: str):
        self.receiver = _receiver
        self.rec_messages = _rec_messages


class Send:
    def __init__(self, _sender: str, _sent_message: str):
        self.sender = _sender
        self.sent_message = _sent_message


data = input()
users = []
received = []
sent = []

while data != "exit":
    if "register" in data:
        users.append(data.split()[1])
    else:
        sender = data.split()[0]
        receiver = data.split()[2]
        message = data.split()[3]
        if sender in users and receiver in users:
            sent.append(Send(sender, message))
            received.append(Receive(receiver, message))
    data = input()

select_users = input().split()
user1 = select_users[0]
user2 = select_users[1]

for item in sent:
    for i in range(len(sent)):
        if user1 not in sent[i].sender and user2 not in sent[i].sender:
            sent.pop(i)
            break

for i in range(len(sent)):
    if user1 in sent[i].sender or user2 in sent[i].sender:
        try:
            if sent[i].sender == sent[i+1].sender:
                if sent[i+1].sender != sent[i+2].sender:
                    sent[i+1], sent[i+2] = sent[i+2], sent[i+1]
        except IndexError:
            pass

        if sent[i].sender == user1:
            print(f"{sent[i].sender}: {sent[i].sent_message}")
        elif sent[i].sender == user2:
            print(f"{sent[i].sent_message} :{sent[i].sender}")
        else:
            print(f"No messages")
