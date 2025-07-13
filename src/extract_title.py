def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line.strip()[2:]
    raise Exception("No h1 header line detected")