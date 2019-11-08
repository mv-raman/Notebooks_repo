

substring='lewaterbott'
actualstring='waterbottle'
print(substring in actualstring+actualstring)


def fizzbuzzfn(num) -> str:
    mod_2 = (num % 2 == 0)
    mod_3 = (num % 3 == 0)
    if (mod_2 or mod_3):
        return (mod_2 * 'Fizz') + (mod_3 * 'Buzz')
    return str(num)
print('\n'.join([fizzbuzzfn(x) for x in range(1,51)]))

