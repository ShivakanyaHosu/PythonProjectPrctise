class O:
    @staticmethod
    def sum(a, b):
        return a + b

    def sub(self, a, b):
        return a - b


sub_ref = O()
print(sub_ref.sub(6, 4))

# not created object for sum method
print(O.sum(3, 4))
