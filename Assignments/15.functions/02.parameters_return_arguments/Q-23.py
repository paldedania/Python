# 23. Define make_sentence(subject, verb, object) that returns a sentence. Call it with keyword arguments in a different order.

def make_sentence(subject, verb, object):
    return subject + " " + verb + " " + object + "."


print(make_sentence(object="Python", subject="Pal", verb="learns"))
