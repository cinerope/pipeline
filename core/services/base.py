from abc import ABC, abstractmethod
from core.services.contracts import GenerationRequest, GenerationJob, GenerationResult

class VideoProvider(ABC):

    @abstractmethod
    async def submit(self, request: GenerationRequest) -> GenerationJob:
        """작업 시작 -> GenerationJob 반환"""
        raise NotImplementedError

    @abstractmethod
    async def poll(self, job: GenerationJob) -> GenerationJob:
        """작업 상태 조회 -> 상태가 반영된 GenerationJob 반환"""
        raise NotImplementedError

    @abstractmethod
    async def result(self, job: GenerationJob) -> GenerationResult:
        """작업 결과 조회 -> GenerationResult 반환"""
        raise NotImplementedError

    async def cancel(self, job: GenerationJob) -> None:
        """선택 구현: provider에서 cancel을 지원하는 경우 override"""
        raise NotImplementedError
