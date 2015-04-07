# -*- mode: python -*-
a = Analysis(['test_py2exe.py'],
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
          name='test_py2exe.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
