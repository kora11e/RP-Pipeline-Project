class HaarFeature:
    def __init__(self, feature_type, position, width, height):
        self.feature_type = feature_type  # 'two-rectangle'
        self.position = position  # (x, y)
        self.width = width
        self.height = height

    def compute_value(self, integral_img):
        x, y = self.position
        w, h = self.width, self.height

        if self.feature_type == 'two-rectangle-horizontal':
            A = self.sum_region(integral_img, x, y, w // 2, h)
            B = self.sum_region(integral_img, x + w // 2, y, w // 2, h)
            return A - B
        elif self.feature_type == 'two-rectangle-vertical':
            A = self.sum_region(integral_img, x, y, w, h // 2)
            B = self.sum_region(integral_img, x, y + h // 2, w, h // 2)
            return A - B
        elif self.feature_type == 'three-rectangle-horizontal':
            A = self.sum_region(integral_img, x, y, w //3, h)
            B = self.sum_region(integral_img, x + w // 3, y, w // 3, h)
            C = self.sum_region(integral_img, x + 2*(w // 3), y, w // 3, h)
            return A - B + C
        elif self.feature_type == 'three-rectangle-vertical':
            A = self.sum_region(integral_img, x, y, w, h // 3)
            B = self.sum_region(integral_img, x, y + h // 3, w, h // 3)
            C = self.sum_region(integral_img, x, y + 2*(h // 3), w, h // 3)
            return A - B + C
        elif self.feature_type == 'four-rectangle':
            A = self.sum_region(integral_img, x, y, w // 2, h // 2)
            B = self.sum_region(integral_img, x + w // 2, y, w // 2, h // 2)
            C = self.sum_region(integral_img, x, y + h // 2, w // 2, h // 2)
            D = self.sum_region(integral_img, x + w // 2, y + h // 2, w // 2, h // 2)
            return A - B - C + D
        else:
            return 0

    def sum_region(self, integral_img, x, y, w, h):
        A = integral_img[y-1, x-1] if y > 0 and x > 0 else 0
        B = integral_img[y-1, x+w-1] if y > 0 else 0
        C = integral_img[y+h-1, x-1] if x > 0 else 0
        D = integral_img[y+h-1, x+w-1]
        return D - B - C + A