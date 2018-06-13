Shell permissions

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
