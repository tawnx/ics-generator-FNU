# 编写你自己的学校对象和课表数据！

def oeWeek(startWeek, endWeek, mode): return [i for i in range(
    startWeek, endWeek + 1) if (i + mode) % 2 == 0]  # 奇偶周的实现函数


def rgWeek(startWeek, endWeek): return [
    i for i in range(startWeek, endWeek + 1)]  # 范围周的实现函数


classes = [
	#这里写cmd.js运行后的结果，例如下列代码：
	["概率论与数理统计","陈海霞","立诚1-205",rgWeek(4,7)+rgWeek(9,16),1,[1,2]],
	["计算机网络基础（一）","张金颖","笃行1-311",rgWeek(1,16),1,[5,6]],	

]

print(classes)


class school:

    name = "FNU"               # 学校的名称

    classTime = [
        (8, 20),
		(9, 15),
		(10,20),
		(11,15),
        (14, 0),
        (14, 55),
		(15,50),
		(16,45),
		(18,30),
		(19,25),
		(20,20),
		(21,15)
    ]                             # 每节课的上课时间（如: 这 3 节课的上课时间分别是 上午 8:00、下午 2:10、晚上 8:20）

    classPeriod = 45              # 每一节课的时长分钟数（如: 50 分钟）

    starterDay = [2022, 8, 29]    # 开学第一周星期一的日期，存储为年、月、日三项

    def AppleMaps(loc): return [     # （如果不使用 Apple Maps 可以完全忽略！）返回 Apple Maps 地址字典的匿名函数

        # 使用 r-String 以及三引号文段可以避免转义符号的歧义

        {
            "judge": "教学楼一" in loc,  # 设置匹配「教学楼一」的条件
            "text": r"""LOCATION:某大学一教学楼\n某大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=某大学一教学楼\\n某大学内:geo:30.0000,100.000"""  # 复制 Apple Maps 信息
        },
        {
            "judge": True,        # 请设置一个一直为 True 的建筑用于缺省匹配
            "text": r"""LOCATION:某大学一教学楼\n某大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=某大学一教学楼\\n某大学内:geo:30.0000,100.000"""
        }
    ]

    def geo(classroom):

        # 方法零：完全不使用任何地理坐标信息（不建议）
        return ""

        # 方法一：将教室文字搭配坐标信息显示在日历中（几乎所有 ICS 客户端都支持）

        loc = "教室 " + classroom  # 想要显示在日历项地址中的文字
        cor = "30.0000;100.000"   # 地理坐标，纬度、经度之间以 ; 间隔
        return f"LOCATION:{loc}\nGEO:{cor}"  # 包装为符合 ICS 文件要求的格式

        # 方法二：使用 Apple Maps，匹配 `AppleMaps` 数组当中的场所

        loc = ""
        for place in school.AppleMaps(classroom):
            if place["judge"]:
                loc = place["text"]
                break
        return loc
