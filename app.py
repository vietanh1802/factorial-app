import streamlit as st
from factorial import fact


st.title ("Ứng dụng Tính Toán Cơ Bản")

# Đặt tiêu đề phụ
st.header("Tính Giai Thừa của Một Số Tự Nhiên")

# Đoạn mô tả
st.write("Ứng dụng này cho phép bạn tính giai thừa của một số tự nhiên. Vui lòng nhập số cần tính giai thừa vào ô dưới đây và nhấn nút 'Calculate'.")

def main():
    st.title ("Factorial Calculator")
    number = st.number_input ("Enter a number :", min_value = 0, max_value = 900)

    if st.button("Calculate"):
        result = fact(number)
        st.write (f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()