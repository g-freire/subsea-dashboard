start "" "chrome" "http://127.0.0.1:3000/"

start python insert_mongo.py

start python app.py

cd angular_server
npm start

