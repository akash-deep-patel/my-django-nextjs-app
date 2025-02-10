# My Django Next.js Appointment Scheduler

This project is a web application that allows users to schedule appointments with doctors. It features a Django backend and a Next.js frontend, providing a seamless experience for both patients and doctors.

## Project Structure

```
my-django-nextjs-app
├── backend
│   ├── manage.py
│   ├── myapp
│   ├── myproject
│   ├── db.sqlite3
│   └── requirements.txt
├── frontend
│   ├── pages
│   ├── public
│   ├── styles
│   ├── package.json
│   └── next.config.js
└── README.md
```

## Features

- User authentication for patients
- Appointment scheduling (online and offline)
- Management of doctor and patient information
- Admin interface for managing appointments and users

## Backend Setup

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```
   python manage.py migrate
   ```

4. Create a superuser for the admin interface:
   ```
   python manage.py createsuperuser
   ```

5. Start the Django development server:
   ```
   python manage.py runserver
   ```

## Frontend Setup

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

3. Start the Next.js development server:
   ```
   npm run dev
   ```

## Usage

- Access the application at `http://localhost:3000` for the frontend.
- Access the Django admin interface at `http://localhost:8000/admin` for managing doctors and patients.

## License

This project is licensed under the MIT License.