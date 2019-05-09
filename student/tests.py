from django.test import TestCase

# Create your tests here.
from student.models import Student


class StudentTestCase(TestCase):
    # 用来初始化环境，包括创建初始化的数据，或者做一些其他准备工作
    def setUp(self):
        Student.objects.create(
            name='cz',
            sex=2,
            email='11455@qq.com',
            profession='doctor',
            qq='11455',
            phone='1592',
        )
    # 以 test 开头的方法，会被认为是需要测试的方法，跑测试时会被执行 。
    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='ccenz',
            sex=2,
            email='11455@qq.com',
            profession='dasdsa',
            qq='11455',
            phone='15921',
        )
        self.assertEqual(student.sex_show,'男','两者不一致！')

    def test_filter(self):
        Student.objects.create(
            name='ccenz',
            sex=2,
            email='11455@qq.com',
            profession='dasdsa',
            qq='11455',
            phone='15921',
        )
        name='cz'
        student=Student.objects.filter(name=name)
        self.assertEqual(student.count(),1,'应该只存在一个名称为｛｝的记录'.format(name))
