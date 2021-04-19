# Azure ML Nanodegree Capstone Project - Breast Cancer Prediction 

Worldwide, breast cancer is the most common type of cancer in women and the second highest in terms of mortality rates.Diagnosis of breast cancer is performed when an abnormal lump is found (from self-examination or x-ray) or a tiny speck of calcium is seen (on an x-ray). After a suspicious lump is found, the doctor will conduct a diagnosis to determine whether it is cancerous and, if so, whether it has spread to other parts of the body. This breast cancer dataset was obtained from the University of Wisconsin Hospitals, Madison from Dr. William H. Wolberg. Machine learning is helpful in predicting the basic detection of cancer development.

Dataset is imported to Azure ML studio and two models are trained to obtain the best model. 1. AutoML - produces the various model using Azure SDK and 2. Hyperdrive - Logistic Regression using scikit-learn. Best model is picked based on accuracy and deployed. 


## Dataset

### Overview
Breast cancer prediction dataset is taken from Kaggle. It describes the various clinical observations which helps in determining if cancer cell is predicted. It consists of 570 entries with 6 columns of physical observation values.

### Task
The first five columns contain different physical features of cells. These five columns contain float values. The sixth column is the target column or dependent variable. It is a binary variable containing 1 and 0 as values where 1 means cancerous cell and 0 means non-cancerous cell. Column details are given below:

mean_radius: mean radius value of the cell (decimal value)
mean_texture: mean texture value of the cell (decimal value)
mean_perimeter: mean perimeter of the cell (decimal value)
mean_area: mean area of the cell (decimal value)
mean_smoothness: mean smoothness value of the cell (decimal value)
diagnosis: diagnosis result or target variable (0/1)

### Access
The dataset is pushed into my github repo of this particular project and is registered in Azure ML studio. Same public link is used in the scripts using Python SDK. 
![0  Dataset-push](https://user-images.githubusercontent.com/76555474/115310324-3fedb080-a18b-11eb-858d-e16488f5dfc9.png)
![1  Dataset](https://user-images.githubusercontent.com/76555474/115310330-43813780-a18b-11eb-8f2c-0bb20ec7fab5.png)


## Automated ML
The AutoML run is configured as:
![2  AutoML-config](https://user-images.githubusercontent.com/76555474/115310457-76c3c680-a18b-11eb-8b68-51b0ee0f9b0a.png)
Task type is chosen as Classification as this particular breast cancer problem is binary classification prediction. 
Experiment timeout minutes is chosen as 30 with maximum concurrent iterations as 5. Accuracy is taken as primary metric. 
Diagnosis column is the target column and early stopping policy is enabled. 
With 'auto' featurization - scaling and normalization of the dataset was enabled automatically. Error logs were captured for debugging purpose.

### Results
Best run is produced from Voting Ensemble with 93.84% accuracy.
![9  AutoML-run-complete](https://user-images.githubusercontent.com/76555474/115311126-bccd5a00-a18c-11eb-984d-93fcbfcfa6dc.png)
![10  AutoML-run-details](https://user-images.githubusercontent.com/76555474/115311139-c35bd180-a18c-11eb-965f-92fc25a80e71.png)
Details of Runwidget in notebook script
![11  AutoML-runwidget](https://user-images.githubusercontent.com/76555474/115311200-dff80980-a18c-11eb-884b-4678ab72e8d4.png)
![12  AutoML-runwidget-models](https://user-images.githubusercontent.com/76555474/115311213-e38b9080-a18c-11eb-952e-6fa63e0b852d.png)
Best model is picked up
![13  AutoML-bestmodel](https://user-images.githubusercontent.com/76555474/115311247-f69e6080-a18c-11eb-83a2-c04643b94167.png)
Areas to improve include imrpoving accuracy and increasing experiment timeout minutes.

## Hyperparameter Tuning
Logistic Regression is chosen as it is simple to train and the target variable is linearly separable using the input features.
Hyperdrive run is configured as
![3  HD-policy-sampling](https://user-images.githubusercontent.com/76555474/115311639-9c51cf80-a18d-11eb-9882-452793d0044f.png)
Bandit policy is chosen as early termination policy and Random parameter sampling with C(inverse of regularization strength) and maximum iterations as hyperparaments tuned.
![4  HD-config](https://user-images.githubusercontent.com/76555474/115311844-f5216800-a18d-11eb-9f93-8ba09d5e4530.png)


### Results
Best model with 93.70% accuracy is produced. The hyperparameters tuned as C = 10 and maximum iterations as 100.
![8  HD-bestmodel](https://user-images.githubusercontent.com/76555474/115312047-46315c00-a18e-11eb-8025-d4a60aa63fa6.png)
Snippets of run completion
![5  HD-run-complete](https://user-images.githubusercontent.com/76555474/115312070-50ebf100-a18e-11eb-8fb1-dd3ffd0810ef.png)
![6  HD-run-details](https://user-images.githubusercontent.com/76555474/115312148-724cdd00-a18e-11eb-8d40-59010bb628f6.png)
RunWidget snippets from notebook script
![7  HD-runwidget](https://user-images.githubusercontent.com/76555474/115312177-80026280-a18e-11eb-9e25-ce6de836d23b.png)
Areas to improve include choosing different hyperparameters, removing early termination policy.


## Model Deployment
As AutoMl produced the best model with 93.84% accuracy as compared to Hyperdrive 93.70% accuracy, Voting Ensemble from AutoML tun is chosen to deploy the model.
![14  AutoML-model-conda](https://user-images.githubusercontent.com/76555474/115312470-0323b880-a18f-11eb-987a-2409b1d6e9b0.png)
![15  AutoML-model-deploy](https://user-images.githubusercontent.com/76555474/115312473-06b73f80-a18f-11eb-9998-98580367124d.png)
Endpoint is consumed 
![16  AutoMl-model-scoringURI](https://user-images.githubusercontent.com/76555474/115312561-2d757600-a18f-11eb-880d-89e0633e0cec.png)
![17  AutoMl-model-endpoint](https://user-images.githubusercontent.com/76555474/115312577-323a2a00-a18f-11eb-86a8-b00367d35689.png)


## Screen Recording
Find the below link for screen recording of the demonstration of the project https://youtu.be/nluCovPHImY

## Standout Suggestions
1. AutoML and Hyperdrive models have been used to produce best model for prediction of breast cancer cells.
