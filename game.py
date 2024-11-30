calls = 0 #1
def count_calls(): #2
    global calls
    calls += 1
def string_info(strings): #3
    text = str(strings)
    exit_ = (len(text), text.upper(), text.lower())
    count_calls()
    return exit_
def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            exit_ = True
            break
        else:
            exit_ = False
            continue
    return exit_
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

