## Say Bye
* goodbye
  - utter_goodbye

## thx
* thx
  - utter_thx

## story 1
* greet
    - utter_greet
    - utter_help

## story 2
* queryTrain {"startcity": "合肥", "endcity": "北京","day":"5月1号"}
    - slot{"startcity": "合肥"}
    - slot{"endcity": "北京"}
    - slot{"day":"5月1号"}
    - action_getTrain

## story 3
* queryTrain {"endcity": "北京","day":"5月1号"}
    - slot{"endcity": "北京"}
    - slot{"day":"5月1号"}
    - utter_getStartCity
* getStartCity {"startcity": "合肥"}
    - slot{"startcity": "合肥"}
    - action_getTrain

## story 4
* queryTrain {"startcity": "北京","day":"5月1号"}
    - slot{"startcity": "北京"}
    - slot{"day":"5月1号"}
    - utter_getEndCity
* getStartCity {"endcity": "合肥"}
    - slot{"endcity": "合肥"}
    - action_getTrain

## story 5
* queryTrain {"startcity": "北京","endcity":"合肥"}
    - slot{"startcity": "北京"}
    - slot{"endcity":"合肥"}
    - utter_getDay
* getDay {"day": "明天"}
    - slot{"day": "明天"}
    - action_getTrain


## story 6
* queryTrain {"endcity": "北京"}
    - slot{"endcity": "北京"}
    - slot{"day":"5月1号"}
    - utter_getStartCity
* getStartCity {"startcity": "合肥"}
    - slot{"startcity": "合肥"}
* getDay {"day": "明天"}
    - slot{"day": "明天"}
    - action_getTrain

## story 7
* queryTrain {"endcity": "北京"}
    - slot{"endcity": "北京"}
    - slot{"day":"5月1号"}
    - utter_getStartCity
* getStartCity {"startcity": "合肥"}
    - slot{"startcity": "合肥"}
    - utter_getDay
* getDay {"day": "明天"}
    - slot{"day": "明天"}
    - action_getTrain

## story 8
* queryTrain {"endcity": "北京"}
    - slot{"endcity": "北京"}
    - slot{"day":"5月1号"}
    - utter_getStartCity
* getStartCity {"startcity": "合肥"}
    - slot{"startcity": "合肥"}
    - utter_getDay
* getDay {"day": "明天"}
    - slot{"day": "明天"}
    - action_getTrain
* getDay {"day": "后天"}
    - slot{"day": "后天"}
    - action_getTrain

## story 9
* queryTrain {"startcity": "北京","endcity":"合肥"}
    - slot{"startcity": "北京"}
    - slot{"endcity":"合肥"}
    - utter_getDay
* getDay {"day": "明天"}
    - slot{"day": "明天"}
    - action_getTrain
* getDay {"day": "后天"}
    - slot{"day": "后天"}
    - action_getTrain

## story 10
* greet
    - utter_greet
    - utter_help
* queryTrain {"startcity": "北京","endcity":"合肥"}
    - slot{"startcity": "北京"}
    - slot{"endcity":"合肥"}
    - utter_getDay
* getDay {"day": "明天"}
    - slot{"day": "明天"}
    - action_getTrain
* getDay {"day": "后天"}
    - slot{"day": "后天"}
    - action_getTrain
* thx
  - utter_thx
## Generated Story -6821106330456800482
* queryTrain{"startcity": "\u5317\u4eac", "to": "\u53bb", "endcity": "\u4e0a\u6d77"}
    - slot{"endcity": "\u4e0a\u6d77"}
    - slot{"startcity": "\u5317\u4eac"}
    - slot{"to": "\u53bb"}
    - utter_getDay
* queryTrain{"day": "\u5468\u65e5"}
    - slot{"day": "\u5468\u65e5"}
    - action_getTrain
* queryTrain{"day": "\u4e0b\u5468\u4e00"}
    - slot{"day": "\u4e0b\u5468\u4e00"}
    - action_getTrain
* queryTrain{"day": "\u4e0b \u5468\u4e8c"}
    - slot{"day": "\u4e0b \u5468\u4e8c"}
    - action_getTrain
* queryTrain{"day": "\u4e0b \u5468\u4e94"}
    - slot{"day": "\u4e0b \u5468\u4e94"}
    - action_getTrain

