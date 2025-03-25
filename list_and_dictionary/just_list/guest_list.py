# Creat a invatation_list of people who are invited to a party.
# Start with three people you'd like to invite to dinner.
# Use the invatation_list to print a message to each person, inviting them to dinner.
invatation_list = ["jinpen", "zhangsan", "lisi"]
print(invatation_list)
print("Dear " + invatation_list[0] + ", I would like to invite you to dinner.")
print("Dear " + invatation_list[1] + ", I would like to invite you to dinner.")
print("Dear " + invatation_list[2] + ", I would like to invite you to dinner.")

# You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations.
# Make a unable_to_attend list to store the name of the guest who can't make it.
unable_to_attend = []
unable_to_attend.append(invatation_list.pop(0))
print(f"\n{unable_to_attend}")
print(invatation_list)
invatation_list.insert(0, "wangwu")
print(invatation_list)
print("Dear " + invatation_list[0] + ", I would like to invite you to dinner.")
