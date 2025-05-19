import pandas as pd
import numpy as np

# Đường dẫn tệp gốc
input_file_path = r'C:\Users\Admin\Desktop\E_commerce_proj\data\datainput\Amazon_Sale_Report_Enhanced.csv'
# Đường dẫn tệp đầu ra
output_file_path = r'C:\Users\Admin\Desktop\E_commerce_proj\data\datainput\Amazon_Sale_Report_Enhanced.csv'

# Đọc dữ liệu
data = pd.read_csv(input_file_path)

# Đặt seed để dữ liệu giả lập ổn định
np.random.seed(42)

# Tạo các trường int64 mới
new_columns = {
    'NumReturns': np.random.randint(0, 10, size=len(data)),
    'Customer_Score': np.random.randint(50, 100, size=len(data)),
    'Loyalty_Points': np.random.randint(0, 5000, size=len(data)),
    'Discount_Usage': np.random.randint(0, 20, size=len(data)),
    'Referral_Count': np.random.randint(0, 5, size=len(data)),
    'MntAccessories': np.random.randint(0, 1000, size=len(data)),
    'MntElectronics': np.random.randint(0, 2000, size=len(data)),
    'MntClothing': np.random.randint(0, 1500, size=len(data)),
    'MntHomeDecor': np.random.randint(0, 800, size=len(data)),
    'NumGiftPurchases': np.random.randint(0, 15, size=len(data)),
    'NumHolidayPurchases': np.random.randint(0, 10, size=len(data)),
    'NumSpecialOffers': np.random.randint(0, 20, size=len(data)),
    'NumSocialMediaShares': np.random.randint(0, 50, size=len(data)),
    'NumLoyaltyVisits': np.random.randint(0, 100, size=len(data))
}

# Thêm các cột mới vào dataframe
for col_name, col_data in new_columns.items():
    data[col_name] = col_data

# Xuất dữ liệu đã cập nhật thành tệp CSV
data.to_csv(output_file_path, index=False)

print(f"Dữ liệu đã được lưu vào: {output_file_path}")
