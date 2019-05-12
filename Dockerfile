FROM python:3.6-alpine

# Create a user
RUN adduser -D bjb
# Set working directory for the purpose of this Dockerfile
WORKDIR /home/bjb

# Copy requirements to the app root
COPY Pipfile.lock ./
# Create a virtual environment and install the dependecies
COPY Pipfile Pipfile
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

# Copy the app into our user root
COPY flask_app/ ./flask_app
COPY front-end/dist/ ./front-end/
COPY app.py ./
#COPY bjb/boot.sh /home/bjb/

# Make our entrypoint executable
#RUN chmod +x boot.sh

# Set the user
USER bjb
#ENTRYPOINT ["ash", "./boot.sh"]
## Set the entrypoint
CMD ["gunicorn", "-b", "0.0.0.0:5000" , "--access-logfile", "-", "--error-logfile", "-" ,"app:app"]