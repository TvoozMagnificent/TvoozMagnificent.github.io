
from glob import glob
from re import sub

site_url = "TvoozMagnificent.github.io/test/"
source_directory = \
    "/Users/luchang/Desktop/pythonprojects/TvoozMagnificent.github.io/source/test/"
output_directory = \
    "/Users/luchang/Desktop/pythonprojects/TvoozMagnificent.github.io/test/"

filenames = {
    file[:-4]: open(file).read().strip().split('\n', 1)[0]
    for file in glob(f'{source_directory}*.txt')
}

for file in filenames:
    text = open(f'{file}.txt').read().strip().split('\n', 1)[1]
    for to_replace in filenames:
        text = text.replace(f'[{to_replace.split("/")[-1]}]',
            f'[{filenames[to_replace]}]'
            f'<a href="{to_replace.split("/")[-1]}.html">{filenames[to_replace]}</a>')
    open(f'{file.replace("/source", "")}.html', 'w').write(text)
