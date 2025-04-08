import unittest
import pandas as pd
import numpy as np
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#from solutions.pandas_practice_solution import creat_frame, load_data, handle_missing_values, analyze_statistics, save_processed_data
from src.pandas_practice import creat_frame, load_data, handle_missing_values, analyze_statistics, save_processed_data

class TestPandasPractice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """在所有测试前运行，创建测试数据"""
        creat_frame()
        cls.test_data_path = 'data/data.csv'
        cls.processed_data_path = 'processed_data.csv'
        cls.data = load_data()
        
    def test_file_creation(self):
        """测试数据文件是否创建成功"""
        self.assertTrue(os.path.exists(self.test_data_path))
        
    def test_data_integrity(self):
        """测试数据完整性"""
        # 检查列名
        expected_columns = ['姓名', '年龄', '成绩', '城市']
        self.assertListEqual(list(self.data.columns), expected_columns)
        # 检查行数
        self.assertEqual(len(self.data), 5)
        
    def test_missing_value_handling(self):
        """测试缺失值处理函数"""
        # 检查原始数据是否有缺失值
        self.assertTrue(self.data['年龄'].isnull().any())
        
        # 测试处理缺失值函数
        processed_data = handle_missing_values(self.data.copy())
        
        # 检查处理后是否还有缺失值
        self.assertFalse(processed_data['年龄'].isnull().any())
        # 检查填充值是否正确
        expected_age_mean = self.data['年龄'].mean()
        self.assertAlmostEqual(processed_data['年龄'].mean(), expected_age_mean)
        
    def test_statistical_analysis(self):
        """测试统计分析函数"""
        processed_data = handle_missing_values(self.data.copy())
        
        # 捕获print输出进行验证
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        
        analyze_statistics(processed_data)
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        # 验证输出中包含预期的统计信息
        self.assertIn("成绩 列的均值", output)
        self.assertIn("年龄 列的均值", output)
        
    def test_processed_data_saving(self):
        """测试数据处理完整流程"""
        
        # 执行完整处理流程
        processed_data = handle_missing_values(self.data.copy())
        save_processed_data(processed_data)
        
        # 检查文件是否创建
        self.assertTrue(os.path.exists(self.processed_data_path))
        
        # 检查文件内容
        saved_data = pd.read_csv(self.processed_data_path)
        self.assertEqual(len(saved_data), 5)
        self.assertFalse(saved_data['年龄'].isnull().any())
        
    @classmethod
    def tearDownClass(cls):
        """在所有测试后运行，清理测试文件"""
        if os.path.exists(cls.test_data_path):
            os.remove(cls.test_data_path)
        if os.path.exists(cls.processed_data_path):
            os.remove(cls.processed_data_path)

if __name__ == '__main__':
    unittest.main()