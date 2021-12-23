import os, hashlib, getpass

USER_DATA_PATH = os.path.join('data/users.txt')

def get_data():
    global USER_DATA_PATH
    dic = {}
    with open(USER_DATA_PATH, 'r') as file:
        for line in file:
            data = line.split(' ')
            dic[data[0]] = data[1]
    return dic


def encrypt_string(str):
    return hashlib.sha256(str.encode()).hexdigest()


def verify(user, pw):
    dic = get_data()
    if user in dic.keys():
        real_hash = dic[user]
    else:
        real_hash = 0
    if real_hash == encrypt_string(pw):
        return True
    else:
        return False


def new_data(user, pw):
    file = open(USER_DATA_PATH, 'a')
    file.write(" \n" + user + " " + encrypt_string(pw))


def main():
    user_input = ""
    wrong_count = 0
    while user_input != 'q' and wrong_count < 6:
        user_input = input("e: Enter User/Password\nn: New User/Password\nq: Quit\n")
        if user_input == 'e':
            user = input("User: \n")
            pw = getpass.getpass("Password: \n")
            if verify(user, pw):
                print("Correct, but this does nothing\n")
            else:
                print("Wrong...")
                wrong_count += 1
        elif user_input == 'n':
            pw =  getpass.getpass("User: admin\nPassword:")
            if verify("admin", pw):
                user = input("New User: \n")
                pw = getpass.getpass("Password: \n")
                new_data(user, pw)
            else:
                print("Wrong...")
                wrong_count += 1



if __name__ == "__main__":
    main()

