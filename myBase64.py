import base64 as b64


# 将内容转为base64格式内容
def convertToBase64(info):
    try:
        tmpBytes = info.encode()
        tmpBase64 = b64.b64encode(tmpBytes)
        return tmpBase64
    except Exception as e:
        print("异常：", e)


# 将base64格式内容转为正常信息
def convertTostring(base64Info):
    try:
        tmpBytes = b64.b64decode(base64Info)
        tmpStr = tmpBytes.decode()
        return tmpStr
    except Exception as e:
        print("异常：", e)


convertToBase64("chg")
