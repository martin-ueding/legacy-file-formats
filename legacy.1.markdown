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

## File Formats

The program expects a configuration file with file formats to look for at
`~/.config/legacy/formats.yaml`.

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

## Export Rules

With the `--make` option, the program will try to generate the exports with the
pattern rules in a makefile at `~/.config/legacy/patterns.makefile`.

Make will be called in the directory of the file onto the export file. Example:
`make -f ... -C ... document.ods.pdf`.

For an open document spreadsheet, the rule could look like this:

	%.ods.pdf: %.ods
		libreoffice -convert-to pdf $< --headless
		mv $(<:.ods=.pdf) $@

# CONFORMING TO

The file formats file is in the YAML format.

# BUGS

Please report bugs in English or German to Martin Ueding <dev@martin-ueding.de>.

# EXAMPLE

`legacy`
  ~ Search your current working directory for legacy files.
`legacy --rename`
  ~ Search in the current directory and rename them from `foo.pdf` to `foo.bar.pdf`.
`legacy -v --stat`
  ~ Generate a list of files that could be renamed and also give a file type summary.
