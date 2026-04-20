"# `grep` = Global Regular Expression Print

- searches for text (patterns) inside files.

- *Syntax* :  `grep [option] pattern [file...]
	- [options] : modify the behavior of the command (e.g., ignore case, show line numbers)
	- pattern : the text or regular expression u are searching for 
	- [file...] : the file(s) to search within.

Common Options and Examples

| Option     | Description                                                                | Example Command                                                                                                                       |
| ---------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **-i**     | Ignores case distinctions (case-insensitive search).                       | `grep -i "error" system.log`                                              Finds:<br><br>- error<br>    <br>- ERROR<br>    <br>- Error |
| **-n**     | Displays the line number along with the matching line.   ( exact location) | `grep -n "flag" example.txt`                                            12: FLAG{found_it}                                            |
| **-c**     | Only prints a count of the matching lines, not the lines themselves.       | `grep -c "warning" logfile.txt`                                                                                                       |
| **-v**     | Inverts the match; displays lines that _do not_ match the pattern.         | `grep -v "debug" logfile.txt`                                                                                                         |
| **-w**     | Matches only whole words.                                                  | `grep -w "World" example.txt`                                                                                                         |
| **-l**     | Only lists the names of files containing a match.                          | `grep -l "failure" *.log`                                                                                                             |
| **-r**     | Recursively searches files within directories and subdirectories.          | `grep -r "timeout" /var/log/`                                                                                                         |
| **-E**     | Interprets patterns as extended regular expressions (ERE).                 | `grep -E "abc                                                                                                                         |
| **-A _n_** | Prints _n_ lines _after_ the match for context.                            | `grep -A 3 "start" logfile.txt`                                                                                                       |
| **-B _n_** | Prints _n_ lines _before_ the match for context.                           | `grep -B 2 "end" logfile.txt`                                                                                                         |
| **-C _n_** | Prints _n_ lines of _context_ (before and after) the match.                | `grep -C 2 "middle" logfile.txt`                                                                                                      |

