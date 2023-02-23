
repo = 'calculus'

from glob import glob

filenames = {
    file[len(f'source/{repo}/'):-4]:
        open(file).read().strip().split('\n', 1)[-1]
    for file in glob(f'source/{repo}/*.txt')
}

result = '\n\n'.join([entry + ':\n' + filenames[entry] for entry in filenames])
open(repo + '.txt', 'w').write(result)
