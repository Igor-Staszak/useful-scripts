# Known hosts entry removal script

Simple Bash script to delete entries in `~/.ssh/known_hosts` file.

## Usage

```bash
known_hosts <IP>
```

Where `<IP>` is the IP address of the host you want to remove from `known_hosts`.

## Installation

You can configure the script to be used as `known_hosts` from anywhere using one of the following methods:

### Option 1: Add to `.bashrc`

1. Open your `.bashrc` file:
   ```bash
   vi ~/.bashrc
   ```
2. Add the following line:
   ```bash
   alias known_hosts='bash /path/to/known_hosts.sh'
   ```
   Replace `/path/to/known_hosts.sh` with the actual path to the script.
3. Save and close the file.
4. Apply the changes:
   ```bash
   source ~/.bashrc
   ```

### Option 2: Add to a `bin` Directory

1. Move the script to a directory included in your `PATH`, such as `~/bin/`:
   ```bash
   mv /path/to/known_hosts.sh ~/bin/known_hosts
   ```
2. Make it executable:
   ```bash
   chmod +x ~/bin/known_hosts
   ```
3. Ensure `~/bin/` is in your `PATH`. Add this line to your `.bashrc` if needed:
   ```bash
   export PATH="$HOME/bin:$PATH"
   ```
4. Apply the changes:
   ```bash
   source ~/.bashrc
   ```

Now you can use `known_hosts <IP>` from anywhere in your terminal.
