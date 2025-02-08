# **Waste Classification and Recycling Awareness 🌍♻️**  

## **Overview**  
The world generates over **3.5 million tons of waste per day**, and this number is continuously increasing. Proper **waste classification and recycling** can significantly reduce environmental damage. This project aims to **classify waste materials** and provide awareness about **proper recycling and disposal methods**.  

### **Key Features**  
- Classifies **9 different types** of waste: **Light Bulbs, Paper, Plastic, Organic, Glass, Batteries, Clothes, Metal, and E-Waste**.  
- Uses **VGG16** Transfer Learning for image classification.  
- Dataset curated manually from **Google Images and Dreamstime.com**.  
- **Trained on 8,369 images** across 9 categories.  
- Achieved **69.77% accuracy** using **VGG16**, ensuring reliable classification.  
- Initially trained on **InceptionV3** with **90.34% accuracy**, but VGG16 provided more accurate results in real-world testing.  

---

## **Dataset**  
- The dataset consists of **filtered waste images** categorized into **9 different waste types**.  
- Hosted on **Google Drive** for easy access.  
- [Click here to access the dataset](https://drive.google.com/drive/folders/1CTvT_gnTvwlcKwJ8yz4jUOs0JYTKrplA?usp=sharing).  

---

## **Demo 🚀**  
The project is **deployed on AWS Elastic Beanstalk**.  
🔗 **Live Demo:** [Waste Recycling Classifier](http://wasterecycling-env.eba-xcpktyd2.us-east-2.elasticbeanstalk.com/)  

![Demo](readme_resources/projectDemo.gif)  

---

## **How to Use?**  
1. **Upload an image** of the waste item.  
2. **Click "Classify Your Waste Material"** to identify the waste type.  
3. The system will provide **detailed information** about the waste and proper disposal methods.  

---

## **Technologies Used 💻**  
- **Python** 🐍  
- **Flask** 🔥  
- **AWS Elastic Beanstalk** ☁️  
- **TensorFlow & Keras** 🧠  
- **VGG16 Transfer Learning** 🎯  
- **NumPy, Matplotlib, Pandas** 📊  
- **Bootstrap, HTML, CSS, JavaScript** 🎨  

---

## **Deployment Guide (AWS Elastic Beanstalk)**  
### **Setup Configuration**  
1. **Create a `.ebextensions` folder** in the main directory.  
2. **Inside `.ebextensions`, create a `python.config` file** and define configuration settings.  
3. **Create a `.ebignore` file** to exclude unnecessary files during deployment.  

### **Deploying on Elastic Beanstalk**  
1. Open **AWS Elastic Beanstalk Console**:  
   [AWS Beanstalk Console](https://console.aws.amazon.com/elasticbeanstalk/home#/gettingStarted?applicationName=getting-started-app)  
2. **Enter the application name**.  
3. **Choose Platform** → Select **Python (v3.8)**.  
4. **Upload a ZIP file** containing your project.  
5. Click **Create Application** → AWS will handle deployment automatically.  

---

## **Motivation 💡**  
With increasing environmental challenges, **waste management** and **recycling awareness** are critical. This project is designed to help **educate people** and **encourage sustainable waste disposal habits**.  

---

## **Contributors ✨**  
👤 **Abhishek Pal**  
🔗 [GitHub](https://github.com/Abhi0pal) | [LinkedIn](https://www.linkedin.com/in/abhishek-pal/)  

---

## **Support & Credits**  
If you find this project helpful, please ⭐ **star the repository** on GitHub!  
