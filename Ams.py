# Airline Management System - Version 2.0
# Features: issue/return ticket, fine calculation, online catalogue search
catalogue = ["Mumbai-Hyderbad", "Mumbai(India)-Paris(France)", "Delhi-Pune"]
def issue_ticket(ticket_id, member_id):
  print("Book", book_id, "issued to member", member_id)
def return_ticket(ticket_id):
  print("Book", book_id, "returned")
def calculate_fine(days_late, rate=5):
  fine = days_late * rate
  print("Fine = Rs.", fine)
  return fine
def search_book(title):
  if title in catalogue:
    print(title, "is available")
  else:
    print(title, "not found")
