import base64
from abc import abstractclassmethod, ABCMeta


class EnAndDecode(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def decode():
        pass

    @abstractclassmethod
    def encode():
        pass


class Base64(EnAndDecode):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def encode(string) -> str:
        try:
            base64_bytes = string.encode("utf-8")
            answer = base64.b64encode(base64_bytes)
            return answer.decode("utf-8")
        except Exception as e:
            # 当运行出错
            print(e)

    @staticmethod
    def decode(string) -> str:
        try:
            base64_bytes = string.encode("utf-8")
            answer = base64.b64decode(base64_bytes)
            return answer.decode("utf-8")
        except Exception as e:
            print(e)

    @staticmethod
    def encode_n(string, n):
        for i in range(n):
            try:
                base64_bytes = string.encode("utf-8")
                answer = base64.b64encode(base64_bytes)
                string = answer.decode("utf-8")
            except Exception as e:
                print(e)
        return string

    @staticmethod
    def decode_n(string):
        count = 0
        while True:
            try:
                base64_bytes = string.encode("utf-8")
                string = base64.b64decode(base64_bytes)
                string = string.decode("utf-8")
                count += 1
            except Exception as e:
                return string, count


def menu():
    print(
        """
          1. base64加密
          2. base64解密
          3. base64加密n次
          4. base64解密n次"""
    )


def getOption():
    while True:
        option = input("你的选择是什么？:")
        try:
            option = int(option)
            if option in [1, 2, 3, 4]:
                return option
            else:
                print("请输入正确的选项")
        except Exception as e:
            print("请输入正确的选项")


if __name__ == "__main__":
    # 菜单
    menu()
    # 选项
    option = getOption()

    if option == 1:
        string = input("请输入你要加密的内容：")
        print(Base64.encode(string))
    elif option == 2:
        string = input("请输入你要解密的内容：")
        print(Base64.decode(string))
    elif option == 3:
        string = input("请输入你要加密的内容：")
        n = int(input("你要加密几次？："))          # !这里可以做类型检查
        print(Base64.encode_n(string, n))
    elif option == 4:
        string = input("请输入你要解密的内容：")
        answer,count=Base64.decode_n(string)
        print(f"你的密文一共加密{count}次,结果是：{answer}")
