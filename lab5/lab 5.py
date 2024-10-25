import uuid

class Parcel:
    MAX_WEIGHT = 30

    def __init__(self, sender, recipient, weight):
        if not sender or not recipient:
            raise ValueError("Sender and recipient information is required")
        if weight > self.MAX_WEIGHT:
            raise ValueError("Parcel exceeds maximum weight of 30kg")

        self.tracking_number = str(uuid.uuid4())
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
        self.status = "прийнято"

class PostalOffice:
    def __init__(self):
        self.parcels = {}

    def accept_parcel(self, parcel):
        self.parcels[parcel.tracking_number] = parcel

    def dispatch_parcel(self, parcel):
        parcel.status = "в дорозі"

    def receive_parcel(self, parcel):
        parcel.status = "отримано"

    def deliver_parcel(self, parcel):
        parcel.status = "доставлено"

def track_parcel(tracking_number):
    for office in all_offices:
        if tracking_number in office.parcels:
            parcel = office.parcels[tracking_number]
            return parcel.status, "Postal Office"
    raise ValueError("Parcel with given tracking number does not exist")

all_offices = [PostalOffice() for _ in range(10)]  # Приклад створення кількох відділень
