import zipfile
import pathlib


def make_archive(filepaths, destination):
    dest_path = pathlib.Path(destination, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["bonus3.py", "bonus5.py"], destination="dest")
