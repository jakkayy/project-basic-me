from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    today = datetime.date.today()
    data = request.get_json()
    name = data.get('name')
    day_number = int(data.get('dayNumber'))
    day = data.get('day')
    month = data.get('month')
    year = int(data.get('year'))
    age = int(data.get('age'))
    seven_day = {'sunday': 1, 'monday': 2, 'tuesday': 3, 'wednesday': 4, 'thursday': 5, 'friday':6, 'saturday': 7}
    month_ch = {'january':10, 'febuary':11, 'march':12, 'april':1, 'may':2, 'june':3, 'july':4, 'august':5, 'november':6, 'october':7, 'september':8, 'december':9}
    twelve_year = {'january':1, 'febuary':2, 'march':3, 'april':4, 'may':5, 'june':6, 'july':7, 'august':8, 'november':9, 'october':10, 'september':11, 'december':12}
    
    def get_chinese_zodiac(year):
        zodiac_animals = [
            "ชวด (หนู)", "ฉลู (วัว)", "ขาล (เสือ)", "เถาะ (กระต่าย)", "มะโรง (มังกร)", 
            "มะเส็ง (งู)", "มะเมีย (ม้า)", "มะแม (แพะ)", "วอก (ลิง)", "ระกา (ไก่)", 
            "จอ (สุนัข)", "กุน (หมู)"
        ]
        chinese = {"ชวด (หนู)":1, "ฉลู (วัว)":2, "ขาล (เสือ)":3, "เถาะ (กระต่าย)":4, "มะโรง (มังกร)":5, 
            "มะเส็ง (งู)":6, "มะเมีย (ม้า)":7, "มะแม (แพะ)":8, "วอก (ลิง)":9, "ระกา (ไก่)":10, 
            "จอ (สุนัข)":11, "กุน (หมู)":12}
        return chinese[zodiac_animals[(year - 4) % 12]]
    
    def num(m1,m2,m3,m4):
        one = str(m1+m2+m3+m4)
        two = 0
        for i in range(len(one)):
            two += int(one[i])
        if len(str(two)) == 1:
            if two <= 7: pass
            elif two > 7:
                two -= 7    
        elif len(str(two)) == 2 and two > 10:
            n = 0
            for i in range(len(str(two))):
                n += int(str(two)[i])
            two = n
            if two <= 7: pass
            elif two > 7:
                two -= 7
        elif two in [10,20]:
            if two <= 7: pass
            elif two > 7:
                two -= 7
        return two
    
    def ch_age(age):
        one = str(age)
        two = 0
        for i in range(len(one)):
            two += int(one[i])
        return two
    ch = ch_age(age)
    
    
    # url_up_down = "https://www.myhora.com/%e0%b8%9b%e0%b8%8f%e0%b8%b4%e0%b8%97%e0%b8%b4%e0%b8%99/%e0%b8%9b%e0%b8%8f%e0%b8%b4%e0%b8%97%e0%b8%b4%e0%b8%99-%e0%b8%9e.%e0%b8%a8."+str(year)+".aspx"
    # ud = requests.get(url_up_down)
    # ud_data = BeautifulSoup(ud.text)
    # r1 = ud_data.find('div', {'id' : "container"})
    # r2 = r1.find('div', {'class' : 'content-main-fullwidth'})
    # r3 = r2.find('div' , {'id' : 'panel1'})
    # r4 = r3.find('div' , {'id' : 'print_div1'})
    # r5 = r4.find_all('div' , {'class' : 'col-mnt'})[int(twelve_year[month])-1]
    # r6 = r5.find('div' , {'class' : 'cal-mcm cal-mc'+str(twelve_year[month])})
    # r7 = r6.find('div' , {'class' : 'cmx-tis'})
    # r8 = r7.find_all('div' , {'class' : 'cmx-ddn cmx-bgz cmx-cx1'})[seven_day[day]-1]
    # r9 = r8.find('div' , {'id' : 'div_'+str(int(year)-543)+str(twelve_year[month])+str(day)})
    # r10 = r9.find('div' , {'class' : 'cmx-cx4'})
    # r11 = r10.find('font' , {'class' : 'cmx-fs1'})
    
    
    
    now = datetime.date.today()
    chinese_zodiac = get_chinese_zodiac(year-543) #ปีนักษัตร
    
    url_ch = "https://www.myhora.com/%e0%b8%9b%e0%b8%8f%e0%b8%b4%e0%b8%97%e0%b8%b4%e0%b8%99/%e0%b8%9b%e0%b8%8f%e0%b8%b4%e0%b8%97%e0%b8%b4%e0%b8%99-100%e0%b8%9b%e0%b8%b5-%e0%b8%9e.%e0%b8%a8."+str(year)+".aspx"
    if 10 <= month_ch[month] <= 12:
        url_ch = "https://www.myhora.com/%e0%b8%9b%e0%b8%8f%e0%b8%b4%e0%b8%97%e0%b8%b4%e0%b8%99/%e0%b8%9b%e0%b8%8f%e0%b8%b4%e0%b8%97%e0%b8%b4%e0%b8%99-100%e0%b8%9b%e0%b8%b5-%e0%b8%9e.%e0%b8%a8."+str(year-1)+".aspx"
    
    res = requests.get(url_ch)

    data = BeautifulSoup(res.text)
    round1 = data.find('div', {'class':'rowx'})
    round2 = round1.find_all('div', {'class':'clm-'+str(month_ch[month])})[1]
    round3 = round2.find_all('div', {'class':'cl3'})[day_number]
    
    main1 = int(day_number)
    main2 = int(seven_day[day])
    main3 = int(round3.text.strip())
    if int(round3.text.strip()) == 88:
        main3 = 8
    main4 = int(chinese_zodiac)
    main5 = int(age+1)
    num1 = int(num(main1,main2,main3,main4))
    num2 = int(num(main2,main3,main4,main5))
    num3 = 0
    ch_new = ch+1
    if ch_new <= 10:
        num3 = int(ch_new)
    else:
        n = 0
        for i in range(len(str(ch_new))):
            n += int(str(ch_new)[i])
        num3 = n
    
    def table1(main2,main3,main4):  
        line1 = []
        line2 = []
        line3 = []
        line4 = []
        num1 = main2
        num2 = main3
        num3 = main4
        for i in range(num1,8):
            line1.append(i)   
        for i in range(1,num1):
            line1.append(i)
        for j in range(num2,13):
            line2.append(j)
        for j in range(1,num2):
            line2.append(j)
        for k in range(num3,13):
            line3.append(k)
        for k in range(1,num3):
            line3.append(k)
        for n in range(len(line3)):
            result = 0
            if n <= 6:
                result = line1[n]+line2[n]+line3[n]
                if result > 12:
                    if result > 12:
                        result -= 12
                    elif result > 24:
                        result -= 24
                    elif result > 36:
                        result -= 36
                    line4.append(result)
                else:
                    line4.append(result)
            else:
                result = line2[n]+line3[n]
                if result > 12:
                    if result > 12:
                        result -= 12
                    elif result > 24:
                        result -= 24
                    elif result > 36:
                        result -= 36
                    line4.append(result)
                else:
                    line4.append(result)
        # r_line1 = [str(i) for i in line1]
        r_line1 = ""
        r_line2 = ""
        r_line3 = ""
        r_line4 = ""
        for i in range(len(line1)):
            if len(str(line1[i])) == 1:
                txt = f"{str(line1[i]):<6}"
            elif len(str(line1[i])) == 2:
                txt = f"{str(line1[i]):<5}"
            r_line1 += txt
        for i in range(len(line2)):
            if len(str(line2[i])) == 1:
                txt = f"{str(line2[i]):<6}"
            elif len(str(line2[i])) == 2:
                txt = f"{str(line2[i]):<5}"
            r_line2 += txt
        for i in range(len(line3)):
            if len(str(line3[i])) == 1:
                txt = f"{str(line3[i]):<6}"
            elif len(str(line3[i])) == 2:
                txt = f"{str(line3[i]):<5}"
            r_line3 += txt
        for i in range(len(line4)):
            # if len(str(line4[i])) == 1:
            #     txt = f"{str(line4[i]):<6}"
            #     if i in [0,6,11]:
            #         position = f'<span style="color:red">{line4[i]}</span>     '
            #         txt = f"{position:<6}"
            # elif len(str(line4[i])) == 2:
            #     txt = f"{str(line4[i]):<5}"
            #     if i in [0,6,11]:
            #         position = f'<span style="color:red">{line4[i]}</span>     '
            #         txt = f"{position:<5}"
            if len(str(line4[i])) == 1:
                txt = f"{str(line4[i]):<6}"
            elif len(str(line4[i])) == 2:
                txt = f"{str(line4[i]):<5}"
            r_line4 += txt
        #ans = f"{r_line1}\n{r_line2}\n{r_line3}\n{r_line4}\n\n\n"
        ans = [r_line1,r_line2,r_line3,r_line4]
        return ans
                    
    def table2(main2,main3,main4):
        line1 = []
        line2 = []
        line3 = []
        line4 = []
        num1 = main2
        if num1 > 7:
            num1 -= 7
        num2 = main3
        if num2 > 7:
            num2 -= 7
        num3 = main4
        if num3 > 7:
            num3 -= 7
        for i in range(num1,8):
            line1.append(i)   
        for i in range(1,num1):
            line1.append(i)
        for j in range(num2,8):
            line2.append(j)   
        for j in range(1,num2):
            line2.append(j)
        for k in range(num3,8):
            line3.append(k)   
        for k in range(1,num3):
            line3.append(k)
        for n in range(len(line3)):
            result = line1[n]+line2[n]+line3[n]
            line4.append(result)

        r_line2 = ""
        r_line3 = ""
        r_line4 = ""
        r_line1 = ""
        for i in range(len(line1)):
            if len(str(line1[i])) == 1:
            #     txt = f"{str(line1[i]):<6}"
            #     if i in [0,6]:
            #         position = f'<span style="color:red">{line1[i]}</span>     '
            #         txt = f"{str(position):<6}"
            # elif len(str(line1[i])) == 2:
            #     txt = f"{str(line1[i]):<5}"
            #     if i in [0,6]:
            #         position = f'<span style="color:red">{line1[i]}</span>     '
            #         txt = f"{str(position):<5}"
            #     r_line1 += txt
             txt = f"{str(line1[i]):<6}"
            elif len(str(line1[i])) == 2:
                txt = f"{str(line1[i]):<5}"
            r_line1 += txt
        for i in range(len(line2)):
            if len(str(line2[i])) == 1:
                txt = f"{str(line2[i]):<6}"
            elif len(str(line2[i])) == 2:
                txt = f"{str(line2[i]):<5}"
            r_line2 += txt
        for i in range(len(line3)):
            if len(str(line3[i])) == 1:
                txt = f"{str(line3[i]):<6}"
            elif len(str(line3[i])) == 2:
                txt = f"{str(line3[i]):<5}"
            r_line3 += txt
        for i in range(len(line4)):
            if len(str(line4[i])) == 1:
                txt = f"{str(line4[i]):<6}"
            elif len(str(line4[i])) == 2:
                txt = f"{str(line4[i]):<5}"
            r_line4 += txt
        #ans = f"{r_line1}\n{r_line2}\n{r_line3}\n{r_line4}\n\n"
        ans = [r_line1,r_line2,r_line3,r_line4]
        return ans
    
    def table3(num1,main2,num3):
        line1 = []
        line2 = []
        line3 = []
        n1 = num1
        if n1 > 7:
            n1 -= 7
        n2 = main2
        if n2 > 7:
            n2 -= 7
        n3 = num3
        if n3 > 7:
            n3 -= 7
        for i in range(n1,8):
            line1.append(i)   
        for i in range(1,n1):
            line1.append(i)
        for j in range(n2,8):
            line2.append(j)   
        for j in range(1,n2):
            line2.append(j)
        for k in range(n3,8):
            line3.append(k)   
        for k in range(1,n3):
            line3.append(k)

        r_line1 = ""
        r_line2 = ""
        r_line3 = ""
        for i in range(len(line1)):
            if len(str(line1[i])) == 1:
                txt = f"{str(line1[i]):<6}"
            elif len(str(line1[i])) == 2:
                txt = f"{str(line1[i]):<5}"
            r_line1 += txt
        for i in range(len(line2)):
            if len(str(line2[i])) == 1:
                txt = f"{str(line2[i]):<6}"
            elif len(str(line2[i])) == 2:
                txt = f"{str(line2[i]):<5}"
            r_line2 += txt
        for i in range(len(line3)):
            if len(str(line3[i])) == 1:
                txt = f"{str(line3[i]):<6}"
            elif len(str(line3[i])) == 2:
                txt = f"{str(line3[i]):<5}"
            r_line3 += txt
        #ans = f"{r_line1}\n{r_line2}\n{r_line3}\n\n"
        ans = [r_line1,r_line2,r_line3]
        return ans
    
    only_age = str(main5)
    def table4(num2,only_age):
        line1 = []
        line2 = []
        line3 = []
        n1 = num2
        if n1 > 7:
            n1 -= 7
        n2 = int(only_age[0])
        if n2 > 7:
            n2 -= 7
        n3 = int(only_age[1])
        if n3 > 7:
            n3 -= 7
        for i in range(n1,8):
            line1.append(i)   
        for i in range(1,n1):
            line1.append(i)
        for j in range(n2,8):
            line2.append(j)   
        for j in range(1,n2):
            line2.append(j)
        for k in range(n3,8):
            line3.append(k)   
        for k in range(1,n3):
            line3.append(k)

        r_line1 = ""
        r_line2 = ""
        r_line3 = ""
        for i in range(len(line1)):
            if len(str(line1[i])) == 1:
                txt = f"{str(line1[i]):<6}"
            elif len(str(line1[i])) == 2:
                txt = f"{str(line1[i]):<5}"
            r_line1 += txt
        for i in range(len(line2)):
            if len(str(line2[i])) == 1:
                txt = f"{str(line2[i]):<6}"
            elif len(str(line2[i])) == 2:
                txt = f"{str(line2[i]):<5}"
            r_line2 += txt
        for i in range(len(line3)):
            if len(str(line3[i])) == 1:
                txt = f"{str(line3[i]):<6}"
            elif len(str(line3[i])) == 2:
                txt = f"{str(line3[i]):<5}"
            r_line3 += txt
        #ans = f"{r_line1}\n{r_line2}\n{r_line3}\n\n\n"
        ans = [r_line1,r_line2,r_line3]
        return ans
    
    def table5(num2,only_age):
        line1 = []
        line2 = []
        line3 = []
        line4 = []
        # n1 = num2
        # n2 = int(only_age[0])
        # n3 = int(only_age[1])
        n1 = num2
        if n1 > 7:
            n1 -= 7
        n2 = int(only_age[0])
        if n2 > 7:
            n2 -= 7
        n3 = int(only_age[1])
        if n3 > 7:
            n3 -= 7
        for i in range(n1,8):
            line1.append(i)   
        for i in range(1,n1):
            line1.append(i)
        for j in range(n2,13):
            line2.append(j)
        for j in range(1,n2):
            line2.append(j)
        for k in range(n3,13):
            line3.append(k)
        for k in range(1,n3):
            line3.append(k)
        for n in range(len(line2)):
            result = 0
            if n <= 6:
                result = line1[n]+line2[n]+line3[n]
                if result > 12:
                    if result > 12:
                        result -= 12
                    elif result > 24:
                        result -= 24
                    elif result > 36:
                        result -= 36
                    line4.append(result)
                else:
                    line4.append(result)
            else:
                result = line2[n]+line3[n]
                if result > 12:
                    if result > 12:
                        result -= 12
                    elif result > 24:
                        result -= 24
                    elif result > 36:
                        result -= 36
                    line4.append(result)
                else:
                    line4.append(result)
        r_line1 = ""
        r_line2 = ""
        r_line3 = ""
        r_line4 = ""
        for i in range(len(line1)):
            if len(str(line1[i])) == 1:
                txt = f"{str(line1[i]):<6}"
            elif len(str(line1[i])) == 2:
                txt = f"{str(line1[i]):<5}"
            r_line1 += txt
        for i in range(len(line2)):
            if len(str(line2[i])) == 1:
                txt = f"{str(line2[i]):<6}"
            elif len(str(line2[i])) == 2:
                txt = f"{str(line2[i]):<5}"
            r_line2 += txt
        for i in range(len(line3)):
            if len(str(line3[i])) == 1:
                txt = f"{str(line3[i]):<6}"
            elif len(str(line3[i])) == 2:
                txt = f"{str(line3[i]):<5}"
            r_line3 += txt
        for i in range(len(line4)):
            if len(str(line4[i])) == 1:
                txt = f"{str(line4[i]):<6}"
            elif len(str(line4[i])) == 2:
                txt = f"{str(line4[i]):<5}"
            r_line4 += txt
        #ans = f"{r_line1}\n{r_line2}\n{r_line3}\n{r_line4}\n\n"
        ans = [r_line1,r_line2,r_line3,r_line4]
        return ans
    
    t1 = table1(main2,main3,main4)
    t2 = table2(main2,main3,main4)
    t3 = table3(num1,main2,num3)
    t4 = table4(num2,only_age)
    t5 = table5(num2,only_age)

    # result1 = f"วันที่ปัจจุบัน : {now.day}   {now.month}    {now.year+543}      {r11.text.strip()}\n\n\n"
    result1 = f"วันที่ปัจจุบัน : {now.day}   {now.month}    {now.year+543}\n\n\n"
    result2 = f"{num3:>26}\n{main1}  /  {main2}  {main3}  {main4}  /  {main5}\n{num1} {num2:>23}\n\n\n"
    result3 = f"{t1[0]}{t2[0]:>108}\n{t1[1]}{t2[1]:>73}\n{t1[2]}{t2[2]:>73}\n{t1[3]}{t2[3]:>69}"
    result4 = f"\n\n\n\n{t3[0]}\n{t3[1]}\n{t3[2]}\n\n\n\n"
    result5 = f"{t4[0]}{t5[0]:>66}\n{t4[1]}{t5[1]:>93}\n{t4[2]}{t5[2]:>93}\n{t5[3]:>142}"
    
    result = result1 + result2 + result3 + result4 + result5 
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)