config = {
    "USER": {
        "U0":{
            'Name': 'Admin'
        },
    },
    "ACTION_TYPE": ['Read', 'Write', 'Delete'],
    "RESOURCE": {
        "RE0":{
            'Name': 'Resource 1'
        },
        "RE1": {
            'Name': 'Resource 2'
        },
        "RE2": {
            'Name': 'Resource 3'
        }
    },
    "ROLE": {
        "RO0": {
            'Name': 'Engineer'
        },
        "RO1": {
            'Name': 'Manager'
        },
        "RO2": {
            'Name': 'Admin'
        }
    },
    "RoleResourceActionTypeMapping": {
        "RO2":{
            "RE0": ['Read', 'Write', 'Delete'],
            "RE1": ['Read', 'Write', 'Delete'],
            "RE2": ['Read', 'Write', 'Delete'],
        },
        "RO1":{
            "RE0": ['Read', 'Write', 'Delete'],
            "RE1": ['Read', 'Write', 'Delete'],
        },
        "RO0":{
            "RE0": ['Read', 'Write', 'Delete'],
        }
    },
    "UserRoleMapping": {
        "U0":{
            "Role": ["RO2"]
        }
    }
}