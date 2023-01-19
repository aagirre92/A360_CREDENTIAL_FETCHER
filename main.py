import argparse
import pandas as pd
import functions as f

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Get arguments from CMD
    parser = argparse.ArgumentParser(prog="A360 - Credential-Attribute csv",
                                     description='Creates a csv file with all credential-attributes from CR',
                                     epilog="Maybe some attributes can't be fetched either because they have not been "
                                            "setup or they are fetched from external key vault")
    parser.add_argument("--cr_url", help="url of the control room (without the / at the end!) ")
    parser.add_argument("--username", help="full username with domain if AD")
    parser.add_argument("--password", help="password")
    args = parser.parse_args()
    cr_url = str(args.cr_url)
    user = str(args.username)
    password = str(args.password)
    # Get token
    token = f.get_token_password(cr_url, user, password)
    # Credential list
    credential_list_json = f.get_credential_list(cr_url, token)
    # Prepare dataframe
    df = pd.DataFrame({"Credential Name": [], "Attribute Name": [], "Attribute Value": []})
    # Loop for fetching all credential-attributes
    for credential in credential_list_json:
        credential_name = credential["name"]  # dataframe
        credential_id = credential["id"]
        attributes_list = credential["attributes"]  # name of attribute is located here
        for attribute in attributes_list:
            attribute_id = attribute["id"]  # its same as credentialAttributeID!!
            attribute_name = attribute["name"]  # dataframe
            # Get attribute value
            attribute_value = f.get_attribute_values(cr_url, token, credential_id, attribute_id)
            if attribute_value:
                attribute_value = attribute_value[0]["value"]
            else:
                attribute_value = ""

            row_to_append = [credential_name, attribute_name, attribute_value]
            df.loc[len(df)] = row_to_append

    # Print and save as csv within same folder
    print(df)
    df.to_csv("credentials.csv", index=False)
