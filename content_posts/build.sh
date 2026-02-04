#!/usr/bin/env bash
# exit on error
set -o errexit

# Build Frontend (if the folder exists)
if [ -d "frontend" ]; then
  echo "Building frontend..."
  cd frontend
  npm install
  npm run build
  cd ..
fi

# Install Backend Dependencies
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate