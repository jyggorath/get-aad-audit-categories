# Get AAD audit categories
Fetches a list of all the names of AAD audit log categories, as defined here: https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/reference-audit-activities

For easy searching and integration with scripts etc. Uses the GitHub version of the doc to ensure the information is up to date.

## Usage
```
# Fetches ALL the categories
$ ./get-aad-audit-categories.py
```
```
# Fetches only the categories containing the case-insensitive substring "role"
$ ./get-aad-audit-categories.py role
```
```
# Displays help
$ ./get-aad-audit-categories.py -h
# Also displays help
$ ./get-aad-audit-categories.py --help
```