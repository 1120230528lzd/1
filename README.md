

# Tomato was detected separately by the traditional method and the modified YOLOv8

The aim of this project is to compare two different approaches to tomato detection: one based on traditional image processing techniques (using OpenCV) and the other based on deep learning (using YOLOv8). The comparison of these two methods allows us to evaluate the difference in their performance in the tomato detection task.

## Catalogs

- [Traditional methods]
  - [Dependency library]
  - [Procedure for use]
  - [Scripting process]
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
  - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)

### Traditional_methods
This project aims to detect round tomatoes from a picture containing tomatoes through a series of image processing techniques including color segmentation, median filtering, binarization, morphological operations, edge detection and Hough circle detection. The whole processing process aims to improve the image quality, reduce noise and ultimately detect the circular tomato target accurately.
###### Dependency library
- [OpenCV]  :Used for image processing functions such as reading images, color segmentation, filtering, binarization, morphological operations, edge detection, and Hough circle detection.
- [NumPy]:For working with large multi-dimensional arrays and matrices, and performing efficient mathematical operations.
- [Matplotlib]:For displaying and visualizing images.

###### **Procedure for use**

- 1.Install dependent libraries: make sure OpenCV, NumPy and Matplotlib are installed. you can use the pip command to install them:

```sh
pip install opencv-python numpy matplotlib

```
- 2.Prepare the image: Name an image containing tomatoes as tomato1.jpg and make sure it is located in the same directory as the Python script.
- 3.Run Script: Run the Python script directly. The script will automatically load the image, perform a series of image processing steps, and display the results at the end.
###### Scripting process
- Image reading: a color image named tomato1.jpg is read using OpenCV.
- Color Segmentation: highlight the red region (i.e. tomato) by calculating the difference between the red channel and the green channel.
- Image preprocessing: 
  - 1.Median Filtering: reduce image noise using median filtering.
  - 2.Binarization: converts an image to a binary image by automatically determining the threshold value through Otsu thresholding.
  - 3.Morphological operations: fills holes in binary images using a flood-fill algorithm and performs erosion operations to remove small noise.
- Edge Detection: Detects edges in an image using the Canny edge detection algorithm.
- Hough Circle Detection: Apply Hough Circle Detection algorithm on the edge image to identify round tomatoes.
- RESULTS PRESENTATION: Display the processed image, edge detection results and detected round tomatoes using Matplotlib.

Translated with www.DeepL.com/Translator (free version)
eg:

```
filetree 
├── ARCHITECTURE.md
├── LICENSE.txt
├── README.md
├── /account/
├── /bbs/
├── /docs/
│  ├── /rules/
│  │  ├── backend.txt
│  │  └── frontend.txt
├── manage.py
├── /oa/
├── /static/
├── /templates/
├── useless.md
└── /util/

```





### 开发的架构 

请阅读[ARCHITECTURE.md](https://github.com/shaojintian/Best_README_template/blob/master/ARCHITECTURE.md) 查阅为该项目的架构。

### 部署

暂无

### 使用到的框架

- [xxxxxxx](https://getbootstrap.com)
- [xxxxxxx](https://jquery.com)
- [xxxxxxx](https://laravel.com)

### 贡献者

请阅读**CONTRIBUTING.md** 查阅为该项目做出贡献的开发者。

#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

xxx@xxxx

知乎:xxxx  &ensp; qq:xxxxxx    

 *您也可以在贡献者名单中参看所有参与该项目的开发者。*


