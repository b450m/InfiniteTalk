class ModelManager:
    def __init__(self):
        self._model = None
        self._cache = {}

    def _load_model(self):
        # Logic to initialize and load the model
        # For demonstration, we will just use a string as a placeholder
        self._model = "Initialized Model"
        return self._model

    def get_model(self, model_name):
        if model_name not in self._cache:
            self._cache[model_name] = self._load_model()
        return self._cache[model_name]

    def clear_cache(self):
        self._cache = {}

    def get_cached_models(self):
        return list(self._cache.keys())
