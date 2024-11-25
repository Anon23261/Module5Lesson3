import sqlite3
from datetime import datetime
from tabulate import tabulate

def get_members_in_age_range(start_age, end_age):
    """
    Retrieves details of members whose ages fall within the specified range.
    
    Args:
        start_age (int): The starting age of the range
        end_age (int): The ending age of the range
    
    Returns:
        list: List of tuples containing member details (id, name, age)
    """
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()

        # SQL query using BETWEEN clause
        cursor.execute("""
            SELECT id, name, age
            FROM Members
            WHERE age BETWEEN ? AND ?
            ORDER BY age ASC
        """, (start_age, end_age))

        results = cursor.fetchall()
        
        if results:
            # Create headers for the table
            headers = ["Member ID", "Name", "Age"]
            # Format the results into a nice table
            print(f"\nMembers between ages {start_age} and {end_age}:")
            print(tabulate(results, headers=headers, tablefmt="grid"))
            print(f"Total members in range: {len(results)}")
        else:
            print(f"\nNo members found between ages {start_age} and {end_age}.")
        
        return results
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        conn.close()

def get_workout_statistics():
    """
    Retrieves workout statistics for all members including:
    - Total workout sessions
    - Average duration
    - Total calories burned
    - Average calories per session
    
    Returns:
        list: List of tuples containing workout statistics per member
    """
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                m.id,
                m.name,
                COUNT(w.id) as total_sessions,
                ROUND(AVG(w.duration_minutes), 2) as avg_duration,
                SUM(w.calories_burned) as total_calories,
                ROUND(AVG(w.calories_burned), 2) as avg_calories_per_session
            FROM Members m
            LEFT JOIN WorkoutSessions w ON m.id = w.member_id
            GROUP BY m.id, m.name
            ORDER BY total_sessions DESC
        """)

        results = cursor.fetchall()
        
        if results:
            headers = ["Member ID", "Name", "Total Sessions", "Avg Duration (min)", 
                      "Total Calories", "Avg Calories/Session"]
            print("\nWorkout Statistics per Member:")
            print(tabulate(results, headers=headers, tablefmt="grid"))
        else:
            print("\nNo workout statistics available.")
        
        return results
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        conn.close()

def get_monthly_activity_summary(year, month):
    """
    Generates a monthly summary of workout activities.
    
    Args:
        year (int): The year to analyze
        month (int): The month to analyze (1-12)
    
    Returns:
        list: List of tuples containing daily workout summaries
    """
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()

        # Format month for SQL query
        date_pattern = f"{year}-{month:02d}-%"
        
        cursor.execute("""
            SELECT 
                date,
                COUNT(id) as session_count,
                ROUND(AVG(duration_minutes), 2) as avg_duration,
                SUM(calories_burned) as total_calories
            FROM WorkoutSessions
            WHERE date LIKE ?
            GROUP BY date
            ORDER BY date ASC
        """, (date_pattern,))

        results = cursor.fetchall()
        
        if results:
            headers = ["Date", "Sessions", "Avg Duration (min)", "Total Calories"]
            print(f"\nActivity Summary for {datetime(year, month, 1).strftime('%B %Y')}:")
            print(tabulate(results, headers=headers, tablefmt="grid"))
        else:
            print(f"\nNo workout data available for {datetime(year, month, 1).strftime('%B %Y')}.")
        
        return results
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        conn.close()

# Test the functions if this script is run directly
if __name__ == "__main__":
    # Import and run database setup if needed
    from GymManagement import setup_database
    setup_database()
    
    print("\n=== Testing Advanced Data Analysis Functions ===")
    
    # Test age range query
    print("\nTesting age range query (25-30):")
    get_members_in_age_range(25, 30)
    
    # Test workout statistics
    print("\nTesting workout statistics:")
    get_workout_statistics()
    
    # Test monthly activity summary
    print("\nTesting monthly activity summary:")
    current_year = datetime.now().year
    current_month = datetime.now().month
    get_monthly_activity_summary(current_year, current_month)