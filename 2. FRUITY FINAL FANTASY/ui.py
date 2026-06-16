def separator():
    print("\n" + "-" * 40 + "\n")

def header(title):
    print("\n" + "=" * 10 + f" {title} " + "=" * 10)

def ligne(txt):
    print(f"- {txt}")

def section(title):
    print(f"\n--- {title} ---")

def input_prompt(txt):
    return input(f"> {txt} ")