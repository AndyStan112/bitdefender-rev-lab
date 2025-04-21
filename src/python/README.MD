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

