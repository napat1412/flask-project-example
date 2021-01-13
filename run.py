from app import app, db

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    db.create_all()
    print('Initialized the database.')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
