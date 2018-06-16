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
11. 
12.
13. sort | uniq -u for inputs and outputing same characters with no duplicates
14. grep -e "root" /etc/passwd to find "root" in passwd directory
15. sort -e "bin" /etc/passwd | wc -l to find "bin" and output number of lines
16. grep -A 3 "root" /etc/passwd find "root" pattern and display 3 lines after
17. grep -v "bin" /etc/passwd to display lies not containing the pattern