# Python for Beginners  
**Lesson 9: File Handling + Error Handling**

---

### Welcome Back! 🚀

In this lesson, you will learn how to work with files — reading data from files and writing data to files. You will also learn how to handle errors gracefully so your programs don’t crash unexpectedly.

This is a very important lesson because real-world programs often need to save and load data.

---

### 1. Reading Files

```python
# Basic way to read a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()          # Always close the file
```

**Better way (Recommended):**

```python
# Using 'with' statement (automatically closes the file)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

---

### 2. Different Reading Methods

```python
with open("example.txt", "r") as file:
    print(file.read())           # Read entire file
    # print(file.readline())     # Read one line
    # print(file.readlines())    # Read all lines as a list
```

---

### 3. Writing to Files

```python
# Write mode - overwrites the file
with open("output.txt", "w") as file:
    file.write("Hello, this is my first file!\n")
    file.write("This is the second line.\n")

# Append mode - adds to the end of the file
with open("output.txt", "a") as file:
    file.write("This line was appended.\n")
```

---

### 4. File Modes

| Mode | Description |
|------|-----------|
| `"r"` | Read (default) |
| `"w"` | Write (overwrites) |
| `"a"` | Append |
| `"r+"` | Read and Write |

---

### 5. Error Handling with `try` and `except`

```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("❌ Error: The file does not exist!")
except Exception as e:
    print("❌ An unexpected error occurred:", e)
finally:
    print("This will always run.")
```

---

### 6. Practical Example: Simple To-Do List

```python
def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks yet!")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found. Start adding tasks!")

# Usage
add_task("Learn Python")
add_task("Practice file handling")
show_tasks()
```

---

### 📝 Notes

- Always use the `with open(...)` statement — it’s safer and cleaner.
- `FileNotFoundError` is the most common error when reading files.
- Writing in `"w"` mode deletes previous content. Use `"a"` to add without deleting.
- `strip()` is useful to remove newline characters (`\n`).
- Error handling makes your programs more professional and user-friendly.

---

### 🎯 Practice Exercises

**Exercise 1**  
Create a program that asks the user for their name and favorite subject, then saves this information into a file called `student_info.txt`.

**Exercise 2**  
Write a program that reads `student_info.txt` and prints the content nicely formatted.

**Exercise 3**  
Create a simple diary/journal program:
- Ask the user to enter a note.
- Append the note with the current date and time to `diary.txt`.

**Exercise 4**  
Make a program that tries to read `scores.txt`. If the file doesn’t exist, create it and write some sample scores.

---

**Congratulations!** 🎉  
You now know how to read from and write to files, and how to handle errors. These skills are essential for building real applications.

**Ready for Lesson 10?**  
Next lesson: **Modules & Packages** — how to organize your code and use powerful built-in tools.

---

Keep practicing in your `python-course` folder!