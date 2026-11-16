# agentapi-demo

A small project the [AgentAPI](https://github.com/k1dav-c/agentapi) hub hands issues to, for its
documentation's screenshots: an agent takes an issue, opens a pull request, answers the review and
posts what it cost.

`slug.py` turns titles into URL slugs:

```console
$ python3 slug.py "Hello, World!"
hello-world
```

`--max-length N` cuts the slug to at most N characters. It cuts at a dash where it can, so no word
is cut in half, and never leaves a trailing dash:

```console
$ python3 slug.py --max-length 12 "The quick brown fox"
the-quick
```

Run the tests with `python3 -m unittest`.
