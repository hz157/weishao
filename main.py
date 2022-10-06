# description : program enter main function
# author : ryanzhang
# fileName : main.py
# date : 2022-10-06

import sign,post,mail
import os,time,json

if __name__ == '__main__':
    date = time.strftime("%Y/%m/%d")
    print("开始 " + date + " 的打卡任务\n")
    # 读取用户列表
    path = os.getcwd()
    # if path.find("main") == -1:
    #     path += "/main"
    allinfo = json.load(open(path + "/users.json",encoding="utf-8"))
    text = '| 姓名 |  结果  |'
    for item in allinfo:
        name = item.get("name")
        print("开始为 " + name + " 打卡...")
        try:
            # 获取用户cookie
            cook = sign.login(item)
            # print(cook)
            if cook.find("错误") != -1:
                # 触发异常后面的代码将无法执行
                raise Exception(cook)
            # 获取返回的打卡结果
            response = post.run(item, cook)
        except Exception as e:
            print("---为 " + name + " 打卡失败\n" + str(e))
            response = "打卡失败"
        if response == "打卡失败":
            mail.send(item.get('mail'),"{},您今日自动打卡失败".format(item.get('name')))
        # 为推送填写打卡信息
        text += f" \n| {name} | {response} |"


