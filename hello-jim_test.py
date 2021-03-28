from hello-jim import hello_jim

# Jim is a good guy, this should work.
def test_one():
    assert hello_jim(1) == "hello, Jim."

# Sometimes I like to say hello to Jim many times.
def test_two():
    assert hello_jim(2) == "hello, hello, Jim."
