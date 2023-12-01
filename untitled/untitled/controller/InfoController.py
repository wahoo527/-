import json

import pymysql
from django.http import HttpResponse
from django.shortcuts import render

def yiqing(request):
    print("yiqing方法执行了")

    return render(request, 'yiqing.html',context={"username":"lzc"})

def sendMsg(request):
    print("sendMsg方法执行了")
    return HttpResponse("Hello,我是内容")

def sendJson(request):
    msg = request.GET.get('msg')
    return HttpResponse(json.dumps({"msg":msg}),content_type="application/json")

def getConnect():
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='day2',charset='utf8')
    return conn

def selectConfirmedCountTopSeven(request):
    conn = getConnect()
    cur = conn.cursor()
    sql = "SELECT province_name,confirm_count FROM `info` WHERE area_name IS null ORDER BY confirm_count DESC LIMIT 7"
    cur.execute(sql)
    result = cur.fetchall()

    listProvinceName = []
    listConfirmedCount = []

    for one in result:
        listProvinceName.append(one[0])
        listConfirmedCount.append(one[1])

    dictData = {"listProvinceName":listProvinceName,"listConfirmedCount":listConfirmedCount}
    return HttpResponse(json.dumps(dictData),content_type="application/json")

# 查询治愈人数前七的省份
def selectCuredCountTopSeven(request):
    conn = getConnect()
    cur = conn.cursor()
    sql = "Select province_name,cured_count FROM `info` WHERE area_name IS NULL ORDER BY cured_count DESC LIMIT 7"
    cur.execute(sql)
    result = cur.fetchall()

    listProvinceName = []
    listCuredCount = []

    for one in result:
        listProvinceName.append(one[0])
        listCuredCount.append(one[1])

    dictData = {"listProvinceName":listProvinceName,"listCuredCount":listCuredCount}
    return HttpResponse(json.dumps(dictData),content_type="application/json")


def selectMap(request):
    conn = getConnect()
    cur = conn.cursor()
    sql = "SELECT province_name,confirm_count FROM `info` WHERE area_name IS NULL"
    cur.execute(sql)
    result = cur.fetchall()
    listMap = []
    for one in result:
        # 因为每一条数据都是一个字典，所以需要每次循环都初始化定义的字段
        oneDictData = {}
        # 存值
        oneDictData['name'] = one[0]
        oneDictData['value'] = one[1]
        # 把每一次的数据装入listMap
        listMap.append(oneDictData)
    return HttpResponse(json.dumps(listMap),content_type="application/json")

def selectTotal(request):
    conn = getConnect()
    cur = conn.cursor()
    sql = "Select sum(confirm_count),SUM(cured_count) FROM `info`"
    cur.execute(sql)
    result = cur.fetchall()
    dictData = {"totalConfirmedCount":int(result[0][0]),"totalCuredCount":int(result[0][1])}
    return HttpResponse(json.dumps(dictData),content_type="application/json")
