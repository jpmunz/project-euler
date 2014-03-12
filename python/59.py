from itertools import product

alphabet = 'abcdefghijklmnopqrstuvwxyz'

with open('/usr/share/dict/words') as f:
    words = set(f.read().split())

best_match = 0
best_key = ''
best_message = ''
best_match_sum = 0

with open('cipher1.txt') as f:
    characters = f.read().split(',')

    for key in product(alphabet, repeat=3):
        decrypted = []
        i = 0
        ascii_sum = 0
        for c in characters:
            d = int(c) ^ ord(key[i % len(key)])
            ascii_sum += d
            decrypted.append(chr(d))

            i += 1

        message = ''.join(decrypted)
        decrypted_words = set(w.lower() for w in message.split())
        valid_words = len(decrypted_words.intersection(words))

        if valid_words > best_match:
            best_match = valid_words
            best_key = key
            best_match_sum = ascii_sum
            best_message = message

print 'Best match: %s' % str(best_match)
print "Best key: %s" % ''.join(best_key)
print "Sum: %s" % str(best_match_sum)
print "Message: %s" % best_message
