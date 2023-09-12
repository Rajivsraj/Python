s = "ansnablbablbkkkaaaaaaaaaaaaaaaaaaaaaaaaaaa"
mx = 0
mi = 0
st = ""
rev = ""
pal = ""
lst = []

# print(len(s[0]))
for r in range(len(s)):
    st = ""
    for c in s[r:]:
        st = st+c   # ansnab
        rev = st[::-1]
        if st == rev:
            # print(f"{st}, {rev}")
            if len(st) > mx:
                # print("rinku")
                mx = len(st)
                pal = st    # ansna

            else:
                mi = mx

print(pal, mx)


