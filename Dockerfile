# Use the official Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app


# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt


# Copy the Flask app files to the container
COPY app.py .
COPY adaboost.py .
COPY adaboost_predict.py .
COPY adaboost.model .
COPY train.py .
COPY predict.py .
COPY best.model .
COPY dataset.txt .
COPY stump.py .
COPY templates templates/

# Expose the port on which the Flask app will run
EXPOSE 8080

# Set the entrypoint command to run the Flask app
CMD ["python", "app.py"]
