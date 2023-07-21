# Machine learning based approach to predicate bandgap and efficiency of perovskite solar cells

The ability to predict the bandgaps and efficiency of perovskite solar cells rapidly and accurately is of practical interest for a range of applications. However, conventional experimental and theoretical methods for determining these parameters are often costly and time-intensive, making accurate predictions a critical yet challenging problem. A machine learning-based approach offers a promising and computationally efficient means to address this problem. In this study, we trained different machine learning models on past reported experimental data to accomplish this. Among the different ML models, the CatBoostRegressor performed better for both bandgap and efficiency approximation. We evaluated the proposed model using k-fold cross-validation and used Shapley Additive Explanations (SHAP) to inspect the relative importance of input features. Our findings show that machine learning-based approaches can provide a promising and computationally efficient means for accurate and rapid prediction of perovskite solar cell properties.

# Data flow diagram
![Abstract](https://user-images.githubusercontent.com/94437138/236134410-b1a78779-1bb7-48c3-97f1-a6f561c68abf.png)

# Results 
![resultsMain](https://github.com/AsadKhanJBNU/perovskite_bandgap_and_efficiency/assets/94437138/e2118052-c8a8-450c-aac4-8f38281a1c55)
![FoldsR2Bandgap](https://github.com/AsadKhanJBNU/perovskite_bandgap_and_efficiency/assets/94437138/6e37edc5-6608-408c-8f72-5c5355e1fdf7)


# Dummy dataset
We also generated a dummy dataset of millions of data points with random values for a_ions (Cs, FA, MA), b_ions (Pb, Sn), c_ions (Br, I), and the thickness of perovskite layer. We then used our proposed model to predict the bandgap values of these samples. After predicting the bandgaps for all the samples, we selected 500 samples that had high bandgap values. These samples are now available for further experimentation and analysis on the following csv file
[Top_500_prediction.csv](https://github.com/AsadKhanJBNU/perovskite_bandgap_and_efficiency/files/11888539/Top_500_prediction.csv)


# Web-server
In this paper, we provide a web-server tool that we have built to help researchers to calculate the bandgap and efficiency of PSCs. Access to the tool is available at https://nsclbio.jbnu.ac.kr/tools/bandgap. We make a step-by-step guide on using this web-server effectively to simplify things for users.<br>
•	The input to the web-server can be given directly in the text box. <br>
•	a_ions 'Cs', 'FA', 'MA' - note that the sum of these 3 inputs should be equal to 1.<br>
•	b_ions 'Pb', 'Sn' - note that the sum of these 2 inputs should be equal to 1.<br>
•	c_ions 'Br', 'I' - note that the sum of these 2 inputs should be equal to 3.<br>
•	The last input text box is the thickness in Nanometer (nm).

# Requirements
•	Python <br>
•	Numpy <br>
•	sklearn <br>
•	catboost <br>

# Developer
Asad Khan (Contact asadkhan@jbnu.ac.kr)
