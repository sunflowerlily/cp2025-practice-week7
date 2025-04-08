import unittest
import numpy as np
import os
import sys
from unittest.mock import patch, MagicMock
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#from solutions.image_average_solution import create_small_filter, create_large_filter, process_image
from src.image_average import create_small_filter, create_large_filter, process_image

class TestImageAverage(unittest.TestCase):
    def test_small_filter_creation(self):
        """测试3×3滤波器创建"""
        filter = create_small_filter()
        self.assertEqual(filter.shape, (3, 3))
        self.assertAlmostEqual(np.sum(filter), 1.0)
        self.assertTrue(np.allclose(filter, np.ones((3,3))/9))
        
    def test_large_filter_creation(self):
        """测试15×15滤波器创建"""
        filter = create_large_filter()
        self.assertEqual(filter.shape, (15, 15))
        self.assertAlmostEqual(np.sum(filter), 1.0)
        self.assertTrue(np.allclose(filter, np.ones((15,15))/225))

    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.imshow')
    @patch('matplotlib.pyplot.subplot')
    @patch('matplotlib.pyplot.figure')
    @patch('scipy.ndimage.convolve')
    @patch('matplotlib.pyplot.imread')
    def test_process_image(self, mock_imread, mock_convolve, 
                         mock_figure, mock_subplot, 
                         mock_imshow, mock_show):
        """测试图像处理流程"""
        # 设置mock
        mock_img = np.random.rand(100, 100)
        mock_imread.return_value = mock_img
        mock_convolve.side_effect = lambda x, _: x
        
        # 执行测试
        process_image('test_image.tif')
        
        # 验证调用
        mock_imread.assert_called_once_with('test_image.tif')
        self.assertEqual(mock_convolve.call_count, 2)
        
        # 检查figure()是否被调用过
        self.assertTrue(mock_figure.called)
        
        # 检查subplot和imshow调用次数
        self.assertEqual(mock_subplot.call_count, 3)
        self.assertEqual(mock_imshow.call_count, 3)
        mock_show.assert_called_once()

    def test_nonexistent_file(self):
        """测试不存在的文件路径"""
        with self.assertRaises(FileNotFoundError):
            process_image('nonexistent_file.tif')

if __name__ == '__main__':
    unittest.main()