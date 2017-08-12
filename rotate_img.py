img = [
  [ 1, 2, 3, 4],
  [ 5, 6, 7, 8],
  [ 9,10,11,12],
  [13,14,15,16]
  ]

img2 = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

def turn_image(img):
  layers = int(round(len(img) / 2))
  
  for layer in range(layers):
    for i in range(layer, len(img)-1-layer):
      start_to_end = i
      end_to_start = len(img)-1-i
      end = -1 - layer
      start = layer
    
      img[end][end_to_start], img[end_to_start][start], img[start][start_to_end], img[start_to_end][end] = \
        img[start_to_end][end], img[end][end_to_start], img[end_to_start][start], img[start][start_to_end]
    
  return img
  
print turn_image(img)
