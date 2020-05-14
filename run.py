from flaskapp import app

app.run(host="0.0.0.0",port=5000,threaded=False)

if __name__ == '__main__':
    app.run(debug=True)