input_name = input('Enter a name ')
output_text = 'Hello ' + input_name

print(output_text)

# Note: While this script runs in the debugger, it throws the following error when run via the Bash shell:
# $ python hello.py
# Enter a name David
# Traceback (most recent call last):
#   File "hello.py", line 1, in <module>
#     input_name = input('Enter a name ')
#   File "<string>", line 1, in <module>
# NameError: name 'David' is not defined
