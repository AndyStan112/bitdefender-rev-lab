# 🐍 Python Tools

## ⚙️ Setup (Requires Poetry)

To install and activate the virtual environment:

```bash
poetry install
poetry env activate
```

## 🚀 Running a Tool

Use the following command format:

```bash
poetry run \<command\>
```

## 🧰 Available Tools

### 🔍 `permission-scan`

```bash
permission-scan [-h] [--search_time SEARCH_TIME] [--interval INTERVAL] [[-d | -e]] permission
```

Scans for 3rd party apps installed at a given time ± interval that have a specified permission.


### 🔍 `decrypt`

```bash
decrypt [-h] [--types TYPES [TYPES ...]] [--restore] [--verify-filetype] [[-d | -e]]
```

Scans for encrypted files and decrypts them.


### 🔍 `permission-scan`

```bash
keygen [-h] username
```

Generates a valid password based on the username


### 🔍 `rev_dec`

```bash
rev_dec [-h] in_file out_file
```

Decodes the file depending on the filetype.

