## Virtual environments

Python comes with an ability to create virtual environments.

A virtual environment is a sandboxed areas of memory, where modules can be installed without affecting the modules installed and available in other environments.

This allows each project to have its own isolated memory area with its own set of module dependencies, which may be different from that of other projects.

### Create a new virtual environment

This command creates a new virtual environment with the name `.env`:

```bash
python3 -m venv .env
```

### Activate the virtual environment

To activate the virtual environment named `.env`...

On Windows, run:

```bash
.env\Scripts\activate.bat
```

On Mac, run:

```bash
source .env/bin/activate
```

### Install modules into the active virtual environment

The install a new module into the currently-active virtual environment, use `pip`, the default Python "package manager" - software that takes care of installing the correct version of any module into your in the correct place for the current environment.

For example, to install the `emojis` module:

```bash
pip install emojis
```

### View all installed modules in the current environment

The following command will output a list of all modules installed into the current environment, along with their version numbers.

```bash
pip freeze
```

### Save the module dependencies of thee current environment into a file.

To save a list of all modules in the current environment into a file named `requirements.txt`...

```bash
pip freeze > requirements.txt
```

Saving a list of module dependencies into a file like this allows you to easily recreate the virtual environment with the necessary modules on a different computeer.

## Install modules listed in a requirements.txt file

If setting up an existing project from scratch, conventional practice is to first creeate a new virtual environment. Then install all the modules listed in the file named `requirements.txt` by running the following command.

```bash
pip install -r requirements.txt
```
