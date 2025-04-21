# 🧰 `lib/` - Shared Utility Library

This folder contains reusable utility code used by CLI tools in the project, such as `permission-scan`.

## 📄 Modules

### `adb.py`

A lightweight wrapper around `adb` to simplify interactions with Android devices and emulators.

#### 🔧 Features

- Fetch the path of a package on a device using `pm path`
- Pull an APK or file directly into memory (`BytesIO`)
- Execute arbitrary `adb` or `adb shell` commands
- Stream binary data from the device

#### 📦 Example Usage

```python
from lib.adb import Adb

adb = Adb("-e")  # Use "-e" for emulator or "-d" for physical device

# List devices
print(adb.execute("devices"))

# Pull the APK file for a package
apk_bytes = adb.pull_package("com.example.app")
```

---

This library is designed to be extended with additional utility modules shared across different tools.
