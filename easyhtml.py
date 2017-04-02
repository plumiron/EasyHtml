import html as _html

settings = dict(
    indent = 4
)


class Tag(object):
    """
    Base tag
    """
    def __init__(self, *pargs, **kargs):
        self._attrs = kargs
        self._name = self.__class__.__name__
        self._indent_level = 0

    def __iadd__(self, obj):
        raise NotImplementedError

    def __lshift__(self, obj):
        raise NotImplementedError

    def _reindent(self, level):
        self._indent_level = level

    def is_void(self):
        return isinstance(self, VoidTag)

    def render(self):
        raise NotImplementedError


class VoidTag(Tag):
    """
    Void tag
    """
    def render(self):
        output = ''.join([' {}="{}"'.format(item[0], item[1]) for item in self._attrs.items()])
        output = '{}<{}{}>\n'.format(' ' * settings['indent'] * self._indent_level, self._name, output)
        return output


class NonVoidTag(Tag):
    """
    Non-void tag
    """
    def __init__(self, content='', escape=True, *pargs, **kwargs):
        Tag.__init__(self, *pargs, **kwargs)
        self._children = list()
        self._content = _html.escape(content) if escape else content

    def __lshift__(self, obj):
        if isinstance(obj, Tag):
            self._children.append(obj)
            obj._reindent(self._indent_level + 1)
            return obj
        else:
            raise ValueError("Can't insert a non-tag object.")

    def _reindent(self, level):
        Tag._reindent(self, level)
        for child in self._children:
            child._reindent(self._indent_level + 1)

    def render(self):
        output = ''.join([' {}="{}"'.format(item[0], item[1]) for item in self._attrs.items()])
        output = '{}<{}{}>\n'.format(' ' * settings['indent'] * self._indent_level, self._name, output)
        
        if self._content:
            output += '{}{}\n'.format(' ' * settings['indent'] * (self._indent_level + 1), self._content)
        
        for child in self._children:
            output += child.render()
        
        output += '{}</{}>\n'.format(' ' * settings['indent'] * self._indent_level, self._name)
        
        return output


class a(NonVoidTag):
    pass


class abbr(NonVoidTag):
    pass


class address(NonVoidTag):
    pass


class area(VoidTag):
    pass


class article(NonVoidTag):
    pass


class aside(NonVoidTag):
    pass


class audio(NonVoidTag):
    pass


class b(NonVoidTag):
    pass


class base(VoidTag):
    pass


class bdi(NonVoidTag):
    pass


class bdo(NonVoidTag):
    pass


class blockquote(NonVoidTag):
    pass


class big(NonVoidTag):
    pass


class body(NonVoidTag):
    pass


class br(VoidTag):
    pass


class button(NonVoidTag):
    pass


class canvas(NonVoidTag):
    pass


class caption(NonVoidTag):
    pass


class cite(NonVoidTag):
    pass


class code(NonVoidTag):
    pass


class col(VoidTag):
    pass


class colgroup(NonVoidTag):
    pass


class command(NonVoidTag):
    pass


class datalist(NonVoidTag):
    pass


class dd(NonVoidTag):
    pass


class del_(NonVoidTag):
    def __init__(self, *args, **kwargs):
        NonVoidTag.__init__(self, *args, **kwargs)
        self._name = 'del'


class details(NonVoidTag):
    pass


class doctype(VoidTag):
    """
    Only support HTML5.
    """
    def __init__(self):
        VoidTag.__init__(self)
        self._name = '!DOCTYPE html'


class div(NonVoidTag):
    pass


class dfn(NonVoidTag):
    pass


class dialog(NonVoidTag):
    pass


class dl(NonVoidTag):
    pass


class dt(NonVoidTag):
    pass


class em(NonVoidTag):
    pass


class embed(NonVoidTag):
    pass


class fieldset(NonVoidTag):
    pass


class figcaption(NonVoidTag):
    pass


class figure(NonVoidTag):
    pass


class font(NonVoidTag):
    pass


class footer(NonVoidTag):
    pass


class form(NonVoidTag):
    pass


class frame(NonVoidTag):
    pass


class frameset(NonVoidTag):
    pass


class h1(NonVoidTag):
    pass


