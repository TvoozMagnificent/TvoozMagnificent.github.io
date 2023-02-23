
from glob import glob
from re import sub
from os import mkdir

from split import repo
projects = [repo]
for project in projects:
    site_url = f"TvoozMagnificent.github.io/{project}/"
    source_directory = \
        f"/Users/luchang/Desktop/pythonprojects/TvoozMagnificent.github.io/source/{project}/"
    output_directory = \
        f"/Users/luchang/Desktop/pythonprojects/TvoozMagnificent.github.io/{project}/"

    filenames = {
        file[:-4]: open(file).read().strip().split('\n', 1)[0]
        for file in glob(f'{source_directory}*.txt')
    }

    try: mkdir(output_directory)
    except: pass

    for file in filenames:
        text = open(f'{file}.txt').read().strip().split('\n', 1)[-1]
        for to_replace in filenames:
            text = text.replace(f'[{to_replace.split("/")[-1]}]',
                f'<a href="{to_replace.split("/")[-1]}.html">{filenames[to_replace]}</a>')
        open(f'{file.replace("/source", "")}.html', 'w').write(text)
