
from glob import glob
from re import sub
from os import mkdir

projects = ["test"]

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
        content = open(f'{file}.txt').read().strip().split('\n', 1)
        text = "# " + content[0] + '\n\n\n\n\n' + content[1]
        for to_replace in filenames:
            text = text.replace(f'[{to_replace.split("/")[-1]}]',
                f'[{filenames[to_replace]}]({to_replace.split("/")[-1]}.html)')
        open(f'{file.replace("/source", "")}.html', 'w').write(text)
