from website import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(ssl_context=('./cert.pem', './key.pem'), host='localhost', port=5000)