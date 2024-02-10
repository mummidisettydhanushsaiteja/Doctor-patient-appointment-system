# Doctor Patient Appointment system

Doctor Patient Appointment System is a Flask-based web application designed for managing doctor-patient appointments and registrations. It provides functionalities for both patients and doctors to make and manage appointments, as well as for administrators to approve registrations and appointments.

## Features

- **Patient Registration**: Patients can register themselves by providing basic details such as name, date of birth, phone number, and address.
- **Doctor Registration**: Doctors can register themselves with their specialization, date of birth, phone number, and address.
- **Login Pages**: Separate login pages are provided for patients, doctors, and administrators.
- **Appointment Management**: Patients can request appointments with doctors, and doctors can approve or reject these requests.
- **Administrator Panel**: Administrators can approve or reject registration requests for patients and doctors, manage registered patients and doctors, and view appointment requests.
- **Data Validation**: Various validation checks are implemented for ensuring the correctness of data entered during registration and appointment making.

## Setup Instructions

To run the Doctor Patient Appointment System on your local machine, follow these steps:

1. Clone the repository to your local machine.
2. Install Python (if not already installed).
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Ensure you have SQLite installed or configure a different database according to your preference.
5. Navigate to the project directory and run `python app.py` to start the Flask server.
6. Access the application by opening a web browser and going to `http://localhost:5000`.

## Technologies Used

- **Flask**: Flask is a micro web framework for Python used to build web applications.
- **SQLite**: SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
