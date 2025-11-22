#!/usr/bin/env python3
"""
使用 AI 翻译将英文内容翻译为其他语言
"""
import json
import re
import time
from pathlib import Path
from typing import Dict, List
from googletrans import Translator

# 支持的语言
LANGUAGES = {
    'zh': 'Chinese',
    'ru': 'Russian',
    'ja': 'Japanese',
    'fr': 'French',
    'es': 'Spanish'
}

# 翻译延迟（避免 API 限制）
TRANSLATE_DELAY = 1.0

# 需要翻译的固定文本
FIXED_TEXTS = {
    'en': {
        'title': 'Awesome MCP Projects',
        'last_updated': 'Last updated:',
        'total_projects': 'Total projects:',
        'subtitle': 'A curated list of awesome Model Context Protocol (MCP) projects collected from GitHub.',
        'table_of_contents': 'Table of Contents',
        'contributing': 'Contributing',
        'contributing_desc': "Found a great MCP project that's missing? Feel free to open an issue or submit a PR!",
        'license': 'License',
        'license_desc': 'This list is licensed under the Apache License 2.0. See the LICENSE file for details.',
        'tags': 'Tags:',
        'categories': {
            'servers': 'MCP Servers',
            'clients': 'MCP Clients',
            'tools': 'Tools & Libraries',
            'examples': 'Examples',
            'documentation': 'Documentation'
        }
    }
}


def translate_text(translator: Translator, text: str, dest_lang: str, max_retries: int = 3) -> str:
    """翻译文本，带重试机制"""
    if not text or not text.strip():
        return text
    
    for attempt in range(max_retries):
        try:
            result = translator.translate(text, dest=dest_lang)
            time.sleep(TRANSLATE_DELAY)
            return result.text
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"  翻译失败，重试 {attempt + 1}/{max_retries}: {str(e)}")
                time.sleep(TRANSLATE_DELAY * 2)
            else:
                print(f"  翻译失败，跳过: {str(e)}")
                return text
    return text


def translate_markdown_file(input_file: str, output_file: str, target_lang: str):
    """翻译 Markdown 文件"""
    print(f"\n翻译到 {LANGUAGES[target_lang]} ({target_lang})...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    translator = Translator()
    
    # 提取需要翻译的部分
    lines = content.split('\n')
    translated_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 跳过代码块
        if line.strip().startswith('```'):
            translated_lines.append(line)
            i += 1
            # 跳过整个代码块
            while i < len(lines) and not lines[i].strip().startswith('```'):
                translated_lines.append(lines[i])
                i += 1
            if i < len(lines):
                translated_lines.append(lines[i])
                i += 1
            continue
        
        # 跳过链接和代码
        if '[' in line and '](' in line:
            # 保留链接格式，只翻译文本部分
            pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
            matches = list(re.finditer(pattern, line))
            
            if matches:
                translated_line = line
                # 从后往前替换，避免索引问题
                for match in reversed(matches):
                    link_text = match.group(1)
                    link_url = match.group(2)
                    
                    # 不翻译数字开头的链接（如 "1. [name](url)"）
                    if link_text and not link_text[0].isdigit():
                        translated_text = translate_text(translator, link_text, target_lang)
                        translated_line = (
                            translated_line[:match.start()] +
                            f'[{translated_text}]({link_url})' +
                            translated_line[match.end():]
                        )
                
                translated_lines.append(translated_line)
                i += 1
                continue
        
        # 跳过只有特殊字符或URL的行
        if (line.strip().startswith('#') or 
            line.strip().startswith('>') or
            line.strip().startswith('-') or
            line.strip().startswith('*') or
            line.strip().startswith('|') or
            'http' in line or
            line.strip() == '' or
            line.strip() == '---' or
            line.strip().startswith('`')):
            
            # 特殊处理标题和引用
            if line.strip().startswith('#') and '#' in line:
                # 提取标题文本（跳过 # 符号）
                title_text = re.sub(r'^#+\s*', '', line).strip()
                if title_text and not title_text.startswith('['):
                    translated_title = translate_text(translator, title_text, target_lang)
                    translated_lines.append(line.replace(title_text, translated_title))
                else:
                    translated_lines.append(line)
            elif line.strip().startswith('>'):
                # 提取引用文本
                quote_text = line.strip()[1:].strip()
                if quote_text:
                    translated_quote = translate_text(translator, quote_text, target_lang)
                    translated_lines.append(f"> {translated_quote}")
                else:
                    translated_lines.append(line)
            else:
                translated_lines.append(line)
            
            i += 1
            continue
        
        # 翻译普通文本行
        if line.strip() and not line.strip().startswith('⭐') and not line.strip().startswith('🔤'):
            translated_line = translate_text(translator, line, target_lang)
            translated_lines.append(translated_line)
        else:
            translated_lines.append(line)
        
        i += 1
    
    translated_content = '\n'.join(translated_lines)
    
    # 保存翻译后的文件
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated_content)
    
    print(f"✓ 翻译完成: {output_file}")


def translate_fixed_texts(translator: Translator, lang: str) -> Dict:
    """翻译固定文本"""
    fixed_texts = {}
    
    for key, value in FIXED_TEXTS['en'].items():
        if isinstance(value, dict):
            fixed_texts[key] = {}
            for k, v in value.items():
                fixed_texts[key][k] = translate_text(translator, v, lang)
        else:
            fixed_texts[key] = translate_text(translator, value, lang)
    
    return fixed_texts


def main():
    """主函数"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    en_file = project_root / 'docs' / 'en' / 'projects.md'
    
    if not en_file.exists():
        print(f"Error: {en_file} not found. Please run generate_markdown.py first.")
        return
    
    print("开始翻译 Markdown 文件...")
    print("注意: 翻译过程可能需要较长时间，请耐心等待...")
    
    # 翻译到各种语言
    for lang_code, lang_name in LANGUAGES.items():
        try:
            output_file = project_root / 'docs' / lang_code / 'projects.md'
            translate_markdown_file(str(en_file), str(output_file), lang_code)
        except Exception as e:
            print(f"翻译到 {lang_name} 时出错: {str(e)}")
            continue
    
    print("\n所有翻译完成！")


if __name__ == '__main__':
    main()

