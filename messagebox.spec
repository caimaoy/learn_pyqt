# -*- mode: python -*-
a = Analysis(['messagebox.py'],
             pathex=['D:\\learn_pyqt'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='messagebox.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
