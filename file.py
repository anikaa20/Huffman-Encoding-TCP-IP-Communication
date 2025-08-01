def read_text_file(filename):
  try:
    with open(filename, 'r') as file:
      content = file.read()
      return content
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None

# Example usage:
filename = r' ' # enter file path
content = read_text_file(filename)
print(content)
