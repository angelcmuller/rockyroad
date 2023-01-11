
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os


def main():
    print("========Image Classifier ========")
    Classifer()

# Classifies images into categories


def Classifer():
    img = image.load_img(
        "data\\frame0_39.56484544_-119.7043577.jpg")
    plt.imshow(img)
    # plt.show()
    cv2.imread(
        "data\\frame0_39.56484544_-119.7043577.jpg")
    train = ImageDataGenerator(rescale=1/255)
    validation = ImageDataGenerator(rescale=1/255)
    # resize images and assign label
    # given to neural network 3 images a time (batch size)
    train_dataset = train.flow_from_directory(
        'training', target_size=(200, 200), batch_size=3, class_mode='binary')
    validation_dataset = train.flow_from_directory(
        'validation', target_size=(200, 200), batch_size=3, class_mode='binary')

    # make the CNN
    # need to write how many filters (16) size of those filters (3,3) and activation functoin
    model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(200, 200, 3)), tf.keras.layers.MaxPool2D(2, 2),
                                        #
                                        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(
                                            200, 200, 3)), tf.keras.layers.MaxPool2D(2, 2),
                                        #
                                        tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(
                                            200, 200, 3)), tf.keras.layers.MaxPool2D(2, 2),
                                        #
                                        tf.keras.layers.Flatten(),
                                        #
                                        tf.keras.layers.Dense(
        512, activation='relu'),
        # do softmix for multi classification
        tf.keras.layers.Dense(
        1, activation='sigmoid')
    ])

    model.compile(loss='binary_crossentropy', optimizer=RMSprop(
        lr=0.001), metrics=['accuracy'])

    # train the model
    model_fit = model.fit(train_dataset, steps_per_epoch=3,
                          epochs=30, validation_data=validation_dataset)

    # test the practice data set
    dir_path = 'testing'

    for i in os.listdir(dir_path):
        img = image.load_img(dir_path + '\\' + i, target_size=(200, 200, 3))
        plt.imshow(img)
        plt.show()

        X = image.img_to_array(img)
        X = np.expand_dims(X, axis=0)
        images = np.vstack([X])
        val = model.predict(images)
        if val == 0:
            print("Bad road :(")
        else:
            print("Good road :)")


    # main function guarente
if __name__ == "__main__":
    main()
