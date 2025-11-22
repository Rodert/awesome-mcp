#!/usr/bin/env python3
"""
使用离线翻译将英文内容翻译为其他语言
使用 Argos Translate - 完全离线的翻译工具
"""
import re
from pathlib import Path
import argostranslate.package
import argostranslate.translate

# 支持的语言代码映射（Argos Translate 使用 ISO 639-1 代码）
LANGUAGES = {
    'zh': 'zh',
    'ru': 'ru',
    'ja': 'ja',
    'fr': 'fr',
    'es': 'es'
}

# 语言显示名称
LANGUAGE_NAMES = {
    'zh': 'Chinese',
    'ru': 'Russian',
    'ja': 'Japanese',
    'fr': 'French',
    'es': 'Spanish'
}

# 源语言（英文）
SOURCE_LANG = 'en'



def ensure_language_installed(from_code: str, to_code: str):
    """确保所需语言包已安装"""
    # 检查并安装语言包
    installed_languages = argostranslate.translate.get_installed_languages()
    
    from_lang = None
    to_lang = None
    
    for lang in installed_languages:
        if lang.code == from_code:
            from_lang = lang
        if lang.code == to_code:
            to_lang = lang
    
    if from_lang is None or to_lang is None:
        print(f"  安装语言包: {from_code} -> {to_code}")
        # 获取可用的语言包
        available_packages = argostranslate.package.get_available_packages()
        package_to_install = None
        
        for package in available_packages:
            if package.from_code == from_code and package.to_code == to_code:
                package_to_install = package
                break
        
        if package_to_install:
            argostranslate.package.install_from_path(package_to_install.download())
            # 重新获取已安装的语言
            installed_languages = argostranslate.translate.get_installed_languages()
            from_lang = [l for l in installed_languages if l.code == from_code][0]
            to_lang = [l for l in installed_languages if l.code == to_code][0]
        else:
            raise ValueError(f"找不到语言包: {from_code} -> {to_code}")
    
    return from_lang, to_lang

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


def translate_text(text: str, from_lang: str, to_lang: str, from_lang_obj=None, to_lang_obj=None) -> str:
    """使用 Argos Translate 翻译文本，失败则返回原文"""
    if not text or not text.strip():
        return text
    
    try:
        # 如果提供了语言对象，直接使用；否则确保语言包已安装
        if from_lang_obj is None or to_lang_obj is None:
            from_lang_obj, to_lang_obj = ensure_language_installed(from_lang, to_lang)
        
        # 翻译文本
        translated = argostranslate.translate.translate(text, from_lang_obj, to_lang_obj)
        return translated
    except Exception as e:
        print(f"  翻译失败，跳过（保留原文）: {str(e)}")
        return text


def translate_markdown_file(input_file: str, output_file: str, target_lang: str):
    """翻译 Markdown 文件"""
    target_lang_code = LANGUAGES.get(target_lang, target_lang)
    lang_name = LANGUAGE_NAMES.get(target_lang, target_lang)
    print(f"\n翻译到 {lang_name} ({target_lang_code})...")
    
    # 确保语言包已安装
    try:
        from_lang_obj, to_lang_obj = ensure_language_installed(SOURCE_LANG, target_lang_code)
    except Exception as e:
        print(f"  无法安装语言包: {str(e)}")
        print(f"  跳过 {lang_name} 的翻译")
        return
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
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
                        translated_text = translate_text(link_text, SOURCE_LANG, target_lang_code, from_lang_obj, to_lang_obj)
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
                    translated_title = translate_text(title_text, SOURCE_LANG, target_lang_code, from_lang_obj, to_lang_obj)
                    translated_lines.append(line.replace(title_text, translated_title))
                else:
                    translated_lines.append(line)
            elif line.strip().startswith('>'):
                # 提取引用文本
                quote_text = line.strip()[1:].strip()
                if quote_text:
                    translated_quote = translate_text(quote_text, SOURCE_LANG, target_lang_code, from_lang_obj, to_lang_obj)
                    translated_lines.append(f"> {translated_quote}")
                else:
                    translated_lines.append(line)
            else:
                translated_lines.append(line)
            
            i += 1
            continue
        
        # 翻译普通文本行
        if line.strip() and not line.strip().startswith('⭐') and not line.strip().startswith('🔤'):
            translated_line = translate_text(line, SOURCE_LANG, target_lang_code, from_lang_obj, to_lang_obj)
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


def main():
    """主函数"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    en_file = project_root / 'docs' / 'en' / 'projects.md'
    
    if not en_file.exists():
        print(f"Error: {en_file} not found. Please run generate_markdown.py first.")
        return
    
    print("开始翻译 Markdown 文件...")
    print("注意: 使用离线翻译 (Argos Translate)，首次运行需要下载语言包...")
    print("注意: 翻译过程可能需要较长时间，请耐心等待...")
    
    # 翻译到各种语言
    for lang_code, lang_code_map in LANGUAGES.items():
        lang_name = LANGUAGE_NAMES.get(lang_code, lang_code)
        try:
            output_file = project_root / 'docs' / lang_code / 'projects.md'
            translate_markdown_file(str(en_file), str(output_file), lang_code)
        except Exception as e:
            print(f"翻译到 {lang_name} 时出错: {str(e)}")
            continue
    
    print("\n所有翻译完成！")


if __name__ == '__main__':
    main()

