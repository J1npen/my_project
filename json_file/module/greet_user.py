import json

def read_data():
    """ Read data from json """
    filename = 'data.json'
    with open(filename) as f_obj:
        data = json.load(f_obj)
    return data


def get_username():
    """ Get the username if available"""
    filename = 'data.json'
    try:
        data = read_data()
        username = data['name']

    except KeyError:
       return None
    
    except FileNotFoundError:
        msg = "Please enter your username. I will remember it: "
        username = input(msg)
        data = {'name': username, 'age': 0}
        with open(filename,'w') as f_obj:
            json.dump(data,f_obj,indent=4)
        return username

    else:
        return username

def get_new_username():
    filename = 'data.json'
    msg = "Please enter your username. I will remember it: "
    username = input(msg)
    data = read_data()
    data['name'] = username

    with open(filename,'w') as f_obj:
        json.dump(data,f_obj,indent=4)

    return username
        

def greet_user():
    """ Greet the user by username"""
    username = get_username()
    data = read_data()

    if username:
        print(f"Welcome back! {username}!")

    else:
        username = get_new_username()
        print(f'Your username {username} has now stored!')

def main():
    greet_user()

if __name__ == '__main__':
    main()