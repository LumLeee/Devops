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
├── .env                # Biến môi trường (PORT, Database credentials, Student Info)
├── docker-compose.yml  # File điều phối 3 container
└── summary.md          # File này
```

## 2. Tính Năng Đã Triển Khai

| Yêu Cầu | Trạng Thái | Mô Tả |
| :--- | :---: | :--- |
| **Backend API** | ✅ | GET `/about` và `/health`. |
| **Frontend UI** | ✅ | Giao diện điều hướng tới các tính năng của hệ thống. |
| **Database** | ✅ | Sử dụng MySQL 8.0 để lưu trữ thông tin sinh viên (`StudentProfile`). |
| **Trang /about** | ✅ | Hiển thị: Họ tên, MSSV, Lớp (được lấy trực tiếp từ Database). |
| **Health Check** | ✅ | Endpoint `/health` trả về `{ "status": "ok" }`. |
| **Docker** | ✅ | Có Dockerfile cho từng phần và `docker-compose.yml`. |
| **Git History** | ✅ | Danh sách nhiều commit rõ ràng và 3 branch (`main`, `develop`, `feature`). |

## 3. Hướng Dẫn Chạy Project

### Bước 1: Khởi động hệ thống
Run lệnh sau tại thư mục gốc:
```bash
docker-compose up -d --build
```

### Bước 2: Chạy Migrations (Bắt buộc lần đầu)
Sau khi các container đã UP (vui lòng đợi ~10-20 giây cho MySQL khởi động xong), chạy lệnh sau:
```bash
docker-compose exec backend python manage.py makemigrations core
docker-compose exec backend python manage.py migrate
```

### Bước 3: Khởi tạo dữ liệu mẫu vào DB
Chạy lệnh sau để thêm thông tin sinh viên từ file `.env` vào Database:
```bash
docker-compose exec backend python manage.py shell -c "from core.models import StudentProfile; import environ; env = environ.Env(); StudentProfile.objects.update_or_create(student_id=env('STUDENT_ID'), defaults={'fullname': env('STUDENT_NAME'), 'class_name': env('STUDENT_CLASS')})"
```

### Bước 4: Truy cập
- **Frontend (Giao diện chính)**: [http://localhost:3000/](http://localhost:3000/)
- **Trang Thông Tin Cá Nhân (Lấy từ DB)**: [http://localhost:8000/about](http://localhost:8000/about)
- **Health Check**: [http://localhost:8000/health](http://localhost:8000/health)

## 4. Kiểm tra dữ liệu trong DB
Bạn có thể kiểm tra dữ liệu trực tiếp trong database bằng cách truy cập vào container DB:
```bash
docker-compose exec db mysql -u root -prootpassword student_db -e "SELECT * FROM core_studentprofile;"
```

## 5. Lịch Sử Git (Git History)
Bạn có thể kiểm tra danh sách commit bằng lệnh:
```bash
git log --oneline --graph --all
```
Các nhánh hiện có: `main`, `develop`, `feature/initial-setup`.
