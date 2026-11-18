# Git Version Control Practice — To-Do List

A small command-line To-Do List app in Python, used to practice Git branching,
merging, and conflict resolution.

## Features

- Add a task
- View all tasks with their status (Pending / Completed)
- Mark a task as completed
- Delete a task
- Exit the app

## How to Run

```bash
python main.py
```

Then choose an option from the menu (1–5).

## Git Practice Notes

This repository demonstrates:

- A `feature/delete-task` branch created from `master`
- A merge of `master` into the feature branch that produced a **merge conflict**
  on the app banner line
- Manual conflict resolution (combined both banner changes into
  `===== MY TO-DO LIST (v2) =====`)
- A final merge of the feature branch back into `master`

## Repository

https://github.com/Syed-Iliyas/Git-Version-Control
