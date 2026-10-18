"""Достать картинки и напечатанный текст из выполненных ноутбуков: python .github/extract_images.py executed preview"""
import base64
import glob
import io
import os
import sys

import nbformat
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
lines = ['# Картинки выполненных ноутбуков', '', 'Ветку перезаписывает проверка при каждом обновлении `main`.', '']
for f in sorted(glob.glob(os.path.join(src, '*.ipynb'))):
    nb = nbformat.read(f, as_version=4)
    stem = os.path.basename(f)[:-6]
    lines += ['## ' + stem, '']
    for i, c in enumerate(nb.cells):
        k = 0
        text = ''.join(o.get('text', '') for o in c.get('outputs', []) if o.get('output_type') == 'stream')
        if text.strip():                                      # напечатанные числа — для сверки «Что заметить»
            lines += ['`[%d]` %s' % (i, c.source.splitlines()[0][:90]), '', '```', text.strip()[-1500:], '```', '']
        for o in c.get('outputs', []):
            if 'image/png' in o.get('data', {}):
                im = Image.open(io.BytesIO(base64.b64decode(o['data']['image/png']))).convert('RGB')
                if im.width > 1400:
                    im = im.resize((1400, round(im.height * 1400 / im.width)))
                name = '%s_%02d_%d.jpg' % (stem, i, k); k += 1
                im.save(os.path.join(out, name), quality=82)
                lines += ['`[%d]` %s' % (i, c.source.splitlines()[0][:90]), '', '![](%s)' % name, '']
open(os.path.join(out, 'README.md'), 'w').write('\n'.join(lines))
