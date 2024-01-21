def pyramid_blocks(n, m, h):
  x = h*(h-1)//2
  sumToH = (h - 1) * h * (2 * (h - 1) + 1) // 6
  balls = n*m*h + n*x + m*x + sumToH
  return balls
