from config import config, UserRoleMapping, RoleResourceActionTypeMapping
from prettytable import PrettyTable

class RoleBaseAccessControl:
    def loginUser(self, userID):
        if userID in config['USER']:
            return "hi! you are logged in as "+str(userID)+", "+str(config['USER'][userID]['Name'])
        else:
            return "User Doesn't Exist!!"

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
            return "Incorrect User ID"
        elif actionType not in config['ACTION_TYPE']:
            return "Incorrect Action Type"
        elif resourceID not in config['RESOURCE'].keys():
            return 'Resource not Found'
        elif userID not in UserRoleMapping:
            return "You are not allowed to access the given Resource"
        else:
            roles = UserRoleMapping[userID]["Role"]
            for role in roles:
                resourceActionMapping = RoleResourceActionTypeMapping[role]
                for resource_id in resourceActionMapping.keys():
                    if resourceID == resource_id and actionType in resourceActionMapping[resource_id]:
                        is_access_allowed = True
                        break
            if is_access_allowed:
                return "You are allowed to access the given Resource"
            else:
                return "You are not allowed to access the given Resource"


    def assignRole(self, user_id, role_id):
        if user_id not in config["USER"].keys():
            return "Incorrect User ID"
        elif role_id not in config["ROLE"].keys():
            return "Invalid Role ID"
        elif user_id in UserRoleMapping and role_id in UserRoleMapping[user_id]["Role"]:
            return "Role has already been assigned to the User"
        elif user_id in UserRoleMapping:
            UserRoleMapping[user_id]["Role"].append(role_id)
            return "Role has been assigned to the User"
        else:
            UserRoleMapping[user_id] = {
                "Role": [role_id]
            }
            return "Role has been assigned to the User"

    def removeRole(self, user_id, role_id):
        if user_id not in config["USER"].keys():
            return "Incorrect User ID"
        elif role_id not in config["ROLE"].keys():
            return "Invalid Role ID"
        elif user_id not in UserRoleMapping or role_id not in UserRoleMapping[user_id]["Role"]:
            return "There is no such role in the user account"
        elif user_id in UserRoleMapping:
            roles = UserRoleMapping[user_id]["Role"]
            if role_id in roles:
                if len(roles) ==1:
                    UserRoleMapping.pop(user_id)
                else:
                    UserRoleMapping[user_id]["Role"].remove(role_id)
            return "Role has been removed from the User"
        else:
            return "Contact System Administrator"

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
            print("Invalid Input, Please try again")

        print("############################################################ Data ##############################################################")
        print("config", config)
        print("UserRoleMapping", UserRoleMapping)
        print("RoleResourceActionTypeMapping", RoleResourceActionTypeMapping)
        print("################################################################################################################################")

