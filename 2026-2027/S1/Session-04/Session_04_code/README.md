# Session 4 · Online experiments: from a webpage to jsPsych

Code for the hands-on parts of the session. Open any `.html` file directly in a
browser (Chrome or Firefox) and press F12 to open the DevTools.
Part B loads jsPsych 8.3.0 from a CDN (unpkg.com), so it needs an internet connection.

## Part A · What is a webpage?

| File | Use |
|------|-----|
| `partA/a1_skeleton.html` | Minimal HTML document; the invisible div demo (I do) |
| `partA/a2_css/a2_square.html` + `style.css` | External stylesheet, selectors, centering recipe |
| `partA/a2_css/a2_predict.html` | Predict-then-run: which rule wins? |
| `partA/a3_trial_by_hand.html` | One RT trial written without any library (I do) |
| `partA/a3_trial_by_hand_solution.html` | The three "we do" modifications |
| `partA/a4_broken/` | Debugging drill: 4 bugs, DevTools only (you do) |
| `partA/a4_fixed/` | Solution, with the explanation of each bug in a comment |

## Part B · jsPsych

| File | Use |
|------|-----|
| `partB/b1_minimal.html` | Smallest jsPsych experiment; inspect `#jspsych-content` while it runs |
| `partB/b2_rt_task_worked.html` | Worked example: timeline variables, fixation, randomisation (I do) |
| `partB/b2_rt_task_faded.html` | Same task with 5 TODOs (we do → you do) |
| `partB/b2_rt_task_solution.html` | Solution to the TODOs |
| `partB/b3_audit/parity_task.html` | Audit: runs fine, but the data are flawed (you do, in pairs) |
| `partB/b3_audit_solution/` | Corrected version + `AUDIT_KEY.md` (keep for the debrief) |

Tip: distribute `partA/a4_fixed`, `partB/b2_rt_task_solution.html` and
`partB/b3_audit_solution/` only after the corresponding exercise.

All Part B code was tested with jsPsych 8.3.0 and plugins html-keyboard-response 2.2.0,
image-keyboard-response 2.2.0 and preload 2.1.0.
