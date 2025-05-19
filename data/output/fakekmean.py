import pandas as pd
import numpy as np

# Đường dẫn tệp gốc
input_file_path = r'C:\Users\Admin\Desktop\E_commerce_proj\data\output\data_full_cleaned.csv'
output_file_path = r'C:\Users\Admin\Desktop\E_commerce_proj\data\output\data_full_cleaned.csv'

# Đọc dữ liệu
data = pd.read_csv(input_file_path)

# Đặt seed để dữ liệu giả lập ổn định
np.random.seed(42)

# Income - Phân phối ngẫu nhiên từ 10,000 đến 100,000
data['Income'] = np.random.randint(10000, 100000, size=len(data))

# Recency - Số ngày kể từ lần mua cuối cùng
data['Recency'] = np.random.randint(0, 100, size=len(data))

# Purchases - Số lượng giao dịch đã thực hiện
data['NumDealsPurchases'] = np.random.randint(0, 10, size=len(data))
data['NumWebPurchases'] = np.random.randint(1, 15, size=len(data))
data['NumCatalogPurchases'] = np.random.randint(0, 10, size=len(data))
data['NumStorePurchases'] = np.random.randint(1, 15, size=len(data))
data['NumWebVisitsMonth'] = np.random.randint(0, 30, size=len(data))

# Demographics - Tuổi và số trẻ em
data['Age'] = np.random.randint(18, 70, size=len(data))
data['Children'] = np.random.randint(0, 4, size=len(data))

# Thời gian là khách hàng
data['CustomerFor'] = np.random.randint(1, 10, size=len(data))

# Số tiền đã chi tiêu (phụ thuộc vào Income)
data['AmountSpent'] = data['Income'] * np.random.uniform(0.05, 0.3, size=len(data))

# Fake dữ liệu cho các trường ban đầu:
data['NumReturns'] = np.random.randint(0, 5, size=len(data))
data['Customer_Score'] = data['Income'] * 0.001 + data['AmountSpent'] * 0.005 + data['NumWebVisitsMonth'] * 0.2
# Giới hạn từ 50 - 100
data['Customer_Score'] = np.clip(data['Customer_Score'], 50, 100).astype(int)

# Loyalty Points dựa trên AmountSpent và Customer_Score
data['Loyalty_Points'] = (data['AmountSpent'] * 0.1 + data['Customer_Score'] * 10).astype(int)

# Discount_Usage dựa trên NumWebVisitsMonth
data['Discount_Usage'] = data['NumWebVisitsMonth'] // 2

# Referral Count dựa trên Customer_Score
data['Referral_Count'] = (data['Customer_Score'] // 20).astype(int)

# Mnt* columns dựa trên AmountSpent
data['MntAccessories'] = data['AmountSpent'] * 0.1

data['MntElectronics'] = data['AmountSpent'] * 0.2

data['MntClothing'] = data['AmountSpent'] * 0.15

data['MntHomeDecor'] = data['AmountSpent'] * 0.05

# Purchases columns
data['NumGiftPurchases'] = np.random.randint(0, 10, size=len(data))
data['NumHolidayPurchases'] = data['NumGiftPurchases'] // 2
data['NumSpecialOffers'] = np.random.randint(0, 20, size=len(data))

data['NumSocialMediaShares'] = np.random.randint(0, 50, size=len(data))
data['NumLoyaltyVisits'] = data['Loyalty_Points'] // 100

# Xuất dữ liệu đã cập nhật thành tệp CSV
data.to_csv(output_file_path, index=False)

print(f"Dữ liệu đã được lưu vào: {output_file_path}")