# def rgb(r, g, b):
#     rgbAr = [r, g , b]
#     ans = ''
#     for obj in rgbAr:
#         if obj > 255:
#             obj = 255
#             ans += ''.join(list(hex(obj))[2::]).upper()
#         elif obj < 0:
#             obj = 0
#             ans += ''.join(list(hex(obj) + '0')[:1:-1]).upper()
#         elif obj < 16:
#             ans += ''.join(list(hex(obj) + '0')[:1:-1]).upper()
#         else:
#             ans += ''.join(list(hex(obj))[2::]).upper()
#     return ans

checkAr = [[0,0,0], [255,255,255], [-3,268,46]]


def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


print(rgb(2,255,255))
