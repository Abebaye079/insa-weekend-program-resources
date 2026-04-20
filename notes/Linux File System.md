## /root
- `/root` is the **home directory of the root user** (administrator of the Linux system).

- Unlike normal users who have home directories in `/home/<username>`, root has its **own private home**.

## /home

- is where you will find your users’ personal directories ( **parent directory for all normal users**.)

- Each user has their **own subdirectory**, e.g.: /home/kali  
/home/abebaye  

- Unlike `/root`, **permissions may vary**, and some files may be hidden.

## /bin

- short term for binaries 

- contains essential executable programs required by all users like `ls`, `cat`, `cp`, `mv`, `rm`
## /sbin  

 - are system binaries that a system administrator would use and a standard user would not have access to without permission.

-Both /bin and /sbin contain the files that need to be accessible when running in single user mode.

Single user mode is a special mode that boots you in as a root user to allow you to do system repairs and upgrades or testing networking is usually disabled in this mode because of security issues. when installing a program in Linux it's  not placed in these folders.

## /var

- stands for variable

- it stores data and files that change frequently while the system is running.

- E.g.: logs, mail, caches, temporary files, spool files, web data, databases.

#### Subdirectories

| Subdirectory   | Purpose                                         | Cybersecurity relevance                    |
| -------------- | ----------------------------------------------- | ------------------------------------------ |
| `/var/log`     | System and application, service logs            | **Very likely for flags**                  |
| `/var/tmp`     | Temporary files that survive reboot             | Flags often hidden here                    |
| `/var/cache`   | Cached files from apps (like apt)               | Rarely contains flags                      |
| `/var/lib`     | Persistent program data (databases, state info) | Possible flags, important in advanced labs |
| `/var/local`   | Local program data                              | Sometimes labs hide challenge files here   |
| `/var/spool`   | Queued tasks (printing, mail)                   | Rare, but possible                         |
| `/var/www`     | Web server files                                | Common in web challenges                   |
| `/var/run`     | Runtime info (PIDs, sockets)                    | Usually temporary, rarely holds flags      |
| `/var/backups` | Backups of system files                         | Could contain challenge backups            |

### Cybersecurity Lab Mindset for `/var`

- Always check **hidden files** (`.`)
- `/var/log` → very high priority for flags
- `/var/tmp` → flags may survive reboots
- `/var/lib` → persistent challenge data
- `/var/local` → locally installed lab files
- `/var/www` → web-related challenges
- Use **`sudo`** if permissions deny access
- Combine `ls -la`, `grep -Ri`, and `find` for maximum coverage

# `/tmp` and `/var/tmp`

- **`/tmp`** → temporary files directory. Used by **all users and processes**. Files here are usually **deleted on reboot**.

- **`/var/tmp`** → similar to `/tmp`, but files are **persistent across reboots**.

- Both are writable by everyone (sticky bit ensures safety)

- Both `/tmp` and `/var/tmp` are **world-writable**:

drwxrwxrwt 14 root root 4096 Mar 15 /tmp  
drwxrwxrwt  5 root root 4096 Mar 15 /var/tmp

- Sticky bit (`t`) is critical for **security**, preventing users from deleting files they don’t own.

- `/tmp` → temporary, usually cleared on reboot
- `/var/tmp` → temporary, survives reboot

## /etc

- `/etc` stands for **“etcetera”**, but it’s basically the **configuration hub of Linux**.

- Contains **system-wide configuration files and settings**.
  
- Everything from **user accounts** to **network settings** to **service configs** is here.

### Cybersecurity Relevance

1. **User management & passwords**
- `/etc/passwd` and `/etc/shadow` are key for **account info**  and password hashes.
- Beginner labs sometimes hide flags in fake config files.

2. **Network configuration**
- `/etc/hosts`, `/etc/network/interfaces` can contain **clues for labs or network setups**.    

3. **Service configurations**
- `/etc/apache2/`, `/etc/nginx/` → web service config, could point to flag locations
- `/etc/ssh/` → SSH configs, keys may appear here for advanced labs

4. **Permissions & access control**
  - Many files are **root-only**, teaching **sudo usage**

## /opt

- `/opt` stands for **“optional”**.

- Used to store **third-party software** or **custom applications** (not part of the default system).

### `/usr`

- Contains most user programs and libraries

- Example: `/usr/bin`, `/usr/lib`

-  Similar to `/bin` but larger

### `/dev`

- Contains **device files** (hardware representation)

- Example: `/dev/null`, `/dev/sda`

- Used in scripting and advanced exploitation

### `/proc`

- Virtual filesystem (system + process info)

### `/run`

- Temporary runtime data (like PIDs, sockets)

### `/mnt` and `/media`

- Used for mounting external drives