from huggingface_hub import hf_hub_download
from llama_cpp import Llama

# Mengunduh model Qwen hasil kuantisasi yang ringan untuk CPU
model_path = hf_hub_download(
    repo_id="Qwen/Qwen1.5-0.5B-Chat-GGUF", 
    filename="qwen1_5-0_5b-chat-q4_k_m.gguf"
)

# Inisialisasi model (otomatis menggunakan CPU di GH Actions)
llm = Llama(model_path=model_path, verbose=False)

# Eksekusi prompt
output = llm("Tuliskan satu kalimat sambutan untuk user baru.", max_tokens=50)
print("AI Output:", output["choices"][0]["text"])
