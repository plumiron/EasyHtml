#!/usr/bin/env python

import easyhtml as eh


page = eh.html()

div1 = eh.div(id='div1')
div2 = eh.div(id='div2')
div1 << div2
div3 = div1 << eh.div(id='div3')

page << div1

p1 = eh.p(content='This is paragraph 1.', id='p1', align='left')
p2 = div3 << p1 << eh.p('This is paragraph 2.', id='p2')

print(page.render())
