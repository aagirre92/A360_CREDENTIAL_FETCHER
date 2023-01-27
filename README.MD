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

|Credential Name                    |Credential Description                                                                                     |Attribute Name  |Attribute Value                               |Masked|
|-----------------------------------|-----------------------------------------------------------------------------------------------------------|----------------|----------------------------------------------|------|
|Email_Credentials                  |Email credentials for xxxx                                                                                 |Username        |lololo@gmail.com                              |False |
|Email_Credentials                  |Email credentials for xxxx                                                                                 |Password        |1234                                          |True  |
|AA Gmail                           |gmail user                                                                                                 |email           |automation.anywhere@gmail.com                 |False |
|AA Gmail                           |gmail user                                                                                                 |password        |1234                                          |False |

