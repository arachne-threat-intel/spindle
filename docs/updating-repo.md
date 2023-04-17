# Updating rosettaStone via GitHub

* [Branch Selection](#branch-selection)
* [Committing Your Changes](#committing-your-changes)
  * [Unable to Select Branch](#unable-to-select-branch)

## Branch Selection

If updating this repo via GitHub directly, updating both our markdown and JSON files with the same groups should be done on the same branch.

On the homepage/Code tab for the repo, select the branches dropdown

![branch-select](https://user-images.githubusercontent.com/52256544/223459950-6cca4462-f176-4416-b4ed-53b2fdd6d45d.png)

Start typing a new branch name for a branch to branch-off of `main`

![create-branch](https://user-images.githubusercontent.com/52256544/223460129-e2a72646-c0bb-472a-be2a-0077efc73988.png)

With the new branch selected, navigate to the file you wish to edit. You can confirm the branch you are on by what is selected in the branches dropdown next to the repo name. The edit icon is the pencil button next to the 'Raw' and 'Blame' buttons.

![edit-file](https://user-images.githubusercontent.com/52256544/223460673-5e7110c7-798c-4624-a10b-2be0e8698088.png)

## Committing Your Changes

**Before committing, please see [our docs on editing JSON files](updating-json-files.md) too.**

When committing your changes, you will then be able to confirm which branch you are committing to

![commit-to-new-branch](https://user-images.githubusercontent.com/52256544/223460917-b6369517-7138-4e25-a31c-ecfe9b0ff5dc.png)

### Unable to Select Branch

**I've started editing, but I think I'm on the wrong branch**

You will see that you can't select the branch you were previously working on

![commit-cannot-see-branch](https://user-images.githubusercontent.com/52256544/223461197-9191a53a-2a4f-47ae-843b-622660e61ad9.png)

If your changes are small, you should be able to 'Preview Changes' to note what you have changed; follow the process above to be on the desired branch; copy-&-paste your changes to the right branch; and 'Cancel changes' on the incorrect branch.

![preview-changes](https://user-images.githubusercontent.com/52256544/223462197-698f7a6d-fce9-4a3d-870b-02dfab71ec85.png)

If there are many complex changes to reapply, you may commit to a new branch and notify someone to do a git merge with your desired branch (if you do not know how to do this).
