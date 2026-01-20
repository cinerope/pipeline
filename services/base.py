from abc import ABC, abstractmethod
from typing import Dict

class VideoProvider(ABC):

    @abstractmethod
    def submit(self, payload: Dict) -> str:
        """작업 시작 → operation_name 반환"""
        pass

    @abstractmethod
    def poll(self, operation_name: str) -> Dict:
        """상태 조회"""
        pass

    @abstractmethod
    def result(self, poll_response: Dict) -> str:
        """video url (또는 gcs uri) 추출"""
        pass
