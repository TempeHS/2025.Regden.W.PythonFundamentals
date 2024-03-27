import inflect

sent = inflect.engine()
array = []
while True:
    try:
        array.append(input())
    except EOFError:
        break

print(f"Adieu, adieu, to {sent.join(array)}")
