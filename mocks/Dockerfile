# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy mock service code
COPY payment_service.py /app/

# Install required packages
RUN pip install fastapi uvicorn pydantic

# Expose FastAPI port
EXPOSE 8000

# Start the mock service
CMD ["uvicorn", "payment_service:app", "--host", "0.0.0.0", "--port", "8000"]
