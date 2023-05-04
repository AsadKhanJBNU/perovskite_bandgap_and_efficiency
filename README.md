# Machine learning based approach to predicate bandgap and efficiency of perovskite solar cells

The ability to predict the bandgaps and efficiency of perovskite solar cells rapidly and accurately is of practical interest for a range of applications. However, conventional experimental and theoretical methods for determining these parameters are often costly and time-intensive, making accurate predictions a critical yet challenging problem. A machine learning-based approach offers a promising and computationally efficient means to address this problem. In this study, we trained different machine learning models on past reported experimental data to accomplish this. Among the different ML models, the CatBoostRegressor performed better for both bandgap and efficiency approximation. We evaluated the proposed model using k-fold cross-validation and used Shapley Additive Explanations (SHAP) to inspect the relative importance of input features. Our findings show that machine learning-based approaches can provide a promising and computationally efficient means for accurate and rapid prediction of perovskite solar cell properties.

# Data flow diagram
![Abstract](https://user-images.githubusercontent.com/94437138/236134410-b1a78779-1bb7-48c3-97f1-a6f561c68abf.png)

# Results 
![merge_from_ofoctNew](https://user-images.githubusercontent.com/94437138/236134654-7b1f07ba-cd90-469e-b035-7bb27d6cc4a7.jpg)
![5FoldsR2](https://user-images.githubusercontent.com/94437138/236134681-ffb5a061-edce-4225-94f3-bf83d5cc5ac1.png)

# Dummy dataset
In this study, we also generated a dummy dataset of millions of data points with random values for a_ions (Cs, FA, MA), b_ions (Pb, Sn), c_ions (Br, I), and the thickness of perovskite layer. We then used our proposed model to predict the bandgap values of these samples. After predicting the bandgaps for all the samples, we selected 500 samples that had high bandgap values. These samples are now available for further experimentation and analysis on the following csv file
[Top_500_prediction.csv](https://github.com/AsadKhanJBNU/perovskite_bandgap_and_efficiency/files/11394564/Top_500_prediction.csv)
