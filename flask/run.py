from app import db, app
import sys

debug = sys.argv[1] if sys.argv[1] else False

if __name__ == '__main__':
    db.create_all()
    app.run(debug=debug)