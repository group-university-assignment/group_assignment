from textcomponent import runprog
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import vlc

doc_path = 'TextFilesTesting/huck-finn-ch-1.txt'
speech, img, result = runprog(doc_path)

speech.play()

img=mpimg.imread(img)
imgplot = plt.imshow(img)
plt.show()

print(result)
