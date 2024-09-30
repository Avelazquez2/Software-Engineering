# get user email address
email = input("Email address: ").strip()
# slice out user name
username = email[:email.index('@')]
# slice domain name
domain = email[email.index('@') + 1:]
# format message
output = "username: {}\ndomain: {}".format(username, domain)
# display output message
print(output)