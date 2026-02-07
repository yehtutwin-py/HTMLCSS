def function_1(text):
    return text.title()

def function_2(text):
    return text+text

output = function_1("hello")
print(output)

output2 = function_2("hello world")
print(output2)

output3 = function_2(function_1("hello"))
print(output3)

