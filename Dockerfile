# Step 1: Use a small, official Python environment
FROM python:3.12-slim

# Step 2: Create a folder inside the container for your code
WORKDIR /app

# Step 3: Copy your 'recipe' of libraries first
COPY requirements.txt .

# Step 4: Install the libraries (Flask, Pytest, Flake8, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy all your project files into the container
COPY . .

# Step 6: Tell Docker which port your Flask app uses
EXPOSE 5000

# Step 7: The command to start your Tabulation App
CMD ["python", "app/main.py"]