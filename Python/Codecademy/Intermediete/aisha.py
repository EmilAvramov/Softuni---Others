from contextlib import contextmanager


@contextmanager
def generic(_card_type, _sender, _recipient):
    card_open = open(_card_type, "r")
    sender_open = open(_sender, "w")
    try:
        yield f"Dear {_recipient} \n {_card_type} \n Sincerely, {_sender}"
    finally:
        card_open.close()
        sender_open.close()


with generic("Thank you card", "Amanda", "Mwenda") as file:
    print("Card Generated!")
