from database import create_cursor


def tenders():
  cursor, db = create_cursor()
  query = "SELECT id, title, description, closing_date FROM tenders ORDER BY closing_date DESC"
  cursor.execute(query)
  for (id, title, description, closing_date) in cursor:
      print(f"Tender {id}: {title}\nDescription: {description}\nClosing date: {closing_date}\n")

  # Close the database connection
  cursor.close()
  db.close()