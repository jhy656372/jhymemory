import glob

path = r'c:\Users\admin\.gemini\antigravity\brain\_company\_agents\youtube\tools\*.py'
for file in glob.glob(path):
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    
    old_patch = "try:\n    import sys\n    sys.stdout.reconfigure(encoding='utf-8')\nexcept:\n    pass\n"
    new_patch = "try:\n    import sys\n    sys.stdout.reconfigure(encoding='utf-8')\n    sys.stderr.reconfigure(encoding='utf-8')\nexcept:\n    pass\n"
    
    if old_patch in c:
        c = c.replace(old_patch, new_patch)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(c)
        print('Fixed stderr in', file)
