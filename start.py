#!/bin/bash
# فعال کردن virtual environment (در صورت وجود)
# source venv/bin/activate

# اجرای Django
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
