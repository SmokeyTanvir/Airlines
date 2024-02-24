# Airlines

## Introduction

Welcome to Airlines! This web application is designed to efficiently manage airline flights and provides a user-friendly interface for users to interact with the system. With features such as user authentication (login, logout), this app aims to streamline the process of managing and booking flights.

## Features

1. **User Authentication:**
   - Secure user authentication system with login and logout functionality.
   - Only authenticated users can access certain features, ensuring data security.

2. **Flight Management:**
   - Easily add, edit, or delete airline flights.
   - View detailed information about each flight, including departure and arrival times, destinations, and available seats.

3. **Booking System:**
   - Users can search for available flights based on various criteria such as date, destination, and departure time.
   - Book flights seamlessly with a user-friendly booking interface.

4. **User Profile:**
   - Each user has a personalized profile with information about their booked flights and travel history.
   - Users can update their profiles, including personal information and preferences.

## Getting Started

Follow these steps to set up the Airlines Django Web App on your local machine:

1. **Clone the Repository:**
```
git clone https://www.github.com/SmokeyTanvir/Airlines.git
cd Airlines
```

3. **Install Dependencies:**
```pip install -r requirements.txt```

5. **Database Migration:**
```
python manage.py makemigrations
python manage.py migrate
```

6. **Create Superuser (Admin):**
```python manage.py createsuperuser```

7. **Run the Development Server:**
```python manage.py runserver```

8. **Access the Web App:**
Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

1. **Login:**
- Access the login page and enter your credentials to log in.

2. **Explore Flights:**
- Browse available flights, filter based on your preferences.

3. **Book a Flight:**
- Select a desired flight and proceed to book it through the booking interface.

4. **User Profile:**
- Update your user profile with personal information and preferences.

5. **Logout:**
- Safely log out to secure your account.

## Technologies Used

- Django
- Python
- HTML/CSS
- Bootstrap
- SQLite (for development)

## Contribution

Feel free to contribute to the development of this web app by submitting issues or pull requests on the GitHub repository.

Happy Flying! ✈️🌍
