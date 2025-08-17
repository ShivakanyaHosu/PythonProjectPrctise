a = 10  # global varible


class p:
    b = 11  # Instanse varible - belongs to class

    def print_info(self):
        c = 12  # Local varible
        print(c)  # local variable we can access directly not required write like print(self.c)
        print(self.b)  # For class varible or instance varibble need self
        # a = "hello"
        # print(a) # Local variable having high preference
        global a
        print(a)


o_r = p()
o_r.print_info()
