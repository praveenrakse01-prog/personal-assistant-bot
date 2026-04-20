# Personal Assistant Bot
# Created by: Praveen
# Features: Chat, Memory, Task Manager
version = "v1.0"
try:
    with open("data.txt", "r") as f:
        name = f.read().strip()
except:
    name = ""

# load tasks
try:
    with open("tasks.txt", "r") as f:
        tasks = f.read().splitlines()
except:
    tasks = []

print("===================================")
print(f"🤖 PERSONAL ASSISTANT BOT {version}")
print("===================================")
print("Type 'help' to see commands\n")

print("💡 Example:")
print(" - add task study")
print(" - show tasks\n")

while True:
    msg = input("you: ").lower()

    if "my name is" in msg:
        name = msg.replace("my name is", "").strip()
        with open("data.txt", "w") as f:
            f.write(name)
        print("Bot: nice to meet you", name)

    elif "what is my name" in msg:
        if name:
            print("Bot: your name is", name)
        else: 
            print("Bot: i don't know your name yet")

    elif "your name" in msg and "my name" not in msg:
        print("Bot: I am your assistant")

    elif "add task" in msg:
        task = msg.replace("add task", "").strip()
        tasks.append(task)

        with open("tasks.txt", "w") as f:
            for t in tasks:
                f.write(t + "\n")

        print("Bot: task added")

    elif "show tasks" in msg or "show task" in msg:
        if tasks:
            print("Bot: here are your tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        else:
            print("Bot: no tasks yet. Try adding one! 😊")

    elif "delete" in msg:
        parts = msg.split()
        if parts[-1].isdigit():
            num = int(parts[-1])
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                with open("tasks.txt", "w") as f:
                    for t in tasks:
                        f.write(t +"\n")
                print("Bot: removed task:", removed)
            else:
                print("Bot: invalid task number")
        else:
            print("Bot: please give a valid task number")

    elif "hi" in msg:
       print("Bot: hello 😊! how can i help you?")

    elif "help" in msg:
       print("\n📌 AVAILABLE COMMANDS:")
       print("1. add task <task>")
       print("2. show tasks")
       print("3. delete task <number>")
       print("4. clear tasks")
       print("5. my name is <name>")
       print("6. what is my name")
       print("7. what is your name")
       print("8. bye\n")

    elif "clear tasks" in msg:
        tasks = []
        with open("tasks.txt", "w") as f:
            pass
        print("Bot: all tasks cleared")

    elif "good" in msg:
        print("Bot: that's great to hear!😊")

    elif "bye" in msg:
        print("Bot: goodbye 👋! see you again")
        break

    else:
        print("Bot: i don't understand 🤔")
        print("type 'help' to see commands")