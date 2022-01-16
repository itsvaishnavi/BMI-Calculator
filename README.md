# BMI-Calculator
This is a Flask project to calculate the BMI(Body Mass Index).

# Cloning the project from GitHub:
Step 1: Using the Git CLI, copy the following command:

git clone https://github.com/itsvaishnavi/BMI-Calculator.git

To download git, visit https://git-scm.com/downloads

Step 2: Form the docker image from the docker file using the folowing command:

# docker build -t bmi_image .

Step 3: Run the docker image

# docker run -p 5000:5000 bmi_image

To run the docker image in detached mode:
**# docker run -d -p 5000:5000 bmi_image**

Open the browser and browse localhost:5000. This should open the window as shown below:

![image](https://user-images.githubusercontent.com/61691914/149667911-888dffd0-b8ae-4845-9929-0495d4709f0c.png)
