import subprocess
import os
import json
import markdown2
import argparse
import re
from datetime import datetime
from slugify import slugify
import codecs

class GitHandler:
    def __init__(self,repo_path):
        self.repo_root = self.set_repo(repo_path)

    def set_repo(self,repo_path):
        repo_path = os.path.abspath(repo_path)
        if os.path.exists(repo_path):
            if os.path.isdir(repo_path):
                if os.path.exists(repo_path+'/.git'):
                    return repo_path
                else:
                    print """Repository doesn't exist. 
                    Follow the instruction in README."""
            else:
                print "Provide path to your repo directory"
                return None
        else:
            print "Path Does Not Exist"
            return None

    def add(self):
        subprocess.call(['git','add',self.repo_root + '/notes/'])

    def commit(self,message):
        subprocess.Popen(['git','--no-pager','commit','-m',message])

    def changed_files(self):
        return subprocess.check_output(['git','diff','--name-only',
                'HEAD']).split('\n')[:-1]


class Note:

    def __init__(self,title,content,tags=[],
            date=datetime.now().strftime("%d-%m-%Y %H:%M:%S")):
        self.title = title
        self.content_raw = content
        self.content = self.md_to_html(content)
        self.id = None
        self.tags = tags
        self.date_created = date

    def md_to_html(self, text):
        return markdown2.markdown(text, extras=['fenced-code-blocks'])

    def __str__(self):
        return """
#{0}

{1}

Posted on {2}
Tags: {3}
""".format(self.title,self.content_raw,self.date_created, ",".join(self.tags or [])).encode('utf-8')

class NoteDB:

    def __init__(self):
        #self.note = self.note_to_dict(note)
        self.data = self.get_db()

    def get_db(self):
        if os.path.isfile("../data.json"):
            json_data = codecs.open("../data.json",encoding='utf-8')
            # This is giving an 
            try:
                data = json.load(json_data)
                json_data.close()
                return data
            # VERY EXPERIMENTAL-- CHECK IOT OUT
            except:
                return "{}"
        else:
            author = raw_input("Enter your name: ")
            blog_title = raw_input("Blog title: ")
            content = {
                "Blog Title": blog_title,
                "Author": author,
                "count": 0,
                "notes": [],
                "pages": []
            }
            self.write_data(content)
            return content

    def write_data(self,data):
        data['count'] = len(data['notes'])
        with codecs.open("../data.json",encoding='utf-8',mode='w') as f:
            json.dump(data,f,ensure_ascii=False)

    def new_id(self):
        try:
            lngth = len(self.data['notes'])
            maxid = max([note['id'] for note in self.data['notes']])
            return max( lngth, maxid)
        except ValueError:
            return 0

    def note_to_dict(self,note):
        return {
            "id": self.new_id(),
            "title": note.title,
            "content": note.content,
            "tags": note.tags,
            "date_created": note.date_created
        }

    def all_entries(self):
        for note in self.data['notes']:
            print "{0} -- {1}".format(note['id'],note['title'])

    def get_entry(self,id):
        for note in self.data['notes']:
            if note['id'] == id:
                return note
        print "Error"

    def post_entry(self, note):
        titles = [n['title'] for n in self.data['notes']]
        if isinstance(note, Note):
            if note.title not in titles:
                self.data['notes'].append(self.note_to_dict(note))
                self.write_data(self.data)
            else:
                print "----------"
                for i,n in enumerate(self.data['notes']):
                    if note.title == n['title']:
                        print "----------"
                        self.data['notes'][i] = self.note_to_dict(note)
                        self.write_data(self.data)
        else: 
            print "Error: must be a note object"

    def put_entry(self,note):
        print "Not implemented"

    def delete_entry(self):
        print "Not implemented"

def cli_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode')
    parser.add_argument('-b', '--body')
    parser.add_argument('-t', '--title')
    parser.add_argument('-g', '--tags')
    return vars(parser.parse_args())

def inline_note(title,body,tags):
        if title and body:
            nt = Note(title,body,tags)
            ndb = NoteDB()
            ndb.post_entry(nt)
            #make sure file doesn't exist in notes/
            file = open(slugify(title)+'.md','w')
            file.write(str(nt))
            file.close()
        else:
            print "Title and body are required. Tags are optional."

def new_note(title, tags):
    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    text = "#{0}\n\nCreated on {2}\nTags:{1}".format(title,tags,date)
    filename = slugify(title)+'.md'
    f = open('../notes/'+filename,'w')
    f.write(text)
    f.close()
    os.system('{0} {1}'.format('xdg-open', '../notes/'+filename))

def parse_md(filename):
    f = open(filename,'r')
    s = f.read()
    f.close()
    title = re.findall(r'#(.+)\n',s)[0]
    tags = re.findall(r'Tags:(.+)',s)[0].strip().split(',')
    date = re.findall(r'Created on (.+)',s)[0].strip()
    body = re.findall(r'\n([^#].*)Created on', s, re.S)[0].strip()
    return title,body,date,tags

def build():

    git = GitHandler(os.path.dirname(os.getcwd()))
    git.add()
    git.commit("Gitnote commit")
    changed_files = git.changed_files()
    for filename in changed_files:
        if filename[-3:] == '.md':
            filename = '../' + filename
            if os.path.isfile(filename):
                print "-----"
                title,body,date,tags = parse_md(filename)
                nt = Note(title,body,tags,date)
                ndb = NoteDB()
                ndb.post_entry(nt)

def dispatch_method(args):
    if args['mode'] == "inline":
        inline_note(args['title'],args['body'],args['tags'].split(','))

    elif args['mode'] == "new":
        new_note(args['title'],args['tags'])

    elif args['mode'] == "build":
        build()

    else:
        print("Doesn't compute. Please type cli --help for usage")

dispatch_method(cli_parse())

