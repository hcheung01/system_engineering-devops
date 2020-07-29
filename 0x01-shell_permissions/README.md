# 0x01. Shell, permissions
---
## Description

This project in the System engineering & DevOps ― Bash series is about:
* What do the commands chmod, sudo, su, chown, chgrp do
* Linux file permissions
* How to represent each of the three sets of permissions (owner, group, and other) as a single digit
* How to change permissions, owner and group of a file
* Why can’t a normal user chown a file
* How to run a command with root privileges
* How to change user ID or become superuser

* How to create a user
* How to create a group
* How to print real and effective user and group IDs
* How to print the groups a user is in
* How to print the effective userid

## Files
---
```bash
.
├── 0-iam_betty
├── 100-Star_Wars
├── 101-man_codingschool
├── 10-mirror_permissions
├── 11-directories_permissions
├── 12-directory_permissions
├── 13-change_group
├── 14-change_owner_and_group
├── 15-symbolic_link_permissions
├── 16-if_only
├── 1-who_am_i
├── 2-groups
├── 3-new_owner
├── 4-empty
├── 5-execute
├── 6-multiple_permissions
├── 7-everybody
├── 8-James_Bond
├── 9-John_Doe
└── README.md

0 directories, 20 files
```

## Tasks
0. su to change owner
1. whoami to display your userid
2. touch to create an empty file
3. groups to print all the groups the current user is part of
4. chown to change owner of a file
5. chmod u+x to change permission to execute
6. chmod ug+x,o+r hello to add execute permission to the owner and group plus read permissions to others
7. chmod a+x hello to add execution permission to user, groups, other
8. chmod 007 hello to set all permissions to others only
9. chmod 753 hello to set specific permissions
10. chmod --reference=olleh hello to set one file equal to another file
11. chmod -R  a+X . to change permissions for all subdirectories
12. mkdir -m751 dir_codingschool to create new directory with 751 permissions
13. chown :codingschool hello to change group owner
14. chown -R betty:codingschool .  to change all files and directories
15. chown -h betty:codingschool _hello to change owner and group owner for file
16. chown --from=guillame betty hello to change owner if it is a specified user
100. script that will play the StarWars IV episode in the terminal
101. Create a man page

## Directories
---
Directory Name | Description
---|---
0x01-shell_permissions | Holds all scripts

## Author
Heindrick Cheung