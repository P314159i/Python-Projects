New concepts here:

* `abc.ABC` and `@abstractmethod`
* inheritance + polymorphism through a common parent type
* `typing.Any`
* `isinstance(...)`
* `typing.Protocol` for “duck-typed interfaces”
* composition: `DataStream` stores processor objects
* plugin architecture
* `for ... else`
* list comprehensions
* routing data to the first compatible processor
* exporting processed data through interchangeable plugins

Practice task:

Create a tiny **Message Processing Pipeline**.

Requirements:

1. Abstract parent `MessageProcessor`

   * abstract `validate(data)`
   * abstract `ingest(data)`
   * stores processed strings in `self.data`

2. Two child processors:

   * `TextMessageProcessor` accepts strings
   * `NumberMessageProcessor` accepts `int`/`float`

3. `MessageStream`

   * stores processors
   * `register_processor(processor)`
   * sends each input to the first processor whose `validate()` returns `True`

4. Create a `DisplayPlugin` Protocol with:

   * `export(data: list[str])`

5. Create two compatible plugins:

   * one prints items one per line
   * one prints them joined with `" | "`

6. Feed mixed data such as:

```text
"hello"
42
3.14
"world"
["invalid"]
```

Goal: practice **ABC → polymorphic processors → stream/router → Protocol plugin**.
