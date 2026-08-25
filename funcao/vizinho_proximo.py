from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

M = Image.open("imagens\cubo.png")

M = np.asarray(M, dtype=np.float32)/255

#M[99:200,:,0] = 0

#M[99:200,:,1] = 0

MTR = np.transpose(M[:,:,0])
MTG = np.transpose(M[:,:,1])
MTB = np.transpose(M[:,:,2])

MT = np.zeros((544,519,3))

MT[:,:,0], MT[:,:,1], MT[:,:,2] = MTR, MTG, MTB

plt.figure(figsize=(3,3))
im = plt.imshow(MT, aspect='auto')
plt.axis("off")
plt.show()
print(MT.shape)