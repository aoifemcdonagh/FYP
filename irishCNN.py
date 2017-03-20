import tensorflow as tf, sys
image_path = sys.argv[1]

# Read in the image data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Load label file, strips off carraige return
label_lines = [line.rstrip() for line in tf.gfile.GFile("/tf_files/retrained_labels")]

# Unpersists graph from file
with tf.gfile.FastGFile("/tf_files/retrained_graph.pb", 'rb') as f:
	graph_def = tf.GraphDef()
	graph.ParseFromString(f.read())
	_ = tf.import_graph_def(graph_def, name=' ')
	
with tf.Session() as sess:
	Feed the image_data as input