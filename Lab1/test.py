import main_task

with open('input.txt', 'r') as fin:
    text = fin.readline()
with open('output.txt', 'w') as fout:
    print(main_task.encode(text), file=fout)
