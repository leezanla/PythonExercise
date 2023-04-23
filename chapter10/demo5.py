class Content(object):
    def __enter__(self):
        print("__enter__方法被调用了")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__方法被调用了")

    def show(self):
        print("show方法被调用了")



































