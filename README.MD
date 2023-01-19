# INTRODUCTION
This script allows to programmatically fetch all credential-attributes from Control Room, creating a output csv file
**Your user must have permissions for fetching these**

# USAGE (powershell)
```
.\main.py --cr_url="https://aa1-app2019.iacc.epam.com" --username="andoni_aguirre_aranguren_creator" --password="notmypasswordyoudumb"

```

# FUTURE POSSIBLE ENHANCEMENTS
* API Key usage instead of password pending (this may be done in next release)
* Multi-threading for the http requests
