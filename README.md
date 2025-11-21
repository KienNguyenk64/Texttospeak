
---

````markdown
# 🤖 Trợ Lý Ảo Python (Voice Assistant Mini)

Một con trợ lý ảo mini viết bằng Python, có khả năng:
- Nghe giọng nói qua microphone 🎤
- Hiểu các câu lệnh cơ bản 🧠
- Nói lại bằng giọng máy 🔊

Hoạt động liên tục cho tới khi bạn nói **"bye"**.

---

## 🚀 Tính năng

Hiện tại trợ lý hỗ trợ một số câu lệnh sau:

| Câu nói | Phản hồi |
|--------|---------|
| `Hello` | Robot chào lại |
| `today` | Đọc ngày hiện tại |
| `time` | Đọc giờ hiện tại |
| `bye` | Kết thúc chương trình |
| Nói không rõ | Robot báo nghe không được |

---

## 🧠 Nguyên lý hoạt động

Trợ lý gồm 3 bước chính:

1. 🎤 **Nghe:** Dùng `speech_recognition` để nhận giọng nói.
2. 🧠 **Xử lý:** Kiểm tra từ khóa (`Hello`, `today`, `time`, `bye`…).
3. 🔊 **Nói:** Dùng `pyttsx3` để phát lại bằng giọng nói.

---

## 📦 Cài đặt thư viện cần thiết

Trước tiên cài các thư viện sau:

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install pyaudio
````

⚠️ Nếu `pyaudio` bị lỗi, dùng:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ Cách chạy chương trình

1. Mở terminal.
2. Di chuyển vào thư mục chứa file.
3. Chạy:

```bash
python trolyao.py
```

Sau đó:

* Nói chuyện với micro.
* Robot sẽ trả lời lại bằng âm thanh.

---

## 📄 Code chính (Tóm tắt chức năng)

Chương trình:

* Nhận giọng nói.
* Xử lý từ khóa.
* Đọc lại kết quả bằng giọng nói.
* Tự thoát khi nghe thấy `"bye"`.

---

## 😎 Gợi ý nâng cấp trong tương lai

Nếu bạn muốn level-up con trợ lý này, có thể thêm:

* Điều khiển mở trình duyệt 🌍
* Phát nhạc 🎵
* Trả lời thời tiết ☁️
* Kết hợp ChatGPT API 🧠🔥

Con này mà làm tiếp là thành project xịn cho IT luôn chứ không đùa.

---

## 👨‍💻 Tác giả

* Dự án: Trợ Lý Ảo Python
* Ngôn ngữ: Python
* Mục đích: Học tập & thử nghiệm công nghệ nhận dạng giọng nói

```


