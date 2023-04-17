class ExampleHelloEntity:
    def __init__(self, value: str):
        self.value = value
        pass
    def serialize(self):
        return {"hello": self.value}


class HelloService:
    def get_one(self) -> ExampleHelloEntity:
        return ExampleHelloEntity("world")