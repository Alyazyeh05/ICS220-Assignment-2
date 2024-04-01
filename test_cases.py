from artwork import Artwork
from exhibition import Exhibition
from visitor import Visitor
from ticket import Ticket
from event import Event
from tour import Tour
from payment import Payment
from staff import Staff
from location import Location
from reservation import Reservation

def test_artwork():
    artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Iconic portrait", "Permanent Gallery")
    assert artwork1.get_title() == "Mona Lisa"
    assert artwork1.get_artist() == "Leonardo da Vinci"
    assert artwork1.get_date_of_creation() == "1503"
    assert artwork1.get_historical_significance() == "Iconic portrait"
    assert artwork1.get_exhibition_location() == "Permanent Gallery"

def test_exhibition():
    exhibition1 = Exhibition("Masterpieces of the Renaissance", "Gallery A", "Ongoing")
    artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Iconic portrait", "Permanent Gallery")
    exhibition1.add_artwork(artwork1)
    assert exhibition1.get_name() == "Masterpieces of the Renaissance"
    assert exhibition1.get_location() == "Gallery A"
    assert exhibition1.get_duration() == "Ongoing"
    assert exhibition1.get_artworks() == [artwork1]

def test_visitor():
    visitor1 = Visitor("Alice", 25, "1234567890")
    ticket1 = Ticket(visitor1, "Renaissance Exhibition", 50.0)
    visitor1.add_ticket(ticket1)
    assert visitor1.get_name() == "Alice"
    assert visitor1.get_age() == 25
    assert visitor1.get_national_id() == "1234567890"
    assert visitor1.get_tickets() == [ticket1]

def test_ticket():
    visitor1 = Visitor("Alice", 25, "1234567890")
    ticket1 = Ticket(visitor1, "Renaissance Exhibition", 50.0)
    assert ticket1.get_visitor() == visitor1
    assert ticket1.get_event() == "Renaissance Exhibition"
    assert ticket1.get_price() == 50.0

def test_event():
    event1 = Event("Classical Music Concert", "Auditorium", "20th April 2024", 80.0)
    assert event1.get_name() == "Classical Music Concert"
    assert event1.get_location() == "Auditorium"
    assert event1.get_duration() == "20th April 2024"
    assert event1.get_ticket_price() == 80.0

def test_tour():
    tour1 = Tour("Guide A", "21st April 2024", "10:00 AM", 30)
    assert tour1.get_guide() == "Guide A"
    assert tour1.get_date() == "21st April 2024"
    assert tour1.get_time() == "10:00 AM"
    assert tour1.get_max_capacity() == 30

def test_payment():
    payment1 = Payment(50.0, "Credit Card", "TXN123456")
    assert payment1.get_amount() == 50.0
    assert payment1.get_payment_method() == "Credit Card"
    assert payment1.get_transaction_id() == "TXN123456"

def test_staff():
    staff1 = Staff("John Doe", "Tour Guide", "john@example.com")
    assert staff1.get_name() == "John Doe"
    assert staff1.get_role() == "Tour Guide"
    assert staff1.get_contact_info() == "john@example.com"

def test_location():
    location1 = Location("Gallery A", 100, 50)
    assert location1.get_name() == "Gallery A"
    assert location1.get_capacity() == 100
    assert location1.get_current_occupancy() == 50

def test_reservation():
    visitor1 = Visitor("Alice", 25, "1234567890")
    reservation1 = Reservation(visitor1, "Renaissance Exhibition", "22nd April 2024", "Confirmed")
    assert reservation1.get_visitor() == visitor1
    assert reservation1.get_event_or_tour() == "Renaissance Exhibition"
    assert reservation1.get_date() == "22nd April 2024"
    assert reservation1.get_status() == "Confirmed"

if __name__ == "__main__":
    test_artwork()
    test_exhibition()
    test_visitor()
    test_ticket()
    test_event()
    test_tour()
    test_payment()
    test_staff()
    test_location()
    test_reservation()
    print("All classes are running correctly")

def test_purchase_ticket():
    # Create a visitor
    visitor = Visitor("Alice", 25, "1234567890")
    
    # Create an exhibition
    exhibition = Exhibition("Masterpieces of the Renaissance", "Gallery A", "Ongoing")
    
    # Create artworks
    artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Iconic portrait", "Permanent Gallery")
    artwork2 = Artwork("Starry Night", "Vincent van Gogh", "1889", "Post-impressionist landscape", "Permanent Gallery")
    
    # Add artworks to the exhibition
    exhibition.add_artwork(artwork1)
    exhibition.add_artwork(artwork2)
    
    # Purchase tickets for the exhibition
    ticket1 = Ticket(visitor, "Masterpieces of the Renaissance", 50.0)
    visitor.add_ticket(ticket1)
    
    # Check if the visitor has the purchased ticket
    assert len(visitor.get_tickets()) == 1
    assert visitor.get_tickets()[0] == ticket1

