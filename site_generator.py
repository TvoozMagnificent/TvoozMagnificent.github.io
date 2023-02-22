
from glob import glob
from re import sub

projects = ["test"]

for project in projects:
    site_url = f"TvoozMagnificent.github.io/{projects}/"
    source_directory = \
        f"/Users/luchang/Desktop/pythonprojects/TvoozMagnificent.github.io/source/{projects}/"
    output_directory = \
        f"/Users/luchang/Desktop/pythonprojects/TvoozMagnificent.github.io/{projects}/"

    filenames = {
        file[:-4]: open(file).read().strip().split('\n', 1)[0]
        for file in glob(f'{source_directory}*.txt')
    }

    for file in filenames:
        text = "# " + open(f'{file}.txt').read().strip()
        for to_replace in filenames:
            text = text.replace(f'[{to_replace.split("/")[-1]}]',
                f'[{filenames[to_replace]}]({to_replace.split("/")[-1]}.html)')
        open(f'{file.replace("/source", "")}.html', 'w').write(text)
