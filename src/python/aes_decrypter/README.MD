# 🔐 AES File Decryptor via ADB

A simple CLI tool for scanning and decrypting AES-encrypted files directly from an Android device using ADB.

## 🛠 Usage

```bash
poetry run decrypt [-h] [--types TYPES [TYPES ...]] [--restore] [--verify-filetype] [{-d,-e,}]
```

### Positional Arguments
| Argument     | Description                                |
|--------------|--------------------------------------------|
| `-d`, `-e`, `` | ADB mode: `-d` for physical device, `-e` for emulator, or blank for default |

### Options
| Option              | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `-h`, `--help`       | Show help message and exit                                                  |
| `--types`            | File extensions to scan (default: `.jpg`, `.xml`)                          |
| `--restore`          | Restore `.bak` backups instead of decrypting                               |
| `--verify-filetype`  | Verify file content signature (JPEG/XML/TXT) before replacing original file |


## ✅ File Type Signature Checks

When `--verify-filetype` is enabled, the tool ensures decrypted content is valid based on its extension:

| Extension | Signature check                   |
|-----------|------------------------------------|
| `.jpg` / `.jpeg` | Starts with `FF D8 FF`                    |
| `.xml`    | Starts with `<` or `<?`                      |
| `.txt`    | UTF-8 printable characters only (basic)     |

Files that do not match their expected signature are **not replaced** on the device.

---

## 🧪 Example Commands

```bash
# Decrypt JPEG and XML files on emulator, verifying file type
poetry run decrypt -e --types .jpg .xml --verify-filetype

# Restore original backups
poetry run decrypt -e --restore
```