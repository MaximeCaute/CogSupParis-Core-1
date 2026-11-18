# B3 · Experiment audit: answer key

The parity task in `b3_audit/parity_task.html` runs without a single error and
produces a tidy CSV. It still has at least seven problems that make the data
wrong, noisy or uninterpretable. The corrected version is `parity_task_fixed.html`
(each fix is marked `[FIX n]`).

| # | Problem | Why it matters | Fix |
|---|---------|----------------|-----|
| 1 | Images are not preloaded | The first presentation of each digit may appear late or progressively; the RT clock starts before the participant can see the stimulus. Worse on slow connections, so it adds noise that correlates with participants' internet. | `jsPsychPreload` trial at the start of the timeline |
| 2 | Response mapping is identical for everyone (even → J, right hand) | Parity and response side are confounded. Known spatial-numerical associations (SNARC: small numbers ↔ left, large ↔ right; MARC: even ↔ right, odd ↔ left) will masquerade as, or hide, the effects you are looking for. | Assign the mapping at random per participant, show the matching instructions, and save it |
| 3 | The data do not record what was shown in analysable form | Digit and parity are only recoverable by parsing file names; the key mapping is not saved at all; trials are not tagged, so filtering relies on plugin names. | Tag trials with `task`, `digit`, `parity`, `correct_response`; add `mapping` with `addProperties` |
| 4 | Accuracy is scored with `===` | With Caps Lock or Shift, the response is recorded as `"F"`, which is not `=== "f"`: correct answers are scored as errors. | `jsPsych.pluginAPI.compareKeys(data.response, data.correct_response)` |
| 5 | No randomisation: digits appear in ascending order, 4 times | Order is confounded with digit magnitude and with practice/fatigue, and the sequence of correct keys (F J F J J F J F) repeats identically 4 times, so it can be learned. | `sample: { type: "fixed-repetitions", size: 4 }` (or at least `randomize_order: true`) |
| 6 | Fixation always lasts exactly 500 ms | Stimulus onset is perfectly predictable: participants can time anticipatory responses. | Jitter the fixation duration |
| 7 | No participant ID; every file is called `data.csv` | Files overwrite each other (or get renamed `data (3).csv`), and rows can't be traced to a participant. | Random ID with `randomID`, added to every row and to the file name |

## Points worth discussing in the debrief

- **None of these problems produces an error message.** The code "works". This is
  exactly the kind of bug an AI assistant is unlikely to flag unless you ask for it,
  and that you will only catch if you know what to look for.
- Problem 5 is the most dramatic: the same 8-key sequence repeats 4 times, so
  later responses can rely on sequence learning rather than on parity
  judgement, and small digits always come before large ones within a cycle.
- Problem 2 is a design question, not a coding one: you need to know the
  literature (SNARC, Dehaene, Bossini & Giraux, 1993) to see it.
- Possible extra findings from students (all fair): no practice block, no
  fullscreen, no check of the device (keyboard vs. phone), no timeout on the
  response, no attention check, local save only.
