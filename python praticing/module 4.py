Practice task: build a tiny notes archive.

Requirements:

Program receives one filename through sys.argv.
Write a function load_note(filename) that:
uses with open(..., "r")
returns (True, content) on success
returns (False, error_message) on OSError
If reading succeeds:
ask the user for a new output filename using sys.stdin.readline()
write the original content plus "\n[BACKUP]" into that file
Normal messages go to sys.stdout.
Errors go to sys.stderr.
Use with open(...) for both reading and writing.

Do not manually call .close().