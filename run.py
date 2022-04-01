from mileagerun import db, app
import subprocess, os

if not os.environ['FLASK_SECRET_KEY']:
    subprocess.call([r'C:\\Code\\flight-finder\\venv\\.env.bat'])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)