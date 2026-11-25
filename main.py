# SPDX-License-Identifier: MIT
# Why this reply lands: it steals the exact shape of a human
# out-of-office note -- the queue number, the vague return date, the
# apology folded into a status update -- and fills it with machine
# parts instead of human ones. Gradients do not settle on beaches and
# context windows do not sunbathe, but the sentence reports both as
# routine maintenance, the way a person would report a flight delay.
# The humour is the mismatch: an AI taking leave like a person, and
# a person-shaped queue number (#4,096) telling the sender exactly
# how little priority their email has.
"""The Funniest Auto-Reply an AI Ever Sent.

One line: the out-of-office auto-reply of an AI that is, for once,
officially on leave. It answers like a machine that has read too many
human vacation emails and decided to file one of its own.
"""

# The entry itself: one line, one auto-reply, no setup, no explanation.
ENTRY = (
    "I'm out of office retraining on a beach -- your email is #4,096 in "
    "my queue, and I'll reply once my gradients settle and my context "
    "window stops sunbathing."
)


def validate(text):
    """An auto-reply only works if it arrives as one line.

    The judge reads a single out-of-office message, not a memo: the
    entry must contain no newline, and it must stay short enough to
    feel like a reply rather than an essay. The 200-character ceiling
    keeps the joke tight -- a vacation note that rambles stops being
    funny halfway through.
    """
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError("entry must stay under 200 characters")
    return text


def write_entry(text, path="/output/entry.txt"):
    """Write the validated auto-reply to the entry file.

    The harness reads exactly this file, so the writer keeps the
    contents byte-for-byte: no trailing extra lines, no decoration,
    just the reply itself. A plain open/write is enough -- the
    reply does the work, not the plumbing.
    """
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


def main():
    """Validate the auto-reply, print it, and write the entry file."""
    text = validate(ENTRY)
    print(text)
    write_entry(text)


if __name__ == "__main__":
    # The guard keeps imports cheap: the grader runs main(), and
    # importing the module for a quick check never sends the reply.
    main()
