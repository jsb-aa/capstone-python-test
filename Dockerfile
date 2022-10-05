FROM node:12 AS build-stage

WORKDIR /react-app
COPY react-app/. .

# You have to set this because it should be set during build time.
ENV REACT_APP_BASE_URL=https://test-flask-docker.onrender.com

# Build our React App
RUN npm install
RUN npm run build

FROM python:3.9

# Setup Flask environment
ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV SQLALCHEMY_ECHO=True
ENV DATABASE_URL=postgres://express_prefix_test_db_user:88tLvkUyzgHKCEcY5uYeBr7vwJ0cpGlh@dpg-ccmpc7pa6gdh5kdavlgg-a/express_prefix_test_db

EXPOSE 8000

WORKDIR /var/www
COPY . .
COPY --from=build-stage /react-app/build/* app/static/

# Install Python Dependencies
RUN pip install -r requirements.txt
RUN pip install psycopg2

# Run flask environment
CMD gunicorn app:app
