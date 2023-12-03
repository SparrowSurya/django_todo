
echo "Installing requirements ..."
python3.9 -m pip install -r requirements.txt

echo "collecting staticfiles ..."
python3.9 manage.py collectstatic --noinput --clear

echo "migrate ..."
python3.9 manage.py migrate --noinput
