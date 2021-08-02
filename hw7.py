# -*- coding: utf-8 -*-

shells_quantity = {}
groups_uids = {}

with open("group", 'r') as group_file:
    groups = []
    gusers = []
    for line in group_file:
        group_split_line = line.split(sep=":")
        groups.append(group_split_line[0])
        gusers.append(group_split_line[-1][:-1])
    with open("passwd", 'r') as passwd_file:
        shells = []
        for line in passwd_file:
            passwd_split_line = line.split(sep=":")
            for users in gusers:
                if "," in users:
                    split_users = users.split(sep=",")
                    for user in split_users:
                        if user in passwd_split_line[0]:
                            split_users[split_users.index(user)] = passwd_split_line[3]
                            split_users = ",".join(split_users)
                            gusers[gusers.index(users)] = split_users
                elif users != '':
                    if users in passwd_split_line[0]:
                        gusers[gusers.index(users)] = passwd_split_line[3]
            shells.append(passwd_split_line[-1:][0][:-1])
        for i in range(len(gusers)):
            if gusers[i] != '':
                groups_uids[groups[i]] = gusers[i]
        for shell in shells:
            if shell in shells_quantity.keys():
                shells_quantity[shell] += 1
            else:
                shells_quantity[shell] = 1

with open("output.txt", 'w') as output_file:
    for shell, quantity in shells_quantity.items():
        output_file.write('{} - {} ; '.format(shell, quantity))
    output_file.write("\n")
    for group, uid in groups_uids.items():
        output_file.write('{}:{}, '.format(group, uid))


