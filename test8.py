import textwrap

def wrap(string, max_width):
    wrapped_string = textwrap.wrap(string, max_width)

    return "\n".join(wrapped_string)





string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)