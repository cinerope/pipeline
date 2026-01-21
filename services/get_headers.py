import google.auth
from google.auth.transport.requests import Request

def get_headers_from_key(key_path):
    # 1. 키 파일을 사용하여 자격 증명 생성
    credentials, project_id = google.auth.load_credentials_from_file(
        key_path,
        scopes=['https://www.googleapis.com/auth/cloud-platform']
    )

    # 2. 토큰이 없거나 만료되었다면 새로 고침 (Access Token 생성)
    auth_request = Request()
    credentials.refresh(auth_request)

    # 3. headers 구성
    headers = {
        "Authorization": f"Bearer {credentials.token}",
        "Content-Type": "application/json",
        "X-Goog-User-Project": project_id
    }
    return headers