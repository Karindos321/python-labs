import uuid

class Parcel:
    MAX_WEIGHT = 30

    def __init__(self, sender, recipient, weight):
        if not sender or not recipient:
            raise ValueError("Необхідна інформація про відправника та одержувача")
        if weight > self.MAX_WEIGHT:
            raise ValueError("Посилка перевищує максимальну вагу 30 кг")

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
    raise ValueError("Посилка з таким номером не існує")

all_offices = [PostalOffice() for _ in range(10)]
