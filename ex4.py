"""
Author: Medis Redzic
Matr.Nr.: K11934616
Exercise: Exercise 4
"""

import numpy as np
from PIL import Image

def ex4(image_array: np.ndarray, offset: tuple, spacing: tuple):

    if type(image_array) != np.ndarray:
        raise TypeError("'image_array' is not a numpy array!")

    if image_array.ndim != 3:
        raise NotImplementedError("'image_array' has to be a 3D array!")

    if image_array.shape[2] != 3:
        raise NotImplementedError('Shape of third dimensions is not equal to 3!')

    if not type(offset[0]) is int or not type(offset[1]) is int:
        raise ValueError(f'Offset can not be converted to an integer! Type: {type(offset[0])} | {type(offset[1])}')

    if not type(spacing[0]) is int or not type(spacing[1]) is int:
        raise ValueError(f'Spacing can not be converted to an integer! Type: {type(spacing[0])} | {type(spacing[1])}')

    if not 0 <= offset[0] <= 32 or not 0 <= offset[1] <= 32:
        raise ValueError('Offset can not be smaller than 0 or larger than 32')

    if not 2 <= spacing[0] <= 8 or not 2 <= spacing[1] <= 8:
        raise ValueError('Spacing can not be smaller than 2 or larger than 8')

    n_axis, m_axis = image_array.shape[0] - offset[0], image_array.shape[1] - offset[1]
    n_axis_s, m_axis_s = n_axis / spacing[0], m_axis / spacing[1]

    if (n_axis_s * m_axis_s) < 144:
        raise ValueError(f'Remaining pixels can not be under 144! Remaining pixels: {n_axis * m_axis_s}')

    img_arr = np.zeros_like(image_array)
    img_arr = np.transpose(img_arr, (2, 0, 1))

    for m in range(offset[1], img_arr.shape[1], spacing[1]):
        for n in range(offset[0], img_arr.shape[2], spacing[0]):
            img_arr[:, m, n] = image_array[m, n, :]

    target_array = np.zeros_like(img_arr)
    known_array = np.zeros_like(img_arr)

    known_array[img_arr > 0] = 1

    target_array = img_arr[known_array == 0]
    target_array = target_array.flatten()

    return img_arr, known_array, target_array


if __name__ == '__main__':
    img_path = '336.jpg'
    open_img = Image.open(img_path)
    image_array = np.asarray(open_img)
    arr, _, _ = ex4(image_array, (0, 0), (8, 8))

    #img_faa = Image.fromarray(kw)
    #img_faa.save('img_kw.jpg')
    arr = np.transpose(arr, (2, 1, 0))
    img_fa = Image.fromarray(arr)
    img_fa.save('img_after.jpg')
