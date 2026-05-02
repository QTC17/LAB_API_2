import streamlit as st
import requests

st.set_page_config(page_title="HCMUS Note App", page_icon="📝")

st.title("📝 Ứng dụng Ghi chú (Lab API)")
st.info("Yêu cầu: Frontend kết nối Backend FastAPI")

with st.sidebar:
    st.header("Xác thực người dùng")
    email = st.text_input("Nhập Email của bạn:", value="MSSV@student.hcmus.edu.vn")
    if email:
        st.success(f"Đang dùng: {email}")


st.subheader("Thêm ghi chú mới")
content = st.text_area("Nội dung ghi chú:", placeholder="Viết gì đó vào đây...")

if st.button("Lưu ghi chú"):
    if content:
       
        payload = {"user_email": email, "content": content}
        try:
            
            res = requests.post("http://127.0.0.1:8000/notes", json=payload)
            if res.status_code == 200:
                st.success("✅ Đã lưu vào Database thành công!")
            else:
                st.error("❌ Lỗi Backend!")
        except:
            st.error("❌ Không kết nối được Backend. Bạn đã chạy lệnh uvicorn chưa?")
    else:
        st.warning("Vui lòng nhập nội dung!")

st.divider()

st.subheader("📚 Danh sách ghi chú đã lưu")
try:
    response = requests.get("http://127.0.0.1:8000/notes")
    if response.status_code == 200:
        data = response.json()
        if not data:
            st.write("Chưa có ghi chú nào.")
        for item in reversed(data): 
            with st.expander(f"Ghi chú từ: {item['user_email']}"):
                st.write(item['content'])
except:
    st.warning("Đang đợi kết nối từ Backend...")