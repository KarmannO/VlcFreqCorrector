class FreqAnalyzer:
    def __init__(self):
        self.img = None
        self.iw = self.ih = 0
        self.fr_data = None
        self.fr_w = self.fr_h = 0
        self.ibuf_1 = self.ibuf_2 = None
        self.fam = self.apl = 0
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

























