# Arquivo app.spec

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=['.'],  # Use caminho relativo para o diretório do projeto
    binaries=[],
    datas=[
        ('data', 'data'),  # Inclui a pasta 'data' no executável
        ('resources', 'resources'),  # Inclui a pasta 'resources' no executável
    ],
    hiddenimports=[
        'pygame',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,  # Apenas uma ocorrência da opção noarchive
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)