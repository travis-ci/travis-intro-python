# travis-intro-python

This is an example application written in Python for
introducing users to basic features of Travis CI.

> This is the fourth portion of the guided tour of Travis CI.
> If you haven't done so, please start with the
> [initial stage](../../tree/01.intro).

## What went wrong?

Our initial build failed, because the default configuration for
Python did not work well.

In particular, there is no real build step that Travis CI taks

## Fixing the build

Since there is no default for Python builds, we must define it.

Edit `.travis.yml` to read:

```yaml
language: python
script: python test/test_simple_server.py # <== new
```

Commit this change, and push to GitHub.

```sh-session
$ git add .travis.yml
$ git commit -m "Override script step"
$ git push origin
```

## Celebrate the passing build

The build passes now. Yes! 🎉

## Next step

In [the next step](../../tree/05.deployment), we learn about deploying our code.
