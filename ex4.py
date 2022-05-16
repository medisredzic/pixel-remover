import numpy as np


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
