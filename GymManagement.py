import sqlite3
from datetime import datetime

def setup_database():
    """
    Initialize the database and create necessary tables if they don't exist.
    """
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()

        # Create Members table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Members (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)

        # Create WorkoutSessions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS WorkoutSessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                duration_minutes INTEGER NOT NULL,
                calories_burned INTEGER NOT NULL,
                FOREIGN KEY (member_id) REFERENCES Members (id)
            )
        """)

        conn.commit()
        print("Database setup completed successfully!")
    except Exception as e:
        print(f"Error setting up database: {e}")
    finally:
        conn.close()

def add_member(member_id, name, age):
    """
    Add a new member to the Members table.
    
    Args:
        member_id (int): Unique identifier for the member
        name (str): Member's name
        age (int): Member's age
    """
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()

        # Check if member ID already exists
        cursor.execute("SELECT id FROM Members WHERE id = ?", (member_id,))
        if cursor.fetchone() is not None:
            print("Error: Member ID already exists.")
            return

        # Add new member
        cursor.execute("""
            INSERT INTO Members (id, name, age) 
            VALUES (?, ?, ?)
        """, (member_id, name, age))

        conn.commit()
        print(f"Member {name} added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Database integrity error occurred.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    """
    Add a new workout session for a member.
    
    Args:
        member_id (int): ID of the member
        date (str): Date of the workout session (YYYY-MM-DD format)
        duration_minutes (int): Duration of the workout in minutes
        calories_burned (int): Calories burned during the workout
    """
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()

        # Check if member exists
        cursor.execute("SELECT id FROM Members WHERE id = ?", (member_id,))
        if cursor.fetchone() is None:
            print("Error: Member ID does not exist.")
            return

        # Validate date format
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD format.")
            return

        # Add workout session
        cursor.execute("""
            INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) 
            VALUES (?, ?, ?, ?)
        """, (member_id, date, duration_minutes, calories_burned))

        conn.commit()
        print("Workout session added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def update_member_age(member_id, new_age):
    """
    Update a member's age.
    
    Args:
        member_id (int): ID of the member to update
        new_age (int): New age value
    """
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()

        # Check if member exists
        cursor.execute("SELECT id FROM Members WHERE id = ?", (member_id,))
        if cursor.fetchone() is None:
            print("Error: Member does not exist.")
            return

        # Update member's age
        cursor.execute("""
            UPDATE Members
            SET age = ?
            WHERE id = ?
        """, (new_age, member_id))

        conn.commit()
        print("Member age updated successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def delete_workout_session(session_id):
    """
    Delete a workout session.
    
    Args:
        session_id (int): ID of the workout session to delete
    """
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()

        # Check if session exists
        cursor.execute("SELECT id FROM WorkoutSessions WHERE id = ?", (session_id,))
        if cursor.fetchone() is None:
            print("Error: Session ID does not exist.")
            return

        # Delete the session
        cursor.execute("DELETE FROM WorkoutSessions WHERE id = ?", (session_id,))

        conn.commit()
        print("Workout session deleted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Initialize the database when the script is run
if __name__ == "__main__":
    setup_database()