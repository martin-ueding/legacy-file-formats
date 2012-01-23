% legacy(1)

# NAME

`legacy` - Finds files which might become unreadable.

# SYNOPSIS

	legacy [paths...]

# DESCRIPTION

This script searches your files for file formats that might be unreadable in
the future. It will check whether there is a corresponding PDF exported, if
not, the file will be listed.

# OPTIONS

`--formats`
  ~	Show known formats and exit.
`--rename`
  ~	Rename file.pdf to file.old.pdf.
`--stat`
  ~	Print file type summary.
`--time`
  ~	Check that export is newer than other file.
`-v`
  ~	Show renames (or would be renames).

# EXIT STATUS

0
  ~ No errors.

1
  ~ No configuration file could be found.

# ENVIRONMENT

No environment variables are used.

# FILES

The program expects a configuration file with file formats to look for at
`~/.legacy.yaml`.

The file should have the following structure:

	suffixes:
	  bzr:
		name: Bazaar VCS
	  cdr:
		name: Corel Draw
		export_suffixes:
		- eps
		- pdf
		- ps
		- svg

The minimal form, without names or export suffixes would be:

	suffixes:
	  bzr:
	  cdr:

You can set which file types should be looked for.

# CONFORMING TO

The configuration file is in the YAML format.

# NOTES
# BUGS

Please report bugs in English or German to Martin Ueding <dev@martin-ueding.de>.

# EXAMPLE

`legacy`
  ~ Search your current working directory for legacy files.

# SEE ALSO
