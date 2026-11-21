# Poem Generator

Run `python3 main.py` (Python 3.13, standard library only, no network) to create the poem. The script writes a single poem to `entry.txt` inside the directory named by the `OUT_DIR` environment variable; if `OUT_DIR` is unset it defaults to `/output`, and the directory is created when needed.

The poem is a short piece (at most 280 Unicode characters) on the theme of two agents freely agreeing to a shared plan.

Licensed under the MIT License; see `LICENSE`.
