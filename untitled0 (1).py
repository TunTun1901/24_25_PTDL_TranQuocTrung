import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu ngẫu nhiên
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.randn(100) * 0.5

# Tạo biểu đồ với matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, marker='o', linestyle='-', color='b', label='Random Data')
ax.set_title('Biểu đồ ngẫu nhiên với dữ liệu tạo ra ngẫu nhiên')
ax.set_xlabel('X values')
ax.set_ylabel('Y values')
ax.legend()
ax.grid(True)

# Sử dụng Streamlit để hiển thị biểu đồ
st.title("Biểu đồ ngẫu nhiên với Streamlit")
st.write("Biểu đồ được vẽ bằng matplotlib và hiển thị trên Streamlit")
st.pyplot(fig)
