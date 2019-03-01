import os
import datetime
import json

path = os.path.dirname(os.path.realpath(__file__))
log_path = path + os.sep + 'log' + os.sep


def readLog():
    report = []
    list_log = os.listdir('/Users/GHIBLI/PycharmProjects/exam/login/log')
    current = datetime.datetime.now().strftime('%Y-%m-%d')
    for i in list_log:
        log_time = i[5:15]
        if log_time == current:
            which_angel = i[:i.index('-')]
            print("time:" + log_time)
            print("angel:" + which_angel)
            with open(log_path + i) as f:
                content = json.load(f)
                print(content)

        for x in content:
            print(x)
            if x == 'whichAngel':
                which_angel = content[x]
            if x == 'total':
                total = content[x]
            if x == 'lost':
                lost = content[x]
            if x == 'score':
                score = content[x]
        record = which_angel + "今天完成" + str(total) + "道题，做对了" + str(score) + "道，做错" + str(lost) + "道"
        report.append(record)
    return report


if __name__ == "__main__":
    report = readLog()
    print(report)
