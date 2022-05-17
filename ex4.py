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

    img_arr = np.zeros_like(image_array)

    for m in range(0, img_arr.shape[0]):
        for n in range(0, img_arr.shape[1], spacing[1]):
            img_arr[m, n, :] = image_array[m, n, :]

    for m in range(0, img_arr.shape[1]):
        for n in range(0, img_arr.shape[0], spacing[0]):
            img_arr[n, m, :] = 0

    img_arr[:, :offset[0], :] = 0
    img_arr[:offset[1], :, :] = 0

    remaining_pixels = (np.sum(np.all(img_arr > 0, axis=2))) // 3

    if remaining_pixels < 144:
        raise ValueError(f'Remaining pixels can not be under 144! Remaining pixels: {remaining_pixels}')

    return img_arr


if __name__ == '__main__':
    img_path = 'img.jpg'
    open_img = Image.open(img_path)
    image_array = np.asarray(open_img)
    arr = ex4(image_array, (2, 1), (2, 3))

    img_fa = Image.fromarray(arr)
    img_fa.save('img_after.jpg')
