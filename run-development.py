from book import app

if __name__ == '__main__':
    app.static_folder = 'static'
    app.run("localhost", port=5000, debug=True)
