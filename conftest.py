import pytest


@pytest.fixture(scope="class")  # When we define scope=class then fixture will run after class only.
def setup():
    print("I'll be execute first !")

    yield
    print("I'll be execute last !")


@pytest.fixture()
def dataload():
    print("User profile data being created.")
    return ["Darshan", "Patel", "Patel Darshan RamnikBhai"]


@pytest.fixture(params=[("chrome", "Rahul", "shetty"), ("firefox", "Rahul"), "IE"])
def crossBrowser(request):
    return request.param
