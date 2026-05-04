#!/bin/bash

TODO_OUTPUT=$1
TEST_OUTPUT=$2

TODO_TASKS=$(grep -A 100 "ToDo Tasks:" "$TODO_OUTPUT" | grep -B 100 "Done Tasks:" | grep -v "ToDo Tasks:" | grep -v "Done Tasks:" | sed '/^$/d')
DONE_TASKS=$(grep -A 100 "Done Tasks:" "$TODO_OUTPUT" | sed '/^$/d' | tail -n +2)
TEST_RESULTS=$(cat "$TEST_OUTPUT")

update_pre() {
    local id=$1
    local content=$2
    local file=$3
    perl -i -0pe "s|(<pre id=\"$id\">).*?(</pre>)|\${1}$content\${2}|s" "$file"
}

update_pre "todo-tasks" "$TODO_TASKS" "index.html"
update_pre "done-tasks" "$DONE_TASKS" "index.html"
update_pre "test-results" "$TEST_RESULTS" "index.html"

git config --global user.email "github-actions@users.noreply.github.com"
git config --global user.name "github-actions"
git add index.html
git commit -m "Update index.html with task and test results"
git push
