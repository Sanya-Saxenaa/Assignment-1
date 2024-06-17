prefix = input("Enter a prefix: ")
suffix = input("Enter a suffix: ")
text = input("Enter a string: ")

if text.startswith(prefix):
    print(f"'{text}' starts with the prefix '{prefix}'.")
if text.endswith(suffix):
    print(f"'{text}' ends with the suffix '{suffix}'.")


