# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy files to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Set the default command to run the bot
CMD ["python3", "GermanA1.py"]
