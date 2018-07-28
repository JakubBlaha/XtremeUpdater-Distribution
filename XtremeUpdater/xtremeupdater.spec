# -*- mode: python -*-
from kivy.deps import sdl2, glew
import PyInstaller.config
PyInstaller.config.CONF['distpath'] = "C:\\Users\\jakub\\Desktop\\XtremeUpdater dist"

block_cipher = None

a = Analysis(['main.py'],
             pathex=['C:\\Users\\jakub\\Desktop\\XtremeUpdater\\src'],
             binaries=[],
             datas=[],
             hiddenimports=['get_version_number', 'tweaks'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='XtremeUpdater',
          debug=False,
          strip=False,
          console=True,
          icon='img/icon.ico')
coll = COLLECT(exe, Tree('.'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               name='XtremeUpdater')
