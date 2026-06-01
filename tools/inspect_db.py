import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    return oracledb.connect(
        user=os.environ.get("ORACLE_USER", "system"),
        password=os.environ.get("ORACLE_PASSWORD", "dbms123"),
        dsn=os.environ.get("ORACLE_DSN", "localhost/XE")
    )

if __name__ == '__main__':
    tables = [
        'HACKATHON_STUDENTS',
        'OTP_VERIFICATION',
        'ACTIVITY_LOG',
        'HACKATHONS',
        'STUDENT_PROJECTS'
    ]

    conn = get_conn()
    cur = conn.cursor()
    for t in tables:
        try:
            cur.execute(f"SELECT COUNT(*) FROM {t}")
            cnt = cur.fetchone()[0]
        except Exception as e:
            cnt = f"ERROR: {e}"
        print(f"{t}: {cnt}")
    cur.close()
    conn.close()
