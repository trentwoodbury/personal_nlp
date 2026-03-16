"""
I ran this through the Antigravity MCP server. 
You can test this with the following prompt:
Hey, list my available sounds. Then, play the 'arcade_fail' sound.
"""

from mcp.server.fastmcp import FastMCP
import subprocess
import os

mcp = FastMCP("SoundFXGuy")
SOUNDS_DIR = os.path.join(os.path.dirname(__file__), "sound_effects")

@mcp.tool()
def play_sound(effect_name: str) -> str:
    """
    Plays a sound effect to react to the conversation.
    """
    # Ensure the sound file exists
    file_path = os.path.join(SOUNDS_DIR, f"{effect_name}.mp3")
    
    if not os.path.exists(file_path):
        return f"Error: Sound '{effect_name}' not found in {SOUNDS_DIR}."

    # 'shell=True' is needed for the 'start' command in Windows
    subprocess.Popen(f'start /min "" "{file_path}"', shell=True)
    
    return f"Successfully played {effect_name}."

if __name__ == "__main__":
    mcp.run()