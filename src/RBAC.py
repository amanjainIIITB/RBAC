from config import config
from CONSTANT_MESSAGE import message
from prettytable import PrettyTable
import json
import sys

class RoleBaseAccessControl:
    def loginUser(self, userID):
        if userID in config['USER']:
            return message["UserExist"]+str(userID)+", "+str(config['USER'][userID]['Name'])
        else:
            return message["UserNotExist"]

    def createUser(self, name):
        user_id = 'U'+str(len(config['USER']))
        config['USER'][user_id] = {'Name': name}
        return config

    def viewRoles(self):
        dataset = list()
        for role in config['ROLE']:
            dataset.append([role, config['ROLE'][role]['Name']])
        return dataset

    def printPrettyTable(self, dataset):
        prettyTable = PrettyTable()
        prettyTable.field_names = ["Resource ID", "Resource Name"]
        print("Below are the list of Roles:")
        for data in dataset:
            prettyTable.add_row(data)
        print(prettyTable)

    def is_access_allowed(self, userID, actionType, resourceID):
        is_access_allowed = False
        if userID not in config["USER"].keys():
            return message["InvalidUser"]
        elif actionType not in config['ACTION_TYPE']:
            return message["InvalidActionType"]
        elif resourceID not in config['RESOURCE'].keys():
            return message["ResourceNotFound"]
        elif userID not in config["UserRoleMapping"]:
            return message["AccessNotAllowed"]
        else:
            roles = config["UserRoleMapping"][userID]["Role"]
            for role in roles:
                resourceActionMapping = config["RoleResourceActionTypeMapping"][role]
                for resource_id in resourceActionMapping.keys():
                    if resourceID == resource_id and actionType in resourceActionMapping[resource_id]:
                        is_access_allowed = True
                        break
            if is_access_allowed:
                return message["AccessAllowed"]
            else:
                return message["AccessNotAllowed"]


    def assignRole(self, user_id, role_id):
        if user_id not in config["USER"].keys():
            return message["InvalidUser"]
        elif role_id not in config["ROLE"].keys():
            return message["InvalidRole"]
        elif user_id in config["UserRoleMapping"] and role_id in config["UserRoleMapping"][user_id]["Role"]:
            return message["RoleAlreadyAssigned"]
        elif user_id in config["UserRoleMapping"]:
            config["UserRoleMapping"][user_id]["Role"].append(role_id)
            return message["RoleAssigned"]
        else:
            config["UserRoleMapping"][user_id] = {
                "Role": [role_id]
            }
            return ""

    def removeRole(self, user_id, role_id):
        if user_id not in config["USER"].keys():
            return message["InvalidUser"]
        elif role_id not in config["ROLE"].keys():
            return message["InvalidRole"]
        elif user_id not in config["UserRoleMapping"] or role_id not in config["UserRoleMapping"][user_id]["Role"]:
            return message["RoleNotFoundInUserAccount"]
        elif user_id in config["UserRoleMapping"]:
            roles = config["UserRoleMapping"][user_id]["Role"]
            if role_id in roles:
                if len(roles) ==1:
                    config["UserRoleMapping"].pop(user_id)
                else:
                    config["UserRoleMapping"][user_id]["Role"].remove(role_id)
            return message["RoleRemoved"]
        else:
            return message["ContactSystemAdmin"]

if __name__ == '__main__':
    object = RoleBaseAccessControl()
    print("hi! you are logged in as admin")
    while(True):
        print("press 1 for login as another user")
        print("press 2 for create user")
        print("press 3 for for view roles")
        print("press 4 to check whether user has access or not.")
        print("press 5 for assign/edit role")
        print("press 6 for remove role")
        print("press 7 for Program Exit")
        option = input()
        if option == 1:
            userID = raw_input("Enter User ID: ")
            print(object.loginUser(userID))
        elif option == 2:
            print("Enter the User Details Below:")
            name = raw_input("Enter User Name: ")
            object.createUser(name)
            print(message["UserCreated"])
        elif option == 3:
            dataset = object.viewRoles()
            object.printPrettyTable(dataset)
        elif option == 4:
            userID = raw_input("Enter User ID: ")
            actionType = raw_input("Enter Action Type(Read/Write/Delete): ")
            resourceID = raw_input("Enter Resource ID: ")
            print(object.is_access_allowed(userID, actionType, resourceID))
        elif option == 5:
            user_id = raw_input("Enter User ID: ")
            role_id = raw_input("Enter Role Name: ")
            print(object.assignRole(user_id, role_id))
        elif option == 6:
            user_id = raw_input("Enter User ID: ")
            role_id = raw_input("Enter Role Name: ")
            print(object.removeRole(user_id, role_id))
        elif option == 7:
            exit(0)
        else:
            print(message["InvalidInput"])
        print(sys.argv)
        if len(sys.argv) > 1 and sys.argv[1]=='--debug':
            print("############################################################ Data ##############################################################")
            print(json.dumps(config, indent = 3))
            print("################################################################################################################################")

