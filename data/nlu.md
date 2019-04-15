## intent: greet
- hey
- hello
- 你好
- 您好

## intent: goodbye
- bye
- bye bye
- 拜拜
- 再见

## intent: queryTrain
- 我要[去](to)[北京](endcity)，帮查下票
- [合肥](startcity)[去](to)[北京](endcity)[明天](day)的火车票
- [深圳](startcity)[到](to)[广州](endcity)[四月1号](day)[上午](time)的高铁票
- [北京](startcity)[到](to)[上海](endcity)[5月2号](day)的票还有几张
- 查下[上海](startcity)[到](to)[南京](endcity) [4月2号](day)[晚上](time)的动车票
- [武汉](startcity)[到](to)[成都](endcity) [今晚](time)的火车票
- [北京](startcity)[到](to)[哈尔滨](endcity)[明天](day)[下午](time)的火车
- [杭州](startcity)[到](to)[上海] (endcity)[后天](day)[下午](time)的火车
- [北京](startcity)[到](to) [长沙] (endcity) [明天](day)的火车票
- [合肥](startcity)[到](to)[北京](endcity)的火车票
- [深圳](startcity)[到](to)[广州](endcity)的高铁票
- [北京](startcity)[去](to)[上海](endcity)的票还有几张
- 查下[上海](startcity)[去](to)[南京](endcity) 的动车票
- [武汉](startcity)[去](to)[成都](endcity) 的火车票
- [北京](startcity)[去](to)[哈尔滨](endcity)的火车
- [杭州](startcity)[去](to)[上海] (endcity)的火车
- [北京](startcity)[去](to)[长沙] (endcity) 的火车票
- 查询下[到](to)[北京](endcity)的火车票
- 查询[明天](day)[去](to)[上海](endcity)的火车票
- 我要[周日](day)从[天津](startcity)[回](to)[北京](endcity)的动车票
- 我要[周五](day)从[天津](startcity)[回](to)[北京](endcity)的动车票
- 我要从[常州](startcity)[到](to)[南京](endcity)的高铁票
- 我要买张[开往](to)[北京](endcity)的火车票
- 查下[去](to)[上海](endcity)的票
- [到](to)[北京](endcity)的火车票
- 买张[去](to)[上海](endcity)的火车票
- 买张[开往](to)[北京](endcity)的火车票



## intent : getDay
- [明天](day)
- [今天](day)
- [5月1号](day)
- [10月3号](day)
- [12月17号](day)
- [后天](day)
- [大后天](day)
- [明天](day)[下午](time)
- [明天](day)[早上](time)
- [明天](day)[晚上](time)
- [今天](day)[下午](time)
- [今天](day)[晚上](time)
- [5月1号](day)[早上](time)
- [5月1号](day)[下午](time)
- [5月1号](day)[晚上](time)
- [明天](day)的呢
- [明天](day)[下午](time)的呢
- [周一](day)
- [周二](day)
- [周三](day)
- [周四](day)
- [周五](day)
- [周六](day)
- [周日](day)
- [下周一](day)
- [下周二](day)
- [下周三](day)
- [下周四](day)
- [下周五](day)
- [下周六](day)
- [下周日](day)


## intent : getStartCity
- [合肥](startcity)
- [深圳](startcity)
- [沈阳](startcity)
- [武汉](startcity)
- [太原](startcity)
- [西安](startcity)
- [西宁](startcity)
- [九江](startcity)
- [黄山](startcity)
- [衡阳](startcity)

## intent: getEndCity
- [北京](endcity)
- [广州](endcity)
- [成都](endcity)
- [深圳](endcity)
- [沈阳](endcity)
- [武汉](endcity)
- [太原](endcity)
- [西安](endcity)
- [西宁](endcity)
- [九江](endcity)
- [黄山](endcity)
- [衡阳](endcity)

## intent :thx
 - 谢谢
 - 多谢
 - 感谢
 - 非常高兴呢
 - 多谢~~
 - 你真棒
 - thanks
 - 很好
 - 非常感谢
 - 我的神，你真棒


## lookup:startcity
data/city.txt

## lookup:endcity
data/city.txt

