import subprocess
import shutil
import sys

def download_ollama_model(model_name: str):
    """
    通过 Ollama 下载适合低配硬件的编码模型。
    """
    # 检查 Ollama 是否安装
    if not shutil.which("ollama"):
        print("错误: 未检测到 Ollama。请先访问 https://ollama.com 下载安装。")
        return False

    print(f"准备下载: {model_name}")
    print("提示: 首次下载约需 4-5GB 磁盘空间，请确保网络稳定。")
    
    try:
        # 调用 ollama pull 命令，支持断点续传
        process = subprocess.Popen(
            ["ollama", "pull", model_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # 实时打印下载进度
        for line in process.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()
            
        process.wait()
        
        if process.returncode == 0:
            print(f"\n✅ 模型 {model_name} 下载完成！")
            print(f"运行测试: ollama run {model_name}")
            return True
        else:
            print(f"\n❌ 下载失败，退出码: {process.returncode}")
            return False
            
    except KeyboardInterrupt:
        print("\n⚠️ 用户中断下载。下次运行脚本可继续下载（Ollama 支持断点续传）。")
        return False
    except Exception as e:
        print(f"发生错误: {e}")
        return False

if __name__ == "__main__":
    # 推荐配置：7B 版本（默认 Q4 量化，约 4-5GB）
    # 如果你的 2 核 CPU 跑起来太慢，请将下方改为 "qwen2.5-coder:1.5b"
    MODEL_TO_DOWNLOAD = "qwen2.5-coder:7b"
    
    success = download_ollama_model(MODEL_TO_DOWNLOAD)
    sys.exit(0 if success else 1)
