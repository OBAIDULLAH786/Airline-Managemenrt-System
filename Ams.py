# Airline Management System - Version 1.0
# Feature: issue and cancel tickets
def issue_ticket(ticket_id, passenger_id):
    print("Ticket", ticket_id, "issued to passenger", passenger_id)
def cancel_ticket(ticket_id):
    print("Ticket", ticket_id, "cancelled")
  def calculate_fine(days_late, rate=5):
  fine = days_late * rate
  print(&quot;Fine = Rs.&quot;, fine)
  return fine
