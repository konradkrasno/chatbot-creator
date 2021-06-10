#!/bin/bash
while true; do
    python3 manage.py migrate --settings=chatbot_creator.settings
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Init command failed, retrying in 5 secs...
    sleep 5
done
python3 manage.py loaddata data.json.gz
python3 manage.py runserver 0.0.0.0:8000 --settings=chatbot_creator.settings
