import unittest
import numpy as np
import os
import sys
from unittest.mock import patch, MagicMock

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

"""
from solutions.image_feature_emphasis_solution import (
    load_stress_fibers,
    create_gauss_filter,
    create_combined_filter,
    process_and_display
)
"""
from src.image_feature_emphasis import (
    load_stress_fibers,
    create_gauss_filter,
    create_combined_filter,
    process_and_display
)

class TestImageFeatureEmphasis(unittest.TestCase):
    def test_load_stress_fibers(self):
        """测试数据加载功能"""
        with patch('numpy.loadtxt') as mock_load:
            mock_load.return_value = np.random.rand(100, 100)
            result = load_stress_fibers()
            self.assertIsInstance(result, np.ndarray)
            mock_load.assert_called_with('data/stressFibers.txt')

    def test_create_gauss_filter(self):
        """测试高斯滤波器创建"""
        filter = create_gauss_filter()
        self.assertEqual(filter.shape, (51, 51))
        self.assertTrue(np.all(filter >= 0))
        self.assertTrue(np.all(filter <= 1))

    def test_create_combined_filter(self):
        """测试组合滤波器创建"""
        gauss = create_gauss_filter()
        combined = create_combined_filter(gauss)
        # 修改预期尺寸为51x51，因为mode='same'会保持原尺寸
        self.assertEqual(combined.shape, (51, 51))
        self.assertTrue(np.any(combined != 0))

    @patch('matplotlib.pyplot.show')
    @patch('matplotlib.pyplot.imshow')
    @patch('matplotlib.pyplot.colorbar')
    @patch('scipy.ndimage.convolve')
    def test_process_and_display(self, mock_convolve, mock_colorbar, mock_imshow, mock_show):
        """测试图像处理和显示"""
        mock_convolve.return_value = np.random.rand(100, 100)
        mock_imshow.return_value = MagicMock()  # 返回一个mock的mappable对象
        
        test_img = np.random.rand(100, 100)
        test_filter = np.random.rand(3, 3)
        
        result = process_and_display(test_img, test_filter)
        
        mock_convolve.assert_called_once()
        mock_imshow.assert_called_once()
        mock_colorbar.assert_called_once()
        mock_show.assert_called_once()
        self.assertIsInstance(result, np.ndarray)

if __name__ == '__main__':
    unittest.main()