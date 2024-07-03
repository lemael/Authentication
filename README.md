#About

This is a Django 4.2.13 based System Authentication.

#Development Setup

    If you're on Windows, install the Windows Subsystem for Linux. Then execute wsl bash and continue with the commands below.
    git clone [git@github.com:lemael/Authentication.git]
    cd Authentication
    apt install python3-venv
    python3 -m venv .venv
    source .venv/bin/activate
    python3 setup.py develop
    python3 manage.py migrate
    python3 manage.py createsuperuser
    python3 manage.py runserver
