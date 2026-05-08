import glob
import os

path = r'c:\Users\admin\.gemini\antigravity\brain\_company\_agents\youtube\tools\*.py'
for file in glob.glob(path):
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if 'sys.stdout.reconfigure' not in c:
        idx = c.find('import ')
        if idx != -1:
            end_idx = c.find('\n', idx)
            new_c = c[:end_idx+1] + "try:\n    import sys\n    sys.stdout.reconfigure(encoding='utf-8')\nexcept:\n    pass\n" + c[end_idx+1:]
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_c)
            print('Fixed', file)
