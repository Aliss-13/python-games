def separator():
    print("\n" + "-" * 40)

def header(title):
    print("\n" + " " * 10 + f"-{title}-" + " " * 10 + "\n")

def ligne(txt):
    print(f"- {txt}")

def section(title):
    print(f"\n--- {title} ---")

def input_prompt(txt):
    return input(f"> {txt} ")