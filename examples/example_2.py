#!/usr/bin/env python

import easyhtml as eh


page = eh.EasyHtml()

div1 = page << eh.div(id='div1')
div2 = eh.div(id='div2')
div1 << div2 << eh.p('This is a script tag.')
div2 << eh.p('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js">')

page.add_meta(charset='utf-8')
page.add_meta(name='meta1', content='abc')

page.add_css(
    href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
    integrity='sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u',
    crossorigin='anonymous',
)

page.add_js(
    'https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js',
).add_js(
    src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js',
    integrity='sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa',
    crossorigin='anonymous',
).add_js_snippet(
    'document.write("<div>Hello World!</div>")',
)

print(page.render())
