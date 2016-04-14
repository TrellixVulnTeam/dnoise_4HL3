from dnoise.cnn import CNN
from dnoise.loaders import load_stl


ds = load_stl(grayscale=False, batch_size=10, n=10)
cnn = CNN(input_shape=[96, 96, 3], output_shape=[10])
cnn.train(ds, debug=True, display_step=None, epochs=10000, learning_rate=0.01)
