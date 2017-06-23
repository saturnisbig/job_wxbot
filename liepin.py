#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import requests
import lxml.html

url = 'https://www.liepin.com/zhaopin/?pubTime=&ckid=d95fe91f9fc429c7&fromSearchBtn=2&compkind=&isAnalysis=&init=-1&searchType=1&flushckid=1&dqs=090020&industryType=industry_02&jobKind=&sortFlag=15&industries=050&salary=&compscale=&clean_condition=&key=&headckid=64cbbc7aea10239f'

def liepin(url):
    result = []
    resp = requests.get(url)
    tree = lxml.html.fromstring(resp.text)
    job_tag_lis = tree.xpath('//ul[@class="sojob-list"]/li')
    # print job_tag_lis
    for li in job_tag_lis:
        job_info = li.xpath('.//div[@class="job-info"]')[0]
        title = job_info.xpath('./h3/a/text()')[0].strip()
        url = job_info.xpath('./h3/a/@href')[0]
        req_t = job_info.xpath('./p[@class="condition clearfix"]')[0]
        # 多余的字符需要清理
        requirement = req_t.xpath('string()').strip()
        # requirement = requirement.replace('\n', ' ')
        # print requirement
        pub_t = job_info.xpath('.//time/text()')[0].strip()
        feedback_t = job_info.xpath('./p[@class="time-info clearfix"]/span/text()')
        # print title, url, requirement
        # print pub_t, feedback_t
        comp_info = li.xpath('.//div[@class="company-info nohover"]')[0]
        comp_name = comp_info.xpath('./p[@class="company-name"]/a/text()')[0].strip()
        field_t = comp_info.xpath('./p[@class="field-financing"]')[0]
        field = field_t.xpath('string()').strip()
        print comp_name, field


if __name__ == "__main__":
    liepin(url)

