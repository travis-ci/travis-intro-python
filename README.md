# travis-intro-python

This is an example application written in Python for
introducing users to basic features of Travis CI.

> This is the fourth portion of the guided tour of Travis CI.
> If you haven't done so, please start with the
> [initial stage](../../tree/01.intro).


## Configuring deployment with GitHub Releases

Having defined the GitHub token in our repository on Travis CI,
it is time to configure deployemnt.

Edit `.travis.yml` to read:

```yaml
language: python
script: python test/test_simple_server.py
# ⬇ new!
deploy:
  provider: releases
  api_key: $GITHUB_OAUTH_TOKEN
  file: lib/server.py
  on:
    tags: true
```

### A note on YAML

Note that YAML is quite strict on the indentation rules.
Indentations are done with at least 2 white spaces, and
they indicate the data nesting.

If you are unsure if you wrote valid YAML (or even if you
are sure), it is a good idea to validate it.
There are many tools for this, including
[Online YAML Parser](https://yaml-online-parser.appspot.com/)
and
[YAML Validator](https://yamlvalidator.com/).

## Tag, push, and deploy!

Commit this change, tag the commit, and push.

```sh-session
$ git add .travis.yml
$ git commit -m "Deploy to GitHub Releases"
$ git tag v0.0.1
$ git push origin --tags
```

Upon pushing the tag, you will see a new build at
https://travis-ci.org/OWNER/travis-intro-ruby/builds.

## Confirm that a new GitHub Release is created

At the end of the build, deployment is triggered, and a new release
will show up with the tag `v0.0.1` in your repository's
Releases page https://github.com/OWNER/travis-intro-ruby/releases.

### Troubleshooting

If the release does not show up, check:

1. `GITHUB_OAUTH_TOKEN` has correct scope (`public_repo` or `repo`).
1. YAML file is indented correctly.
1. The commit is tagged.

## Congratulations! 🎉

You've made it!
You have automated a GitHub release process from commiting a code change
to the release.

## Further Reading

### Continuous Integration

- [Essay on Continuous Integration by Martin Fowler](https://martinfowler.com/articles/continuousIntegration.html)
- [Continuous Integration](https://www.informit.com/store/continuous-integration-improving-software-quality-and-9780321336385) by Duval, et al.

### Travis CI

- [Documentation](https://docs.travis-ci.com)
