---
title: "Integrating YOLO Fire Detection with FastAPI and Next.js 🔥"
slug: "integrating-yolo-fire-detection-with-fastapi-and-nextjs"
author: "Abdullah Javed"
source: "devto_python"
published: "Tue, 27 Oct 2026 11:42:55 +0000"
description: "A practical walkthrough of setting up FlameGuard, connecting a custom YOLO model, and debugging a full-stack Computer Vision application. Introduction I rece..."
keywords: "detection, model, backend, yolo, fire, flameguard, application, fastapi"
generated: "2026-10-27T11:53:35.652449"
---

# Integrating YOLO Fire Detection with FastAPI and Next.js 🔥

## Overview

A practical walkthrough of setting up FlameGuard, connecting a custom YOLO model, and debugging a full-stack Computer Vision application. Introduction I recently explored FlameGuard , an open-source fire detection application built with YOLO, FastAPI, and Next.js. I wanted to understand how a trained object detection model works inside a complete web application. I used the original FlameGuard repository and adapted it to work with my own trained fire detection model. Here's a breakdown of the implementation and what I learned. Tech Stack Technology Purpose Python Backend development YOLO Fire detection OpenCV Image processing FastAPI REST API SQLite Detection history Next.js Frontend React User interface Conda Dependency management 1. Project Setup Clone the repository: git clone https://github.com/nohsangwoo/FlameGuard.git cd FlameGuard The main project structure is: FlameGuard/ ├── backend/ │ ├── app/ │ └── environment.yml ├── frontend/ └── README.md Create the Python environment: cd backend conda env create -f environment.yml conda activate flameguard 2. Integrating the YOLO Model I already had a trained fire detection model named best.pt . The model contains one detection class: { 0 : " fire " } I placed the model in the backend's assets directory and configured the detection endpoint to use it. from pathlib import Path from ultralytics import YOLO APP_DIR = Path ( __file__ ). resolve (). parents [ 2 ] MODEL_PATH = APP_DIR / " assets " / " best.pt " model = YOLO ( str ( MODEL_PATH )) Loading the model outside the API handler avoids repeatedly initializing it for each request. 3. Running Fire Detection The prediction process uses the YOLO model to analyze an uploaded image. results = model . predict ( source = str ( temp_file_path ), conf = 0.25 , imgsz = 640 ) result = results [ 0 ] We can extract detection information: for box in result . boxes : class_id = int ( box . cls . item ()) class_name = model . names [ class_id ] confidence = float ( box . conf . item ()) bbox = box . xyxy [ 0 ]. tolist () print ( class_name , confidence , bbox ) Each detection includes a predicted class, confidence score, and bounding-box coordinates. 4. Creating Annotated Images Ultralytics provides a convenient method for drawing predicted bounding boxes: annotated_img = result . plot () The annotated image can then be saved using OpenCV: import cv2 cv2 . imwrite ( str ( log_file_path ), annotated_img ) These images can be used by the frontend to display detection results. 5. FastAPI Integration The backend exposes a prediction endpoint: POST /predict_fire It receives an uploaded image, processes it with YOLO, and returns a structured detection response. For example, one of my tests returned: { "message" : "fire detected" , "file_name" : "frame.jpg" , "detections" : [ { "class_name" : "fire" , "confidence" : 0.419 } ] } The API can also store detection information in SQLite for later retrieval. 6. Debugging Detection Images One issue I encountered was that the backend returned successful predictions, but detection images were missing. The logs showed: POST /predict_fire 200 OK GET /log/image.jpg 404 Not Found I investigated the image-saving and static-file directory paths. Using pathlib helped keep the paths consistent: from pathlib import Path APP_DIR = Path ( __file__ ). resolve (). parents [ 2 ] LOG_DIR = APP_DIR / " log " LOG_DIR . mkdir ( parents = True , exist_ok = True ) This was a useful lesson in handling generated files inside FastAPI applications. 7. Running the Backend From the backend directory: python -m uvicorn app.main:app --reload The backend runs at: http://localhost:8000 API documentation: http://localhost:8000/docs 8. Running the Next.js Frontend Open another terminal: cd frontend pnpm install pnpm run dev The frontend runs at: http://localhost:3000 The interface communicates with the FastAPI backend to process images and retrieve detection results. 9. Handling Camera Errors During testing, I encountered a browser error related to: navigator . mediaDevices . enumerateDevices () A simple feature check helps prevent the application from crashing when the browser camera API is unavailable: if ( ! navigator . mediaDevices ?. enumerateDevices ) { console . warn ( " Camera API unavailable " ); return ; } const devices = await navigator . mediaDevices . enumerateDevices (); Browser permissions and secure-context requirements are important when working with camera-based applications. 10. Lessons Learned This project helped me better understand: YOLO inference and detection results. FastAPI integration with Computer Vision models. Image annotation and file management. SQLite detection logging. Next.js and backend communication. Debugging missing images and browser camera errors. Organizing a full-stack AI application. Future Improvements I plan to explore better detection accuracy, improve frontend interactions, test more challenging images, and make the application more reliable for continuous monitoring. The current project is a learning experiment rather than a production-ready fire safety system. Conclusion Working on FlameGuard was a valuable opportunity to connect Computer Vision concepts with full-stack application development. It also reminded me that a trained AI model is only one part of a complete application. There is much more to explore, and I look forward to improving my understanding through more practical projects. Original project: FlameGuard by nohsangwoo GitHub: github.com/abdullahjave Thanks for reading!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/abdullah_javed_287f38c45e/integrating-yolo-fire-detection-with-fastapi-and-nextjs-19k1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
