# Updating JSON files via GitHub

* [Before a Commit (Optional)](#before-a-commit-optional)
  * [Using the Python Test-Suite](#using-the-python-test-suite)
  * [Using Online Tools](#using-online-tools)
* [After a Commit](#after-a-commit)
* [More Info on JSON Syntax](#more-info-on-json-syntax)

This guidance is for editing JSON files via GitHub.

Unlike Markdown (.md) files, JSON has a syntax.

The editor in GitHub (at time of writing) will not highlight any syntax errors.

## Before a Commit (Optional)

### Using the Python Test-Suite

If you have Python installed, via the terminal and whilst in the top-level directory, you can do

`python -m unittest discover tests/`

A test failure will tell you (one error at a time) which line(s) to address. The same test output is shown in our [after-a-commit](#after-a-commit) example.

### Using Online Tools

Copy its contents and paste in an IDE or JSON-checker to quickly see and correct any errors before committing.

In the video below:
- I'm using the JSON-checker https://jsonlint.com/.
- I did a select-all using Ctrl+A (right-click and Select-All only did a partial-selection).
  - Don't be confused by the line numbers also being highlighted, when pasting this elsewhere, you can see the line numbers are not also pasted.
- I pasted into the checker website and checked all 415 lines were pasted.
- I corrected the errors.

If you are struggling to address any JSON syntax errors, you may still proceed with your commit and your pull request will flag any errors.

[json-validate.webm](https://user-images.githubusercontent.com/52256544/232485080-7c95d708-a574-41be-8e18-c3f61404cbe5.webm)

## After a Commit

If your JSON has any syntax errors, your pull request's tests will fail.

In the video below:
- I see an x by my pull request.
- I click on the x and select any failing test.
- I check the test-failure output for the line to fix my JSON file.

[failed-workflow.webm](https://user-images.githubusercontent.com/52256544/232527206-f4814af7-09b1-4c3d-abc2-0d8eb28d59f8.webm)


## More Info on JSON Syntax

Some JSON syntax rules are:
- Double quotes `""`, no single quotes `''`
- Arrays use square brackets `[]`
- Objects use curly brackets `{}`
- Objects must have a key-value separated by a colon `{"key": "value"}`
- Objects with multiple properties/keys, must be separated with a comma `{"key": "value", "key2": "value2"}`

You can read more about this [here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON).
