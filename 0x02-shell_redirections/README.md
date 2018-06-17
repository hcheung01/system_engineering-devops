1. echo "Hello, World" to print the string
2. cat /etc/passwd to display the content of the the file passwd
3. cat /etc/passwd /etc/hosts to display two files contents
4. tail /etc/passwd to display the last 10 lines of passwd file
5. head /etc/passwd to display the first 10 lines of passwd file
6. head -n 3 iacta | tail -n 1
7. echo -e "Holberton School\n" > "\*\\'"Holberton" "School"\'\\*$\?\*\*\*\*\*:)" to create file name with special characters.
8. ls -la > ls_cwd_content to push list into file
9. tail -n 1 iacta >> iacta to push last line into another file
10. find . -name \*.js -type f -delete to remove files in current directory or subdirectories.
11. find . maxdepth 1 -type d -print | wc -l to search and count subdirectories print by per line
12. ls -t -1 | head to display first 10 lines of directory
13. sort | uniq -u for inputs and outputing same characters with no duplicates
14. grep -e "root" /etc/passwd to find "root" in passwd directory
15. sort -e "bin" /etc/passwd | wc -l to find "bin" and output number of lines
16. grep -A 3 "root" /etc/passwd find "root" pattern and display 3 lines after
17. grep -v "bin" /etc/passwd to display lines not containing the pattern
18. grep -e [:alpha:] /etc/ssh/sshd_config to display all lines starting with a letter
19. tr Ac Ze for swapping specific characters
20. tr -d cC to delete all letters c and C from input
21. rev to reverse string inputs
22. sort /etc/passwd | cut -d : -f 1,7 to display and sort users and home directory
23. find -empty -printf "%f\n" to find all empty files and directories in current directory
24.   