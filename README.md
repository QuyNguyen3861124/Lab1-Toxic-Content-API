# Bài Thực Hành 1: Hệ Thống Web API Kiểm Duyệt Nội Dung (Toxic Content Detection)

## 1. Thông tin sinh viên
* **Họ và tên:** Nguyễn Lê Ngọc Quý
* **MSSV:** 24120422
* **Môn học:** Tư duy tính toán - Trường ĐH Khoa Học Tự Nhiên (KHTN), ĐHQG-HCM

## 2. Thông tin mô hình
* **Tên mô hình:** `unitary/toxic-bert`
* **Nền tảng:** Hugging Face
* **Đường dẫn:** [https://huggingface.co/unitary/toxic-bert](https://huggingface.co/unitary/toxic-bert)
* **Mô tả chức năng:** Mô hình này được Fine-tune từ kiến trúc BERT, có khả năng đọc hiểu văn bản tiếng Anh và phân loại xem văn bản đó có chứa các nội dung độc hại, chửi bậy, đe dọa hay xúc phạm hay không. Hệ thống API này ứng dụng mô hình để tự động kiểm duyệt bình luận của người dùng.

## 3. Hướng dẫn cài đặt
Để chạy hệ thống trên máy tính cá nhân, yêu cầu cài đặt Python và thực hiện các bước sau:

**Bước 1:** Clone repository này về máy.

**Bước 2:** Cài đặt các thư viện cần thiết thông qua file `requirements.txt`:
```bash
pip install -r requirements.txt
```
*(Các thư viện chính bao gồm: fastapi, uvicorn, transformers, torch, omegaconf, requests).*

## 4. Hướng dẫn chạy chương trình
Mở terminal tại thư mục chứa mã nguồn và chạy lệnh sau để khởi động FastAPI Server:
```bash
uvicorn main:app --reload --port 8000
```
Sau khi khởi động, bạn có thể truy cập tài liệu API tự động (Swagger UI) tại: `http://127.0.0.1:8000/docs`

## 5.Ví dụ

Hệ thống cung cấp 3 endpoint chính:
* `GET /`: Xem thông tin giới thiệu hệ thống.
* `GET /health`: Kiểm tra trạng thái hoạt động của Server.
* `POST /predict`: Dự đoán mức độ độc hại của văn bản.

**Ví dụ:**

```python
import requests

url = "[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)"

# 1. Gửi một câu bình luận lịch sự
response = requests.post(url, params={"message": "I love this application, it is very helpful!"})
print("Test 1:", response.json())

# 2. Gửi một câu chửi thề/độc hại
response_toxic = requests.post(url, params={"message": "You are a stupid and toxic idiot!"})
print("Test 2:", response_toxic.json())
```

### Triển khai Public API
Hệ thống hỗ trợ public ra Internet thông qua đường hầm **Localtunnel** hoặc **Pinggy** để giả lập môi trường Cloud thực tế.

**Ví dụ test qua Public API bằng file `test_api.py`:**
```python
import requests

# Link thay đổi linh hoạt tùy theo phiên chạy của Localtunnel/Pinggy
PUBLIC_URL = "https://[LINK-PUBLIC-CỦA-BẠN]"
API_URL = f"{PUBLIC_URL}/predict"

# Gửi request với header bypass của Localtunnel
response = requests.post(
    API_URL, 
    params={"message": "You are a stupid and toxic idiot!"},
    headers={"Bypass-Tunnel-Reminder": "true"}
)

print("Kết quả từ Internet:", response.json())
```
# 6. Video Demo Hệ Thống
* **Link Video Demo:** https://drive.google.com/drive/folders/1kp_PKBTid2sU3dIQkZt9mCrL3qzPs8MW?usp=sharing
