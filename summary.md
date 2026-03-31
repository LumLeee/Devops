# Hướng Dẫn Đồ Án DevOps - Hệ Thống Quản Lý Thông Tin Sinh Viên

Dự án này được xây dựng theo các yêu cầu của bài tập DevOps, bao gồm Backend (Django), Frontend (Nginx), và Database (MySQL) chạy trong các container riêng biệt.

## 1. Cấu Trúc Dự Án
```text
/
├── backend/            # Django Application
│   ├── core/           # Logic chính (API, Models, Views)
│   ├── Dockerfile      # Docker build cho Backend
│   └── requirements.txt
├── frontend/           # Nginx & Static Files
│   ├── index.html      # Giao diện tương tác
│   └── Dockerfile      # Docker build cho Frontend
├── .env                # Biến môi trường (PORT, DB, Student Info)
├── docker-compose.yml  # File điều phối 3 container
└── summary.md          # File này (Nếu bạn muốn lưu lại trong repo)
```

## 2. Tính Năng Đã Triển Khai

| Yêu Cầu | Trạng Thái | Mô Tả |
| :--- | :---: | :--- |
| **Backend API** | ✅ | 2 API: GET `/api/messages` và POST `/api/messages`. |
| **Frontend UI** | ✅ | Hiển thị lời nhắn từ backend và có form nhập liệu. |
| **Database** | ✅ | Sử dụng MySQL 8.0 để lưu trữ dữ liệu thực tế thực thụ. |
| **Route /about** | ✅ | Hiển thị: Họ tên, MSSV, Lớp (lấy từ `.env`). |
| **Health Check** | ✅ | Endpoint `/health` trả về `{ "status": "ok" }`. |
| **Docker** | ✅ | Có Dockerfile cho từng phần và `docker-compose.yml`. |
| **Git History** | ✅ | Danh sách ≥ 5 commit và 3 branch (`main`, `develop`, `feature`). |

## 3. Hướng Dẫn Chạy Project

### Bước 1: Khởi động hệ thống
Run lệnh sau tại thư mục gốc:
```bash
docker-compose up -d --build
```

### Bước 2: Chạy Migrations (Bắt buộc lần đầu)
Sau khi các container đã UP (vui lòng đợi ~1-2 phút cho MySQL khởi động xong), chạy lệnh sau:
```bash
docker-compose exec backend python manage.py makemigrations core
docker-compose exec backend python manage.py migrate
```

### Bước 3: Truy cập
- **Frontend (Giao diện chính)**: [http://localhost/](http://localhost/)
- **Thông tin cá nhân**: [http://localhost:8000/about](http://localhost:8000/about)
- **Health Check**: [http://localhost:8000/health](http://localhost:8000/health)
- **API Messages**: [http://localhost:8000/api/messages](http://localhost:8000/api/messages)

## 4. Docker Hub (Build & Push)
Để đẩy ảnh lên Docker Hub, bạn có thể thực hiện theo các lệnh sau (thay `yourusername` bằng username của bạn):

1. **Login**: `docker login`
2. **Build & Tag**:
   - `docker build -t yourusername/student-backend ./backend`
   - `docker build -t yourusername/student-frontend ./frontend`
3. **Push**:
   - `docker push yourusername/student-backend`
   - `docker push yourusername/student-frontend`

## 5. Lịch Sử Git (Git History)
Danh sách các nhánh: `main`, `develop`, `feature/initial-setup`.
Các commit message đều rõ ràng và đúng quy chuẩn assignment.
