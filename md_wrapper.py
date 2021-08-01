from pathlib import Path
from shutil import move

__template = Path('md_wrapper_template.html').read_text()


def to_html(path: Path):
    return __template.replace('{PATH}', path.__str__())


def read_files(path: Path):
    return filter(lambda f: not f.is_dir(), list(path.rglob('*.md')))


def main():
    path = Path('docs')
    files = read_files(path)
    for file in files:
        name = file.name
        directory = file

        file = file.rename('__temp')

        directory.mkdir()
        move(file, directory.joinpath(name))

        index = directory.joinpath('index.html')
        index.write_text(to_html(Path(name)))


main()
