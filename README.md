# travis-intro-python

This is an example application written in Python for
introducing users to basic features of Travis CI.

## Fork, and look around

First, [fork this repository](https://github.com/travis-ci/travis-intro-python/fork).

Clone to your local development machine, and have a look around.

```sh-session
$ git clone https://github.com/OWNER/travis-intro-python.git
$ cd travis-intro-python
```

To start the server, run

```sh-session
$ python lib/server.py
```

If you visit [http://localhost:8000](http://localhost:8000), you should see
a bare minimum web page.

You can confirm that the following runs our basic test, and passes:

```sh-session
$ python test/test_simple_server.py
```

## Next step

Time to head on over to [the next step](../../tree/02.signup).
