import label_image #on site


graph = "retrained_graph.pb" # on site
image = "/Users/Rohan/Desktop/1.jpeg" # user input
textFile = "retrained_labels.txt" #on the site

label_image.function(graph, image, textFile)
