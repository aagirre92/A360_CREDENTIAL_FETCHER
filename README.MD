# INTRODUCTION
This script allows to programmatically fetch all credential-attributes from Control Room, creating a output csv file
**Your user must have permissions for fetching these**

# USAGE (powershell)
* Be careful when you insert the API KEY in powershell, use the appropriate **escape characters!**
```
.\main.py --cr_url="https://aa1-app2019.iacc.epam.com" --username="andoni_aguirre_aranguren_creator" --api_key="123fsda"

```

# FUTURE POSSIBLE ENHANCEMENTS
* Multi-threading for the http requests

# OUTPUT

Output **credentials.csv** file will be created under execution folder and will look like this:

|Credential Name                    |Credential Description                                                                                     |Attribute Name  |Attribute Description         |Attribute Value                               |Masked Attribute|Attribute Password Flag|
|-----------------------------------|-----------------------------------------------------------------------------------------------------------|----------------|------------------------------|----------------------------------------------|----------------|-----------------------|
|Email_Credentials                  |                                                                                                           |Username        |                              |ASDF@GMAIL.COM                                |False           |False                  |
|Email_Credentials                  |                                                                                                           |Password        |                              |11222333                                      |True            |False                  |
|test_credential_API                |CREDENTIAL DESCRIPTION OIOIOI                                                                              |username        |ATTRIBUTE DESCRIPTION UEUEUEUE|ASDFFDSAFSD@GMAIL.COM                         |False           |False                  |
