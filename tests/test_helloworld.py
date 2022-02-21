from toolbox.helloworld import helloworld

def test_helloworld():
    assert helloworld() == 'Hello world!'
    assert helloworld('NAME') == 'Hello world, and more specifically, hello NAME!'
