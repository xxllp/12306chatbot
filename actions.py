# coding=utf-8
from rasa_core_sdk import Action
from  train import queryTrain,prettyprint
from TimeNormalizer import TimeNormalizer
from datetime import datetime, timedelta
import json
tn = TimeNormalizer()

class ActiongetTrain(Action):
    def name(self):
        return 'action_getTrain'

    def run(self, dispatcher, tracker, domain):
        startcity=tracker.get_slot("startcity")
        endcity = tracker.get_slot("endcity")
        day=tracker.get_slot("day")
        date=json.loads(tn.parse(target=day)).get("timestamp")[0:10]
        interday=(datetime.strptime(date,"%Y-%m-%d")-datetime.now()).days
        print(date)
        if interday >=0 and interday<=30:
           dispatcher.utter_message("正在查询{}到{} 在{}的车票信息".format(startcity,endcity,date))
           try:
             result=queryTrain(startcity, endcity, date)
             result=prettyprint(result)
             if len(result)==0:
                dispatcher.utter_message("未查到任何车次有余票")
             else:
                dispatcher.utter_message("查到以下车次符合条件：")
                for line in result:
                   dispatcher.utter_message(line)
           except :
               dispatcher.utter_message("当前服务出现问题~~")
        else:
            dispatcher.utter_message("选择的时间不在可查询的范围~~")

        #dispatcher.utter_message("请选择你要乘坐的车座和座位类型")
        return []
