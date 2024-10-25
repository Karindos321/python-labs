import pytest
from your_module import Parcel, PostalOffice, track_parcel

def test_create_parcel():
    parcel = Parcel(sender="Alice", recipient="Bob", weight=10)
    assert parcel.sender == "Alice"
    assert parcel.recipient == "Bob"
    assert parcel.weight == 10
    assert parcel.status == "прийнято"
    assert parcel.tracking_number is not None

def test_accept_parcel():
    office = PostalOffice()
    parcel = Parcel(sender="Alice", recipient="Bob", weight=10)
    office.accept_parcel(parcel)
    assert parcel.status == "прийнято"
    assert office.parcels[parcel.tracking_number].status == "прийнято"

def test_dispatch_parcel():
    office = PostalOffice()
    parcel = Parcel(sender="Alice", recipient="Bob", weight=10)
    office.accept_parcel(parcel)
    office.dispatch_parcel(parcel)
    assert parcel.status == "в дорозі"

def test_receive_parcel():
    office = PostalOffice()
    parcel = Parcel(sender="Alice", recipient="Bob", weight=10)
    office.accept_parcel(parcel)
    office.dispatch_parcel(parcel)
    office.receive_parcel(parcel)
    assert parcel.status == "отримано"

def test_deliver_parcel():
    office = PostalOffice()
    parcel = Parcel(sender="Alice", recipient="Bob", weight=10)
    office.accept_parcel(parcel)
    office.dispatch_parcel(parcel)
    office.receive_parcel(parcel)
    office.deliver_parcel(parcel)
    assert parcel.status == "доставлено"

def test_track_parcel():
    office = PostalOffice()
    parcel = Parcel(sender="Alice", recipient="Bob", weight=10)
    office.accept_parcel(parcel)
    status, location = track_parcel(parcel.tracking_number)
    assert status == "прийнято"
    assert location == "Postal Office"
    
def test_missing_tracking_number():
    with pytest.raises(ValueError):
        track_parcel("non_existing_tracking_number")

def test_invalid_parcel_information():
    with pytest.raises(ValueError):
        Parcel(sender="Alice", recipient="", weight=10)

def test_exceed_maximum_weight():
    with pytest.raises(ValueError):
        Parcel(sender="Alice", recipient="Bob", weight=31)
