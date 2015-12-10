# YaMath

A comprehensive demo of python package development.

## Reading

- [Hitchhiker's Guide to Python!](http://docs.python-guide.org/en/latest/)
- [Code Like a Pythonista: Idiomatic Python](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)


## Tools

- python version control, [pyenv](https://github.com/yyuu/pyenv)
- project coding style consistency, [editorconfig](http://editorconfig.org/)
- docstring styling, [google docstring style](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html)
- docstring test, [doctest](https://docs.python.org/2/library/doctest.html)
- test framework, [pytest](http://pytest.org/latest/contents.html)
- advanced test, [mock](https://pypi.python.org/pypi/mock)
- test coverage, [pytest-cov](https://pypi.python.org/pypi/pytest-cov)
- distribute package to private pypi, [devpi](http://doc.devpi.net/latest/userman/index.html)


## Project Description

```

.
├── .editorconfig
├── MANIFEST.in
├── README.md
├── setup.py
├── tests
│   └── test_add.py
├── tox.ini
└── yamath.py
```

- _.editorconfig_, coding style configuration
- _yamath.py_ is our module to be distributed
- _setup.py_ declare the infomation of our package
- _MANIFEST.in_ tell _setup.py_ to distribute more files
- _tox.ini_ controls multiple python version and how we test our package
- any file under _tests_ start with `test_` will be found by `py.test`
