
repo = "calculus"
content = open(repo + '.txt').read().strip().split('\n\n')
content = [
    [
        entry.split(':\n', 1)[0],
        entry.split(':\n', 1)[0],
        entry.split(':\n', 1)[1],
    ]
    for entry in content
]

for file, title, content in content:
    open(f'source/{repo}/{file}.txt', 'w').write(title + '\n' + content)
