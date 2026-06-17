import os
import re

def clean_escapes(content):
    # Regex to match:
    # 1. Code blocks: ```...```
    # 2. Inline code: `...`
    # 3. Math blocks: $$...$$
    # 4. Inline math: $...$
    pattern = re.compile(
        r'(```[a-zA-Z0-9#+\-]*\n.*?\n```'
        r'|`[^`\n]+`'
        r'|\$\$.*?\$\$'
        r'|\$[^\$\n]+\$)',
        re.DOTALL
    )
    
    parts = []
    last_end = 0
    for match in pattern.finditer(content):
        # Text before the match (plain text)
        plain = content[last_end:match.start()]
        parts.append(('plain', plain))
        
        # The matched code/math block
        block = match.group(0)
        parts.append(('code', block))
        
        last_end = match.end()
        
    plain = content[last_end:]
    parts.append(('plain', plain))
    
    cleaned_parts = []
    for kind, text in parts:
        if kind == 'plain':
            # Remove escapes
            escapes = [
                (r'\==', '=='),
                (r'\!=', '!='),
                (r'\-', '-'),
                (r'\+', '+'),
                (r'\*', '*'),
                (r'\=', '='),
                (r'\.', '.'),
                (r'\_', '_'),
                (r'\(', '('),
                (r'\)', ')'),
                (r'\[', '['),
                (r'\]', ']'),
                (r'\&', '&'),
                (r'\/', '/'),
                (r'\>', '>'),
                (r'\<', '<'),
                (r'\!', '!'),
                (r'\?', '?'),
                (r'\~', '~'),
                (r'\#', '#'),
                (r'\"', '"'),
                (r"\'", "'"),
            ]
            for esc, raw in escapes:
                text = text.replace(esc, raw)
            
            # Replace escaped backslashes last
            text = text.replace(r'\\', '\\')
            
            # Clean trailing spaces from each line
            lines = text.split('\n')
            cleaned_lines = []
            for line in lines:
                # Replace tabs with 4 spaces
                line_no_tabs = line.replace('\t', '    ')
                cleaned_lines.append(line_no_tabs.rstrip())
            text = '\n'.join(cleaned_lines)
            
            cleaned_parts.append(text)
        else:
            cleaned_parts.append(text)
            
    return ''.join(cleaned_parts)

def fix_title_and_structure(file_path, content):
    filename = os.path.basename(file_path)
    title_suggested = os.path.splitext(filename)[0]
    
    # Check if this is an okruhy file and if it starts with a title
    lines = content.split('\n')
    
    # Strip leading empty lines
    start_idx = 0
    while start_idx < len(lines) and not lines[start_idx].strip():
        start_idx += 1
        
    if start_idx >= len(lines):
        return content
        
    # Check if the first non-empty line starts with '# '
    first_line = lines[start_idx].strip()
    if not first_line.startswith('# '):
        # We need to insert a title
        title_line = f"# {title_suggested}\n"
        print(f"Adding title to {filename}: {title_line.strip()}")
        # Check if the first line is an outline or osnova, and make sure we have a clean transition
        content_with_title = title_line + '\n' + '\n'.join(lines[start_idx:])
        return content_with_title
        
    return content

def fix_links(file_path, content):
    # Fix asset links:
    # 1. Change absolute asset links '/assets/...' to '/informatika/assets/...'
    # 2. Change absolute task texts links '/ulohy/texty/...' to '/informatika/ulohy/texty/...'
    content = content.replace('(/assets/', '(/informatika/assets/')
    content = content.replace('(/ulohy/texty/', '(/informatika/ulohy/texty/')
    
    # If the file is under ulohy/web, replace './' in iframe or anchor links with 'index.html'
    if 'ulohy/web' in file_path:
        content = content.replace('src="./"', 'src="index.html"')
        content = content.replace('href="./"', 'href="index.html"')
        
    return content

def main():
    root_dir = '/home/kokulan/Projects/Matury/informatika'
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}...")
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 1. Clean escapes and tabs
                cleaned = clean_escapes(content)
                
                # 2. Fix links (assets, texts, iframes)
                cleaned = fix_links(file_path, cleaned)
                
                # 3. Add title if missing (specifically for files under okruhy)
                if 'okruhy' in file_path:
                    cleaned = fix_title_and_structure(file_path, cleaned)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned)

if __name__ == '__main__':
    main()
