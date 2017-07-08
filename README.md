# Data Sinez

Slack stats slide builder

- Purpose: Fun
- Correctness: None
- Accuracy: None

# Requirements

- Build: [Python3](https://www.python.org/downloads/)
- Present: [mdp](https://github.com/visit1985/mdp)

```
$ pip install -r requirements.txt
```

## Run

```
$ ./build.py
$ mdp output/stats.md
```

one of the build steps combines all the logs into a single frame prior to
generating the stats; This step takes a while to complete. However, every
build caches the combined logs into a single file stored on disk. You can
opt not to rebuild the combined logs everytime by simply using `--cached`.

```
$ ./build --cached
```
