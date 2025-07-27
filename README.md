# Moss_ML_Capstone

**Directional Forecasting of the NASDAQ Index with Machine Learning**  
Author: Nolan Moss  
Date: July 8, 2025  

This project forecasts daily directional movements (up/down) in the NASDAQ index using historical price data and sentiment analysis from Reddit posts. The final model combines traditional financial indicators with natural language processing (NLP) of social media content.

---

## Key Features
- Historical data extraction via yfinance
- Feature engineering with rolling indicators
- Binary classification using RandomForestClassifier
- TimeSeriesSplit cross-validation
- Sentiment analysis of Reddit posts using SpaCyTextBlob
- Correlation analysis and performance visualizations

---

## Project Setup
### 1. **Create a Virtual Environment**  
From your project root directory:

```bash
py -m venv .venv


## Create Project Virtual Environment

```shell

py -m venv .venv
.venv\Scripts\Activate

```
3. Requirements
- Install packages 
```console
py -m pip install -r requirements.txt
```
- Freeze your requirements to requirements.txt. 
```console
py -m pip install requests
py -m pip freeze > requirements.txt
```

## Git add and commit 

```shell
git add .
git commit -m "add .gitignore, readme, and requirements"
git push origin main
```


**Author:** Nolan Moss  
**Date:** July 8, 2025  
**University:** Northwest Missouri State University, Maryville MO  
**Email:** s573653@nwmissouri.edu, nolanmmoss@gmail.com  
**GitHub:** [Moss_ML_Capstone](https://github.com/Crusoe22/Moss_ML_Capstone)  
**Overleaf Report:** [Capstone Report](https://www.overleaf.com/read/jcwythzsmyxw#6fd6b9)


