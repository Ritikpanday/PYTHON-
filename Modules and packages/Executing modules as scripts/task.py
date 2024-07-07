from some_module import func

print(f'This is a message from {__name__}.')
func()

# Make a change here (add a main block)
if __name__ == "_main__":
    print('This should be printed ONLY when task.py is called directly.')

