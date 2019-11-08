# vimonous

Venomous file parser powered with Python and Vim

If you use Vim, you have probably wanted to automate file editing for other automated tasks.

With Vimonous, you can use python to create and execute Vim commands on files!

Vimonous contains a `vimonous` module, and a `main.py` file for bash scripting.

# Installing

```
$ git clone https://github.com/dosisod/vimonous.git
$ cd vimonous
$ pip3 install -e .
```

# Usage (Python)

After installing with `pip`, you can use Vimonous in your python projects:

```python
from vimonous import Vimonous as v

parser=v("filename")

for word in ["hello", "world"]:
	parser.add("[" + word + "]\n")

parser.run()
```

The above will open `"filename"`, and print `"hello"` and `"world"` in brackets.

Vimonous will auto save files, so no need to `:wq!`.

# Usage (Bash)

For bash scripting, put the following in your `~/.bashrc`:

```bash
alias vimonous="/path/to/vimonous/main.py"
```

Now, you can do the following in bash scripts:

```bash
#this will find the first "hello" and replace it with "hi!"
#use $'' to allow for escape characters!

vimonous "filename" $'/hello\ncawhi!'
```
