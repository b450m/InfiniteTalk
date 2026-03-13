# model configuration for WAN variants
WAN_MODELS = {
    "14B": {
        "type": "WAN",
        "parameters": {
            "num_layers": 48,
            "hidden_size": 1408,
            "num_attention_heads": 16,
        }
    },
    "7B": {
        "type": "WAN",
        "parameters": {
            "num_layers": 32,
            "hidden_size": 1024,
            "num_attention_heads": 16,
        }
    },
    "FusionX": {
        "type": "WAN",
        "parameters": {
            "num_layers": 48,
            "hidden_size": 1648,
            "num_attention_heads": 16,
        }
    }
}

# CLIP models configurations
CLIP_MODELS = {
    "Standard": {
        "type": "CLIP",
        "parameters": {
            "vision_backbone": "ViT-B/32",
            "text_backbone": "Transformer",
        }
    },
    "FP8": {
        "type": "CLIP",
        "parameters": {
            "vision_backbone": "ViT-B/32",
            "text_backbone": "Transformer",
            "quantization": "FP8",
        }
    }
}

# T5 models configurations
T5_MODELS = {
    "Standard": {
        "type": "T5",
        "parameters": {
            "num_layers": 12,
            "d_model": 768,
            "num_heads": 12,
        }
    },
    "FP8": {
        "type": "T5",
        "parameters": {
            "num_layers": 12,
            "d_model": 768,
            "num_heads": 12,
            "quantization": "FP8",
        }
    }
}

# LoRA configuration with auto-discovery from lora subfolder
LORA_CONFIG = {
    "enabled": True,
    "auto_discover": "lora/",
}

# Advanced options
ADVANCED_OPTIONS = {
    "sampling": {
        "method": "top_k",
        "k": 50,
    },
    "memory": {
        "max_memory": "12GB",
    },
    "optimization": {
        "learning_rate": 0.0001,
        "batch_size": 32,
    },
    "quality": {
        "metrics": ["BLEU", "ROUGE"],
    },
    "distributed_training": {
        "num_gpus": 2,
        "strategy": "ddp",
    }
} 
