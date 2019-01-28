# 0x02. Shell, I/O Redirections and filters
---
## Description

This project in the System engineering & DevOps ― Bash series is about:
* What do the commands head, tail, find, wc, sort, uniq, grep, tr do
* How to redirect standard output to a file
* How to get standard input from a file instead of the keyboard
* How to send the output from one program to the input of another program
* How to combine commands and filters with redirections
* What are special characters
* Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them
* How to display a line of text
* How to concatenate files and print on the standard output
* How to reverse a string
* How to remove sections from each line of files
* What is the /etc/passwd file and what is its format
* What is the /etc/shadow file and what is its format

## Files
---
```bash
.
├── 0-hello_world
├── 100-empty_casks
├── 101-gifs
├── 102-acrostic
├── 103-the_biggest_fan
├── 10-no_more_js
├── 11-directories
├── 12-newest_files
├── 13-unique
├── 14-findthatword
├── 15-countthatword
├── 16-whatsnext
├── 17-hidethisword
├── 18-letteronly
├── 19-AZ
├── 1-confused_smiley
├── 20-hiago
├── 21-reverse
├── 22-users_and_homes
├── 2-hellofile
├── 3-twofiles
├── 4-lastlines
├── 5-firstlines
├── 6-third_line
├── 7-file
├── 8-cwd_state
├── 9-duplicate_last_line
└── README.md
```

## Directories
---
Directory Name | Description
---|---
0x02-shell_redirections | main directory for all files

## Commands and tasks
1. echo "Hello, World" to print the string
2. cat /etc/passwd to display the content of the the file passwd
3. cat /etc/passwd /etc/hosts to display two files contents
4. tail /etc/passwd to display the last 10 lines of passwd file
5. head /etc/passwd to display the first 10 lines of passwd file
6. head -n 3 iacta | tail -n 1
7. echo -e "Holberton School\n" > "\*\\'"Holberton" "School"\'\\*$\?\*\*\*\*\*:)" to create file name with special characters.
8. ls -la > ls_cwd_content to push list into file
9. tail -n 1 iacta >> iacta to push last line into another file
10. find . -name \*.js -type f -delete to remove files in current directory or subdirectories
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
24. find . -type f -name "*.gif" -printf "%f\n" | rev | cut -d. -s -f2- | rev | LC_ALL=C sort -f to search for gifs in current and subdirectories with no extension  
25. echo $(cut -c 1 | tr -d "\n") using echo variable expansion to decode acrostics

## Author
Heindrick Cheung