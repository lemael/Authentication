About

This is a Django 2 based visual word trainer for small training sets of technical terms.
License

This project is licensed with the Apache 2.0 License.

Development Setup

    If you're on Windows, install the Windows Subsystem for Linux. Then execute wsl bash and continue with the commands below.
    git clone [git@github.com:lemael/Authentication.git
    cd Authentication
    apt install python3-venv
    python3 -m venv .venv
    source .venv/bin/activate
    python3 setup.py develop
    python3 manage.py migrate
    python3 manage.py createsuperuser
    python3 manage.py runserver


