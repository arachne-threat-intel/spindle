# Updating JSON files via GitHub

This guidance is for editing JSON files via GitHub.

Unlike Markdown (.md) files, JSON has a syntax*.

The editor in GitHub (at time of writing) will not highlight any syntax errors.

Therefore, when editing JSON, please copy its contents and paste in an IDE or JSON-checker to quickly see and correct any errors before committing.

In the video below:
- I'm using the JSON-checker https://jsonlint.com/.
- I did a select-all using Ctrl+A (right-click and Select-All only did a partial-selection).
  - Don't be confused by the line numbers also being highlighted, when pasting this elsewhere, you can see the line numbers are not also pasted.
- I pasted into the checker website and checked all 415 lines were pasted.
- I corrected the errors.

If you are struggling to address any JSON syntax errors, as a last-resort do proceed with your commit and flag this in your pull request via a comment.

[json-validate.webm](https://user-images.githubusercontent.com/52256544/232485080-7c95d708-a574-41be-8e18-c3f61404cbe5.webm)

---

*Some more info:

Some JSON syntax rules are:
- Double quotes `""`, no single quotes `''`
- Arrays use square brackets `[]`
- Objects use curly brackets `{}`
- Objects must have a key-value separated by a colon `{"key": "value"}`
- Objects with multiple properties/keys, must be separated with a comma `{"key": "value", "key2": "value2"}`

You can read more about this [here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON).
