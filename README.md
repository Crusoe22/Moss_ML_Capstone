# Moss_ML_Capstone

**Directional Forecasting of the NASDAQ Index with Machine Learning**  
**Author:** Nolan Moss  
**Date:** July 8, 2025  
**University:** Northwest Missouri State University, Maryville MO  
**Email:** s573653@nwmissouri.edu, nolanmmoss@gmail.com  
**GitHub:** [Moss_ML_Capstone](https://github.com/Crusoe22/Moss_ML_Capstone)  
**Overleaf Report:** [Capstone Report](https://www.overleaf.com/read/jcwythzsmyxw#6fd6b9)

This project forecasts daily directional movements (up/down) in the NASDAQ index using historical price data and sentiment analysis from Reddit posts. The final model combines traditional financial indicators with natural language processing (NLP) of social media content.


## Overview

Many investors and analysts seek ways to better anticipate market direction, especially in a technology-heavy index like the NASDAQ. This project aims to build a predictive model using a combination of:

- Historical NASDAQ price and volume data (via Yahoo Finance)
- Reddit sentiment extracted from user posts on r/WallStreetBets
- Feature engineering to extract signals like moving averages, price ratios, and text polarity scores

By integrating financial and social media data, this project explores how online investor sentiment may influence market behavior.

---

## Methodology

- **Data Collection**  
  - Price data from Yahoo Finance  
  - Reddit posts sourced from r/WallStreetBets

- **Preprocessing**  
  - Cleaned and merged sentiment and financial data on a daily level  
  - Engineered rolling indicators (SMA, price change %, ratios)  
  - Used `SpaCyTextBlob` for sentiment scoring (polarity, subjectivity)

- **Model Training**  
  - Random Forest Classifier with `TimeSeriesSplit` to preserve temporal order  
  - Binary classification: predict whether the NASDAQ will go up (1) or down (0) the next day  
  - Evaluated using directional accuracy and feature importance

---

## Results

- The best-performing model achieved approximately **52% accuracy** in predicting daily direction.
- Sentiment polarity scores showed a **weak but consistent correlation** with market direction.
- Price momentum features (e.g., 3-day and 7-day moving averages) had the highest predictive importance.
- Reddit sentiment did not drastically improve prediction performance but added valuable signal in certain periods.
- Visualizations supported model interpretability and highlighted temporal trends in sentiment and market behavior.

---

## Limitations and Future Work

- The model uses **daily data**, which misses intraday fluctuations and rapid sentiment shifts.
- Sentiment analysis was limited by the **context-insensitivity** of the SpaCyTextBlob tool.
- Reddit post data only covered a portion of the timeline, reducing the volume of training examples.
- Future work could incorporate:
  - More advanced NLP models 
  - Real-time or intraday sentiment and price data
  - Alternative models or deep learning

---
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





