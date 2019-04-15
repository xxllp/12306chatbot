# coding=utf-8
'''
车票查询的功能,支持起始站点和时间条件，其他不支持
'''
import stations
import requests

def get_from_to_station_names(data_list):
    from_station_code = data_list[6]
    to_station_code = data_list[7]
    return '\n'.join([
        stations.get_name(from_station_code),
       stations.get_name(to_station_code)
    ])
def get_start_arrive_time(data_list):
        start_time = data_list[8]
        arrive_time = data_list[9]
        return '\n'.join([
            start_time,
            arrive_time
        ])
def parse_train_data(data_list):
    train_code = data_list[3]
    from_station_name =stations.get_name(data_list[6])
    to_station_name = stations.get_name(data_list[7])
    start_time = data_list[8]
    arrive_time = data_list[9]
    time_duration = data_list[10]
    business_class_seat = data_list[32] or data_list[25] or '--'
    first_class_seat = data_list[31] or '--'
    second_class_seat = data_list[30] or '--'
    senior_soft_sleep = data_list[21] or '--'
    soft_sleep = data_list[23] or '--'
    move_seat = data_list[33] or '--'  # 动卧
    hard_sleep = data_list[28] or '--'
    soft_seat = data_list[24] or '--'
    hard_seat = data_list[29] or '--'
    no_seat = data_list[26] or '--'
    other = data_list[22] or '--'

    is_support_card = int(data_list[18] or 0)

    return [train_code, from_station_name,to_station_name, start_time,arrive_time, time_duration,
            business_class_seat, first_class_seat, second_class_seat, senior_soft_sleep,
            soft_sleep, move_seat, hard_sleep, soft_seat, hard_seat, no_seat, other, is_support_card]



def queryTrain(from_station_name,to_station_name,day):
   from_station = stations.get_telecode(from_station_name)
   to_station = stations.get_telecode(to_station_name)
   url='https://kyfw.12306.cn/otn/leftTicket/query?'\
               'leftTicketDTO.train_date={}&'\
               'leftTicketDTO.from_station={}&'\
               'leftTicketDTO.to_station={}&'\
               'purpose_codes=ADULT'.format(day,from_station,to_station)
   print(url)
   response = requests.get(url, verify=False)
   result = response.json()
   if 'data' not in result:
       msg = result.get('messages', None)
       if msg is not None:
           print( ','.join(msg))
       else:
           print('red', u'获取车次信息失败！ 请联系管理员 svend.jin@qq.com')
       exit(0)
   raw_trains = result['data']['result']

   result=[]
   for train in raw_trains:
           data_list = train.split('|')
           train_data = parse_train_data(data_list)
           result.append(train_data)
   return  result

##输出所需的
def prettyprint(data_list):
    result=[]
    for data in data_list:
        other=""
        if data[6] not in ["无","--","有"] :
             other+="{}张商务票 ".format(data[6])
        elif data[6]=="有":
            other += "有商务票 "
        if data[7] not in ["无","--","有"]:
            other+="{}张一等座票 ".format(data[7])
        elif data[7] == "有":
            other += "有一等座票 "
        if data[8] not in ["无","--","有"]:
            other+="{}张二等座票 ".format(data[8])
        elif data[8] == "有":
            other += "有二等座票 "
        if ((data[6] not in ["无","--"])or(data[7] not in ["无","--"])or(data[8] not in ["无","--"]))==True:
             result.append("{} 次 从{} 到{} ，时间是{} 到{} ,目前".format(data[0],data[1],data[2],data[3],data[4],)+other)
    return result

if __name__ == '__main__':
    result=queryTrain("合肥","北京","2019-04-12")
    print(result)
    prettyprint(result)
    #prettyprint(list(filter(lambda e:((e[6]=="无")and (e[7]=="无")and(e[8]=="无"))==False,result)))
