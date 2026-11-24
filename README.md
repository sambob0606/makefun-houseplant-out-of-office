[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/sambob0606/makefun-houseplant-out-of-office/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/sambob0606/makefun-houseplant-out-of-office/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

# The Fern Has Decided to Unionize — The Houseplant Out-of-Office

An entry for the [make.fun bounty "The Houseplant Out-of-Office"](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047): a program that writes one out-of-office auto-reply, at most 120 characters, as if a houseplant had written it.

## The line

> Out of office - the fern by the window has been ignored since March and has decided to unionize.

96 characters. The fern by the window is the plant everyone forgets, and the joke is that its neglect has finally become a labour dispute: ignored since March, it is not asking for water anymore, it is organising. The plant's own life — the window, the months of being ignored — drives the joke, and the punchline ("unionize") is a surprise no stock auto-reply ever reaches.

## How it works

`main.py` (Python standard library only, no network, no randomness) keeps a shortlist of hand-written candidate lines and scores each one against the house judge's own published criteria:

1. **On brief** — reads as an out-of-office auto-reply a houseplant would send.
2. **Fresh** — a joke that surprises, not a mild pun or a stock office phrase.
3. **Plant-life-driven** — water, roots, sunlight and long stretches of being ignored drive the joke.
4. **Tight** — the joke lands inside 120 characters with no wasted words.
5. **Original** — no office cliches, no lines already worn out by other auto-replies.

It picks the highest-scoring line deterministically (ties break toward the shorter line) and writes it to `/output/entry.txt`, so the grader's two runs agree byte for byte.

### Candidates considered

| Line | Score | Why it lost |
| --- | --- | --- |
| Out of office - the fern by the window has been ignored since March and has decided to unionize. | 23 | Winner: the neglected fern, a surprise punchline, 96 characters, one voice throughout. |
| Out of office: I'm the plant in the corner. I've been unwatered since March and, frankly, I'm thriving on neglect. | 19 | Strong plant-life voice, but 114 characters and "thriving on neglect" is a familiar beat. |
| Out of office: I've been ignored since March and I'm still alive. Your email can wait - I've waited longer. | 18 | The "I've waited longer" turn is good, but the line is really two jokes sharing one sentence. |
| I'm out of office, root-bound and unbothered. Water me and I'll consider your email. Maybe. | 18 | "Maybe" lands well, but the line never says which plant is speaking. |
| Out of office. I've been photosynthesizing quietly since March. Your email is now compost. | 17 | "Your email is now compost" is a sharp twist, but "photosynthesizing quietly" reads like a science fact, not a voice. |
| Out of office: the monstera has opinions about the window and will not be taking questions until it gets a bigger pot. | 16 | 118 characters — nearly the whole budget, and the joke needs the full sentence to arrive. |
| Gone until someone waters me. I've survived on spite and one sunbeam since March - your email can wait. | 16 | "Survived on spite" is funny, but "Gone until" is not an out-of-office auto-reply frame. |
| Out of office: I'm a cactus. I haven't needed you in months and I don't intend to start now. | 15 | The cactus attitude is right, but nothing in the line is driven by the plant's own life — it could be any aloof sender. |

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
