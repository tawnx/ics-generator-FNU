var table=document.getElementById('kblist_table')
var classtags=table.getElementsByTagName('tr')
var python_code_all=""
for(const classtag of classtags){
    //获取星期几，第几节
    if(classtag.getElementsByTagName('td')[0].id.indexOf('jc_')==-1){
        continue;
    }
    var date=classtag.getElementsByTagName('td')[0].id.match(/\d+/g)
    var weekday=date[0]
    var daysection_start=date[1]
    var daysection_end=date[2]

    //获取周数
    var week_ranges=classtag.innerText.match(/(\d+-\d+|\d+)周[\(\)单双]*/g)
    var week_str_all=""
    for(const week_range of week_ranges){
        var week=week_range.match(/\d+/g)
        week[1]=week[1]?week[1]:week[0]
        week_str="rgWeek("+week[0]+","+week[1]+")+"
        
        //单双周处理
        if(week_range.indexOf('单')>-1){
            week_str=week_str.replace('rg','oe')
            week_str=week_str.replace(')',',1)')
        }
        if(week_range.indexOf('双')>-1){
            week_str=week_str.replace('rg','oe')
            week_str=week_str.replace(')',',0)')
        }
        week_str_all+=week_str
    }
    //删除最后的+号
    week_str_all=week_str_all.substring(0,week_str_all.length-1)


    //获取课程的名称、教师、地点
    var classname=classtag.getElementsByClassName('title')[0].innerText
    var teacher=classtag.innerText.match(/(?<=教师：)[\u4e00-\u9fa5]+/g)[0]
    var address=classtag.innerText.match(/(?<=上课地点：)[\u4e00-\u9fa5\-\d]+/g)[0]

    //["概率论与数理统计", "陈海霞", "立诚1-205", rgWeek(4, 7) + rgWeek(9, 16), 1, [1, 2]],
    
    var section=daysection_start==daysection_end?'['+daysection_start+']':'['+daysection_start+','+daysection_end+']'
    var python_code='[\"'+classname+'\",'+'\"'+teacher+'\",'+'\"'+address+'\",'+week_str_all+','+weekday+','+section+'],\n'
    python_code_all+=python_code
}
console.log(python_code_all)
