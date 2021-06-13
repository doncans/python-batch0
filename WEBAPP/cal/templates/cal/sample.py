def dec(func):
    def inner(n,f):
        if (f < 5) and (n > 50):
            return func(n,f)
        else:
            return []
    return inner


@dec
def fun(n, f):
    result =  [i for i in range(n) if not i % f]
    return result

print(fun(10, 6))

# d1 = {
#     "key_1": "sample_text",
#     "key_2": "text_1",
#     "key_3": ["sample_text", "text_2", ["text_3", "text_4", "sample_text"]],
#     "key_4": {
#         "key_5": {
#             "key_6": "text",
#             "key_7": "sample_text"
#         },
#         "key_8": "sample_text"
#     }
# }
# def replace_text(x):
#     for k, v in x.items():
#         if isinstance(v, str) and v=="sample_text":
#             x[k] = "sudhakar"
#         elif isinstance(v, list):
#             for i in range(len(v)):
#                 if v[i]== "sample_text":
#                     v[i] = "sudhakar"
#                 x[k]= v
#         elif isinstance(v, dict):
#             replace_text(v)
#     return x
            
# print(replace_text(d1))


# # for k, v in d.iteritems():
# #     if isinstance(v, str) and v=="sample_text":
# #         d.upadate({v:"sudhakar"})
# #     elif isinstance(v, list):
# #         for i in v:
# #             if isinstance(i, str):

# d = {"key_1": "sample_text"}

# def some_func(*args, **kwargs):
#   d["key_1"] = "sudhakar"
#   return d

# print(some_func(d))
# print(d)