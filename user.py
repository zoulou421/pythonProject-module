import faker

fake = faker.Faker()


def get_user():
    return f"{fake.first_name()} {fake.last_name()}"

def get_users(n):
    users = []
    for i in range(n):
        users.append(get_user())

    return  users

def get_users_v2(n):
    users = []
    for _ in range(n): #i replace with _
        users.append(get_user())

    return  users
def get_users_v3(n):
    return  [get_user() for _ in range(n)]


if __name__=="__main__":
    users=get_users(n=5)
    print(users)






