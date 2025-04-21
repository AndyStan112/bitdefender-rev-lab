# 📦 `permission-scan` CLI Tool

A simple CLI tool to scan for 3rd party apps installed at `SEARCH_TIME ± INTERVAL` that have a specific permission.

## 🧪 Usage

```bash
poetry run permission-scan [-h] [--search_time SEARCH_TIME] [--interval INTERVAL] [[-d | -e]] permission
```

## 📥 Positional Arguments

| Argument       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `[-d \| -e]`    | *(Optional)* Mode of operation: `-d` for physical device, `-e` for emulator. If omitted, defaults to the latest device used in `adb`. |
| `permission`   | **(Required)** The permission to be searched.                               |

## ⚙️ Options

| Option                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `-h`, `--help`             | Show this help message and exit.                                           |
| `--search_time SEARCH_TIME` | Datetime to search in the format `YYYY-MM-DD HH:MM`. <br>Default: current time. |
| `--interval INTERVAL`     | Interval to search, composed of multiple pairs like `<value> <unit>`. <br>Possible units: `microseconds`, `milliseconds`, `seconds`, `minutes`, `hours`, `days`, `weeks`. <br>Extra text and plural forms are ignored. <br>**Example:** `'1 day, 3 hours and 2 minutes'` = `'1 day 3 hour 2 minute'`. <br>Default: `'1 hour'`. |

## ✅ Example

```bash
poetry run permission-scan --interval "2 hours" --search_time "2025-04-21 08:30" READ_EXTERNAL_STORAGE
```

**Output:**

```
Found 1 app(s) with permission 'READ_EXTERNAL_STORAGE' installed near 2025-04-21 08:30:00:

PACKAGE                                            INSTALL TIME
----------------------------------------------------------------------
com.android.one.ui                                 2025-04-21 09:01:20
```
