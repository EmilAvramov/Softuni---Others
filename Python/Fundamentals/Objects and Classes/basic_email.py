class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True
        return self.is_sent

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


command = input().split()
email_list = []

while command[0] != "Stop":
    send = command[0]
    receive = command[1]
    message = command[2]
    email = Email(send, receive, message)
    email_list.append(email)
    command = input().split()

indices = [int(i) for i in input().split(", ")]

for i in indices:
    Email.send(email_list[i])

for email in email_list:
    print(email.get_info())
