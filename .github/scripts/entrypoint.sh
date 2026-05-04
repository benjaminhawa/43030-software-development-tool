#!/bin/bash

echo "Starting Task Manager..."

# Run todo.py and save output
python3 /app/.github/scripts/todo.py | tee /app/todo_output.txt

# Run todo-test.py and save output
cd /app/.github/scripts && python3 /app/.github/scripts/todo-test.py | tee /app/test_output.txt

# Run update_index.sh with both outputs
bash /app/.github/scripts/update_index.sh /app/todo_output.txt /app/test_output.txt

echo "Process Completed!"
