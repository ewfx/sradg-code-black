# 🚀 CODE BLACK
Smarter Reconciliation and Anomaly detection using Gen AI

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [What It Does](#what-it-does)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
This project is designed to enhance financial reconciliation by leveraging AI-driven anomaly detection. Businesses process a huge number of transactions daily, and identifying mismatches (or breaks) manually is tedious and error-prone. Our solution integrates Large Language Models (LLMs) with historical data to automate anomaly detection, classify break reasons, and provide insights—reducing manual effort and improving accuracy.

We are addressing the Hackathon Problem Statement that focuses on:
- Automatically detecting anomalies in reconciliation data
- Providing insights on potential root causes using historical trends
- Minimizing manual intervention with AI-generated explanations

Our system processes real-time transactions, compares them against historical records, and explains anomalies efficiently. It is built using Mistral 7B, running locally on Ollama, and designed to be modular for future improvements. 🚀

## 🎥 Demo
📹 [Video Demo](/artifacts/demo/demo.mp4) 

## ⚙️ What It Does

Our **AI-powered reconciliation anomaly detection system** automates the process of identifying and explaining mismatches in financial transactions. It leverages **historical data and real-time inputs** to detect anomalies and provide meaningful insights.  

### 🔹 **Key Features & Functionalities**  

- **🚀 Real-Time Anomaly Detection** – Compares each new transaction against historical data to determine if it's an anomaly.  

- **📊 Historical Data Analysis** – Reads past records related to the same entity set to understand patterns and trends.  

- **🤖 LLM-Powered Explanations** – Uses **Mistral 7B** to generate detailed insights on **why** a record is flagged as an anomaly.  

- **🔧 Modular & Scalable** – Designed for easy model switching (e.g., Mistral → LLaMA, GPT, etc.), making it adaptable for future enhancements.  

By automating anomaly detection and classification, our system significantly **reduces manual workload**, **enhances accuracy**, and **streamlines financial reconciliation workflows**. 🚀

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/your-repo.git
   ```
2. Install the model 
   - Install Ollama tool in the machine from https://ollama.com/
   - Install Mistral model locally 
   ```
   ollama pull mistral
   ```
3. Install Dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook app.ipynb to demo the application

## 🏗️ Tech Stack
- 🔹 Python

## 👥 Team
- **Kaushik Parthasarathy**
- **Shreya Mittal**
- **Piyush Patel**
- **Surbhi Sinha**