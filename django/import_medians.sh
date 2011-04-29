export DJANGO_SETTINGS_MODULE="courseproject.settings"
export PYTHONPATH=$PYTHONPATH:`pwd`
date
python ./courseproject/import_medians.py
