#!/usr/bin/python3

import os

import bibtexparser


def format_authors(entry):
    if 'author' not in entry:
        return '[]'

    authors = entry['author']

    def _format(author):
        if ',' not in author:
            return '"' + author.strip() + '"'
        sep = author.index(',')
        author = author[sep+1:].strip() + ' ' + author[:sep].strip()
        return '"' + author + '"'

    authors = authors.split('and')
    authors = [_format(author) for author in authors]
    return '[' + ','.join(authors) + ']'


def format_publisher(entry):
    entry_type = entry['ENTRYTYPE'].lower()
    publisher = ''
    if entry_type == 'inproceedings':
        publisher = entry['booktitle']
    elif entry_type == 'article':
        publisher = entry['journal']

    if 'year' in entry:
        publisher += ' ' + entry['year']

    return publisher.strip()


def fix(s):
    return s.replace('\n', '').replace('\\', '')


def main():
    script_dir = os.path.dirname(__file__)
    content_dir = os.path.join(os.path.dirname(script_dir), 'content')

    bib = bibtexparser.load(open(os.path.join(script_dir, 'seppi.bib')))
    for entry in bib.entries:
        name = entry['ID'].replace('/', '-').replace(':', '-')

        md_path = os.path.join(content_dir, 'publications', name+'.md')
        with open(md_path, 'w') as md_file:
            print('+++', file=md_file)
            print('title = ', '"' + fix(entry['title']) +'"', file=md_file)
            print('authors =', format_authors(entry), file=md_file)
            print('bibtex =', '"' + 'bib/' + name + '"', file=md_file)
            print('+++', file=md_file)
            if 'abstract' in entry:
                print(file=md_file)
                print(entry['abstract'], file=md_file)

            bib_path = os.path.join(content_dir, 'bib', name+'.md')
            with open(bib_path, 'w') as bib_file:
                print('+++', file=bib_file)
                print('title =', '"' + name + '"', file=bib_file)
                print('+++', file=bib_file)
                print(file=bib_file)
                print('@' + entry['ENTRYTYPE'] + '{' + entry['ID'] + ',',
                        file=bib_file)
                for key, value in entry.items():
                    if key not in ['ENTRYTYPE', 'ID']:
                        print('   ' + key + '={' + value + '},', file=bib_file)
                print('}', file=bib_file)


if __name__ == '__main__':
    main()
