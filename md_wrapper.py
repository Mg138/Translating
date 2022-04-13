from pathlib import Path
from shutil import move
import markdown

__template = Path('md_wrapper_template.html').read_text()


def to_html(path: Path, md):
    return __template.replace('{NAME}', path.parent.name + '/' + path.name)\
                     .replace('{MD}', md)


def read_files(path: Path):
    return filter(lambda f: not f.is_dir(), list(path.rglob('*.md')))


def main():
    path = Path('docs')
    files = read_files(path)

    for file in files:
        directory = file
        html = directory.joinpath('index.html')

        filedata = file.read_text()

        md = markdown.markdown(filedata)

        file.unlink()

        directory.mkdir()
        html.write_text(to_html(html, md))



main()
