import faker

fake = faker.Faker()


def get_user():
    return f"{fake.first_name()} {fake.last_name()}"

def get_users(n):
    pass

if __name__=="__main__":
    user=get_user()
    print(user)






