# nodes = [0] * 10001
# parent = 1
# gparent = 1
# while True:
#     try:
#         node = int(input())
#         if nodes[1] == 0:
#             nodes[parent] = node
#         else:
#             if node > nodes[parent]:
#                 if node > nodes[parent//2]:
#                     nodes[parent + 1] = node
#                     parent = parent //2
#                 else:
#                     nodes[parent * 2 + 1] = node
#                     parent = parent * 2 + 1
#             elif node < nodes[parent]:
#                 if node > nodes[parent // 2]:
#                     nodes[parent * 2] = node
#                     parent = parent * 2
#         print(node, parent)
#     except EOFError:
#         print('end')
#         break
