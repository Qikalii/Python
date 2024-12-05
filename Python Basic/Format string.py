contacts = ["老余", "老林", "老陈", "老曾", "老李", "老张"]
##
# for name in contacts:
#     masseage_content = name + "\n:祝福" + name + "虎年大吉"
#     print(masseage_content)

# ##
# year = "虎年"
# for name in contacts:
#     masseage_content = ("{0}\n:祝福{0}{1}大吉").format(year, name)
#     print(masseage_content)

##
year = "虎年"
for name in contacts:
    masseage_content = ("{name}\n:祝福{name}{year}大吉").format(name=name, year=year)
    print(masseage_content)
