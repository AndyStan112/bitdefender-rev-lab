#!/usr/bin/env python3
from lib.adb import Adb
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from datetime import datetime
from loguru import logger
import argparse
import tempfile
import os

def is_valid_file(self, data: bytes, ext: str) -> bool:
    if ext in (".jpg", ".jpeg"):
        return data.startswith(b'\xFF\xD8\xFF')
    if ext == ".xml":
        return data.lstrip().startswith(b'<')
    if ext == ".txt":
        try:
            preview = data[:128].decode("utf-8")
            return all(31 < ord(c) < 127 or c in "\r\n\t" for c in preview)
        except Exception:
            return False
    return True


class AESDecryptor:
    def __init__(self, mode: str, filetypes: list[str], verify_filetype: bool):
        self.adb = Adb(mode)
        self.iv = b"The BigIV's here"
        self.filetypes = tuple(filetypes)
        self.verify_filetype = verify_filetype

    def get_keys(self) -> list[bytes]:
        secrets_path = "/sdcard/SECRETS/nothingsecrethere"
        logger.debug(f"Reading keys from {secrets_path}")
        raw = self.adb.shell(f'cat "{secrets_path}"')
        keys = [line.strip().encode() for line in raw.splitlines() if line.strip()]
        logger.debug(f"Loaded {len(keys)} keys.")
        return keys

    def list_files(self) -> list[str]:
        logger.debug("Listing all files under /sdcard using ls -R")
        result = self.adb.shell("ls -R /sdcard")
        paths = []
        current_dir = "/sdcard"
        for line in result.splitlines():
            if line.endswith(":"):
                current_dir = "/sdcard" + line[:-1].replace("/sdcard", "")
            elif line.strip() and not line.startswith(" "):
                full_path = f"{current_dir}/{line.strip()}"
                if full_path.endswith(self.filetypes):
                    paths.append(full_path)
        logger.debug(f"Collected {len(paths)} matching file(s) from /sdcard")
        return paths

    def try_decrypt(self, data: bytes, keys: list[bytes], filepath: str) -> tuple[bytes, int]:
        for index, key in enumerate(keys):
            try:
                # if logger.level("DEBUG").no <= logger.level(logger._core.min_level).no:
                #     logger.debug(f"Trying key {index + 1}/{len(keys)} on {filepath}")
                cipher = AES.new(key, AES.MODE_CBC, self.iv)
                decrypted = unpad(cipher.decrypt(data), AES.block_size)
                return decrypted, index + 1
            except Exception:
                continue
        return b"", -1

    def decrypt_files(self):
        keys = self.get_keys()
        files = self.list_files()

        logger.info(f"Starting scan at {datetime.now()}")
        logger.info(f"Scanning {len(files)} file(s)...\n")

        for path in files:
            try:
                logger.debug(f"Attempting to pull file: {path}")
                content = self.adb.pull(path).read()
                logger.debug(f"Read {len(content)} bytes from {path}")

                if len(content) % AES.block_size != 0:
                    logger.debug(f"Skipping {path} (not AES block aligned)")
                    continue

                decrypted, key_index = self.try_decrypt(content, keys, path)
                if decrypted:
                    if self.verify_filetype and not self.is_valid_file(decrypted, ext):
                        logger.warning(f"Decrypted {path} using key {key_index}, but file type doesn't match {ext}. Skipping push.")
                        continue
                    logger.success(f"Decrypted: {path} using key {key_index}/{len(keys)}")


                    with tempfile.NamedTemporaryFile(delete=False) as tmp:
                        tmp.write(decrypted)
                        tmp_path = tmp.name
                    logger.debug(f"Temporary decrypted file stored at {tmp_path}")

                    backup_path = f"{path}.bak"
                    logger.debug(f"Creating backup: {backup_path}")
                    self.adb.shell(f'cp "{path}" "{backup_path}"')

                    self.adb.shell(f'rm "{path}"')
                    logger.debug(f"Deleted original file on device: {path}")

                    self.adb.execute(f'push "{tmp_path}" "{path}"')
                    logger.debug(f"Pushed decrypted file back to: {path}")
                    os.remove(tmp_path)
                else:
                    logger.warning(f"No key could decrypt {path}. Possibly not AES-encrypted.")
            except Exception as e:
                logger.error(f"Error processing {path}: {e}")

    def restore_backups(self):
        logger.info("Restoring .bak backups on device...")
        files = self.list_files()
        for path in files:
            backup = f"{path}.bak"
            try:
                self.adb.shell(f"mv '{backup}' '{path}'")
                logger.success(f"Restored backup: {path}")
            except Exception as e:
                logger.warning(f"Failed to restore {backup}: {e}")


def main():
    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level="DEBUG")

    parser = argparse.ArgumentParser(description="AES File Decryptor via ADB")
    parser.add_argument("mode", choices=["-d", "-e", ""], nargs="?", default="", help="ADB mode")
    parser.add_argument("--types", nargs="+", default=[".jpg", ".xml"], help="File extensions to scan (e.g., .jpg .xml)")
    parser.add_argument("--restore", action="store_true", help="Restore .bak backups instead of decrypting")
    parser.add_argument("--verify-filetype", action="store_true", help="Check file signature before restoring")
    args = parser.parse_args()

    decryptor = AESDecryptor(args.mode, args.types, args.verify_filetype)
    if args.restore:
        decryptor.restore_backups()
    else:
        decryptor.decrypt_files()


if __name__ == "__main__":
    main()
