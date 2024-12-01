from huggingface_hub import snapshot_download
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM
import zipfile
import io
from ...adapters.logger import Logger, DEBUG
from ...adapters.api import Settings


class ModelService:
    def __init__(self):
        """
        Сервис для работы с ML-моделью.
        """
        
        self.settings = Settings()

        self.model_path = Path.home().joinpath('mistral_models', 'Nemo-Instruct')
        self.model = None
        self.tokenizer = None

        self.logger = Logger(name="ModelService", level=DEBUG, log_file="model_service.log")


    def load_model(self):
        """
        Загрузка и инициализация модели.
        """

        self.logger.info("Загрузка модели...")
        self.model_path.mkdir(parents=True, exist_ok=True)
        snapshot_download(
            repo_id="mistralai/Mistral-Nemo-Instruct-2407",
            allow_patterns=["params.json", "consolidated.safetensors", "tekken.json"],
            local_dir=self.model_path,
            use_auth_token=self.settings.huggingface_hub_token
        )
        self.logger.info("Модель успешно загружена.")

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_path)


    def generate_text(self, prompt: str) -> str:
        """
        Генерация текста на основе промпта.
        """

        if not self.model or not self.tokenizer:
            raise RuntimeError("Модель не загружена. Сначала вызовите load_model().")

        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs.input_ids, max_length=200)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


    def process_multiple_files(self, archive_content: bytes) -> str:
        """
        Обработка нескольких файлов из архива.
        """

        results = []
        with zipfile.ZipFile(io.BytesIO(archive_content), 'r') as archive:
            for file_name in archive.namelist():
                with archive.open(file_name) as file:
                    content = file.read().decode("utf-8")
                    result = self.generate_text(content)
                    results.append(f"{file_name}: {result}")
        return "\n".join(results)
