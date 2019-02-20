formmatter = "%r %r %r %r"
print formmatter % (1, 2, 3, 4)
print formmatter % ("one", "two", "three", "four")
print formmatter % (True, False, False, True)
print formmatter % (formmatter, formmatter, formmatter, formmatter)
print formmatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it  didn't sing.",
        "So I said goodnight."
        )
