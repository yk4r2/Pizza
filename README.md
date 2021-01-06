# Pizza project
You can either enter menu or bake pizza.
## Menu entering
`python cli.py menu`
## Pizza baking
We can deliver your pizza to you or it is possible to take it yourself.\
With delivery: `python cli.py order Margherita --delivery`\
Without one: `python cli.py order Hawaiian`\
You can even choose size: `python cli.py order Pepperoni --size=M`
# Tests coverage
```
│============= test session starts =============│
│platform linux -- Python 3.8.6, pytest-6.2.1, p│
│platform linux -- Python 3.8.6, pytest-6.2.1, p│
│y-1.10.0, pluggy-0.13.1                        │
│rootdir: /home/yk4r2/Documents/Pizza           │
│plugins: cov-2.10.1                            │
│collected 12 items                             │
│                                               │
│tests/test_cli.py ......                [ 50%] │
│tests/test_pizza.py ......              [100%] │
│                                               │
│============= 12 passed in 0.07s ==============│
```

All I made with my *** idea to use regular expressions is 50% coverage. I'd better use mock.patch, but "it is too easy".
