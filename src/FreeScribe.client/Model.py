from llama_cpp import Llama
import os
from typing import Optional, Dict, Any

class Model:
    """
    Model class for handling GPU-accelerated text generation using the Llama library.

    This class provides an interface to initialize a language model with specific configurations
    for GPU acceleration, generate responses based on a text prompt, and retrieve GPU settings.
    The class is configured to support multi-GPU setups and custom configurations for batch size,
    context window, and sampling settings. 

    Attributes:
        model: Instance of the Llama model configured with specified GPU and context parameters.
        config: Dictionary containing the GPU and model configuration.

    Methods:
        generate_response: Generates a text response based on an input prompt using
                        the specified sampling parameters.
        get_gpu_info: Returns the current GPU configuration and batch size details.
    """

    def __init__(
        self,
        model_path: str,
        chat_template: str = None,
        context_size: int = 4096,
        gpu_layers: int = -1,  # -1 means load all layers to GPU
        main_gpu: int = 1,     # Primary GPU device index
        tensor_split: Optional[list] = None,  # For multi-GPU setup
        n_batch: int = 512,    # Batch size for inference
        n_threads: Optional[int] = None,  # CPU threads when needed
        seed: int = 1337
    ):
        """
        Initializes the GGUF model with GPU acceleration.
        
        Args:
            model_path: Path to the model file
            context_size: Size of the context window
            gpu_layers: Number of layers to offload to GPU (-1 for all)
            main_gpu: Main GPU device index
            tensor_split: List of GPU memory splits for multi-GPU setup
            n_batch: Batch size for inference
            n_threads: Number of CPU threads
            seed: Random seed for reproducibility
        """
        # Set environment variables for GPU
        os.environ["CUDA_VISIBLE_DEVICES"] = str(main_gpu)
        
        # Initialize model with GPU settings
        self.model = Llama(
            model_path=model_path,
            n_ctx=context_size,
            n_gpu_layers=gpu_layers,
            n_batch=n_batch,
            n_threads=n_threads or os.cpu_count(),
            seed=seed,
            tensor_split=tensor_split,
            chat_format=chat_template,
        )
      
        # Store configuration
        self.config = {
            "gpu_layers": gpu_layers,
            "main_gpu": main_gpu,
            "context_size": context_size,
            "n_batch": n_batch
        }
        
    def generate_response(
        self,
        prompt: str,
        max_tokens: int = 50,
        temperature: float = 0.1,
        top_p: float = 0.95,
        repeat_penalty: float = 1.1
    ) -> str:
        """
        Generates a response using GPU-accelerated inference.
        
        Args:
            prompt: Input text prompt
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature (higher = more random)
            top_p: Top-p sampling threshold
            repeat_penalty: Penalty for repeating tokens
            
        Returns:
            Generated text response
        """
        try:
            response = self.model.create_completion(
                prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                repeat_penalty=repeat_penalty,
                echo=False
            )

            print (response)
           
            return response["choices"][0]["text"]
            
        except Exception as e:
            print(f"GPU inference error: {str(e)}")
    
    def get_gpu_info(self) -> Dict[str, Any]:
        """
        Returns information about the current GPU configuration.
        """
        return {
            "gpu_layers": self.config["gpu_layers"],
            "main_gpu": self.config["main_gpu"],
            "batch_size": self.config["n_batch"],
            "context_size": self.config["context_size"]
        }
    
    def __del__(self):
        """Cleanup GPU memory on deletion"""
        self.model = None