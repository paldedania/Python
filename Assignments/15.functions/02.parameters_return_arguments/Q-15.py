# 15. Define create_email(username, domain="example.com") that returns an email address.

def create_email(username, domain="example.com"):
    return username + "@" + domain


print(create_email("pal"))
print(create_email("pal", domain="school.edu"))
