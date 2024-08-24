data = ("self", "py", 1.543)
format_string = "Hello {self}.{py} learner, you have only {num:.1f} units left before you master the course!"

print(format_string.format(self = data[0],py = data[1], num = data[2]))
