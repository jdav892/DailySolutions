def potatoes(p0, w0, p1):
    dry = (100 - p0) * w0
    return dry // (100 - p1)