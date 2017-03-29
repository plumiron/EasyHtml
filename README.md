# easyhtml
A tool to generate html easily with Python, inspired by [pyh](https://github.com/hanxiaomax/pyh).

## Installation
```bash
python setup.py install
```

## Usage
```python
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
```

Output:
```html
<html>
    <div id="div1">
        <div id="div2">
        </div>
        <div id="div3">
            <p id="p1" align="left">
                This is paragraph 1.
                <p id="p2">
                    This is paragraph 2.
                </p>
            </p>
        </div>
    </div>
</html>
```
