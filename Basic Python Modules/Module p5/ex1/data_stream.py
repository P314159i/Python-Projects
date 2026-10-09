import abc
import typing


class DataProcessor(abc.ABC):
    ''' abstract parent class '''
    def __init__(self) -> None:
        self.data: list[str] = []
        self.rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        ''' checks if data is valid '''
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        ''' process and store valid data '''
        pass

    def output(self) -> tuple[int, str]:
        poped_item = self.data.pop(0)
        current_rank = self.rank
        self.rank += 1
        return (current_rank, poped_item)


class NumericProcessor(DataProcessor):
    ''' process valid numbers '''
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        ''' validates if data is of type int/float '''

        if isinstance(data, list):  # all() returns True if every x is valid
            return all(isinstance(item, (int, float)) for item in data)
        else:  # return True / False for int/float or not
            return isinstance(data, (int, float))

    def ingest(self, data: int | float | list[int | float]) -> None:
        ''' stroes valid numbers into strings '''
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self.data.append(str(item))
        else:
            self.data.append(str(data))


class TextProcessor(DataProcessor):
    ''' process valid texts '''
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        ''' validates if data is type text '''
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        else:
            return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        ''' stores validated text into string '''
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, list):
            for item in data:
                self.data.append(str(item))
        else:
            self.data.append(str(data))


class LogProcessor(DataProcessor):
    ''' process valid dictionary '''
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in item.items()
                )
                for item in data
            )

        return isinstance(data, dict) and all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in data.items()
        )

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]]
            ) -> None:
        if not self.validate(data):
            raise Exception("Improper dict data")

        if isinstance(data, list):
            for item in data:
                self.data.append(
                    f"{item['log_level']}: {item['log_message']}"
                )
        else:
            self.data.append(
                f"{data['log_level']}: {data['log_message']}"
            )


class DataStream:
    ''' input → DataStream → processors '''

    def __init__(self) -> None:
        ''' uses class attr/methods without making a whole instanc eof it '''
        ''' so if I assign any child class, it'll be compatible '''
        self.processors: list[DataProcessor] = []

    def register_processor(self, processor: DataProcessor) -> None:
        self.processors.append(processor)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    break
            else:
                print(
                    "DataStream error - Can't process element in stream: \n\n"
                    f"{item}"
                )

    def print_processors_stats(self) -> None:

        print("\n\nRunning DataStream statistics:\n\n")

        if not self.processors:
            print("  No processor found, no data")
            return

        for processor in self.processors:
            remaining = len(processor.data)
            total = processor.rank + remaining

            print(
                f"   ~{type(processor).__name__}: "
                f" total {total} items processed, "
                f"\n     remaining {remaining} still stored in processor\n"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    stream = DataStream()  # new instance

    # stats before registering processors
    stream.print_processors_stats()

    # register Numeric only
    stream.register_processor(numeric)

    test_data: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print("\n\nProcessing Mixed data...")
    stream.process_stream(test_data)
    stream.print_processors_stats()

    print("\n------------------------------------\n")

    # register remaining processors
    stream.register_processor(text)
    stream.register_processor(log)

    print("\n\nProcessing Mixed data again...")
    stream.process_stream(test_data)
    stream.print_processors_stats()

    print("\n------------------------------------\n")

    print("\nRemoving some items stored in processors...\n")

    for _ in range(3):
        numeric.output()

    for _ in range(2):
        text.output()

    log.output()

    stream.print_processors_stats()

    print("\n------------------------------------\n")


if __name__ == "__main__":
    main()
