class Coupon:
    def __init__(self, mode, code, expire_at, limit, value):
        self.mode = mode
        self.code = code
        self.expire_at = expire_at
        self.limit = limit
        self.value = value