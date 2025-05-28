import datetime
import os

# 오늘 날짜를 문자열로 포맷팅 (예: 2025-05-26)
today = datetime.datetime.today().strftime("%Y-%m-%d")

# 🔧 경로를 "절대 경로"로 정확히 지정
# C:\Python\blog-content\logs 폴더에 저장할 거예요
base_path = r"C:\Users\user\Code\growth-log\logs"

# 📂 폴더가 없으면 자동으로 생성
os.makedirs(base_path, exist_ok=True)

# 🔖 파일 경로를 날짜에 맞춰 생성
file_path = os.path.join(base_path, f"{today}.md")

# ✍️ 마크다운 템플릿 내용
content = f"""# {today} 일일 기록

## ✅ 오늘 한 일
- Bigquery DB 리팩토링
- 주목적
1. 비용 절감
2. 쿼리 최적화
3. 공유하고 있는 Bigquery DB 협업 효율성
4. 데이터 품질 향상

- Grafana를 통한 Bigquery DB 모니터링
1. 일일 쿼리 사용량 및 평일 사용량 넘어갈 시 alert 기능
2. 가장 많이 스캔이 된 테이블 - 스캔량 많은 테이블, 주요 비용 유발 원인 테이블, 

## ❗ 고민 / 이슈
- WITH 구문 후에, INSERT INTO 에서 KEYWORD ERROR 발생
- WITH CTE절에서 사용한 테이블을 INSERT INTO 에서 참조 테이블로 사용 에러 발생
- INSERT INTO + WITH + SELECT절로 예약 쿼리 구성해야 함 - WITH + SELECT로 여러개의 INSERT INTO 구문 불가능함 
- TYPE과 SCHEMA가 다 일치해야 데이터 적재가 가능함
## 📌 메모











"""

# 📝 파일이 아직 없으면 생성해서 내용 쓰기
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[✔] {file_path} 생성 완료")
else:
    print(f"[!] {file_path} 이미 존재함")