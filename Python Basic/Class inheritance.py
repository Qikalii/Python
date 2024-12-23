## 类继承联系：人力系统
# - 员工分为俩类：全职员工 FullTimeEmployee、兼职员工 PartTimeEmpluyee。
# - 全职和兼职员工都有“姓名 name”、“工号 id”属性。
#   都具备“打印信息 print_info" (打印姓名、工号)方法。
# - 全职有“月薪 monthly_salary”属性。
#   兼职有“日薪 dayly_salary”属性、“每月工作天数 work_days”的属性。
# - 全职和兼职都有“计算月薪 calculate_mothly_pay”的方法，但具体计算过程不一样。


class Employee:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def print_info(self):
        print(f"员工姓名:{self.name}\n员工工号:{self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary) -> None:
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_mothly_pay(self):
        return self.monthly_salary


class ParPartTimeEmpluyee(Employee):
    def __init__(self, name, id, dayly_salary, work_days) -> None:
        super().__init__(name, id)
        self.dayly_salary = dayly_salary
        self.work_days = work_days

    def calculate_mothly_pay(self):
        calculate_mothly_pay = self.dayly_salary * self.work_days
        return calculate_mothly_pay


chen = FullTimeEmployee("小陈", 123, 5000)
chen.print_info()
print(f"每月的工资为{chen.calculate_mothly_pay()}")
zeng = ParPartTimeEmpluyee("小曾", 456, 150, 20)
zeng.print_info()
print(f"每月的工资为{zeng.calculate_mothly_pay()}")
