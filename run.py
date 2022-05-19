import subprocess, os

# if 'FLASK_SECRET_KEY' not in os.environ:
#     subprocess.call([r'C:\\Code\\flight-finder\\venv\\.env.bat'])

from mileagerun import db, app

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)