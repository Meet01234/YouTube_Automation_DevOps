# Use official Python base image
FROM python:3.12-slim
 
# Set working directory inside container
WORKDIR /app
 
# Copy backend files
COPY . .
 
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
 
# Run the backend app
CMD ["python", "app.py"]
