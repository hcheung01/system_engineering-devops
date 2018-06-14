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
12. mkdir -m751 dir_holberton to create new directory with 751 permissions
13. chown :holberton hello to change group owner
14. chown -R betty:holberton .  to change all files and directories
15. chown -h betty:holberton _hello to change owner and group owner for file
16. chown --from=guillame betty hello to change owner if it is a specified user

EXTRA CREDIT
17. telnet towel.blinkenlights.nl to play Star Wars