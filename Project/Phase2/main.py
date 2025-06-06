from mnist.train_mlp import train_mnist_mlp
from mnist.train_cnn import train_mnist_cnn
from dog_cat_classifier.train_dog_cat import train_dog_cat
from fer2013.train_fer import train_fer
from speech_commands.recognize import speech_command_recognizer

if __name__ == "__main__":
    print("1. MNIST MLP")
    print("2. MNIST CNN")
    print("3. 猫狗图像分类")
    print("4. FER 表情识别")
    print("5. Google Speech Commands")
    print("6. 图像风格迁移")
    c = input("选择项目编号: ")
    if c == '1': train_mnist_mlp()
    elif c == '2': train_mnist_cnn()
    elif c == '3': train_dog_cat()
    elif c == '4': train_fer()
    elif c == '5': speech_command_recognizer()
    elif c == '6':
        print("请参考: https://pytorch.org/tutorials/advanced/neural_style_tutorial.html")
