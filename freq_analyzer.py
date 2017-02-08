import numpy as np

class FreqAnalyzer:
    def __init__(self):
        self.img = None
        self.mask = None
        self.mw = self.mh = 0
        self.iw = self.ih = 0
        self.fr_data = []
        self.fr_w = []
        self.fr_h = []
        self.ibuf_1 = self.ibuf_2 = None
        self.fam = 0
        self.apl = []
        self.auto_size_mode = 0
        self.base_w_pot = 10
        self.base_h_pot = 10

    def EnableAutoSizeLess(self):
        self.auto_size_mode = 1

    def EnableAutoSizeMore(self):
        self.auto_size_mode = 2

    def DisableAutoSize(self):
        self.auto_size_mode = 0

    def SetBaseSizePow(self, w_pot, h_pot):
        self.base_w_pot = max(1, min(w_pot, 13))
        self.base_h_pot = max(1, min(w_pot, 13))

    def ReserveMemory(self):
        mx = 1
        while 1 << mx <= self.iw:
            mx += 1
        if self.auto_size_mode == 1:
            mx -= 1
        elif self.auto_size_mode == 0:
            mx = self.base_w_pot
        xres = 1 << mx
        my = 1
        while 1 << my <= self.ih:
            my += 1
        if self.auto_size_mode == 1:
            my -= 1
        elif self.auto_size_mode == 0:
            my = self.base_h_pot
        yres = 1 << my
        if mx < my: self.fam = mx
        else: self.fam = my
        self.fam += 1
        self.fr_w = np.zeros(self.fam).astype(int)
        self.fr_h = np.zeros(self.fam).astype(int)
        self.fr_w[0], self.fr_h[0] = xres, yres
        for i in range(1, self.fam):
            self.fr_w[i] = self.fr_w[i - 1] // 2
            self.fr_h[i] = self.fr_h[i - 1] // 2
        self.fr_data = np.array([[0 for j in range(self.fr_w[i] * self.fr_h[i])] for i in range(self.fam)])
        self.apl = np.zeros(self.fam)
        self.ibuf_1 = np.zeros(xres * yres)
        self.ibuf_2 = np.zeros(xres * yres)

    def BuildLevel(self, id):
        if id == self.fam:
            self.fr_data[id] = self.ibuf_1[::]
            return
        w, h = self.fr_w[id], self.fr_h[id]
        sw, sh = w / 2, h / 2
        for i in range(0, sh):
            for j in range(0, sw):
                self.ibuf_2[i * sw + j] = 0.25 * (self.ibuf_1[i * 2 * w + j * 2] +
                                                  self.ibuf_1[(i * 2 + 1) * w + j * 2] +
                                                  self.ibuf_1[(i * 2 + 1) * w + j * 2 + 1] +
                                                  self.ibuf_1[i * 2 * w + j * 2 + 1]
                                                 )
                d = self.fr_data[id]
                for i in range(0, h):
                    for j in range(0, w):
                        d[i * w + j] = self.ibuf_1[i * w + j] - self.ibuf_2[(i >> 1) * sw + (j >> 1)]
                d = self.ibuf_1[::]
                self.ibuf_1 = self.ibuf_2[::]
                self.ibuf_2 = d[::]

    def CalculateAmplitudes(self):
        for i in range(0, self.fam):
            self.apl[i] = 0.0
            for j in range(0, self.fr_w[i] * self.fr_h[i]):
                self.apl[i] = abs(self.fr_data[i][j])
            self.apl[i] /= float(self.fr_w[i] * self.fr_h[i])

    def CalculateMaskedAmplitudes(self):
        mask_buf = np.zeros(self.fr_w[0] * self.fr_h[0])
        mask_reduced = np.zeros(self.fr_w[0] // 2 * self.fr_h[0] // 2)
        




























