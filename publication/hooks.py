"""MkDocs hooks for the public site.

- Adds to the site the repo pages listed in "nav" (mkdocs.yml), read
  in place (lore/, regles/…), without copying them.
- In these pages, a link to an unpublished page (races, items, places,
  archives…) becomes plain text: the site doesn't show these pages.
"""
import os
import posixpath
import re

from mkdocs.structure.files import File

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)\s]+)\)')

published = set()


def _nav_paths(items):
    for item in items or []:
        if isinstance(item, str):
            yield item
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, str):
                    yield value
                else:
                    yield from _nav_paths(value)
        elif isinstance(item, list):
            yield from _nav_paths(item)


def on_files(files, config):
    published.clear()
    for path in _nav_paths(config['nav']):
        if '://' in path:
            continue
        published.add(path)
        if files.get_file_from_path(path) is None:
            abs_path = os.path.join(ROOT, path)
            if not os.path.isfile(abs_path):
                raise FileNotFoundError(f'Page du menu introuvable : {path}')
            files.append(File.generated(config, path, abs_src_path=abs_path))
    return files


def on_page_markdown(markdown, page, config, files):
    base = posixpath.dirname(page.file.src_uri)

    def keep_or_unlink(match):
        text, target = match.group(1), match.group(2)
        if re.match(r'^[a-z]+:', target) or target.startswith('#'):
            return match.group(0)
        path = target.split('#', 1)[0]
        resolved = posixpath.normpath(posixpath.join(base, path))
        if resolved in published:
            return match.group(0)
        return text

    return LINK.sub(keep_or_unlink, markdown)
