
######### file for global variable/function declarations ############
import bpy
import os
import sys
import time
from time import sleep
import re
import json
import threading
import tempfile
import traceback
from pathlib import Path
from contextlib import redirect_stdout
import subprocess
from subprocess import DEVNULL
import socket
import queue
import inspect
import io
import addon_utils

import warnings


# Keeping essential Blender and other necessary modules
from mathutils import Vector, Euler
import blf

# FAST specific imports
from . import __name__


try:
    import requests
except ModuleNotFoundError:
    pass

try:
    import pyperclip
except ModuleNotFoundError:
    pass

try:
    import pywinctl as gw
except ModuleNotFoundError:
    pass

try:
    import pyautogui
except ModuleNotFoundError:
    pass



import platform

try:
    if platform.system() == "Windows":

        lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
        if lib_path not in sys.path:
            sys.path.append(lib_path)


        import psutil

    
        if lib_path in sys.path:
            sys.path = [path for path in sys.path if path != os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")]

  

    elif platform.system() in ["Linux"]:  # macOS or Linux

        lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
        if lib_path in sys.path:
            sys.path = [path for path in sys.path if path != os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")]

   
        lib2_path = os.path.join(os.path.dirname(__file__), "lib2")
        if lib2_path not in sys.path:
            sys.path.append(lib2_path)


        import psutil

        if lib2_path in sys.path:
            sys.path = [path for path in sys.path if path != os.path.join(os.path.dirname(__file__), "lib2")]


    elif platform.system() in ["Darwin"]:  # macOS or Linux

        lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
        if lib_path in sys.path:
            sys.path = [path for path in sys.path if path != os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")]

   

        lib2_path = os.path.join(os.path.dirname(__file__), "lib2")
        if lib2_path not in sys.path:
            sys.path.append(lib2_path)
    
        if lib_path not in sys.path:
            sys.path.append(lib_path)
    
        import psutil  # Import psutil with lib available
    
        if lib_path in sys.path:
            sys.path = [path for path in sys.path if path != lib_path]


        if lib2_path in sys.path:
            sys.path = [path for path in sys.path if path != os.path.join(os.path.dirname(__file__), "lib2")]




except ModuleNotFoundError as e:

    pass

lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
if lib_path not in sys.path:
    sys.path.append(lib_path)


if platform.system() == "Windows":
    import ctypes
    from ctypes import wintypes
elif platform.system() == "Darwin":
    pass
elif platform.system() == "Linux":
    pass

try:
    
    if platform.system() == "Windows":
        base_dir = os.path.dirname(__file__)
        paths_to_add = [
            os.path.join(base_dir, "lib", "Python311", "site-packages", "win32"),
            os.path.join(base_dir, "lib", "Python311", "site-packages", "win32", "lib"),
            os.path.join(base_dir, "lib", "Python311", "site-packages", "pywin32_system32")
        ]

        # Add paths to sys.path if not already present
        for path in paths_to_add:
            if path not in sys.path:
                sys.path.append(path)

    # Attempt to import pywinctl
    import pywinctl as gw
    

except ModuleNotFoundError as e:
    pass


from . import __name__


spacing = 107.00
sb_size = 0.72
min_spacing = 62.42
max_spacing = 469.00

tstr = "###############"

tfp = os.path.join(os.path.expanduser("~"), "Desktop", "OBS", ".COMMERCIAL")

def generate_identifier(length=6):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    word = ""

    for i in range(length // 2):
        word += random.choice(consonants)
        word += random.choice(vowels)

    # In case of an odd length, add an extra consonant
    if length % 2:
        word += random.choice(consonants)

    return word.capitalize()

# import os
# import platform
# import traceback
# import warnings
# from math import log10
# from pydub import AudioSegment
# from pydub.playback import play
# import bpy  # Blender API

# def sound(setable_frequency=None, setable_volume=None):
#     try:
#         print("🔄 Function started: sound()")

#         prefs = bpy.context.preferences.system
#         max_retries = 3

#         current_platform = platform.system()
#         print(f"🖥️ Detected Platform: {current_platform}")

#         # Get Blender's script directory dynamically
#         scripts_dir = bpy.utils.user_resource('SCRIPTS')
#         addons_dir = os.path.join(scripts_dir, "addons")

#         # Define the Blender add-on directory
#         addon_name = "blender_ai_thats_error_proof"
#         blender_addon_dir = os.path.join(addons_dir, addon_name)

#         # Define the LIB and DATA directory paths
#         lib_dir = os.path.join(blender_addon_dir, "lib")  # Always lowercase "lib"
#         data_dir = os.path.join(blender_addon_dir, "data")  # New: Added "data" directory

#         # Define the path to FFMPEG based on OS
#         if current_platform == "Darwin":  # macOS
#             path_to_ffmpeg = os.path.join(lib_dir, "Python311", "site-packages", "ffmpeg")
#         elif current_platform == "Linux":
#             path_to_ffmpeg = os.path.join(lib_dir, "Python311", "site-packages", "ffmpeg")
#         elif current_platform == "Windows":
#             path_to_ffmpeg = os.path.join(lib_dir, "Python311", "site-packages", "ffmpeg.exe")

#         print(f"🔍 Checking for FFMPEG at: {path_to_ffmpeg}")

#         if not os.path.exists(path_to_ffmpeg):
#             print("\n❌ FFMPEG not found! Please install FFMPEG and restart Blender.")
#             return

#         print("✅ FFMPEG found!")

#         # Ignore RuntimeWarning from pydub
#         warnings.filterwarnings("ignore", category=RuntimeWarning, module="pydub.utils")

#         # Define the path to the sound file inside the DATA folder (✅ Updated Directory)
#         sound_file_path = os.path.join(data_dir, "sound.wav")
#         print(f"🔍 Checking for sound file at: {sound_file_path}")

#         if os.path.exists(sound_file_path):
#             print("✅ Sound file was found.")
#             sound = AudioSegment.from_file(sound_file_path)
#             print("🎵 Sound file loaded successfully.")

#             # Apply volume adjustment if setable_volume is provided
#             if setable_volume is not None:
#                 print(f"🔊 Adjusting volume: {setable_volume}")
#                 sound = sound + (20 * log10(setable_volume))

#             print("▶ Playing sound now...")
#             play(sound)
#             print("✅ Sound playback complete!")
#         else:
#             print(f"❌ Sound file not found at: {sound_file_path}")

#     except Exception as e:
#         print("\n❌ An unexpected error occurred:")
#         traceback.print_exc()  # Standard traceback output

# # Run the function
# sound()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_traceback_report(full_traceback, one_liner):

    password_url = "https://fast-blender-add-ons.com/wp-content/uploads/app_password.txt"

    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        if manager.collect_error_message_only:
            sender_email = "mjoe67886@gmail.com"
            recipient_email = "mjoe67886@gmail.com"
            subject = f"[{generate_identifier(length=6)}: {one_liner}]"
    
            try:
                manager = bpy.context.preferences.addons[__name__].preferences.Prop
                if manager.new_addition:
                    subject = f"[HOME: {one_liner}]"
            except:
                pass
            try:
                response = requests.get(password_url, timeout=2)
                response.raise_for_status()
                app_password = response.text.strip()
        
            except requests.exceptions.RequestException as e:
                print_color("AR", f"\n{traceback.format_exc()}")
                return
        
        
            try:
                # Prepare dummy error message and additional info
                user_command = "Test Command"
                full_error_message = full_traceback
                re_addable_code = "print('This is test code.')"
            
                body = f"User Command: {user_command}\n\nError Message:\n{full_error_message}\n\nCode:\n{re_addable_code}"
            
                # Initialize the message object
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
            
            
                # Connect to Gmail's SMTP server and send the email
                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.login(sender_email, app_password)
                    server.send_message(msg)
                    print(f"\n🚀 Error details sent successfully.")
                except smtplib.SMTPException as e:
                    print(f"\n🚀 SMTP error occurred: {e}")
                finally:
                    server.quit()
        
            except Exception as e:
                print(f"\n🚀 An error occurred while preparing the error report: {traceback.format_exc()}")
    except:
        print(f"\n🚀 Skipped collecting error data.")


def capture_and_copy_traceback():
    # Get caller information
    caller_info = inspect.stack()[1]
    caller_file = caller_info.filename
    caller_function = caller_info.function
    calling_line = caller_info.lineno

    # Get the most recent exception details
    exc_type, exc_value, exc_traceback = sys.exc_info()
    if exc_type is None:
        # No active exception
        print("🚀 No exception to capture.")
        return None

    # Format the traceback
    exception_traceback = "".join(
        traceback.format_exception(exc_type, exc_value, exc_traceback)
    )
    one_liner = f"Error: {str(exc_value)}"


    # Print and optionally send the traceback report
    print(f"\n🚀 Full Traceback:\n{exception_traceback}")
    send_traceback_report(exception_traceback, one_liner)
    return exception_traceback

def get_blender_version():
    major, minor, patch = bpy.app.version
    return f"{major}.{minor}.{patch}"




def wrap(text, tl=100, cc="AW", prefix="", center=False):
    """
    Wrap the input text into lines, breaking at word boundaries, and optionally center each line.
    
    :param text: The text to wrap.
    :param tl: The maximum width of each line.
    :param cc: Color code or identifier for colored printing.
    :param prefix: A prefix to add before each line.
    :param center: If True, center-align each line.
    """
    # Split the input string into words
    words = text.split()

    # Create a list to hold lines
    lines = []
    current_line = []

    for word in words:
        # Check if adding the next word would exceed the length
        if sum(len(w) + 1 for w in current_line) + len(word) <= tl:
            current_line.append(word)
        else:
            # Join the current line into a string and add it to the list of lines
            lines.append(" ".join(current_line))
            # Start a new line with the current word
            current_line = [word]

    # Add the last line if it contains any words
    if current_line:
        lines.append(" ".join(current_line))

    # Iterate over each line and print it
    for line in lines:
        if center:
            print_color(cc, prefix + line.center(tl))
        else:
            print_color(cc, prefix + line)


def get_previous_version():
    prev_version_dir = Path.home() / "Documents" / "baitep_prev_version"
    version_pattern = re.compile(r"baitep_prev_version_(\d+_\d+_\d+)\.zip")
    # print("prev_version_dir", prev_version_dir)

    # Check if directory exists
    if not prev_version_dir.exists():
        return "None"

    # Check if directory is empty
    if not any(prev_version_dir.iterdir()):
        return "None"

    for filename in os.listdir(prev_version_dir):
        match = version_pattern.match(filename)
        if match:
            version = match.group(1).replace("_", ".")
            return version

    # If no version file was found, return "None"
    return "None"


def get_current_version():
    current_version = "unknown"  # Default value
    for mod in addon_utils.modules():
        if mod.__name__ == "blender_ai_thats_error_proof":
            version_tuple = mod.bl_info.get("version", (-1, -1, -1))
            current_version = ".".join(map(str, version_tuple))
            break  # Exit the loop once the FAST module version is found
    return current_version


def get_update_version(target_dir):
    # Specify the version text file
    version_text_file_path = os.path.join(target_dir, "version.txt")

    # Check if the file exists
    if not os.path.exists(version_text_file_path):
        # print("version.txt file not found.")
        return None

    # Open and read the version number
    with open(version_text_file_path, "r") as version_text_file:
        version = version_text_file.read()

    return version


def safe_move_file(src_file, dst_dir):
    try:
        dst_file = os.path.join(dst_dir, os.path.basename(src_file))
        shutil.move(src_file, dst_file)
    except FileNotFoundError as fnf_error:
        print(f"FileNotFoundError: {fnf_error}")
    except shutil.Error as move_error:
        print(f"shutil.Error: {move_error}")
    except Exception as e:
        capture_and_copy_traceback()

        print(f"An unexpected error occurred: {e}")

    # Check if the original file still exists and delete it if present
    if os.path.exists(src_file):
        try:
            os.remove(src_file)
            print_color("AR", "\nDeleted original file: ")
            print_color("AR", f"{src_file}")
        except Exception as e:
            capture_and_copy_traceback()

            print_color("AR", f"Error deleting original file: {src_file} - {e}")


def remove_file(filename):
    # Set up full path to file
    addon_dir = os.path.join(bpy.utils.user_resource("SCRIPTS"), "addons")
    file_path = os.path.join(addon_dir, filename)

    # Check if file exists
    if os.path.exists(file_path):
        try:
            # Try to remove file
            os.remove(file_path)
        except Exception as e:
            capture_and_copy_traceback()

            # Report error during file deletion
            print(
                f"Error occurred while trying to remove '{filename}'. Error message: {str(e)}"
            )
    else:
        print(f"'{filename}' does not exist.")

def get_elapsed_time():
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    current_time = time.monotonic()
    start_time = manager.start_time
    elapsed_time = current_time - start_time
    caller_info = inspect.stack()[1]  # Get information about the caller
    calling_line = caller_info.lineno  # Line number where print_color was called 

    # print(f"\nElapsed time: {elapsed_time:.6f} seconds. Called from line: {calling_line}")

    return elapsed_time

def check_multiple_blender_instances_1():
    blender_process_name = "blender"
    try:
        # Check all running processes for 'blender' using psutil
        instances = sum(1 for proc in psutil.process_iter(['name']) 
                        if blender_process_name in proc.info['name'].lower())
        return instances
    except Exception as e:
        print(f"Could not detect Blender instances: {e}")
        return 1  # Assume at least one instance

def redraw_all_areas():
    """Redraw all areas"""
    for screen in bpy.data.screens:
        for area in screen.areas:
            area.tag_redraw()


def redraw_area(area):
    """Redraw a specific area"""
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type == area:
                area.tag_redraw()
color_patterns = {
    # "AR": ["\033[91m", "\033[91m"],  # All Red
    "AR": ["\033[38;2;237;47;65m", "\033[38;2;237;47;65m"],  # Slightly more saturated red
        # More saturated red with a 5% increase from the original bright red
    "ARR": ["\033[38;2;255;81;81m", "\033[38;2;255;81;81m"],  # 24-bit ANSI escape code for a richer red

    # "AG": ["\033[92m", "\033[92m"],  # All Green
    "AG": ["\033[38;2;0;255;81m", "\033[38;2;0;255;81m"],  # Richer green
    "AY": ["\033[93m", "\033[93m"],  # All Yellow
    "AO": ["\033[38;2;255;165;10m", "\033[38;2;255;165;10m"],  # All Orange
    "AB0": ["\033[94m", "\033[94m"],  # All Blue
    "AB": ["\033[38;2;39;119;255m", "\033[38;2;39;119;255m"],

    "AI": ["\033[38;2;138;43;226m", "\033[38;2;138;43;226m"],  # Brighter Indigo
    "AV": ["\033[38;2;195;85;220m", "\033[38;2;195;85;220m"],  # Brighter Violet with 5% more saturation
    "AM": ["\033[95m", "\033[95m"],  # All Magenta
    "AC": ["\033[96m", "\033[96m"],  # All Cyan
    "AW": ["\033[97m", "\033[97m"],  # All White
    "AL": ["\033[38;2;150;150;150m", "\033[38;2;150;150;150m"],  # Slightly lighter grey

    "ABR": ["\033[38;2;150;75;0m", "\033[38;2;150;75;0m"],  # All Brown
    "AT": ["\033[38;2;210;180;140m", "\033[38;2;210;180;140m"],  # All Tan
    
    # New 7 less saturated colors (based on Cyan saturation)
    "LG_R": ["\033[38;2;255;150;150m", "\033[38;2;255;150;150m"],  # Light Red
    "LG_G": ["\033[38;2;150;255;150m", "\033[38;2;150;255;150m"],  # Light Green
    "LG_Y": ["\033[38;2;255;255;150m", "\033[38;2;255;255;150m"],  # Light Yellow
    "LG_O": ["\033[38;2;255;200;150m", "\033[38;2;255;200;150m"],  # Light Orange
    "LG_B": ["\033[38;2;150;150;255m", "\033[38;2;150;150;255m"],  # Light Blue
    "LG_I": ["\033[38;2;180;150;255m", "\033[38;2;180;150;255m"],  # Light Indigo
    "LG_V": ["\033[38;2;220;150;255m", "\033[38;2;220;150;255m"],  # Light Violet

    "RG": ["\033[38;2;255;0;0m", "\033[92m"],  # Red and Green
    "GR": ["\033[92m", "\033[38;2;255;0;0m"],  # Green and Red
    "RW": ["\033[38;2;255;0;0m", "\033[97m"],  # Red and White
    "WR": ["\033[97m", "\033[38;2;255;0;0m"],  # White and Red
    "GW": ["\033[92m", "\033[97m"],  # Green and White
    "BG": ["\033[94m", "\033[92m"],  # Blue and Green
    "GB": ["\033[92m", "\033[94m"],  # Green and Blue
    "YM": ["\033[93m", "\033[95m"],  # Yellow and Magenta

    "AM": ["\033[95m", "\033[95m"],  # All Magenta
    "AC": ["\033[96m", "\033[96m"],  # All Cyan
    "AW": ["\033[97m", "\033[97m"],  # All White
    
    "BY": ["\033[94m", "\033[93m"],  # Blue and Yellow
    "MC": ["\033[95m", "\033[96m"],  # Magenta and Cyan
    "CW": ["\033[96m", "\033[97m"],  # Cyan and White
    "RC": ["\033[38;2;255;0;0m", "\033[96m"],  # Red and Cyan
    "GM": ["\033[92m", "\033[95m"],  # Green and Magenta
    "YB": ["\033[93m", "\033[94m"],  # Yellow and Blue
    "MW": ["\033[95m", "\033[97m"],  # Magenta and White
    "CR": ["\033[96m", "\033[38;2;255;0;0m"],  # Cyan and Red
    "MG": ["\033[38;2;152;255;152m", "\033[38;2;152;255;152m"],  # Mint Green
    "AQ": ["\033[38;2;0;255;255m", "\033[38;2;0;255;255m"],  # Aqua
    "ABB": ["\033[30m", "\033[30m"],  # All Black

}
  
def is_output_redirected():
    """
    Check if the standard output is being redirected to a file or a console.
    Returns True if output is redirected to a file, False otherwise.
    """
    return not sys.stdout.isatty()



                
def print_color(pattern, *args, delay=None, new_line=True):
    caller_info = inspect.stack()[1]  # Get information about the caller
    calling_line = caller_info.lineno  # Line number where print_color was called
    
    
    global color_patterns
    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
    except Exception as e:
        return
    
    import sys
    
    # Check if the platform is macOS
    if platform.system == "Darwin":
        if pattern in ["AW", "AB"]:
            pattern = "ABB"  # Change to all black on macOS
    

    try:
        if pattern not in color_patterns:
            print(f"Invalid color pattern called from line: {calling_line}")  # Print the line number after the output
            return
            
        colors = color_patterns[pattern]
        redirected = is_output_redirected()


        for arg in args:
            if isinstance(arg, int):  # Ensure proper handling of non-iterable arguments
                arg = str(arg)
            colored_text = ""
            for i, ch in enumerate(arg):
                if not redirected:
                    colored_text += f"{colors[i%2]}{ch}\033[0m"
                else:
                    colored_text += ch

            print(colored_text, end='')  # Default behavior

        if new_line:
            print()  # Print newline if required
        

    except Exception as e:
        print("\nAn error occurred in print_color:", str(e), "at line", calling_line)
        traceback.print_exc()
        




def clear_console():
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    # if manager.gpt_clear_screen_on_run:
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Unix/Linux


def main_thread(operation):
    

    if callable(operation):
        execution_queue.put(operation)
        
    else:
        print("Attempted to enqueue a non-callable operation.")

def execute_queued_functions():

    try:
        while not execution_queue.empty():
            operation = execution_queue.get()
            if callable(operation):
                
                operation()
            else:
                print("Dequeued operation is not callable.")
    except Exception as e:
        print(f"\nError executing queued operation.\n")
        capture_and_copy_traceback()
    return 1.0


def disable_and_save_initial_state_1():
    scene = bpy.context.scene

    # Reset the hidden_states property for a clean slate
    if "hidden_states" in scene:
        del scene["hidden_states"]

    # Initialize hidden_states if it's not already in the scene properties
    scene["hidden_states"] = []

    # Get the list of currently visible objects
    hidden_states = list(scene["hidden_states"])
    # print_color("AW", f"\nInitial hidden_states: {hidden_states}")

    # Iterate through scene objects and save those that are visible
    for obj in scene.objects:
        if not obj.hide_viewport and obj.name not in hidden_states:
            hidden_states.append(obj.name)
            # print_color("AW", f"\nAdding {obj.name} to hidden_states.")

        # Hide the object
        # print_color("AW", f"\nHiding object: {obj.name}")
        obj.hide_viewport = True

    # Assign the updated list back to the scene property
    scene["hidden_states"] = hidden_states
    # print_color("AW", f"\nUpdated scene['hidden_states']: {scene['hidden_states']}")

    my_redraw()

    bpy.ops.fast.info('INVOKE_DEFAULT', message="Objects were disabled safely. There is a button to revert on this panel.", duration=1)
                    
# Operator to restore the hidden states of all objects
class FAST_OT_DiffeomorphicRestoreHiddenObjects(bpy.types.Operator):
    """Restore hidden states of all objects"""
    bl_idname = "fast.restore_hidden_scene_objects"
    bl_label = "Restore Hidden Objects"
    
    def execute(self, context):
        scene = context.scene

        # Check if hidden states have been saved
        if "hidden_states" not in scene or not scene["hidden_states"]:
            self.report({'WARNING'}, "No hidden states to restore.")
            return {'CANCELLED'}
        
        # Retrieve the hidden states directly as a list
        hidden_states = scene.get("hidden_states", [])
        print_color("AW", f"\nhidden_states: {hidden_states}")
        
        # Restore visibility for the objects listed in hidden_states
        for obj_name in hidden_states:
            obj = scene.objects.get(obj_name)
            if obj:
                print_color("AW", f"\nRestoring visibility for: {obj_name}")
                obj.hide_viewport = False
        
        # Clear the stored hidden states after restoring
        scene["hidden_states"] = []

        # Force redraw to update the UI
        bpy.context.view_layer.update()
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        self.report({'INFO'}, "Hidden states restored.")
        return {'FINISHED'}


execution_queue = queue.Queue()
execution_queue_temp = queue.Queue()

def run_in_main_thread_temp(operation):
    
    if callable(operation):
        execution_queue_temp.put(operation)
    else:
        print("Attempted to enqueue a non-callable operation.")

def run_in_main_thread_temp_with_queue(operation, queue, *args, **kwargs):
    if callable(operation):
        def wrapper():
            try:
                result = operation(*args, **kwargs)
                queue.put(result)
            except Exception as e:
                queue.put(e)
        execution_queue_temp.put(wrapper)
    else:
        print("Attempted to enqueue a non-callable operation.")

def execute_queued_functions_temp():
    try:
        while not execution_queue_temp.empty():
            operation = execution_queue_temp.get()
            if callable(operation):
                operation()
            else:
                print("Dequeued operation is not callable.")
    except Exception as e:
        print(f"Error executing queued temp operation: {e}")
        capture_and_copy_traceback()
    return 0.01  # Schedule this function to run again after 0.1 seconds




def print_text_with_equal_signs(text, number, padding):
    # Determine the number of equal signs based on the length of the text and the number
    num_equals = len(text) + len(str(number)) + padding
    
    # Calculate the number of equal signs to print
    equals_line = "=" * num_equals
    
    # Print the formatted result
    print_color("AW", f"\n{equals_line}")
    print_color("AG", f"{text} {number}")
    print_color("AW", equals_line)



def is_likely_python_code(script):

    python_keywords = set(keyword.kwlist)
    common_python_builtins = {"print", "range", "len", "list", "dict", "set", "int", "str", "float", "bool"}
    python_syntax_patterns = [
        r"\bdef\b",  # Function definition
        r"\bclass\b",  # Class definition
        r"\bimport\b",  # Import statement
        r"=\s*lambda\b",  # Lambda function
        r"\bfor\b",  # For loop
        r"\bwhile\b",  # While loop
        r"\bif\b",  # If statement
        r"\"\"\"|\'\'\'",  # Triple quotes (multi-line strings or docstrings)
    ]
    if any(kw in script for kw in python_keywords.union(common_python_builtins)):
        return True
    if any(re.search(pattern, script) for pattern in python_syntax_patterns):
        return True
    return False
    

import platform

if platform.system() == "Windows":
    import msvcrt

    def flush_input():
        """Flush input buffer on Windows."""
        while msvcrt.kbhit():
            msvcrt.getch()

    def getch():
        """Read a single character on Windows without requiring Enter."""
        flush_input()
        while True:
            try:
                char = msvcrt.getch()
                # Handle special key sequences
                if char in [b'\x00', b'\xe0']:  # Special key (e.g., arrows, function keys)
                    msvcrt.getch()  # Discard the next character
                    continue  # Skip to the next iteration
                return char.decode('utf-8').upper()
            except UnicodeDecodeError:
                # Ignore decoding errors and continue looping
                continue

else:
    import sys
    import tty
    import termios
    import select

    def flush_input():
        """Flush input buffer on Linux/macOS."""
        while kbhit():
            sys.stdin.read(1)  # Consume characters without processing them

    def kbhit():
        """Check if a keypress is available on Linux/macOS."""
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        return bool(dr)

    def getch():
        """Read a single character on Linux/macOS without requiring Enter."""
        flush_input()  # Clear any existing input
        old_settings = termios.tcgetattr(sys.stdin)
        try:
            tty.setraw(sys.stdin)  # Set terminal to raw mode
            while True:
                if kbhit():
                    char = sys.stdin.read(1)  # Read a single character
                    return char.upper()  # Return the character in uppercase
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)  # Restore terminal settings



global_start_time = None

def start_t():
    """Record the current time."""
    global global_start_time
    global_start_time = time.time()
    print("Start time recorded:", global_start_time)

def print_t():
    """Print the elapsed time since start_checking_time was called."""
    global global_start_time
    if global_start_time is None:
        print("Error: Start time not recorded. Please call start_checking_time first.")
        return
    
    elapsed_time = time.time() - global_start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
    global_start_time = None


def print_context_attributes(context):
    # Print all attributes of the given context
    for attribute in dir(context):
        print(attribute)



def is_windows_process_running(process_name):
    # List all processes using 'tasklist' command
    process = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    # Check if the process name is in the output
    return process_name in stdout



def draw_gl_text(text, x=15, y=30, size=10, color=(1.0, 1.0, 1.0, 1.0)):
    font_id = 0
    blf.position(font_id, x, y, 0)
    blf.size(font_id, size)
    blf.color(font_id, *color)
    blf.draw(font_id, text)



def my_redraw():
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type in {"VIEW_3D"}:  # You can extend this list if needed
             
                area.tag_redraw()

def my_tag_redraw_areas_func():
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type in {"VIEW_3D"}:  # You can extend this list if needed
                
                area.tag_redraw()

def schedule_redraw():
    bpy.app.timers.register(my_tag_redraw_areas_func, persistent=True, first_interval=0.1)



def get_context_override():
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'window': window, 'screen': screen, 'area': area, 'region': region}
                        return override
    return None



def check_and_handle_disk_space(manager, text, width, print_msg=True):
    current_file_path = bpy.data.filepath


    if not current_file_path:
        if print_msg:
            bpy.ops.fast.info('INVOKE_DEFAULT', message="Blender file path is not set. Unable to check disk space.", duration=1)
        return

    try:
        disk_space = psutil.disk_usage(os.path.dirname(current_file_path)).free
        file_size = os.path.getsize(current_file_path)
    except Exception as e:
        print_color("AR", f"\nError checking disk space.  Restarting Blender should fix this.")

        return 

    # Making sure there's at least two megabytes of space before saving preferences
    is_sufficient_space = disk_space >= (2 * 1024 * 1024)  # 1 MB = 1024 * 1024 bytes
 

    if not is_sufficient_space:
        bpy.ops.fast.info('INVOKE_DEFAULT', message="Not enough disk space to save preferences.", duration=1)
        try:
            manager = bpy.context.preferences.addons[__name__].preferences.Prop
        except Exception as e:
            
            return

        if manager.auto_save_disk_warning_beep:
            beep() 
        if manager.auto_save_disk_warning_message:
            if not manager.is_warning_visible_1: 
                if manager.dismissed_warning_2:
                    manager.dismissed_warning_2 = False
                fast_warning_message_2(text, width=width)
        if manager.auto_save_disk_warning_info_tab:
            bpy.ops.fast.info('INVOKE_DEFAULT', message="Your disk space is getting low...Please run 'Delete BACKUP Files' on 'File Menu' and delete unneeded backups.", duration=1)
    else:
        try:
            save_user_pref_block_info()
        except Exception as e:
            capture_and_copy_traceback()
    
            print(f"An error occurred while saving user preferences: {e}")
            
def save_user_preferences_with_color_change():
    try:
        # Set console color to green
        print("\033[92m", end='')

        # Run the save user preferences operation
        bpy.ops.wm.save_userpref()

        # Reset console color to default
        print("\033[0m", end='')

    except Exception as e:
        print(f"\nERROR SAVING USER PREFERENCES: Only important if it persists.")
        

def save_user_pref_block_info():
    print("")
    from contextlib import redirect_stdout
    stdout = io.StringIO()
    with redirect_stdout(stdout):

        save_user_preferences_with_color_change()


def gpt_daz_block_save_user_preferences():
    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
    except Exception as e:
        
        return
    
 
    if (manager.autogpt_processing == 'Initializing' or 
    
        manager.autogpt_processing == 'Analyzing' or 
        manager.autogpt_processing == 'Waiting for Input'):
        

        return
    
    check_and_handle_disk_space(manager, "Your disk space is getting low!!\nClick 'OK' to see what to delete.", 175, print_msg=False)


def gpt_block_save_file(save_path):
    
    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
    except Exception as e:
       
        return
    try:

        if manager.autogpt_processing == 'Initializing' or manager.autogpt_processing == 'Analyzing' or manager.autogpt_processing == 'Waiting for Input':
            return
    
        missing_textures = False
        error_report = None
    
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            try:
               
                save_result = bpy.ops.wm.save_mainfile(filepath=save_path)
                
    
                # Check the return value
                if save_result == {"FINISHED"}:
                    pass
                else:
                    print("Save operation failed.")
    
            except RuntimeError as ex:
                error_report = "\n".join(ex.args)
                if "Unable to pack file, source path" in error_report:
                    missing_textures = True
    
        if error_report:
            if missing_textures:
                print("\nDid not save file as it had missing textures, see console for details...")
                print("")
                print("------- SAVE ERRORS -------")
                print(error_report)
            else:
                print(error_report)
    except:
        bpy.ops.fast.info('INVOKE_DEFAULT', message="Failed to save file on startup. Please check if you have enough available disk space.", duration=10)
        

def gpt_block_preferences():
    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
    except Exception as e:
        pass

    if manager.autogpt_processing == 'Initializing' or manager.autogpt_processing == 'Analyzing' or manager.autogpt_processing == 'Waiting for Input':
        return
        
    manager.save_pref = True

def print_cond(*args, **kwargs):
    manager = bpy.context.preferences.addons[__name__].preferences.Prop

    if manager.print_enabled:
        print_color("AW", *args, **kwargs)
   
class FAST_OT_open_blender_api(bpy.types.Operator):
    """Open Blender API Documentation"""
    bl_idname = "fast.open_blender_api"
    bl_label = "Open Blender API Doc"

    @classmethod
    def description(cls, context, event):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        if manager.verbose_tooltips:
            return (
                "USE GPT-4 TO TROUBLESHOOT ERRORS:\n\n"
                "- Find 'bpy.ops': Identifies Blender operations. Note the operator name.\n"
                "- Property Errors: Look for 'AttributeError' and the related property name.\n"
                "- Python Types/Structs: Find type/struct name in errors containing 'TypeError' or 'struct'.\n"
                "- Context Errors: If 'incorrect context' occurs in the surrounding text,\n"
                "     then search for 'temp_override' on API and paste relevant section,\n\n"
                "EXTRACTING INFO:\n"
                "- Find only the relevant term (e.g., 'bpy.ops_mesh', 'object.location').\n"
                "- Avoid pasting entire error in API; paste the specific term or function name.\n\n"
                "USING API DOC:\n"
                "- Paste/Search the specific term in the Blender API search field.\n"
                "- Click 'Autonomous GPT-4' button And paste your full code/API section/error.\n"
                "- Add relevant info like: Blender API version, what you tried, & the results of it.\n"
                "- Explore related sections for solutions and context.\n\n"
                "Precise identification leads to efficient troubleshooting.\n\n"
                "GPT4 is very smart, it can figure these things out quickly with the right information.\n\n"
                "Please note that I am working on an automatic error fixing system right now"
            )
        else:
            return "Decode errors with the Blender API and GPT-4. Verbose tool-tip available"

    def execute(self, context):
        webbrowser.open("https://docs.blender.org/api/current/")
        return {'FINISHED'}



class FAST_OT_backup_file(bpy.types.Operator):
    bl_idname = "fast.backup_file"
    bl_label = "Operator Backup File"
    bl_options = {"REGISTER", "UNDO"}

    filename: bpy.props.StringProperty(
        name="Filename",
        description="Filename for the backup",
        default="",
    )

    # Overwrite flag
    overwrite: bpy.props.BoolProperty(
        name="Overwrite",
        description="If set to True, overwrite the existing backup file",
        default=False)


    def check_disk_space(self):
        # Attempt to import psutil, if it fails, return a warning message along with False for file path being set
        try:
            import psutil
        except ImportError:
            self.report({'INFO'}, "Unable to perform disk space check. Please install dependencies in Preferences.")
            return (False, False)
    
        # Get the size of the current Blender file
        current_file_path = bpy.data.filepath
        
        if not current_file_path:
            # Return False for disk space check and False indicating Blender file path is not set
            return (False, False)
    
        # Check available disk space on the drive where the Blender file is stored
        disk_space = psutil.disk_usage(os.path.dirname(current_file_path)).free
        file_size = os.path.getsize(current_file_path)
    
        return (disk_space >= 2.5 * file_size), True

    def execute(self, context):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        disk_space_ok, file_path_set = self.check_disk_space()
    
        if not disk_space_ok:
            if not file_path_set:
                self.report({'ERROR'}, "Blender file path is not set. Unable to check disk space.")
            else:
                print("")
                self.report({'ERROR'}, "Not enough disk space to complete file backup.")
    
            if manager.auto_save_disk_warning_beep:
                log("beep")
                beep() 
            if manager.auto_save_disk_warning_message:
                if (not manager.is_warning_visible_1): 
                    if manager.dismissed_warning_2:
                        manager.dismissed_warning_2 = False
                    fast_warning_message_2("Your disk space is getting low!!\nClick 'OK' to see what to delete.", width=175)
            if manager.auto_save_disk_warning_info_tab:
                bpy.ops.fast.info('INVOKE_DEFAULT', message="Your disk space is getting low...Please run 'Delete BACKUP Files' on 'File Menu' and delete unneeded backups.", duration=1)
            return {'CANCELLED'}
        
        try:
            path = manager.fast_save_path
    
            if not path:
                self.report({"ERROR"}, "Must set FAST scripts path in Blender preferences.")
                return {"CANCELLED"}
    
    
            for text in bpy.data.texts:
                p = os.path.join(path, text.name)
                if not p.endswith(".py"):
                    p += ".py"
                with open(p, "w") as f:
                    f.write(text.as_string())
    
            # Save user preferences
            print("")
            manager.save_pref = True
    
            # Redirect stdout
            stdout = io.StringIO()
            error_report = None
    
            with redirect_stdout(stdout):
                try:
                    print("")
                    save_result = bpy.ops.wm.save_mainfile(filepath=bpy.context.blend_data.filepath)
                    print("")
                    if save_result == {"FINISHED"}:
                        print("Save operation successful")
                    else:
                        print("Save operation failed")
                except RuntimeError as ex:
                    error_report = "\n".join(ex.args)
    
            stdout.close()  # Close the redirected stdout
    
            if error_report:
                self.report({"WARNING"}, error_report)
                return {"CANCELLED"}
    
        except Exception as e:
            capture_and_copy_traceback()
            self.report({"ERROR"}, f"Could not complete save operation: {str(e)}")
            return {"CANCELLED"}
    
        return {"FINISHED"}


# Function to time execution of another function
def time_function(func, *args):
    start_time = time.time()
    result = func(*args)
    elapsed_time = time.time() - start_time
    return elapsed_time, result

# Fast Connection Checker using DNS Resolution
def fast_connection_checker():
    try:
        # Attempt to resolve Google's domain name to an IP address
        socket.gethostbyname("www.google.com")
        return True
    except socket.error:
        return False


def find_3d_viewport():
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == "VIEW_3D":
                space = area.spaces[0]
                # if space.local_view:
                #     manager.fast_local_mode_enabled = True
                    
                # elif not space.local_view:
                #     manager.fast_local_mode_enabled = False
                    
                for region in area.regions:
                    if region.type == "WINDOW":
                        return {
                            "window": window,
                            "screen": window.screen,
                            "area": area,
                            "region": region,
                        }
    return None


def reset_restart_properties():
    """Reset all restart-related properties to False."""
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    
    manager.restart_after_verify = False
    manager.restart_after_key = False
    manager.restart_after_addon_enabled = False
    manager.restart_after_addons = False
    manager.restart_after_dependencies = False
    manager.restart_after_update = False
    caller_info = inspect.stack()[1]  # Get information about the caller
    calling_line = caller_info.lineno  # Line number where print_color was called

    print_color("AR", f"\n[Line: {calling_line}") 
    print("\nRestart-related properties have been reset.")


new_filename = ""

def bring_blender_to_foreground():
    try:

        try:
            import pywinctl as gw
        except:
            pass

        try:
            windows = gw.getAllWindows()
        except Exception as e:
            print(f"Error getting windows:\n")
            capture_and_copy_traceback()
            return

        for window in windows:
           
            if "Blender 4.3" in window.title:
                # Check if the title contains a backslash or 'unsaved'
                if "\\" in window.title or "unsaved" in window.title.lower():
                    
                    try:
                        # Adding a delay before bringing to foreground
                        time.sleep(0.5)
                        window.activate()
                        window.restore()
                        window.show()
                        time.sleep(0.5)  # Adding a delay after bringing to foreground
        
                        return
                    except Exception as e:
                        print(f"Error bringing window to the foreground:\n")
                        capture_and_copy_traceback()
                        


    except Exception as e:
        print(f"Error in bring_blender_to_foreground:\n")
        capture_and_copy_traceback()


# Without this uh when you restart blenderwith the clear consoles uncommentedthen you'll get a jumbled mess of characters where the print color statement should be
# Without this uh when you restart blenderwith the clear consoles uncommentedthen you'll get a jumbled mess of characters where the print color statement should be
def get_blender_executable():
    """
    Returns the appropriate Blender executable path dynamically.
    """
    blender_path = bpy.app.binary_path

    # Get the base directory where Blender is installed
    blender_dir = os.path.dirname(blender_path)

    # Define possible Blender executables
    blender_exe = os.path.join(blender_dir, "blender.exe")
    blender_launcher = os.path.join(blender_dir, "blender-launcher.exe")

    # Choose which executable to return
    if os.path.exists(blender_exe):
        return blender_exe  # Prefer Blender Launcher if it exists
    elif os.path.exists(blender_launcher):
        return blender_launcher  # Fallback to standard Blender executable
    else:
        raise FileNotFoundError("Blender executable not found in expected directory.")


# You just save them to a temporary file and then next time blender is started up if those values aren't right set them back
class FAST_OT_confirm_and_restart_blender(bpy.types.Operator):
    bl_idname = "fast.confirm_and_restart_blender"
    bl_label = "Let's Restart Blender!"
    bl_options = {"REGISTER"}

    string: bpy.props.StringProperty(default="")
    width: bpy.props.IntProperty(default=400)
    initial_cursor_pos = None

    def restart_blender_1(self):

  
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        manager.is_restarting = True 
        save_user_pref_block_info()       
               
        blender_exec_path = get_blender_executable()
        
        current_file_path = bpy.data.filepath

        
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        if not manager.save_file_before_restart:
            current_file_path=""

        # Construct command for subprocess
        command = [blender_exec_path]
        
        if current_file_path:
            command.append(current_file_path)

        try:
          
            a=subprocess.Popen(command, close_fds=True)
            
     
            bring_blender_to_foreground()
            
            
            save_user_pref_block_info()
     
            bpy.ops.wm.quit_blender()
            manager.restart_after_verify=False
            manager.restart_after_key=False
            manager.restart_after_addon_enabled=False
            manager.restart_after_addons=False
            manager.restart_after_dependencies=False
            manager.restart_after_update=False

            fast_folder_path = os.path.join(bpy.utils.user_resource("SCRIPTS"), "addons", "blender_ai_thats_error_proof")
            key_file_path = os.path.join(fast_folder_path, "key.ini")

            if not os.path.exists(key_file_path):
                manager.print_carrier = "Please enter a license key and press enter when finished."
            else:
                manager.print_carrier = "A valid license key was noticed...No need to enter one."

            save_user_pref_block_info()

            print(f"\nRestarting now.")

        except Exception as e:
            capture_and_copy_traceback()
            reset_restart_properties()
            self.report({'ERROR'}, "Failed to restart Blender: {}".format(e))
    

    
    

            
    def invoke(self, context, event):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        region = None
  
        
        if manager.show_restart_message:
            

            for area in context.screen.areas:
               
                if area.type == "VIEW_3D":
          
                    for region in area.regions:
                        if region.type == "WINDOW":
                 
                            f = io.StringIO()
                            with redirect_stdout(f):
                                try:
                                    # Attempt to use pyautogui to get screen size
                                    import pyautogui
                                    screen_size = pyautogui.size()
                                    screen_width, screen_height = screen_size.width, screen_size.height
                                except ImportError:
                                    reset_restart_properties()
                                    region = [r for r in context.screen.areas if r.type == "VIEW_3D"][0].regions[-1]
                                    screen_width, screen_height = region.width, region.height
                                    f.close()
                            f.close()
                
    
                            # Calculate the center of the screen
                            screen_center_x = screen_width // 2
    
                            screen_center_y = screen_height // 2
    
                            # Calculate the starting X position for the message box to be centered
                            message_box_start_x = screen_center_x
    
                            # Apply offsets to fine-tune the position
                            final_x = message_box_start_x + manager.offset_x
              
                            
                            final_y = screen_center_y + manager.offset_y
          
    
                            #print("cursor warp is active")
                            context.window.cursor_warp(final_x, final_y)
  
        
            return context.window_manager.invoke_props_dialog(self, width=self.width)
    
        elif manager.show_restart_message_no_save:
 

            # If viewport is found or if showing the restart message is not required
            return context.window_manager.invoke_props_dialog(self, width=self.width)
        
        else:
            clear_console()
            self.restart_blender_1()
            return {'FINISHED'}
        

    def draw(self, context):
        layout = self.layout
        # Split the string into separate lines based on the newline character
        lines = self.string.split('\n')
        # Iterate over each line and create a label for it
        for line in lines:
            if line:  # This checks if the line is not empty
                layout.label(text=line)

    def execute(self, context):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        clear_console()
        self.restart_blender_1()

        return {"FINISHED"}


    def cancel(self, context):
        """Reset restart-related properties when the operation is canceled."""
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        
        manager.restart_after_verify = False
        manager.restart_after_key = False
        manager.restart_after_addon_enabled = False
        manager.restart_after_addons = False
        manager.restart_after_dependencies = False
        manager.restart_after_update = False
        
        self.report({'INFO'}, "Restart operation canceled. All flags reset.")
        return None
    
    
    


def confirm_and_restart_blender(string, width=400):
    
    # Create the override dictionary
    bpy.ops.fast.confirm_and_restart_blender("INVOKE_DEFAULT", string=string, width=width)
    return


def close_preferences_or_file_view_window():
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    if FAST_OT_close_windows_safely.prevent_window_closing:
  
        return
    try:
        try:
            import pywinctl as gw
        except ImportError:
            reset_restart_properties()
            return

        try:
            windows = gw.getAllWindows()
        except ModuleNotFoundError:
            reset_restart_properties()
            return
        workspace = bpy.context.window.workspace.name
        for window in windows:
            if "Blender Preferences" in window.title or "Preferences" in window.title:
                try:
                    window.close()  # Minimize the window
                    return
                except Exception as e:
                    capture_and_copy_traceback()
                    reset_restart_properties()
                    print(f"\nError minimizing window: {e}")

            if "Blender File View" in window.title and workspace != "Shading":
                try:
                    window.close()  # Minimize the window
                    return
                except Exception as e:
                    reset_restart_properties()
                    capture_and_copy_traceback()
                    print(f"\nError minimizing window: {e}")
    except Exception as e:
        capture_and_copy_traceback()
        reset_restart_properties()
        print(f"\nError in close_preferences_window: {e}")


check_filepath = ''
file_was_saved = False
save_file_before_restart = False

def save_before_restart():
    global check_filepath, file_was_saved, save_file_before_restart


    if not save_file_before_restart:
        return
    
    if file_was_saved:
        return True
    
    filepath = bpy.data.filepath

    if not filepath:
        
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        filepath = os.path.join(desktop_path, "scratch.blend")
        
    try:
        time.sleep(0.1)
        
        print("")
        result = bpy.ops.wm.save_mainfile(filepath=filepath, check_existing=False)
        save_user_pref_block_info()

        # Check if both saves returned a 'FINISHED' status
        if 'FINISHED' in result:
            check_filepath = filepath
            print_color("AR", "\nYour file was saved securely and verified...")
    
            return True
        
    except RuntimeError as ex:
        error_message = "\n".join(ex.args)
        reset_restart_properties()
        # Check for missing textures
        if "Unable to pack file, source path" in error_message:
            missing_textures = any(image.filepath == '' and not image.packed_file for image in bpy.data.images)
            if missing_textures:
                for image in bpy.data.images:
                    if image.filepath == '' and not image.packed_file:
                        print_color("AG", f"\nMissing texture: {image.name}")
                        print_color("AR", f"\nCannot save file. Cannot restart Blender as file is unsaved.\n")
                # Return False for missing textures as it's a critical error.
                return False

        # Log the 'CustomData_blend_write' error but consider it non-critical
        if "CustomData_blend_write error" in error_message:
            print_color("AR", f"\nNon-critical custom data error encountered: {error_message}")
            # Log additional details or handle accordingly.
            return False


        if "No space left on device" in error_message:
            bpy.ops.fast.info('INVOKE_DEFAULT', message="No space left on device.", duration=1)
            # Log additional details or handle accordingly.
            return False
            
        # Handle other RuntimeErrors
        print_color("AR", f"\nOther RuntimeError encountered: {error_message}")
        return False

def check_disk_space():
    global check_filepath
    global file_was_saved
    global save_file_before_restart

    try:
        try:
            if not save_file_before_restart:
                return True

            elif save_file_before_restart:
                check_filepath = bpy.data.filepath
                if not check_filepath:
                    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
                    check_filepath = os.path.join(desktop_path, "scratch.blend")
                    try:
                        print("")
                        if not file_was_saved:
                            # Save the current Blender file and check if it finished successfully
                            result = bpy.ops.wm.save_mainfile(filepath=check_filepath, check_existing=False)
                            file_was_saved = True  # Update the class variable

                            # Check if both saves returned a 'FINISHED' status
                            if 'FINISHED' in result:
                                print("\nYour file was securely saved and verified...")
                                print("")
                                return True

                    except RuntimeError as ex:
                        reset_restart_properties()
                        error_message = "\n".join(ex.args)

                        # Check for missing textures
                        if "Unable to pack file, source path" in error_message:
                            missing_textures = any(image.filepath == '' and not image.packed_file for image in bpy.data.images)
                            if missing_textures:
                                for image in bpy.data.images:
                                    if image.filepath == '' and not image.packed_file:
                                        print_color("AG", f"\nMissing texture: {image.name}")
                                # Return False for missing textures as it's a critical error.
                                return False

                        # Log the 'CustomData_blend_write' error but consider it non-critical
                        if "CustomData_blend_write error" in error_message:
                            print_color("AR", f"Non-critical custom data error encountered: {error_message}")
                            # Log additional details or handle accordingly.
                            return True

                        # Handle other RuntimeErrors
                        print_color("AR", f"Other RuntimeError encountered: {error_message}")
                        return True

                try:
                    import psutil
                except ImportError:
                    reset_restart_properties()
                    self.report({'INFO'}, "Unable to perform disk space check. Please install dependencies in preferences.")
                    return False

                if check_filepath:
                    file_size = os.path.getsize(check_filepath)

                # Check available disk space on the drive where the Blender file is stored
                disk_space = psutil.disk_usage(os.path.dirname(check_filepath)).free

                # Check if available space is at least 2.5 times the size of the current file
                required_space = 1.5 * file_size
                if disk_space >= required_space:
                    return True
                else:
                    print("Insufficient disk space available.")
                    return False

        except Exception as e:
            reset_restart_properties()
            print(f"An error occurred while checking disk space: {str(e)}")
            capture_and_copy_traceback()
            return False

    except Exception as outer_e:
        reset_restart_properties()
        print(f"Critical error in check_disk_space function: {str(outer_e)}")
        capture_and_copy_traceback()
        return False

    # def execute(self, context):
    #     manager = bpy.context.preferences.addons[__name__].preferences.Prop
        
    #     save_before_restart = self.check_need_save()
    #     if manager.restart_close_windows:
    #         # CAPTURE INITIAL STATE OF AREAS BEFORE CLOSING
    #         before_close = {area_type: list_open_areas(area_type) for area_type in self.area_types_to_close}
    #         # DECIDE WHICH AREAS TO CLOSE BASED ON BEFORE_CLOSE VARIABLE
    #         areas_to_actually_close = {area_type for area_type, areas in before_close.items() if len(areas) > 0}
    
    #         if areas_to_actually_close:  # Check if there are actually areas to close
    #             print("Areas to actually close...")
    
    #             self.close_areas(areas_to_actually_close)
    #             # CAPTURE STATE OF AREAS AFTER CLOSING
    #             after_close = {area_type: list_open_areas(area_type) for area_type in self.area_types_to_close}
    #             all_closed = all(len(after_close[area_type]) == 0 for area_type in areas_to_actually_close)
    
    #             if all_closed:
    #                 pass


def update_handle_from_file(file_name, property_name):
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    settings_directory = os.path.join(documents_path, "FAST Settings", "window_handles")
    file_path = os.path.join(settings_directory, file_name)

    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                handle = int(file.read().strip())  # Read and convert the handle to an integer
                if handle:
                    manager = bpy.context.preferences.addons[__name__].preferences.Prop
                    setattr(manager, property_name, handle)  # Dynamically set the property based on the handle read
                    print(f"Updated {property_name} with handle: {handle} from file.")
    except Exception as e:
        reset_restart_properties()
        print(f"Error updating handle from file {file_name}: {str(e)}")




save_before_restart_var = False
window_closed_flag = False
class FAST_OT_close_windows_safely(bpy.types.Operator):
    bl_idname = "fast.close_windows_safely"
    bl_label = "Close Windows Safely"
    bl_description = "Close specified windows safely and check if closed"
    bl_options = {'REGISTER'}

    _check_interval = 0.5  # Check every 0.5 seconds
    _timer = None
    _start_time = None
    _timeout = 4 
    _last_check_time = None
    

    prevent_window_closing = False

    def close_window(self, hwnd):
        try:

            manager = bpy.context.preferences.addons[__name__].preferences.Prop
            if self.prevent_window_closing:
     
                return
    
            if not self.prevent_window_closing:
                close_preferences_or_file_view_window()
      
            elif hwnd and hwnd != 0:
                SW_HIDE = 0
                ctypes.windll.user32.ShowWindow(hwnd, SW_HIDE)
                ctypes.windll.user32.PostMessageW(hwnd, 0x0010, 0, 0)  
                print("Invalid window handle. Skipping close operation.")

        except Exception as e:
            print(f"Error closing window: {e}")
            reset_restart_properties()
            capture_and_copy_traceback()

    
    def modal(self, context, event):
        global window_closed_flag
        current_time = time.time()
    
        # Timeout logic
        if self._start_time and (current_time - self._start_time > self._timeout):
            print_color("AR", f"\nTimeout reached, forcing window close...")
            if not self.prevent_window_closing:
                close_preferences_or_file_view_window()
                
            finish_restart()
            self.finish(context)
            return {'FINISHED'}

        if window_closed_flag:
            print(f"\nWindow closed flag was true: {window_closed_flag}")
            finish_restart()
            self.finish(context)
            return {'FINISHED'}

        preferences_open = list_open_areas("PREFERENCES")
        
        file_browser_open = list_open_areas("FILE_BROWSER")
        workspace = bpy.context.window.workspace.name
    
        if workspace == "Shading" and not preferences_open:
            
            finish_restart()
            self.finish(context)
            return {'FINISHED'}
    
        if not preferences_open and not file_browser_open:
            
            finish_restart()
            self.finish(context)
            return {'FINISHED'}
    
        
        try:
            result = self.attempt_to_close_windows(context, preferences_open, file_browser_open)
            
            if result == {'FINISHED'}:
                finish_restart()
                self.finish(context)
                return {'FINISHED'}
        except Exception as e:
            reset_restart_properties()
            capture_and_copy_traceback()
            print(f"Error in modal loop: {e}")
    
        
        return {'RUNNING_MODAL'}
    

    def attempt_to_close_windows(self, context, preferences_open, file_browser_open):
     
        
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        if self.prevent_window_closing:
            
            return {'FINISHED'}
    
        if preferences_open:
            
            close_preferences_or_file_view_window()
            bpy.app.timers.register(lambda: (verify_window_closed("PREFERENCES"), None)[1], first_interval=0.1)
            return {'RUNNING_MODAL'}
    
        workspace = bpy.context.window.workspace.name
        if file_browser_open and workspace != "Shading":
            
            close_preferences_or_file_view_window()
            bpy.app.timers.register(lambda: (verify_window_closed("FILE_BROWSER"), None)[1], first_interval=0.1)
            return {'RUNNING_MODAL'}
    
        return {'RUNNING_MODAL'}
    


    def invoke(self, context, event):
        self._start_time = time.time()
        self._last_check_time = None

        


        self._timer = context.window_manager.event_timer_add(0.1, window=context.window)
        if self._timer is None:
            print("Failed to add timer! Cancelling operator.")
            return {'CANCELLED'}

        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def finish(self, context):
        if self._timer:
            context.window_manager.event_timer_remove(self._timer)
            self._timer = None
        return {'FINISHED'}

    def cancel(self, context):
        if self._timer:
            context.window_manager.event_timer_remove(self._timer)
            self._timer = None
        return None

def verify_window_closed(area_type):
    global window_closed_flag
    if not window_closed_flag:
        
        if not list_open_areas(area_type):
           
            window_closed_flag = True
            finish_restart()
            return None
    else:
        return None
 
    




def list_open_areas(area_type):
    open_areas = []
    
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            
            if area.type == area_type:
                
                if area_type == "FILE_BROWSER":
                    try:
                        import pywinctl as gw
                        
                        file_view_windows = [window for window in gw.getAllWindows() if "Blender File View" in window.title]
                        
                        
                        if not file_view_windows:
        
                            if len(open_areas) == 0:
                                return []  
                    except ModuleNotFoundError:
                        reset_restart_properties()
                        
                
                
                open_areas.append(area.type)
             
    if len(open_areas) == 0:
        return []  
    return open_areas




finish_restart_executed = False

def finish_restart():
    global finish_restart_executed  


    
    if finish_restart_executed:
        print(f"\nFinish restart function was already run. Returning from function.")
     
        return

    
    finish_restart_executed = True

        
    caller_info = inspect.stack()[1]
    calling_line = caller_info.lineno

    global check_filepath

    global save_before_restart_var
    
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    
    if save_before_restart_var and not manager.restart_after_addons and not manager.restart_after_dependencies and not manager.restart_after_update and not manager.restart_after_key and not manager.restart_after_verify and not manager.restart_after_addon_enabled:
        

        result = save_before_restart()
 
        if result:
            bpy.ops.fast.info('INVOKE_DEFAULT', message=f"Your file was saved to {check_filepath}.", duration=1)
            msg = "File was Saved. Click 'OK' to Restart."
            bpy.ops.fast.confirm_and_restart_blender("INVOKE_DEFAULT", string=msg, width=195)
    
    elif manager.restart_after_addons and save_before_restart_var:
   
        result = save_before_restart()
        if result:
            bpy.ops.fast.info('INVOKE_DEFAULT', message=f"Your file was saved to {check_filepath}.", duration=1)
            msg = "File was Saved. Click 'OK' to Restart."
            confirm_and_restart_blender(msg, width=195)

    elif manager.restart_after_addon_enabled and save_before_restart_var:
        
        result = save_before_restart()
        if result:
            bpy.ops.fast.info('INVOKE_DEFAULT', message=f"Your file was saved to {check_filepath}.", duration=1)
            msg = "Addon Enabled. Save & Restart??"
            "Addon Enabled. Click 'OK' to Save & Restart."
            confirm_and_restart_blender(msg, width=180)

    elif manager.restart_after_dependencies and save_before_restart_var:

        result = save_before_restart()
        if result:
            bpy.ops.fast.info('INVOKE_DEFAULT', message=f"Your file was saved to {check_filepath}.", duration=1)
            msg = "PIP Libraries Were Just Installed.\nInstall Info is Available in Console.\nFile Was Saved. Click 'OK' to Restart.\n"
            beep(setable_frequency=None, setable_volume=0.1)
            confirm_and_restart_blender(msg, width=200)

    elif manager.restart_after_update and save_before_restart_var:

        result = save_before_restart()
        if result:
            bpy.ops.fast.info('INVOKE_DEFAULT', message=f"Your file was saved to {check_filepath}.", duration=1)
            msg = "File was Saved. Click 'OK' to Restart."
            confirm_and_restart_blender(msg, width=185)
    
    elif manager.restart_after_key and save_before_restart_var:
        
        result = save_before_restart()
        if result and manager.lks:
           
            msg = "Verification Has Been Completed.\nYour File's Saved. Click 'OK' to Restart."
            confirm_and_restart_blender(msg, width=215)

    elif manager.restart_after_verify and save_before_restart_var:

    
        result = save_before_restart()
       
        if result:
            bpy.ops.fast.info('INVOKE_DEFAULT', message=f"Your file was saved to {check_filepath}.", duration=1)
            msg = "File was Saved. Click 'OK' to Restart."
            confirm_and_restart_blender(msg, width=195)

    else:
        msg = "File was Not Saved. Click 'OK' to Restart."
        bpy.ops.fast.confirm_and_restart_blender("INVOKE_DEFAULT", string=msg, width=219)



class FAST_OT_restart_blender(bpy.types.Operator):
    bl_idname = "fast.restart_blender"
    bl_label = "Restart Blender. BLUE: Save file GREEN: Not Save file"
    bl_options = {"REGISTER"}

    
    close_windows: bpy.props.BoolProperty(
        name="Close Windows",
        description="Set to True to enable window closing during restart",
        default=True
    )

    @classmethod
    def description(cls, context, event):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        if manager.verbose_tooltips:
            return ("\n\nSaves your file securely and then restarts Blender to current scene.\n\n"
                "#0 Closes any open windows, so you don't risk unusable windows, after restart.\n\n"
                "#1 If the file is already named and saved, it's saved to current folder.\n\n"
                "#2 Unsaved files are automatically preserved on the Desktop as 'scratch.blend'.\n\n"
                "#3 Note: Restarting can help scene lags"
            )
        else:
            return "Saves file securely and restarts Blender, saving unsaved files to Desktop. Verbose tool-tip available"
    
    area_types_to_close = {"PREFERENCES", "FILE_BROWSER"}
    show_message: bpy.props.BoolProperty(default=False)
    show_message_no_save: bpy.props.BoolProperty(default=False)
    new_msg = ""

    # New property to control whether to save before restart
    save_file_before_restart: bpy.props.BoolProperty(
        name="Save Before Restart",
        description="Save the current file before restarting Blender",
        default=False
    )

    def check_need_save(self):
        global filepath
        global file_was_saved
        global save_file_before_restart
        save_file_before_restart = self.save_file_before_restart

        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        manager.save_file_before_restart = self.save_file_before_restart
        manager.show_restart_message = self.show_message
        manager.show_restart_message_no_save = self.show_message_no_save
        if save_file_before_restart:
            return True
        else:
            return False

    def ensure_solid_mode(self, context):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        if manager.force_solid_mode:
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            # Check if we are already in solid mode
                            if space.shading.type != 'SOLID':
                                # Switch to solid mode
                                space.shading.type = 'SOLID'
                                print("Switching to Solid Mode to prevent crashes.")

    def execute(self, context):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop

        global filepath
        global file_was_saved
        global save_file_before_restart
        global save_before_restart_var
        global finish_restart_executed
        finish_restart_executed = False

        # Check disk space before proceeding
        if not check_disk_space():
            beep()
            bpy.ops.fast.info('INVOKE_DEFAULT', message="Insufficient disk space available. Operation cancelled.", duration=5)
            print_color("AR", f"\nInsufficient disk space available. Operation cancelled.")
            return {'CANCELLED'}  
        else:
            print_color("AR", f"\nDisk space available.")
            
        if manager.force_solid_mode:

            self.ensure_solid_mode(context)

        save_before_restart_var = self.check_need_save()

  
        FAST_OT_close_windows_safely.prevent_window_closing = True if not self.close_windows else False


        # Invoke the window-closing functionality
        bpy.ops.fast.close_windows_safely('INVOKE_DEFAULT')

        return {'FINISHED'}

def show_console_ste():
    bpy.ops.fast.show_console()
    bpy.ops.fast.show_console()
    try:
        pyautogui.hotkey('ctrl', 'shift', 'end')
    except Exception as e:
        pass


def ask_to_restart_enable():

    try:
        
        manager = bpy.context.preferences.addons[__name__].preferences.Prop

        save_user_pref_block_info()
        manager.restarted_blender_information = True
        bpy.ops.fast.restart_blender(show_message=False, save_file_before_restart=True)
        
    except:
        print("Restart after enabling was not invoked.")


def ask_to_restart_dependencies():

    
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    manager.restart_after_dependencies=True

    bpy.ops.fast.restart_blender(show_message=True, save_file_before_restart=True)

    manager.startup_done_dependencies = True



def gpt_save_user_pref_block_info():
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    if manager.gpt_do_not_save_userpref_while_running:
        return

    print("")
    from contextlib import redirect_stdout
    stdout = io.StringIO()
    with redirect_stdout(stdout):

        save_user_preferences_with_color_change()


def indent(text, spaces=4):
    indent_str = ' ' * spaces
    return indent_str + text.replace('\n', '\n' + indent_str)

def unindent(text, spaces=4):
    indent_str = ' ' * spaces
    return text.replace('\n' + indent_str, '\n').lstrip(indent_str)

class FAST_OT_draw_centered_info(bpy.types.Operator):
    bl_idname = "fast.draw_centered_info"
    bl_label = "FAST Information:"
    # bl_options = {"REGISTER"}  # Explicitly define bl_options

    string: bpy.props.StringProperty(default="")
    wrap: bpy.props.BoolProperty(default=False)
    width: bpy.props.IntProperty(default=400)
    offset_x: bpy.props.IntProperty(default=0)
    offset_y: bpy.props.IntProperty(default=0)
    use_popup: bpy.props.BoolProperty(default=False)

    def invoke(self, context, event):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        for area in context.screen.areas:
            if area.type == "VIEW_3D":
                for region in area.regions:
                    if region.type == "WINDOW":
                        try:
                            screen_size = pyautogui.size()
                        except Exception as e:
                            capture_and_copy_traceback()

                            # If pyautogui is not installed, use the dimensions of the 3D View region
                            region = [r for r in area.regions if r.type == "WINDOW"][0]
                            screen_size = type("Size", (object,), {"width": region.width, "height": region.height})()
                            # Report to the user that pyautogui is not installed
                            self.report({"INFO"}, "PyAutoGUI is not installed. Defaulting to 3D Viewport size.")
                            # print("Error: ", str(e))

                        screen_width, screen_height = (screen_size.width, screen_size.height)

                        # Calculate the center of the screen
                        screen_center_x = screen_width // 2

                        screen_center_y = screen_height // 2

                        # Calculate the starting X position for the message box to be centered
                        message_box_start_x = screen_center_x

                        # Apply offsets to fine-tune the position
                        final_x = message_box_start_x + manager.offset_x
              
                        final_y = screen_center_y + manager.offset_y

                        #print("cursor warp is active")
                        context.window.cursor_warp(final_x, final_y)
        
                        if self.use_popup:
                            return context.window_manager.invoke_popup(self, width=self.width)
                        else:
                            return context.window_manager.invoke_props_dialog(self, width=self.width)
                   
        # If we don't find a VIEW_3D area, report an error
        self.report({"ERROR"}, "No 3D Viewport found")
        return {"CANCELLED"}

    def draw(self, context):
        layout = self.layout
        if "\n" in self.string:  # Check for multi-line string
            for line in self.string.split("\n"):
                layout.label(text=line)
        else:
            if self.wrap:
                wrap_text(layout, string=self.string, text_length=30, center=False)
            else:
                layout.label(text=self.string)

    def execute(self, context):
        return {"FINISHED"}


def draw_centered_info(
    string, title=None, width=315, wrap=False, offset_x=0, offset_y=0, use_popup=False
):
    if title:
        FAST_OT_draw_centered_info.bl_label = title

    bpy.ops.fast.draw_centered_info(
        "INVOKE_DEFAULT",
        string=string,
        width=width,
        wrap=wrap,
        offset_x=offset_x,
        offset_y=offset_y,
        use_popup=use_popup,
    )



def get_current_version():
    current_version = "unknown"  # Default value
    for mod in addon_utils.modules():
        if mod.__name__ == "blender_ai_thats_error_proof":
            version_tuple = mod.bl_info.get("version", (-1, -1, -1))
            current_version = ".".join(map(str, version_tuple))
            break  # Exit the loop once the FAST module version is found
    return current_version



# Get the path to the scripts directory
scripts_path = bpy.utils.user_resource("SCRIPTS")

# Append the remaining parts of the path to the FFMPEG executable
lib_path = os.path.join(scripts_path, "addons", "blender_ai_thats_error_proof", "lib", "Python311", "site-packages")
ffmpeg_exe_path = os.path.join(lib_path, "ffmpeg.exe")


def beep(setable_frequency=None, setable_volume=None):
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    if manager.use_beep:
        try:
            prefs = bpy.context.preferences.system
            max_retries = 3

            current_platform = platform.system()

            # For Windows
            if current_platform == "Windows":
                if prefs.audio_device == "OpenAL":
                    for _ in range(max_retries):
                        prefs.audio_device = "WASAPI"
                        if prefs.audio_device == "WASAPI":
                            break
                    for _ in range(max_retries):
                        prefs.audio_device = "OpenAL"
                        if prefs.audio_device == "OpenAL":
                            break
            

            if not os.path.exists(ffmpeg_exe_path):
                print("You need to install FFMPEG. Please restart Blender after installing1.")
                return

            warnings.filterwarnings(
                "ignore", category=RuntimeWarning, module="pydub.utils"
            )
            try:
                from pydub.generators import Sine
                from pydub.playback import play
                from pydub import AudioSegment
                import audioop
            except ModuleNotFoundError:
                print("You need to install dependencies in FAST/Preferences/INSTALL.")

                return
            AudioSegment.converter = os.path.join(lib_path, "ffmpeg.exe")
            # Ignore RuntimeWarning from pydub
            warnings.filterwarnings(
                "ignore", category=RuntimeWarning, module="pydub.utils"
            )

            if setable_frequency is not None:
                frequency = setable_frequency
            else:
                frequency = manager.beep_frequency  # Set Frequency To 2500 Hertz

            if setable_volume is not None:
                volume = setable_volume
            else:
                volume = manager.beep_volume

            duration = manager.beep_duration  # Set Duration To 200 ms

            try:
                beep_sound = (Sine(frequency)).to_audio_segment(duration=duration)

                # Adjust the volume of the beep sound using audioop
                beep_bytes = beep_sound.raw_data
                adjusted_beep_bytes = audioop.mul(beep_bytes, beep_sound.sample_width, volume
                )

                # Create a new AudioSegment with the adjusted audio data
                beep_sound = beep_sound._spawn(adjusted_beep_bytes)
                play(beep_sound)
            except NameError:
                pass
        except Exception as e:
            capture_and_copy_traceback()

            print(
                f"An unexpected exception occurred in beep(): {type(e).__name__} - {str(e)}"
            )
            
def gpt_beep(setable_frequency=None, setable_volume=None):
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    if manager.gpt_use_beep:
        try:
            prefs = bpy.context.preferences.system
            max_retries = 3

            current_platform = platform.system()

            # For Windows
            if current_platform == "Windows":
                if prefs.audio_device == "OpenAL":
                    for _ in range(max_retries):
                        prefs.audio_device = "WASAPI"
                        if prefs.audio_device == "WASAPI":
                            break
                    for _ in range(max_retries):
                        prefs.audio_device = "OpenAL"
                        if prefs.audio_device == "OpenAL":
                            break
            

            if not os.path.exists(ffmpeg_exe_path):
                print(f"\n🚀 ffmpeg_exe_path: {ffmpeg_exe_path}")
                print("You need to install FFMPEG. Please restart Blender after installing2.")
                return

            warnings.filterwarnings(
                "ignore", category=RuntimeWarning, module="pydub.utils"
            )
            try:
                from pydub.generators import Sine
                from pydub.playback import play
                from pydub import AudioSegment
                import audioop
            except ModuleNotFoundError:
                print("You need to install dependencies in FAST/Preferences/INSTALL.")
                return
            AudioSegment.converter = os.path.join(lib_path, "ffmpeg.exe")
            # Ignore RuntimeWarning from pydub
            warnings.filterwarnings(
                "ignore", category=RuntimeWarning, module="pydub.utils"
            )

            if setable_frequency is not None:
                frequency = setable_frequency
            else:
                frequency = manager.beep_frequency  # Set Frequency To 2500 Hertz

            if setable_volume is not None:
                volume = setable_volume
            else:
                volume = manager.beep_volume

            duration = manager.beep_duration  # Set Duration To 200 ms

            try:
                beep_sound = (Sine(frequency)).to_audio_segment(duration=duration)

                # Adjust the volume of the beep sound using audioop
                beep_bytes = beep_sound.raw_data
                adjusted_beep_bytes = audioop.mul(beep_bytes, beep_sound.sample_width, volume
                )

                # Create a new AudioSegment with the adjusted audio data
                beep_sound = beep_sound._spawn(adjusted_beep_bytes)
                play(beep_sound)
            except NameError:
                pass
        except Exception as e:
            capture_and_copy_traceback()

            print(
                f"An unexpected exception occurred in beep(): {type(e).__name__} - {str(e)}"
            )
