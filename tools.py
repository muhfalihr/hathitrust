from utility import dtddList, unique


class Book:
    def __init__(self, list1, list2, item):
        self.list1 = list1
        self.list2 = list2
        self.item = item

    def author(self):
        if 'main_author' not in self.list1:
            return ''
        else:
            authors = dtddList(self.item, 'Main Author')
            if authors:
                return authors[0] if len(authors) == 1 else unique(authors)

    def relnam(self):
        if 'main_author' not in self.list1:
            return ''
        else:
            authors = dtddList(self.item, 'Main Author')
            if authors:
                return authors[0] if len(authors) == 1 else unique(authors)

    def language(self):
        if 'language(s)' not in self.list1:
            return ''
        else:
            indeks = self.list1.index('language(s)')
            return self.list2[indeks]

    def publish(self):
        if 'published' not in self.list1:
            return ''
        else:
            indeks = self.list1.index('published')
            return self.list2[indeks]

    def subject(self):
        if 'subjects' not in self.list1:
            return ''
        else:
            subjects = dtddList(self.item, 'Subjects')
            if subjects:
                return subjects[0] if len(subjects) == 1 else unique(subjects)

    def summaryTeks(self):
        if 'summary' not in self.list1:
            return ''
        else:
            indeks = self.list1.index('summary')
            return self.list2[indeks]

    def noteTeks(self):
        if 'note' not in self.list1:
            return ''
        else:
            indeks = self.list1.index('note')
            return self.list2[indeks]

    def physdesc(self):
        if 'physical_description' not in self.list1:
            return ''
        else:
            indeks = self.list1.index('physical_description')
            return self.list2[indeks]
