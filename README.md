# Buyogo-Assignment

This project provides an API for managing training centers, including features for retrieving and creating training center records. The API allows filtering by city and state.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used
- Python
- Django
- Django REST Framework
- SQLite (or any other database of your choice)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/traini8_registry.git
   cd traini8_registry

2. Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:

   On Windows:
    venv\Scripts\activate

   On macOS/Linux:
     source venv/bin/activate

4. Install the required packages:

   pip install -r requirements.txt


## Setup

1. Run migrations: Make sure your database is set up and then run the migrations to create the necessary tables.

   python manage.py migrate

2. Create a superuser (optional): You can create a superuser to access the Django admin interface.

   python manage.py createsuperuser

3. Run the development server: Start the Django development server.

   python manage.py runserver

4. Access the API: Open your browser or an API client (like Postman) and go to http://127.0.0.1:8000/api/.



 # API Endpoints

1. Get Training Centers
   
    URL: http://localhost:8000/api/centers/

    Method: GET
   
    Response:
      Returns a list of training centers.
      Example Request:
         GET /api/centers/

3. Create a Training Center

    URL: http://localhost:8000/api/centers/create/

    Method: POST

    Request Body:

       {
          "center_name": "Teaching Cheetah",
          "center_code": "7181717",
          "address": {
              "detailed_address": "123 Main St",
              "city": "New Delhi",
              "state": "Delhi",
              "pincode": "110001"
          },
          "student_capacity": 100,
          "courses_offered": ["Java", "Python", "Data Science"],
          "contact_email": "contact@raghav.com",
          "contact_phone": "9876543210"
       }

   Response:
      Returns the created training center object.


## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.




   

