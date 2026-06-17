import os
import re

def get_markdown_title(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    # Remove the '# ' and strip formatting
                    title = line[2:].strip()
                    # Strip bold/italic if any
                    title = re.sub(r'\*\*|\*|`|_', '', title)
                    return title
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    # Fallback to filename
    base = os.path.basename(file_path)
    return os.path.splitext(base)[0]

def main():
    inf_dir = '/home/kokulan/Projects/Matury/informatika'
    
    toc_content = []
    
    # 1. Overview
    toc_content.append("- name: Přehled")
    toc_content.append("  href: index.md")
    toc_content.append("")
    
    # 2. Okruhy (Topics)
    okruhy_dir = os.path.join(inf_dir, 'okruhy')
    okruhy_items = []
    
    if os.path.exists(okruhy_dir):
        files = sorted(os.listdir(okruhy_dir))
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(okruhy_dir, file)
                title = get_markdown_title(file_path)
                # Escape double quotes in yaml titles if necessary
                title_escaped = title.replace('"', '\\"')
                okruhy_items.append(f'    - name: "{title_escaped}"\n      href: "okruhy/{file}"')
            elif file.endswith('.html'):
                # Handle HTML okruh if any (Základy číslicové techniky.html)
                file_path = os.path.join(okruhy_dir, file)
                # Simple name from file
                title = os.path.splitext(file)[0]
                okruhy_items.append(f'    - name: "{title}"\n      href: "okruhy/{file}"')
                
    if okruhy_items:
        toc_content.append("- name: Okruhy")
        toc_content.append("  items:")
        toc_content.extend(okruhy_items)
        toc_content.append("")
        
    # 3. Ulohy (Exercises)
    ulohy_items = []
    
    # C# exercises
    csharp_dir = os.path.join(inf_dir, 'ulohy', 'csharp')
    csharp_items = []
    if os.path.exists(csharp_dir):
        files = sorted(os.listdir(csharp_dir))
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(csharp_dir, file)
                title = get_markdown_title(file_path)
                title_escaped = title.replace('"', '\\"')
                csharp_items.append(f'        - name: "{title_escaped}"\n          href: "ulohy/csharp/{file}"')
                
    # Web exercises
    web_dir = os.path.join(inf_dir, 'ulohy', 'web')
    web_items = []
    if os.path.exists(web_dir):
        subdirs = sorted(os.listdir(web_dir))
        for subdir in subdirs:
            subdir_path = os.path.join(web_dir, subdir)
            if os.path.isdir(subdir_path):
                info_md = os.path.join(subdir_path, 'info.md')
                if os.path.exists(info_md):
                    title = get_markdown_title(info_md)
                    title_escaped = title.replace('"', '\\"')
                    web_items.append(f'        - name: "{title_escaped}"\n          href: "ulohy/web/{subdir}/info.md"')
                    
    # Combine exercises
    exercise_categories = []
    if csharp_items:
        exercise_categories.append("    - name: C#")
        exercise_categories.append("      items:")
        exercise_categories.extend(csharp_items)
    if web_items:
        if exercise_categories:
            exercise_categories.append("")
        exercise_categories.append("    - name: Web")
        exercise_categories.append("      items:")
        exercise_categories.extend(web_items)
        
    if exercise_categories:
        toc_content.append("- name: Úlohy")
        toc_content.append("  items:")
        toc_content.extend(exercise_categories)
        toc_content.append("")
        
    # Write to informatika/toc.yml
    toc_path = os.path.join(inf_dir, 'toc.yml')
    with open(toc_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(toc_content))
    print(f"Generated {toc_path}")

if __name__ == '__main__':
    main()
