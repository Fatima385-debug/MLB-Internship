Transfer Learning:
Transfer Learning is a technique where a model is already been trained on a large dataset and then reused for new task. For training a model from scratch, it uses the pre-known knowledge it has already learned to improve accuracy and reduce training time.

Use of MobileNetV2:
MobileNetV2 because is fast and provides high accuracy. It is pre-trained on the ImageNet dataset and works well for image classification while using less computational power.

Experiments Performed:
To improve the model performance, resized all images to (224 × 224), normalize pixel values, froze the MobileNetV2 base model, added custom classification layers, and trained the model for 5 epochs using the Adam optimizer.

Challenges and Lessons:
Understanding how transfer learning works and how freezing the base model affects training. This also help me learn on how to preprocess image data, build a classification head, and evaluate the model using accuracy and loss graphs.