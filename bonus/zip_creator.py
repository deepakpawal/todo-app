import zipfile
import pathlib



def make_archive(filepaths, dest_dir):
    dest_dir=pathlib.Path(dest_dir,"compress.zip")
    with zipfile.ZipFile(dest_dir, 'w') as archive:

        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["bonus15.py","bonus16.py"],dest_dir="dest")