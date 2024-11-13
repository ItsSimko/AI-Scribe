# Settings Documentation
## General Settings
- **Show Welcome Message**
  - Description: Display welcome message on startup
  - Default: `true`
  - Type: boolean
## Whisper Settings
- **Whisper Endpoint**
  - Description: API endpoint for Whisper service
  - Default: `https://localhost:2224/whisperaudio`
  - Type: string
- **Whisper Server API Key**
  - Description: API key for Whisper service authentication
  - Default: `None`
  - Type: string
- **Whisper Model**
  - Description: Whisper model to use for speech recognition
  - Default: `small.en`
  - Type: string
- **Local Whisper**
  - Description: Use local Whisper instance instead of cloud service
  - Default: `false`
  - Type: boolean
- **Real Time**
  - Description: Enable real-time processing
  - Default: `false`
  - Type: boolean
## LLM Settings
- **Model Endpoint**
  - Description: API endpoint URL for the model service
  - Default: `https://api.openai.com/v1/`
  - Type: string
- **Use Local LLM**
  - Description: Toggle to use a locally hosted language model instead of cloud service
  - Default: `false`
  - Type: boolean
## Advanced Settings
- **use_story**
  - Description: Enable story context for generation
  - Default: `false`
  - Type: boolean
- **use_memory**
  - Description: Enable memory context for generation
  - Default: `false`
  - Type: boolean
- **use_authors_note**
  - Description: Enable author's notes in generation
  - Default: `false`
  - Type: boolean
- **use_world_info**
  - Description: Enable world information in context
  - Default: `false`
  - Type: boolean
- **Enable Scribe Template**
  - Description: Enable Scribe template functionality
  - Default: `false`
  - Type: boolean
- **max_context_length**
  - Description: Maximum number of tokens in the context window
  - Default: `5000`
  - Type: integer
- **max_length**
  - Description: Maximum length of generated text
  - Default: `400`
  - Type: integer
- **rep_pen**
  - Description: Repetition penalty factor
  - Default: `1.1`
  - Type: float
- **rep_pen_range**
  - Description: Token range for repetition penalty
  - Default: `5000`
  - Type: integer
- **rep_pen_slope**
  - Description: Slope of repetition penalty curve
  - Default: `0.7`
  - Type: float
- **temperature**
  - Description: Controls randomness in generation (higher = more random)
  - Default: `0.1`
  - Type: float
- **tfs**
  - Description: Tail free sampling parameter
  - Default: `0.97`
  - Type: float
- **top_a**
  - Description: Top-A sampling parameter
  - Default: `0.8`
  - Type: float
- **top_k**
  - Description: Top-K sampling parameter
  - Default: `30`
  - Type: integer
- **top_p**
  - Description: Top-P (nucleus) sampling parameter
  - Default: `0.4`
  - Type: float
- **typical**
  - Description: Typical sampling parameter
  - Default: `0.19`
  - Type: float
- **sampler_order**
  - Description: Order of sampling methods to apply
  - Default: `[6, 0, 1, 3, 4, 2, 5]`
  - Type: string (JSON array)
- **singleline**
  - Description: Output single line responses only
  - Default: `false`
  - Type: boolean
- **frmttriminc**
  - Description: Trim incomplete sentences from output
  - Default: `false`
  - Type: boolean
- **frmtrmblln**
  - Description: Remove blank lines from output
  - Default: `false`
  - Type: boolean
- **Use best_of**
  - Description: Enable best-of sampling
  - Default: `false`
  - Type: boolean
- **best_of**
  - Description: Number of completions to generate and select from
  - Default: `2`
  - Type: integer
- **Real Time Audio Length**
  - Description: Length of audio segments for real-time processing (seconds)
  - Default: `5`
  - Type: integer
- **Use Pre-Processing**
  - Description: Enable text pre-processing
  - Default: `true`
  - Type: boolean
- **Use Post-Processing**
  - Description: Enable text post-processing
  - Default: `false`
  - Type: boolean
## Docker Settings
- **LLM Container Name**
  - Description: Docker container name for LLM service
  - Default: `ollama`
  - Type: string
- **LLM Caddy Container Name**
  - Description: Docker container name for Caddy reverse proxy
  - Default: `caddy-ollama`
  - Type: string
- **LLM Authentication Container Name**
  - Description: Docker container name for authentication service
  - Default: `authentication-ollama`
  - Type: string
- **Whisper Container Name**
  - Description: Docker container name for Whisper service
  - Default: `speech-container`
  - Type: string
- **Whisper Caddy Container Name**
  - Description: Docker container name for Whisper Caddy service
  - Default: `caddy`
  - Type: string
- **Auto Shutdown Containers on Exit**
  - Description: Automatically stop Docker containers on application exit
  - Default: `true`
  - Type: boolean
- **Use Docker Status Bar**
  - Description: Show Docker container status in UI
  - Default: `false`
  - Type: boolean