class h2(NonVoidTag):
    pass


class h3(NonVoidTag):
    pass


class h4(NonVoidTag):
    pass


class h5(NonVoidTag):
    pass


class h6(NonVoidTag):
    pass


class head(NonVoidTag):
    pass


class header(NonVoidTag):
    pass


class hr(VoidTag):
    pass


class html(NonVoidTag):
    pass


class i(NonVoidTag):
    pass


class iframe(NonVoidTag):
    pass


class img(NonVoidTag):
    pass


class input_(NonVoidTag):
    def __init__(self, *args, **kwargs):
        NonVoidTag.__init__(self, *args, **kwargs)
        self._name = 'input'


class ins(NonVoidTag):
    pass


class kbd(NonVoidTag):
    pass


class label(NonVoidTag):
    pass


class legend(NonVoidTag):
    pass


class li(NonVoidTag):
    pass


class link(VoidTag):
    pass


class map_(NonVoidTag):
    def __init__(self, *args, **kwargs):
        NonVoidTag.__init__(self, *args, **kwargs)
        self._name = 'map'


class mark(NonVoidTag):
    pass


class menu(NonVoidTag):
    pass


class menuitem(NonVoidTag):
    pass


class meta(VoidTag):
    pass


class meter(NonVoidTag):
    pass


class nav(NonVoidTag):
    pass


class noframes(NonVoidTag):
    pass


class noscript(NonVoidTag):
    pass


class object_(NonVoidTag):
    def __init__(self, *args, **kwargs):
        NonVoidTag.__init__(self, *args, **kwargs)
        self._name = 'object'


class ol(NonVoidTag):
    pass


class optgroup(NonVoidTag):
    pass


class option(NonVoidTag):
    pass


class output(NonVoidTag):
    pass


class p(NonVoidTag):
    pass


class param(VoidTag):
    pass


class pre(NonVoidTag):
    pass


class progress(NonVoidTag):
    pass


class q(NonVoidTag):
    pass


class script(NonVoidTag):
    pass


class section(NonVoidTag):
    pass


class select(NonVoidTag):
    pass


class small(NonVoidTag):
    pass


class source(NonVoidTag):
    pass


class span(NonVoidTag):
    pass


class strong(NonVoidTag):
    pass


class style(NonVoidTag):
    pass


class sub(NonVoidTag):
    pass


class summary(NonVoidTag):
    pass


class sup(NonVoidTag):
    pass


class table(NonVoidTag):
    pass


class tbody(NonVoidTag):
    pass


class td(NonVoidTag):
    pass


class textarea(NonVoidTag):
    pass


class tfoot(NonVoidTag):
    pass


class th(NonVoidTag):
    pass


class thead(NonVoidTag):
    pass


class time(NonVoidTag):
    pass


class tr(NonVoidTag):
    pass


class track(NonVoidTag):
    pass


class tt(NonVoidTag):
    pass


class u(NonVoidTag):
    pass


class ul(NonVoidTag):
    pass


class var(NonVoidTag):
    pass


class video(NonVoidTag):
    pass


class EasyHtml(html):
    """
    A complete HTML document.
    Users could use this class to create a complete HTML document.
    """
    def __init__(self, *pargs, **kargs):
        html.__init__(self, *pargs, **kargs)
        self._head = html.__lshift__(self, head())
        self._body = html.__lshift__(self, body())
        self._name = 'html'

    def __lshift__(self, obj):
        if (isinstance(obj, head) and hasattr(self, '_head')) \
            or (isinstance(obj, body) and hasattr(self, '_body')):
            raise ValueError('There is already a %s tag in the HTML document.' % obj.__class__.__name__)
        return self._body << obj

    def add_css(self, href='', **kargs):
        self._head << link(rel='stylesheet', type='text/css', href=href, **kargs)
        return self

    def add_js(self, src='', **kargs):
        self._body << script(src=src, **kargs)
        return self

    def add_js_snippet(self, snippet, **kargs):
        self._body << script(snippet, escape=False, **kargs)
        return self

    def add_meta(self, **kargs):
        self._head << meta(**kargs)
        return self

    def render(self):
        output = doctype().render()
        output += html.render(self)
        return output
