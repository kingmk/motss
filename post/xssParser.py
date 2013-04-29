from htmllib import HTMLParser
from cgi import escape
from urlparse import urlparse
from formatter import AbstractFormatter
from htmlentitydefs import entitydefs
from xml.sax.saxutils import quoteattr
from member.models import MotssUser
import re

def xssescape(text):
    return escape(text, quote=True).replace(':','&#58;')

class XssParser(HTMLParser):
    def __init__(self, fmt = AbstractFormatter):
        HTMLParser.__init__(self, fmt)
        self.result = ""
        self.open_tags = []
        self.at_users = []

        self.permitted_tags = ['a', 'b', 'blockquote', 'br', 'i', 
        					'li', 'ol', 'ul', 'p', 'cite', 'span']

        self.requires_no_close = ['img', 'br']

        self.allowed_attributes = \
            {'a':['href','title', 'style'],
             'img':['src', 'width', 'height'],
             'blockquote':['type'],
             'span':['style']}

        self.allowed_schemes = ['http','https','ftp']

    def clear(self) :
        self.result = ''
        self.at_users = []

    def replace_at_user(self, matchobj) :
        matchstr = matchobj.group(0)
        username = matchstr[1:]
        rq = MotssUser.objects.values('id', 'username').filter(username=username)
        if rq.exists():
            self.at_users.append(rq.get())
            return '<a href="">%s</a>'%matchstr
        else:
            return matchstr

    def handle_data(self, data):
        if data:
            data = xssescape(data)
            if 'a' not in self.open_tags:
                pattern = '@[^\s]*'
                data = re.sub(pattern, self.replace_at_user, data)
            self.result += data

    def handle_charref(self, ref):
        if len(ref) < 7 and ref.isdigit():
            self.result += '&#%s;' % ref
        else:
            self.result += xssescape('&#%s' % ref)
    def handle_entityref(self, entitydefs):
        if ref in entitydefs:
            self.result += '&%s;' % ref
        else:
            self.result += xssescape('&%s' % ref)
    def handle_comment(self, comment):
        if comment:
            self.result += xssescape("<!--%s-->" % comment)
    def handle_starttag(self, tag, method, attrs):
        if tag not in self.permitted_tags:
            self.result += xssescape("<%s>" %  tag)
        else:
            bt = "<" + tag
            if tag in self.allowed_attributes:
                attrs = dict(attrs)
                self.allowed_attributes_here = \
                  [x for x in self.allowed_attributes[tag] if x in attrs \
                   and len(attrs[x]) > 0]
                for attribute in self.allowed_attributes_here:
                    if attribute in ['href', 'src', 'background']:
                        if self.url_is_acceptable(attrs[attribute]):
                            bt += ' %s="%s"' % (attribute, attrs[attribute])
                    else:
                        bt += ' %s=%s' % \
                           (xssescape(attribute), quoteattr(attrs[attribute]))
            if bt == "<a" or bt == "<img":
                return
            if tag in self.requires_no_close:
                bt += "/"
            bt += ">"
            self.result += bt
            self.open_tags.insert(0, tag)
            
    def handle_endtag(self, tag, attrs):
        bracketed = "</%s>" % tag
        if tag not in self.permitted_tags:
            self.result += xssescape(bracketed)
        elif tag in self.open_tags:
            self.result += bracketed
            self.open_tags.remove(tag)
            
    def unknown_starttag(self, tag, attributes):
        self.handle_starttag(tag, None, attributes)
    def unknown_endtag(self, tag):
        self.handle_endtag(tag, None)
    def url_is_acceptable(self,url):
        #parsed = urlparse(url)
        #return parsed[0] in self.allowed_schemes and '.' in parsed[1]
        return url.find('(')==-1

    def strip(self, rawstring):
        self.result = ""
        self.feed(rawstring)
        for endtag in self.open_tags:
            if endtag not in self.requires_no_close:
                self.result += "</%s>" % endtag
        return self.result
    def xtags(self):
        self.permitted_tags.sort()
        tg = ""
        for x in self.permitted_tags:
            tg += "<" + x
            if x in self.allowed_attributes:
                for y in self.allowed_attributes[x]:
                    tg += ' %s=""' % y
            tg += "> "
        return xssescape(tg.strip())