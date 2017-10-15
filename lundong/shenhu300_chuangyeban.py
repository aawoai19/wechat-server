#coding=utf-8


from lundong.sel import *
from lundong.models import Bankuailundong

sh300_Num = '002987'
cyb_Num = '001593'
sz50_Num = '001549'
zz500_Num = '002903'
url = 'http://fund.eastmoney.com/f10/jjjz_%s.html'

def get_40day_value(Num):
    data = {
        'date':[],
        'value':[]
    }
    this_url = url%Num
    driver.get(this_url)
    for t in range(0,2):
        wait.until(isPrased('//*[@id="jztable"]/table/tbody/tr[1]'))
        for i in range(1,21):
            date = get_xpath_text('//*[@id="jztable"]/table/tbody/tr[%d]/td[1]'%i)
            value = get_xpath_text('//*[@id="jztable"]/table/tbody/tr[%d]/td[3]'%i)
            data['date'].append(date)
            data['value'].append(value)
        driver.find_element_by_xpath('//*[@id="pagebar"]/div[1]/label[8]').click()
    return data

def get_20day_ch(data):
    day20_ch = []
    for i in range(0,20):
        change = (float(data['value'][i])-float(data['value'][i+20]))/float(data['value'][i+20])
        change = '%.2f'%(change*100)
        day20_ch.append(change)
    re = {
        'date':data['date'][0:20],
        'change':day20_ch
    }
    return re

def draw(re1,re2,re3,re4):
    x = range(0,20)
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for i in range(0,20):
        t = 19-i
        y1.append(float(re1['change'][t]))
        y2.append(float(re2['change'][t]))
        y3.append(float(re3['change'][t]))
        y4.append(float(re4['change'][t]))
    for i in range(0,20):
        shenhu300 = Bankuailundong.objects.get(num=i+1)
        shenhu300.value=y1[i]
        shenhu300.typ='shenhu300'
        shenhu300.save()
        # print y1[i]
        cyb = Bankuailundong.objects.get(num=i+21)
        cyb.value=y2[i]
        cyb.typ='cyb'
        cyb.save()
        # print y2[i]
        try:
            sz50 = Bankuailundong.objects.get(num=i+41)
            sz50.value=y3[i]
            sz50.typ='sz50'
            sz50.save()
        except:
            sz50 = Bankuailundong.objects.create(num=i+41,value=y3[i],typ='sz50')

        try:
            zz500 = Bankuailundong.objects.get(num=i+61)
            zz500.value=y4[i]
            zz500.typ='zz500'
            zz500.save()
        except:
            zz500 = Bankuailundong.objects.create(num=i+61,value=y4[i],typ='zz500')

def save_data():
    try:
        sh300_40_data = get_40day_value(sh300_Num)
        sh300_20_change = get_20day_ch(sh300_40_data)
        cyb_40_data = get_40day_value(cyb_Num)
        cyb_20_change = get_20day_ch(cyb_40_data)
        sz50_data = get_40day_value(sz50_Num)
        sz50_20_change = get_20day_ch(sz50_data)
        zz500_data = get_40day_value(zz500_Num)
        zz500_20_change = get_20day_ch(zz500_data)
        draw(sh300_20_change, cyb_20_change,sz50_20_change,zz500_20_change)

    finally:
        driver.quit()
        display.stop()

# if __name__ == '__main__':
#     try:
#         print u'正在查询中'
#         sh300_40_data = get_40day_value(sh300_Num)
#         sh300_20_change = get_20day_ch(sh300_40_data)
#         cyb_40_data = get_40day_value(cyb_Num)
#         cyb_20_change = get_20day_ch(cyb_40_data)
#         print u'正在绘制图像'
#         draw(sh300_20_change,cyb_20_change)
#         raw_input()
#     except:
#         print ImportError
#         raw_input()
#     finally:
#         driver.quit()
