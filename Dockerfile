# 1. বেস ইমেজ হিসেবে একটি আধুনিক এবং হালকা ভার্সন ব্যবহার করুন
FROM python:3.11-slim

# 2. এনভায়রনমেন্ট ভ্যারিয়েবল সেট করুন
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. ওয়ার্কিং ডিরেক্টরি সেট করুন
WORKDIR /app

# 4. শুধুমাত্র requirements.txt ফাইলটি কপি করুন এবং লাইব্রেরি ইনস্টল করুন
# এটি Docker-এর লেয়ার ক্যাশিং (layer caching) ব্যবহার করে বিল্ড টাইম কমায়
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 5. এখন বাকি সব কোড কপি করুন
COPY . .

# 6. সরাসরি আপনার বট চালু করুন, start.sh এর প্রয়োজন নেই
# আপনার মূল ফাইলের নাম যদি bot.py হয়
CMD ["python3", "bot.py"]
