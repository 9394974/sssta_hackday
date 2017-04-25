if __name__ == '__main__':
    from app import create_app, db

    app = create_app()

    app.debug = True
    app.run(host='0.0.0.0', port=15000, threaded=True)
    # git pull test 
