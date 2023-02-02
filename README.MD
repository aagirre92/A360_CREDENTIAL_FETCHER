# INTRODUCTION
This script allows to programmatically fetch all credential-attributes from Control Room, creating a output csv file
**Your user must have permissions for fetching these. Your user must have a role with the following permission:**

* _View and edit ALL credentials attributes value_

# USAGE (powershell)
* Be careful when you insert the API KEY in powershell, use the appropriate **escape characters!**
```
.\main.py --cr_url="https://aa1-app2019.iacc.epam.com" --username="andoni_aguirre_aranguren_creator" --api_key="123fsda"

```

# FUTURE POSSIBLE ENHANCEMENTS
* Multi-threading for the http requests

# OUTPUT

Output **credentials.csv** file will be created under execution folder and will look like this:

|Credential Name                    |External Vault Credential Name|Credential Description                                                                                     |Attribute Name  |Attribute Description         |Attribute User Provided| Attribute Value               |Masked Attribute|Attribute Password Flag|
|-----------------------------------|------------------------------|-----------------------------------------------------------------------------------------------------------|----------------|------------------------------|-----------------------|-------------------------------|----------------|-----------------------|
|Email_Credentials                  |                              |                                                                                                           |Username        |                              |False                  | oeoe@gmail.com                |False           |False                  |
|Email_Credentials                  |                              |                                                                                                           |Password        |                              |False                  | 1234                          |True            |False                  |
|AA Gmail                           |                              |                                                                                                           |email           |                              |False                  | automation.anywhere@gmail.com |False           |False                  |
|AA Gmail                           |                              |                                                                                                           |password        |                              |False                  | 43214213                      |False           |False                  |
|SAP                                |SAP2                          |                                                                                                           |password        |                              |True                   |                               |False           |False                  |
|SAP                                |SAP2                          |                                                                                                           |username        |                              |True                   |                               |False           |False                  |
|test_credential_API                |                              |CREDENTIAL DESCRIPTION OIOIOI                                                                              |username        |ATTRIBUTE DESCRIPTION UEUEUEUE|False                  | ASDFFDSAFSD@GMAIL.COM         |False           |False                  |
