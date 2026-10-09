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


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("\n\nTesting Numeric Processor...\n")
    print(f"-- Trying to validate input '42': {numeric.validate(42)}")
    print(f"-- Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("-- Test invalid ingestion of 'foo' no prior validation:")
    try:
        numeric.ingest("foo")
    except Exception as error:
        print(f"   Got exception: {error} 'foo'\n")

    print(". . . . . . . . . . . .\n")

    numeric_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}\n")
    numeric.ingest(numeric_data)

    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"  Numeric value {rank}: '{value}'")
    print(f"\ndata after removal: {numeric.data}\n")

    print("------------------------------------\n")

    print("Testing Text Processor...\n")
    print(f"-- Trying to validate input 'Hello': {text.validate('Hello')}")
    print(f"-- Trying to validate input '42': {text.validate(42)}")
    try:
        text.ingest(42)
    except Exception as error:
        print(f"   Got exception: {error} '42'\n")

    print(". . . . . . . . . . . .\n")

    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}\n")
    text.ingest(text_data)

    print("Extracting 1 value...")
    for _ in range(1):
        rank, value = text.output()
        print(f"  Text value {rank}: '{value}'")
    print(f"\ndata after removal: {text.data}\n")

    print("------------------------------------\n")

    print("Testing Log Processor...\n")

    valid_log = {
        "log_level": "INFO",
        "log_message": "Connected"
    }

    print(f"-- Trying to validate valid log: {log.validate(valid_log)}")
    print(f"-- Trying to validate input 'Hello': {log.validate('Hello')}")

    try:
        log.ingest("Hello")
    except Exception as error:
        print(f"   Got exception: {error} 'Hello'\n")

    print(". . . . . . . . . . . .\n")

    log_data = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server"
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!"
        }
    ]

    print(f"Processing data:\n {log_data}\n\n")
    log.ingest(log_data)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"  Log value {rank}: '{value}'")
    print(f"\ndata after removal: {log.data}\n")
    print("------------------------------------\n")


if __name__ == "__main__":
    main()
