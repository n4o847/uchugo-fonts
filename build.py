#!/usr/bin/env python3

import fontforge

def build():
    for name in ['UFSteleto']:
        font = fontforge.open(f'src/{name}.sfd')
        print(f'Building {font.fontname} {font.version}')
        font.generate(f'dist/{name}.ttf')
        font.generate(f'dist/{name}.otf')
        font.generate(f'dist/{name}.woff')
    print('Done')

if __name__ == '__main__':
    build()
