# Gym Management System

A comprehensive Python-based gym management system that handles member data and workout sessions with advanced analytics capabilities.

## Features

### Basic Management (GymManagement.py)
- Member management (add, update)
- Workout session tracking
- Database initialization and setup
- Comprehensive error handling

### Advanced Analytics (AdvancedDataAnalysis.py)
- Age-based member filtering using SQL BETWEEN
- Detailed workout statistics per member
- Monthly activity summaries
- Data visualization using tabulated output

## Requirements

- Python 3.6+
- SQLite3
- tabulate

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Anon23261/Module5Lesson3.git
```

2. Install required packages:
```bash
pip install tabulate
```

## Usage

### Basic Management

```python
from GymManagement import add_member, add_workout_session

# Initialize the database
setup_database()

# Add a new member
add_member(1, "John Doe", 28)

# Add a workout session
add_workout_session(1, "2024-01-20", 60, 300)
```

### Advanced Analytics

```python
from AdvancedDataAnalysis import get_members_in_age_range, get_workout_statistics

# Get members in age range
members = get_members_in_age_range(25, 30)

# Get workout statistics
stats = get_workout_statistics()

# Get monthly activity summary
summary = get_monthly_activity_summary(2024, 1)
```

## Database Schema

### Members Table
- id (INTEGER PRIMARY KEY)
- name (TEXT NOT NULL)
- age (INTEGER NOT NULL)

### WorkoutSessions Table
- id (INTEGER PRIMARY KEY AUTOINCREMENT)
- member_id (INTEGER NOT NULL, FOREIGN KEY)
- date (TEXT NOT NULL)
- duration_minutes (INTEGER NOT NULL)
- calories_burned (INTEGER NOT NULL)

## Error Handling

The system includes comprehensive error handling for:
- Duplicate member IDs
- Invalid member references
- Database connection issues
- Invalid date formats
- General SQL errors

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
