

# Write file
def write_to_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Append to file
def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')








