from config import config, UserRoleMapping, RoleResourceActionTypeMapping
from prettytable import PrettyTable

class RoleBaseAccessControl:
    def loginUser(self):
        userID = raw_input("Enter User ID: ")
        if userID in config['USER']:
            print("hi! you are logged in as "+str(userID)+", "+str(config['USER'][userID]['Name']))
        else:
            print("User Doesn't Exist!!")

    def createUser(self):
        print("Enter the User Details Below:")
        user_id = 'U'+str(len(config['USER']))
        name = raw_input("Enter User Name: ")
        config['USER'][user_id] = {'Name': name}

    def viewRoles(self):
        prettyTable = PrettyTable()
        prettyTable.field_names = ["Resource ID", "Resource Name"]
        print("Below are the list of Roles:")
        for role in config['ROLE']:
            prettyTable.add_row([role, config['ROLE'][role]['Name']])
        print(prettyTable)

    def is_allowed(self):
        is_access_allowed = False
        userID = raw_input("Enter User ID: ")
        actionType = raw_input("Enter Action Type(Read/Write/Delete): ")
        resourceID = raw_input("Enter Resource ID: ")
        if userID not in config["USER"].keys():
            print("Incorrect User ID")
        elif actionType not in config['ACTION_TYPE']:
            print("Incorrect Action Type")
        elif resourceID not in config['RESOURCE'].keys():
            print('Resource not Found')
        elif userID not in UserRoleMapping:
            print("You are not allowed to access the given Resource")
        else:
            roles = UserRoleMapping[userID]["Role"]
            for role in roles:
                resourceActionMapping = RoleResourceActionTypeMapping[role]
                for resource_id in resourceActionMapping.keys():
                    if resourceID == resource_id and actionType in resourceActionMapping[resource_id]:
                        is_access_allowed = True
                        break
            if is_access_allowed:
                print("You are allowed to access the given Resource")
            else:
                print("You are not allowed to access the given Resource")


    def assignRole(self):
        user_id = raw_input("Enter User ID: ")
        role_id = raw_input("Enter Role Name: ")
        if user_id not in config["USER"].keys():
            print("Incorrect User ID")
        elif role_id not in config["ROLE"].keys():
            print("Invalid Role ID")
        elif user_id in UserRoleMapping and role_id in UserRoleMapping[user_id]["Role"]:
            print("Role has already been assigned to the User")
        elif user_id in UserRoleMapping:
            UserRoleMapping[user_id]["Role"].append(role_id)
        else:
            UserRoleMapping[user_id] = {
                "Role": [role_id]
            }

    def removeRole(self):
        user_id = raw_input("Enter User ID: ")
        role_id = raw_input("Enter Role Name: ")
        if user_id not in config["USER"].keys():
            print("Incorrect User ID")
        elif role_id not in config["ROLE"].keys():
            print("Invalid Role ID")
        elif user_id not in UserRoleMapping or role_id not in UserRoleMapping[user_id]["Role"]:
            print("There is no such role in the user account")
        elif user_id in UserRoleMapping:
            roles = UserRoleMapping[user_id]["Role"]
            if role_id in roles:
                if len(roles) ==1:
                    UserRoleMapping.pop(user_id)
                else:
                    UserRoleMapping[user_id]["Role"].remove(role_id)
        else:
            print("Contact System Administrator")


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
        object.loginUser()
    elif option == 2:
        object.createUser()
    elif option == 3:
        object.viewRoles()
    elif option == 4:
        object.is_allowed()
    elif option == 5:
        object.assignRole()
    elif option == 6:
        object.removeRole()
    elif option == 7:
        exit(0)
    else:
        print("Invalid Input, Please try again")

    print("############################################################ Data ##############################################################")
    print("config", config)
    print("UserRoleMapping", UserRoleMapping)
    print("RoleResourceActionTypeMapping", RoleResourceActionTypeMapping)
    print("################################################################################################################################")