def test_event_registration():
    # Create a visitor
    visitor = Visitor("Bob", 30, "0987654321")
    
    # Create an event
    event = Event("Classical Music Concert", "Auditorium", "20th April 2024", 80.0)
    
    # Register for the event
    ticket = Ticket(visitor, "Classical Music Concert", event.get_ticket_price())
    visitor.add_ticket(ticket)
    
    # Check if the visitor is registered for the event
    assert len(visitor.get_tickets()) == 1
    assert visitor.get_tickets()[0].get_event() == "Classical Music Concert"

def test_tour_booking():
    # Create a visitor
    visitor = Visitor("Charlie", 35, "1357924680")
    
    # Create a tour
    tour = Tour("Guide A", "21st April 2024", "10:00 AM", 30)
    
    # Book a tour
    reservation = Reservation(visitor, "Tour", "21st April 2024", "Confirmed")
    
    # Check if the tour is booked
    assert reservation.get_event_or_tour() == "Tour"
    assert reservation.get_status() == "Confirmed"

def test_multiple_ticket_purchase():
    # Create visitors
    visitors = [
        Visitor("Alice", 25, "1234567890"),
        Visitor("Bob", 30, "0987654321"),
        Visitor("Charlie", 35, "1357924680")
    ]
    
    # Create an exhibition
    exhibition = Exhibition("Modern Art Gallery", "Gallery B", "Ongoing")
    
    # Create artworks
    artworks = [
        Artwork("The Persistence of Memory", "Salvador Dalí", "1931", "Surrealist painting", "Gallery B"),
        Artwork("The Starry Night", "Vincent van Gogh", "1889", "Post-impressionist landscape", "Gallery B")
    ]
    
    # Add artworks to the exhibition
    for artwork in artworks:
        exhibition.add_artwork(artwork)
    
    # Purchase tickets for the exhibition by multiple visitors
    for visitor in visitors:
        ticket = Ticket(visitor, "Modern Art Gallery", 50.0)
        visitor.add_ticket(ticket)
    
    # Check if each visitor has purchased the ticket
    for visitor in visitors:
        assert len(visitor.get_tickets()) == 1
        assert visitor.get_tickets()[0].get_event() == "Modern Art Gallery"

def test_multiple_event_registration():
    # Create visitors
    visitors = [
        Visitor("David", 40, "1111111111"),
        Visitor("Eva", 45, "2222222222"),
        Visitor("Frank", 50, "3333333333")
    ]
    
    # Create events
    events = [
        Event("Jazz Night", "Auditorium", "25th April 2024", 60.0),
        Event("Art Workshop", "Studio", "27th April 2024", 40.0)
    ]
    
    # Register visitors for events
    for visitor, event in zip(visitors, events):
        ticket = Ticket(visitor, event.get_name(), event.get_ticket_price())
        visitor.add_ticket(ticket)
    
    # Check if each visitor is registered for the event
    for visitor, event in zip(visitors, events):
        assert len(visitor.get_tickets()) == 1
        assert visitor.get_tickets()[0].get_event() == event.get_name()

def test_multiple_tour_booking():
    # Create visitors
    visitors = [
        Visitor("Grace", 55, "4444444444"),
        Visitor("Harry", 60, "5555555555"),
        Visitor("Isabelle", 65, "6666666666")
    ]
    
    # Create tours
    tours = [
        Tour("Guide X", "22nd April 2024", "11:00 AM", 20),
        Tour("Guide Y", "24th April 2024", "2:00 PM", 25)
    ]
    
    # Book tours for visitors
    reservations = []
    for visitor, tour in zip(visitors, tours):
        reservation = Reservation(visitor, "Tour", tour.get_date(), "Confirmed")
        reservations.append(reservation)
    
    # Check if each tour is booked
    for reservation, tour in zip(reservations, tours):
        assert reservation.get_event_or_tour() == "Tour"
        assert reservation.get_status() == "Confirmed"

if __name__ == "__main__":
    test_purchase_ticket()
    test_event_registration()
    test_tour_booking()
    print("Integrated test cases passed successfully!")
    test_multiple_ticket_purchase()
    test_multiple_event_registration()
    test_multiple_tour_booking()
    print("Additional integrated test cases passed successfully!")
