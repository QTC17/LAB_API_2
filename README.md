# 📝 Simple Note Application - Lab API 2

Dự án này là một ứng dụng ghi chú đơn giản được xây dựng theo kiến trúc **Client-Server**. 

## 🏗 Cấu trúc thư mục
project/
├── frontend/        # Ứng dụng giao diện người dùng (Streamlit)
│   └── app.py
├── backend/         # API Server (FastAPI)
│   ├── main.py
│   └── serviceAccountKey.json (Firebase Key)
├── requirements.txt # Danh sách thư viện cài đặt
└── README.md        # Hướng dẫn sử dụng
🚀 Các tính năng chính
Xác thực người dùng: Đăng nhập và nhận diện thông qua Email (Tích hợp Firebase Auth).

Thêm ghi chú: Người dùng nhập nội dung và gửi request đến Backend.

Lưu trữ dữ liệu: Backend tiếp nhận và lưu trữ ghi chú.

Hiển thị danh sách: Đọc dữ liệu từ Backend và hiển thị lại lên giao diện.

🛠 Công nghệ sử dụng
Frontend: Streamlit

Backend: FastAPI

Database: Firebase Admin SDK (Giả lập mảng dữ liệu)

Ngôn ngữ: Python 3.10+

📥 Hướng dẫn cài đặt
Cài đặt các thư viện cần thiết:
Mở terminal tại thư mục gốc và chạy:

Bash
pip install -r requirements.txt
(Hoặc cài lẻ: pip install fastapi uvicorn streamlit requests firebase-admin)

Cấu hình Firebase:
Đảm bảo file JSON của Firebase Service Account đã được đặt trong thư mục backend/.

🏃 Cách chạy ứng dụng
Bạn cần chạy đồng thời cả Backend và Frontend trên 2 cửa sổ Terminal riêng biệt:

Bước 1: Khởi động Backend (Port 8000)
Bash

cd Backend

python -m uvicorn Backend.main:app --reload

Kiểm tra trạng thái tại: http://127.0.0.1:8000/health
Kiểm tra dữ liệu ở backend : http://127.0.0.1:8000/notes
Bước 2: Khởi động Frontend (Port 8501)
Mở terminal mới:

Bash

cd Frontend

python -m streamlit run Frontend/app.py

Ứng dụng sẽ tự động mở tại: http://localhost:8501

📺 Video Demo
Link : https://drive.google.com/drive/folders/1XvPyCZAdhmrVW-rIn2dP7KpuS5k6vYiI?usp=sharing
