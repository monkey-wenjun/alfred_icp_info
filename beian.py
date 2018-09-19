# -*-coding:utf-8-*-
# Auth: awen
# E-mail:hi@awen.me


from workflow import Workflow, ICON_WEB, web
import sys



def main(wf):
    param = (wf.args[0] if len(wf.args) else '').strip()
    domain = param
    url = "https://sapi.k780.com?app=domain.beian&domain="+domain+"&appkey=xxxx&sign=xxxx&format=json"
    r = web.get(url)
    r.raise_for_status()
    r = r.json()
    try:
        if r['result']['icpno']:
            icpno = r['result']['icpno']
            wf.add_item(title=domain, subtitle=icpno)
            wf.send_feedback()
        else:
            wf.add_item(title=domain, subtitle=u"没有查询到备案信息")
            wf.send_feedback()
    except:
         wf.add_item(title=domain, subtitle=u"没有查询到备案信息")
         wf.send_feedback()
                 
if __name__ == '__main__':
   wf = Workflow()
   sys.exit(wf.run(main))
