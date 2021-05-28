python3 -m venv venv
rm -f /tmp/kassk_mrozy_2021.log
. ./venv/bin/activate
pip install -U pip setuptools wheel
pip install -r requirements.txt

