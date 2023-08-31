#!/usr/bin/env bash

# [bash_init]-[BEGIN]
# Exit whenever it encounters an error, also known as a non–zero exit code.
set -o errexit
# Return value of a pipeline is the value of the last (rightmost) command to exit with a non-zero status,
#   or zero if all commands in the pipeline exit successfully.
set -o pipefail
# Treat unset variables and parameters other than the special parameters ‘@’ or ‘*’ as an error when performing parameter expansion.
set -o nounset
# Print a trace of commands.
set -o xtrace
# [bash_init]-[END]

# Apply database migrations.
make migrate

python manage.py delete_users

python manage.py generate_users

python manage.py create_superuser

python manage.py delete_contacts

python manage.py generate_contacts

python manage.py delete_contact_data

python manage.py generate_contact_data

# Run application.
python manage.py runserver 0.0.0.0:8000
