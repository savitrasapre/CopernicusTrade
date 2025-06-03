# CopernicusTrade

A full-stack web application for retrieving and visualizing stock market data using custom financial strategies. The backend is built with Python, Django, PostgreSQL, and Redis, while the frontend delivers interactive charts and user-friendly interfaces.

## Features

- Fetches real-time and historical stock market data using the yfinance library.
- Implements custom financial strategies for analyzing and visualizing stock data.
- Displays interactive charts for user-friendly data exploration.
- Scalable backend with Django and PostgreSQL for data storage.
- Redis for caching to optimize performance.
- Responsive frontend for seamless user interaction.

## Tech Stack

- Python 3.13
- Django
- PostgreSQL
- Redis
- Celery
- yfinance
- Docker
- React for frontend

## Configuration
Create a .env file in the backend directory:


```sh
DATABASE_URL=postgresql://user:password@localhost:5432/stock_analysis
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your_django_secret_key
DEBUG=True
```

Generate a Django secret key and update the .env file.

## License

MIT