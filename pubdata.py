from scholarly import scholarly
import os

# 确保 _publications 目录存在
if not os.path.exists('./_publications'):
    os.makedirs('./_publications')

# 获取作者信息
search_query = scholarly.search_author_id('VL1nzesAAAAJ')
author = scholarly.fill(search_query, sections=['basics', 'publications'])

# 遍历所有论文并生成 markdown 文件
for pub in author['publications']:
    # 获取完整的出版物信息
    filled_pub = scholarly.fill(pub)
    
    try:
        # 生成作者列表
        authors = filled_pub.get('bib', {}).get('author', '').split(' and ')
        authors_yaml = '\n'.join([f'  - {author.strip()}' for author in authors if author.strip()])
        
        # 生成 markdown 文件内容
        content = f"""---
title: "{filled_pub.get('bib', {}).get('title', '')}"
authors:
{authors_yaml}
venue: "{filled_pub.get('bib', {}).get('venue', 'Arxiv Preprint')}"
year: {filled_pub.get('bib', {}).get('pub_year', '')}"
abstract: "{filled_pub.get('bib', {}).get('abstract', '')}"
links:
  arxiv: "{filled_pub.get('pub_url', '')}"
  citations: "{filled_pub.get('citedby_url', '')}"
weight: {filled_pub.get('num_citations', 0)}
---
"""
        # 生成安全的文件名
        safe_title = filled_pub.get('bib', {}).get('title', '').lower()
        safe_title = ''.join(c if c.isalnum() or c in '-_ ' else '-' for c in safe_title)
        safe_title = safe_title.replace(' ', '-')
        filename = f"./_publications/{safe_title}.md"
        
        # 写入文件
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Created: {filename}")
            
    except Exception as e:
        print(f"Error processing publication: {e}")
        continue