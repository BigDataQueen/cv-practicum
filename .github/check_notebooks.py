"""Выполнить ноутбуки целиком и напечатать выводы ячеек; ненулевой код, если хоть одна ячейка упала.

Запуск: python .github/check_notebooks.py *.ipynb   (выполненные копии — в папку executed/)
"""
import os
import sys

import nbformat
from nbclient import NotebookClient

os.makedirs('executed', exist_ok=True)
failed = []
PARTICIPANT = int(os.environ.get('PARTICIPANT', '0'))   # номер участника из поля ноутбука; пара — тот же номер по модулю 5
for src in sys.argv[1:]:
    nb = nbformat.read(src, as_version=4)
    for c in nb.cells:
        if c.cell_type == 'code':
            c.source = c.source.replace('participant = 0  #@param', 'participant = %d  #@param' % PARTICIPANT)
            c.source = c.source.replace('pair = 0  #@param', 'pair = %d  #@param' % (PARTICIPANT % 5))
    NotebookClient(nb, timeout=1800, kernel_name='python3', allow_errors=True,
                   resources={'metadata': {'path': 'executed'}}).execute()
    nbformat.write(nb, os.path.join('executed', os.path.basename(src)))
    print('\n' + '#' * 100 + '\n# ' + src + '\n' + '#' * 100)
    for i, c in enumerate(nb.cells):
        if c.cell_type != 'code':
            continue
        print('=== [%d] %s' % (i, c.source.splitlines()[0][:90]))
        for o in c.get('outputs', []):
            if o.output_type == 'stream':
                print(o.text[:4000], end='')
            elif o.output_type == 'error':
                failed.append('%s [%d] %s: %s' % (src, i, o.ename, o.evalue[:300]))
                print('!!! ERROR %s: %s' % (o.ename, o.evalue[:2000]))
                print('\n'.join(o.traceback)[-3000:])
            elif 'text/plain' in o.get('data', {}) and 'image/png' not in o.get('data', {}):
                print(o['data']['text/plain'][:3000])
            elif 'image/png' in o.get('data', {}):
                print('[рисунок]')
print('\nНомер участника: %d' % PARTICIPANT)
print('\n' + ('ВСЕ ЯЧЕЙКИ ВЫПОЛНЕНЫ БЕЗ ОШИБОК' if not failed else 'ОШИБКИ:\n' + '\n'.join(failed)))
sys.exit(1 if failed else 0)
