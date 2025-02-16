
bl_info = {
    "name": "*Blender AI...That's ErrorProof!",
    "author": "Toapy & Friends",
    "version": (1, 0, 2),
    "blender": (4, 2, 0),  
    "location": ":-D It's on the N Panel!! :-D",
    "description": "Automate Blender with Virtually Error-Free AI Code Generation!",
    "category": "3D View",
}



hand_icon = "👉"

import bpy
import os
import sys
import platform
import requests
import shutil
import zipfile
import tempfile
import datetime
import urllib.request
try:
    import pyautogui
except ModuleNotFoundError:
    pass

# def show_console_ste_for_ai_import():
#     bpy.ops.fast.show_console()
#     bpy.ops.fast.show_console()
#     try:
#         pyautogui.hotkey('ctrl', 'shift', 'end')
#     except Exception as e:
#         pass


import zipfile
block_register = False


color_patterns = {
    "AR": ["\033[38;2;237;47;65m", "\033[38;2;237;47;65m"],  # Slightly more saturated red
    "ARR": ["\033[38;2;255;81;81m", "\033[38;2;255;81;81m"],  
    "AG": ["\033[38;2;0;255;81m", "\033[38;2;0;255;81m"],  # Richer green
    "AY": ["\033[93m", "\033[93m"],  # All Yellow
    "AO": ["\033[38;2;255;165;10m", "\033[38;2;255;165;10m"],  # All Orange
    "AB0": ["\033[94m", "\033[94m"],  # All Blue
    "AB": ["\033[38;2;39;119;255m", "\033[38;2;39;119;255m"],

}
  
def is_output_redirected():
    """
    Check if the standard output is being redirected to a file or a console.
    Returns True if output is redirected to a file, False otherwise.
    """
    return not sys.stdout.isatty()

                
def print_color_2(pattern, *args, delay=None, new_line=True, end="\n", flush=False):

    caller_info = inspect.stack()[1]  # Get information about the caller
    calling_line = caller_info.lineno  # Line number where print_color was called
    
    
    global color_patterns
    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
    except Exception as e:
        return
    


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

            print(colored_text, end=end, flush=flush)


        if new_line:
            print()  # Print newline if required
        

    except Exception as e:
        print("\nAn error occurred in print_color:", str(e), "at line", calling_line)






try:
    if platform.system() == "Windows":
        # Check if "lib" path is in sys.path
        lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
        if lib_path not in sys.path:
            sys.path.append(lib_path)


        import psutil



        # Remove "lib" after import to avoid redundancy
        if lib_path in sys.path:
            sys.path[:] = [p for p in sys.path if p != lib_path]

  

    elif platform.system() in ["Darwin", "Linux"]:  # macOS or Linux
        # Check if "lib" path is in sys.path and remove it
        lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
        if lib_path in sys.path:
            sys.path[:] = [p for p in sys.path if p != lib_path]

   

        # Add "lib2" to sys.path if not already there
        lib2_path = os.path.join(os.path.dirname(__file__), "lib2")
        if lib2_path not in sys.path:
            sys.path.append(lib2_path)
      

        import psutil


        # Remove "lib2" after import
        if lib2_path in sys.path:
            sys.path[:] = [p for p in sys.path if p != lib2_path]

        # print(f"{platform.system()}: Removed {lib2_path} from sys.path")

except ModuleNotFoundError as e:

    pass

from .fast_operators import *


def update_gpt_script_file_index(self, context):

    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    scn = bpy.context.scene
    # Check if there are any items in the collection
    if len(manager.GPTScriptFileItems) != 0:
        selected_index = scn.GPTScriptFileIndex
        
        # Ensure the selected index is within the valid range
        if selected_index < len(manager.GPTScriptFileItems):
            selected_item = manager.GPTScriptFileItems[selected_index]

            # Handle the "No Selection" case
            if selected_item.name == 'unlink':
                
                scn.gpt_added_code = ""
            
                gpt_save_user_pref_block_info()
                my_redraw()
                return

            else:
                home_directory = os.path.expanduser("~")
                
                base_directory = os.path.join(home_directory, "Documents", "FAST Settings", "AGPT-4 Scripts")
                full_file_path = os.path.join(base_directory, selected_item.name)
        
                scn.gpt_added_code = full_file_path
                print_color("AG", f"\nLinked code file: ", new_line=False)
                print_color("AR", f"{scn.gpt_added_code}")
                gpt_save_user_pref_block_info()
                my_redraw()


try:
    from .fast_preferences import FAST_Preferences, FAST_OT_fast_issues
    from .fast_properties import (
        FAST_Properties,
        GPTScriptFileItem,
        update_gpt_max_iterations,
        update_gpt_boost_user_command,
        update_gpt_advanced_boost_user_command,
        update_api_key,
        update_gpt_file_permission_fixer_path,
    )

    
except ImportError as e:
    print(f"❌ Failed to import required modules: {e}")
    

from .fast_global import *
from .fast_global import tfp

try:
    # Add the default "lib" path back to sys.path globally
    lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
    if lib_path not in sys.path:
        sys.path.append(os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages"))
except Exception as e:
    capture_and_copy_traceback()
    print(f"Error adding paths to sys.path: {e}")

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


def threaded_check_for_updates():

    try:

        # Check the connection
        result = fast_connection_checker()
        if result:
            pass
        else:
            print("\nNo Internet connection. Cannot check for updates.")
            return

        time.sleep(0.5) 


        try:
            def register_timer():
        
                try:
            
                    manager = bpy.context.preferences.addons[__name__].preferences.Prop
              
                    
                except KeyError as e:
                    
                    return
            
                manager.timer_start_time = time.time()
            
                bpy.app.timers.register(check_for_updates, first_interval=20.0)
           

            register_timer()

        except Exception as e:
            print(f"\nAn error occurred: {e}")
            capture_and_copy_traceback()
     
        return True

    except Exception as e:
        capture_and_copy_traceback()
        text = "\nAn error occurred during the checking process. Check PIP_dependency_errors.log in /BAITEP/logs for details."
        print_color("AW", text)
        return False

    
try:
    def run_first():

        print_color("AR", f"\nThis add-on is only tested on Blender 4.3+")

        try:
            bpy.utils.register_class(FAST_OT_install_fast)
        except ValueError:
            capture_and_copy_traceback()

        try:
            bpy.utils.register_class(FAST_OT_check_addon_version_op_1)
        except ValueError:
            capture_and_copy_traceback()

        try:
            bpy.utils.register_class(FAST_OT_info)
        except ValueError:
            pass
        try:

      

            try:
                bpy.utils.register_class(GPTScriptFileItem)
            except ValueError:
                pass
        
            try:
                bpy.utils.register_class(FAST_Properties)
            except ValueError:
                pass
                
            try:
                bpy.utils.register_class(FAST_Preferences)
            except ValueError:
                pass
    
    
        except ValueError:
           
            traceback.print_exc()

        try:
            manager = bpy.context.preferences.addons[__name__].preferences.Prop
        except KeyError:
            print("Manager Error.")
            return

        if manager.run_it_first_2:
            manager.run_it_first_2 = False
            save_user_pref_block_info()
        else:
            
            check_thread = threading.Thread(target=threaded_check_for_updates)
            check_thread.start()
  


    run_first()

except Exception:
    
    capture_and_copy_traceback()

def run_second():

    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
    except:
        print(f"\nManager Error. No big deal.")
        return
    get_elapsed_time()  
    check_dependencies_func()

# cython exclusions

class FAST_UL_script_files(bpy.types.UIList):
    # I think unused variables in the draw item function have to stay there I think it needs like 7 or 8 variables even if you're not using them.
    def draw_item(
        self, context, layout, data, item, icon, active_data, active_propname, index
    ):
        layout.prop(item, "name", text="", emboss=False, icon_value=icon)



# Check if running on the user's system
tfp = os.path.join(os.path.expanduser("~"), "Desktop", "OBS", ".COMMERCIAL")

def backup_fast_ai():
    """
    If running on the user's system, back up 'fast_ai.py' before replacing it.
    This happens immediately when Blender starts.
    """
    if os.path.exists(tfp):  # Confirms it's your system
        print("❗ Running on the user's system, performing immediate backup...")


        scripts_dir = bpy.utils.user_resource('SCRIPTS')
        addons_dir = os.path.join(scripts_dir, "addons", "blender_ai_thats_error_proof")
        fast_ai_path = os.path.join(addons_dir, "fast_ai.py")

        if os.path.exists(fast_ai_path):
            # Set backup folder on the Desktop
            backup_dir = os.path.join(os.path.expanduser("~"), "Desktop", "FastAI_Backups")
            os.makedirs(backup_dir, exist_ok=True)  # Create backup folder if it doesn't exist

            # Create a backup file with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            backup_file = os.path.join(backup_dir, f"fast_ai_backup_{timestamp}.py")

            # Copy the file
            shutil.copy2(fast_ai_path, backup_file)
            print(f"✅ Backup created: {backup_file}")
        else:
            print("❌ No existing 'fast_ai.py' found to back up.")


# Perform the backup immediately on startup
backup_fast_ai()

def check_ai_runtime():
    """
    Checks if the required AI runtime files exist.
    Returns True if everything is already installed.
    """
    scripts_dir = bpy.utils.user_resource('SCRIPTS')
    addons_dir = os.path.join(scripts_dir, "addons", "blender_ai_thats_error_proof")

    fast_ai_path = os.path.join(addons_dir, "fast_ai.py")
    pyarmor_runtime_path = os.path.join(addons_dir, "data", "pyarmor_runtime_004830", "pyarmor_runtime.pyd")
    pyarmor_init_path = os.path.join(addons_dir, "data", "pyarmor_runtime_004830", "__init__.py")

    if os.path.exists(fast_ai_path) or (os.path.exists(fast_ai_path) and os.path.exists(pyarmor_runtime_path) and os.path.exists(pyarmor_init_path)):
        print("✅ All required AI runtime files are present. Skipping AI setup prompt.")
        return True
    else:

        return False


def download_and_extract_obfuscated():
    """
    Downloads and extracts the obfuscated AI runtime for the current OS.
    Only copies the OS-specific folder (e.g., "obfuscated_windows" on Windows).
    Uses headers to bypass 403 Forbidden errors.
    """
    scripts_dir = bpy.utils.user_resource('SCRIPTS')
    addons_dir = os.path.join(scripts_dir, "addons", "blender_ai_thats_error_proof", "data")

    # Define the zip file name and URL
    obfuscated_zip_name = "obfuscated.zip"
    download_url = f"https://fast-blender-add-ons.com/wp-content/uploads/{obfuscated_zip_name}"
    temp_zip_path = os.path.join(tempfile.gettempdir(), obfuscated_zip_name)

    # Headers to mimic a browser request and avoid 403 Forbidden
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Download the zip file using requests
    try:

        response = requests.get(download_url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        # Save to temporary path
        with open(temp_zip_path, "wb") as f:
            f.write(response.content)

        print("✅ Download completed successfully!")

    except requests.exceptions.RequestException as e:
        print(f"ERROR: Failed to download {obfuscated_zip_name}: {e}")
        return False

    # Extract the zip file
    extract_dir = os.path.join(tempfile.gettempdir(), "extracted_ai_files")

    # Remove any old extracted files
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)

    try:
        with zipfile.ZipFile(temp_zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_dir)
      
    except zipfile.BadZipFile:
        print("ERROR: The downloaded zip file is corrupted!")
        return False

    # Determine the correct OS folder inside the extracted directory
    system_name = platform.system().lower()
    os_folder_mapping = {
        "windows": "obfuscated_windows",
        "darwin": "obfuscated_mac",
        "linux": "obfuscated_linux",
    }

    os_folder_name = os_folder_mapping.get(system_name)

    if not os_folder_name:
        print(f"ERROR: Unsupported platform: {system_name}")
        return False

    extracted_os_folder = os.path.join(extract_dir, os_folder_name)

    # If the OS-specific folder does not exist, warn and exit
    if not os.path.exists(extracted_os_folder):
        print(f"⚠ WARNING: No '{os_folder_name}' folder found inside extracted files. Skipping copy.")
        return False

    # Copy extracted files to the add-on directory
    try:
        for item in os.listdir(extracted_os_folder):
            source = os.path.join(extracted_os_folder, item)
    
            # If the file is fast_ai.py, move it to the main module folder
            if item == "fast_ai.py":
                destination = os.path.join(scripts_dir, "addons", "blender_ai_thats_error_proof", "fast_ai.py")
                shutil.copy2(source, destination)
                print(f"✅ fast_ai.py moved to module folder: {destination}")
            else:
                destination = os.path.join(addons_dir, item)
    
                if os.path.isdir(source):
                    if os.path.exists(destination):
                        shutil.rmtree(destination)
                    shutil.copytree(source, destination)
                else:
                    shutil.copy2(source, destination)
    
        print(f"✅ Successfully installed runtime")
    
    except Exception as e:
        print(f"ERROR: Failed to copy extracted files: {e}")
        return False
    
    return True
    

def setup_obfuscated_runtime_ai():
    """
    Directly use the existing 'obfuscated' folder inside the Blender add-ons directory.
    """
    scripts = bpy.utils.user_resource('SCRIPTS')
    main_path = os.path.join(scripts, "addons", "blender_ai_thats_error_proof", "data")


    if not os.path.exists(main_path):
        print(f"ERROR: Obfuscated folder not found at: {main_path}")
        return False

    # Ensure the obfuscated folder is in sys.path
    if main_path not in sys.path:

        sys.path.append(main_path)  # Ensure it is prioritized

    return True

# If AI runtime is already installed, skip the prompt
if not check_ai_runtime():
    enable_ai = input("🛠️ Would you like to install AI features? Type 'y' to proceed: ").strip().lower()
    if enable_ai.lower() == "y":
        print("✅ AI Features Enabled!")

        # Download and extract the obfuscated AI runtime before importing
        if download_and_extract_obfuscated():
            if setup_obfuscated_runtime_ai():
                try:
        
                    pyarmor_runtime_path = os.path.join(
                        bpy.utils.user_resource('SCRIPTS'),
                        "addons", "blender_ai_thats_error_proof", "data", "pyarmor_runtime_004830", "pyarmor_runtime.pyd"
                    )

                    if not os.path.exists(pyarmor_runtime_path):
                        print(f"❌ PyArmor runtime missing at {pyarmor_runtime_path}")


                    # Ensure fast_ai.py exists
                    module_path = os.path.join(
                        bpy.utils.user_resource('SCRIPTS'),
                        "addons", "blender_ai_thats_error_proof", "fast_ai.py"
                    )

                    if not os.path.exists(module_path):
                        print(f"❌ fast_ai.py not found at {module_path}")



            
                    from .fast_ai import *
                    from .fast_ai import gpt_enable_pref, ensure_example_files
                    from .fast_ai import (
                        log_autogpt_state
                    )
                    
                except Exception as e:
                    print(f"Failed to import 'fast_ai': {e}")
                    import traceback
                    traceback.print_exc()
            else:
                print("❌ Failed to set up the obfuscated fast_ai runtime.")
        else:
            print("❌ Failed to download and extract the obfuscated runtime.")
    else:
        print("🚫 AI Features Disabled. The add-on will still work, but AI-powered functions are turned off.")

else:

    def setup_obfuscated_runtime_ai():
        """
        Directly use the existing 'obfuscated' folder inside the Blender add-ons directory.
        """
        scripts = bpy.utils.user_resource('SCRIPTS')
        obfuscated_path = os.path.join(scripts, "addons", "blender_ai_thats_error_proof", "data")
    
    

    
        if not os.path.exists(obfuscated_path):
            print(f"🚨 Obfuscated folder not found at: {obfuscated_path}")
            return False
    
    
        # Ensure the obfuscated folder is in sys.path
        if obfuscated_path not in sys.path:
           
            sys.path.insert(0, obfuscated_path)  # Ensure it is prioritized
    
    
        return True
    
    
    # Ensure the runtime is set up before importing
    if setup_obfuscated_runtime_ai():
        try:
   
            pyarmor_runtime_path = os.path.join(
                bpy.utils.user_resource('SCRIPTS'),
                "addons", "blender_ai_thats_error_proof", "data", "pyarmor_runtime_004830", "pyarmor_runtime.pyd"
            )
    
    
            if not os.path.exists(pyarmor_runtime_path):
                print(f"❌ PyArmor runtime missing at {pyarmor_runtime_path}")

    
            # Manually set the package name to avoid relative import errors
            package_name = "fast_ai"
            module_path = os.path.join(
                bpy.utils.user_resource('SCRIPTS'),
                "addons", "blender_ai_thats_error_proof", "fast_ai.py"
            )
    
    
            if not os.path.exists(module_path):
                print(f"❌ fast_ai.py not found at {module_path}")

    
   
            from .fast_ai import *
            from .fast_ai import gpt_enable_pref
            from .fast_ai import (
                log_autogpt_state
            )
        except Exception as e:
            print(f"🚨 Failed to import 'fast_ai': {e}")
            traceback.print_exc()
    else:
        print("❌ Failed to set up the obfuscated fast_ai runtime.")




from .fast_icons import *
from .fast_keymaps import *
from bpy.props import PointerProperty
from bpy.app.handlers import persistent
from bpy.types import Operator, Panel, AddonPreferences
import threading
import traceback
import functools

# Platform-specific ctypes import
if platform.system() == "Windows":
    import ctypes

elif platform.system() == "Darwin":
    pass
elif platform.system() == "Linux":
    pass

else:
    print(f"[INFO] Unsupported platform: {platform.system()}")


from . import __name__


app = {"keymaps": [], "items": []}

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))









def run_once_on_install():
    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        
    except KeyError as e:
        #print("Manager error.")
        return
    
    manager.restart_after_enabling_addons = False

    if manager.startup_done == False:
        manager.startup_done = True

        manager.startup_done_2 = True
        

        save_user_pref_block_info()
        manager.restart_after_enabling_addons = True
        print("\nPlease wait for add-on to fully load, save your file and restart.")
        

        manager.run_once_prop = True

        
        manager.restart_after_enable=True
   






def initialize_text_editor():
    manager = bpy.context.preferences.addons[__name__].preferences.Prop

    if not bpy.data.texts:
        context = bpy.context
        current_time = datetime.now().strftime("%H_%M_%S")
        text_block_name = f"Text_{current_time}"
        text_block = bpy.data.texts.new(name=text_block_name)
        text_block.clear()
    
        text_block.write('import bpy\n\n')  
    
        window = context.window if context.window else bpy.context.window_manager.windows[0]
        screen = window.screen
    
        # Store the current workspace
        original_workspace = window.workspace
    
    
        scripting_workspace = bpy.data.workspaces.get('Scripting')
        ide_workspace = bpy.data.workspaces.get('SCRIPTING')
        
        if not scripting_workspace and not ide_workspace:
            print("Neither 'Scripting' nor 'SCRIPTING' workspace found. Ensure at least one exists.")
            return False
    
        # Prefer scripting_workspace if it exists, otherwise use ide_workspace
        workspace_to_use = scripting_workspace if scripting_workspace else ide_workspace
    
        window.workspace = workspace_to_use
        text_editor_area = next((area for area in workspace_to_use.screens[0].areas if area.type == 'TEXT_EDITOR'), None)
        if not text_editor_area:
            print("Text Editor area not found in the selected workspace.")
            return False
    
        text_editor_area.spaces.active.text = text_block
        text_editor_area.spaces.active.show_word_wrap = True
        text_editor_area.spaces.active.use_find_wrap = True
        text_block.current_line_index = 2  # Set the cursor position two lines below the import statement
        text_block.select_end_line_index = 2  # Ensure no text is selected
        text_block.select_end_character = 0   # Ensure no text is selected
        text_editor_area.spaces.active.top = 0

        workspace_to_use = scripting_workspace if scripting_workspace else ide_workspace
        
        window.workspace = workspace_to_use
        outliner_area = next((area for area in workspace_to_use.screens[0].areas if area.type == 'OUTLINER'), None)
        if not outliner_area:
            print("Outliner area not found in the selected workspace.")
            return False
        
        # Set restrict columns for the Outliner
        outliner_area.spaces.active.show_restrict_column_viewport = True
        outliner_area.spaces.active.show_restrict_column_select = True


        # Switch back to the original workspace
        window.workspace = original_workspace

    return True

# Define a global variable to track whether the messages have been printed
messages_printed = False
def print_update_messages():
    global messages_printed  # Access the global variable

    # if not messages_printed:  # Only print if the messages haven't been printed yet
    #     print_color("AR", "\nWe've set the update feature as first run process in the add-on.")
    #     print_color("AR", "Ironically, a 20-sec. app timer starts it, making it the last print.")
    #     print_color("AR", "This ensures if any error disables the add-on, updates will still work.\n")

    if not messages_printed:  # Only print if the messages haven't been printed yet
        print_color("AR", "\nAuto update system hasn't been tested in the first release.")
        print_color("AR", "Updates may only work partially & get errors, or not work at all.")
        print_color("AR", "We will have the update system fully tested by the next release.\n")

    
        messages_printed = True  # Mark as printed


@persistent
def enable_pref(dummy=None):

    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
    except KeyError as e:
        
        return  
    print_update_messages()
    try:
   
        te_init = initialize_text_editor()

        get_api_key()
        gpt_enable_pref()

        return None  


    except Exception as e:
        capture_and_copy_traceback()

        print("Error in delayed_function:", e)
 
        return



# Function to write handle to file
def write_handle_to_file(file_name, handle):
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    settings_directory = os.path.join(documents_path, "FAST Settings", "window_handles")
    if not os.path.exists(settings_directory):
        os.makedirs(settings_directory)

    file_path = os.path.join(settings_directory, file_name)
    with open(file_path, 'w') as file:
        file.write(str(handle))


blender_just_started = True
def scene_sync():

    global blender_just_started

    if blender_just_started:
        blender_just_started = False
        return 5.0  # or whatever your timer interval is

    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
    except KeyError as e:
        #print("Manager error.")
        return

    except AttributeError as ae:
        print("Scene sync attribute error: ", ae)
        capture_and_copy_traceback()
    except Exception as e:
        capture_and_copy_traceback()

        
        print("Scene sync error.", e)

    return 1.0  # Timer interval






#tv
gpt_props = {
    "auto_gpt_assistant": None,
    "bse_current_line": None,
    "fast_auto_gpt_panel_main_1": None,
    "fast_auto_gpt_panel_main_2": None,
    "fast_auto_gpt_panel_main_3": None,
    "disable_restart_blender": None,
    "disable_save_startup": None,
    "disable_delete_startup": None,
    "disable_show_console": None,
    "disable_n_panel": None,
    "disable_verbose_tool_tips": None,
    "gpt_auto_open_text_file": None,
    "gpt_beep_frequency": None,
    "gpt_choose_auto_run_command": None,
    "gpt_choose_random_command_type": None,
    "gpt_data": None,
    "gpt_hide_master_goal_text": None,
    "gpt_hide_user_command_text": None,
    "gpt_hide_user_instruction_set_text": None,
    "gpt_list_display_rows": None,
    "gpt_model": None,
    "gpt_node_image_path": None,
    "gpt_random_user_command_line_count": None,
    "gpt_relevant_bone_frames": None,
    "gpt_relevant_bones": None,
    "gpt_run_script_at_end": None,
    "gpt_show_console_on_run": None,
    "gpt_text_box_scale": None,
    "gpt_user_command": None,
    "gpt_user_instruction_set": None,
    "GPTScriptFileItems": None,
    "show_gpt_operator":  None,

}
new_properties = {
    'auto_save_disk_warning_beep': None,
    'diffeomorphic_disable_locks': None,
    "diffeomorphic_show_bones": None,
    # "diffeomorphic_parent_camera_to_head": None,
    'include_blend1': None,
    'include_scratch': None,    
    "add_audio_video_t": None,
    "add_audio_video": None,
    "add_camera_at_view": None,
    "advanced_local_mode": None,
    "auto_save_disk_warning_info_tab": None,
    "auto_save_disk_warning_message": None,
    "childless_empties": None,
    "clean_up": None,
    "collect_error_message_only": None,
    "current_frame": None,
    "cycle_cameras": None,
    "delete_clip": None,
    "delete_hierarchy_prop": None,
    "delete_keyframes": None,
    "duplicate_keyframe": None,
    "empty_func": None,
    "enable_addons": None,
    "fast_save_file_text": None,
    "fast_save_file": None,
    "frame_nodes": None,
    "jump_count_1": None,
    "jump_count_10": None,
    "jump_count_15": None,
    "jump_count_5": None,
    "jump_count_all": None,
    "keyframe_objects": None,
    "keyframe_purge": None,
    "lock_camera_to_view": None,
    "move_to_collection": None,
    "open_keyframe": None,
    "play_timeline_overlays": None,
    "play_timeline_overlays_prop": None,
    "play_timeline": None,
    "render_viewport": None,
    "save_and_enter_material_preview_mode": None,
    "select_objects_prop": None,
    "select_objects": None,
    "set_frame": None,
    "set_keys": None,
    "show_active": None,
    "show_agpt4": None,
    "text_copy": None,
    "text_cut": None,
    "text_indent": None,
    "text_paste": None,
    "text_print": None,
    "text_select_all": None,
    "text_toggle_comment": None,
    "text_unindent": None,
}
previous_values = {
    "ActionFileIndex": None,
    "action_list_display_rows": None,
    "add_tab_to_adj_colors": None,
    "addons_status": {},
    "adjustable_restart_delay": None,
    "anim_action_editor": None,
    "anim_shape_key_editor": None,
    "fast_append_markers": None,
    "fast_append_sound": None,
    "auto_convert_to_xyz": None,
    "auto_keyframe_timeout": None,
    "auto_reselect_objects": None,
    "auto_resize_camera": None,
    "auto_save_custom_directory": None,
    "auto_save_directory": None,
    "auto_save_disk_warning_info_tab": None,
    "auto_save_disk_warning_message": None,
    "auto_save_increment_notification": None,
    "auto_save_preferences": None,
    "auto_save_scripts": None,
    'auto_save_file_state_prop': None,
    "beep_duration": None,
    "beep_frequency": None,
    "beep_volume": None,
    "button_file_state": None,
    "button_spacing": None,
    "copy_traceback": None,
    "current_frame": None,
    "delete_original_clip": None,
    "hide_original_clip": None,
    "daz_32_bit_path": None,
    "daz_64_bit_path": None,
    "daz_label_split": None,
    "daz_scale_factor": None,
    "DELETE_action_editor": None,
    "DELETE_clips": None,
    "DELETE_keyframes": None,
    "DELETE_markers": None,
    "DELETE_shape_key": None,
    "disable_modal_auto_resize_modal": None,
    "disable_modal_auto_save_operator": None,
    "disable_modal_scene_sync": None,
    "disable_modal_test_values_function": None,
    "disable_modal_save_user_preferences": None,
    "disable_modal_run_daz_modal": None,
    "disable_modal_depsgraph_callback": None,
    "diffeomorphic_add_camera": None,
    "diffeomorphic_object_dbz": None,
    "diffeomorphic_object_duf": None,
    "diffeomorphic_object_duf_png": None,
    "diffeomorphic_object_tip_png": None,
    "diffeomorphic_pose_duf": None,
    "diffeomorphic_pose_duf_png": None,
    "diffeomorphic_pose_tip_png": None,    
    "diffeomorphic_apply_zero_subdivision": None,
    "disable_high_poly": None,
    "disable_high_poly_render": None,
    "disable_high_poly_viewport": None,
    "fast": None,
    "fast_lines_of_code": None,
    "fast_menu": None,
    "fast_save_path": None,
    "force_solid_mode": None,
    "google_playback_audio": None,
    "icon_scale_factor": None,
    "include_fast_increment_backup": None,
    "join_clips": None,
    "key_add_lights": None,
    "key_color_values": None,
    "key_focus_plane": None,
    "key_hide_cube": None,
    "key_readd_settings": None,
    "key_reimport_clip": None,
    "key_switch_to_material_preview": None,
    "keying_node_name": None,
    "last_clip_name": None,
    "list_display_rows": None,
    "min_silence_length": None,
    "internal_testing": None,
    "maximum_subdivision_level": None,
    "my_keying_set": None,
    "offset_x": None,
    "offset_y": None,
    "open_referenced_file_in_vscode": None,
    "openai_template_icon_scale": None,
    "operator_and_args": None,
    "outliner_delete_perm": None,
    "operator_name": None,
    "pf_1": None,
    "pf_2": None,
    "play_error_sound": None,
    "play_timeline_overlays": None,
    "poly_count_amount": None,
    "poly_count_amount": None,
    "print_suppressed": None,
    "remove_short_clips": None,
    "render_filename": None,
    "render_viewport_custom_render_filepath": None,
    "render_viewport_image_jpg": None,
    "render_viewport_image_png": None,
    "render_viewport_backup_file": None,
    "render_viewport_film_transparent": None,
    "render_viewport_frame_end": None,
    "render_viewport_frame_start": None,
    "render_viewport_mp4": None,
    "render_viewport_png": None,
    "render_viewport_frame_delay": None,
    "render_viewport_show_render": None,
    "rhubarb_dialog_file": None,
    "rhubarb_silence_length": None,
    "rhubarb_padding": None,
    "rhubarb_sound_file": None,
    "rhubarb_start_frame": None,
    "run_operator": None,
    "seek_step": None,
    "select_coll_contents": None,
    "semitones": None,
    "set_output_sound_file_level": None,
    "show_daz_icon": None,
    "show_setup_controls": None,
    "show_topbar_buttons": None,
    "show_light_buttons": None,
    "show_view_buttons": None,
    "show_active_timing": None,
    "silence_thresh": None,
    "last_speech_bubble_location": None,
    "split_factor_1": None,
    "split_factor_2": None,
    "start_music": None,
    "startup_dependency_info": None,
    "startup_timer": None,
    "tab_items": None,
    "tab_index": None,
    "test_tensorflow": None,
    "theme_file_state": None,
    "timeout_duration_prop": None,
    "timeout_duration_prop": None,
    "tool_inner_color_pass": None,
    "transform_button_scale_prop": None,
    "transform_local_prop": None,
    "welcome_message_count": None,
}
previous_values_scene = {
    "add_blue_cube": None,
    "add_viewport_color": None,
    "adv_local_keep_armature": None,
    "animation_layers_location": None,
    "api_key": None,


    "bse_search_term": None,
    "gpt_show_add_example_prompt": None,
    "gpt_added_code": None,
    "gpt_advanced_api_or_manual_or_fast_decider": None,
    "gpt_advanced_boost_user_command": None,
    "gpt_boost_user_command": None,
    "gpt_choose_to_take_snapshot": None,
    "gpt_confirm_data": None,
    "gpt_data_limit": None,
    "gpt_edit_user_command_prompt": None,
    "gpt_error_check_timeout": None,
    "gpt_extra_data_for_find_code_examples": None,
    "gpt_file_permission_fixer_path": None,
    "gpt_find_code_examples": None,
    "gpt_main_assistant_temperature": None,
    "gpt_main_assistant_top_p": None,
    "gpt_max_iterations": None,
    "gpt_model_secondary": None,
    "gpt_operator_name": None,
    "gpt_pause_before_fixing_errors": None,
    "gpt_random_user_command": None,
    "gpt_run_final_script": None,
    "gpt_run_on_selected_objects": None,
    "gpt_send_anonymous_data": None,
    "gpt_show_code": None,
    "gpt_show_cost": None,
    "gpt_show_lookups": None,
    "gpt_smtp_lib_app_password": None,
    "gpt_smtp_lib_server": None,
    "gpt_use_beep": None,
    "gpt_show_verify_example_prompt": None,
    "gpt_hide_scene_objects": None,
    "GPTScriptFileIndex": None,
    "hdri_maker_location": None,
    "include_fast_startup_backup": None,
    "is_dirty": None,
    "key_saved_clip_for_reimport_clip": None,
    "left_padding": None,
    "light_coll_contents_enum": None,
    "new_workspace": None,
    "nview_location": None,
    "overlays_prop": None,
    "pull_se_examples_iterations": None,
    "poliigon_location": None,
    "procedural_crowds_location": None,
    "rhubarb_2d_lip_sync_for_blender_location": None,
    "rhubarb_add_markers": None,
    "rhubarb_enable_rest_keyframes": None,
    "rhubarb_recognizer": None,
    "rhubarb_silence_thresh": None,
    "rig_gns_pro_location": None,
    "right_padding": None,
    "save_on_startup": None,
    "show_se_content": None,
    "show_active_auto_viewport": None,
    "show_active_auto_outliner": None,
    "speech_bubble_flip": None,
    "speech_bubble_last": None,
    "speech_bubble_offset_x": None,
    "speech_bubble_offset_y": None,
    "speech_bubble_offset_z": None,
    "speech_bubble_overlays": None,
    "speech_bubble_size": None,
    "speech_bubble_text_last": None,
    "speech_bubble_text_size": None,
    "speech_bubble_words_per_line": None,
    "transform_nudge_prop": None,
    "transportation_location": None,
    "use_beep_local_global": None,
    "use_beep": None,
    "window_offset_x": None,
    "window_offset_y": None,
    "render_viewport_overlays": None,
    "auto_save_toggle": None,
    "auto_save_startup_file": None,
    "exit_to_solid_mode": None,
    "diffeomorphic_disable_hair": None,
}


previous_values_addons_and_settings = {
    "enable_node_wrangler": None,
    "enable_node_arrange": None,
    "enable_stored_views": None,
    "enable_F2": None,
    "enable_copy_attributes": None,
    "enable_extra_mesh_objects": None,
    "enable_io_scene_fbx": None,
    "enable_io_scene_gltf2": None,
    "enable_rigify": None,
    "enable_development_icon_get": None,
    "enable_cycles": None,
    "enable_pose": None,
    "show_developer_ui": None,
    "show_tooltips_python": None,
    "undo_steps": None,
    "use_auto_keying": None,
    "use_mouse_depth_navigate": None,
    "use_rotate_around_active": None,
    "use_zoom_to_mouse": None,
}



JSON_FILE_PATH = os.path.join(os.path.expanduser("~"), "Documents", "FAST Settings", "fast_settings.json")
HANDLE_FLOAT_VECTOR = True
DESKTOP_DUMP_PATH = r"C:\Users\W\Desktop\corrupted_files"

def handle_corrupted_json(file_path, dump_path):
    """
    Handles corrupted JSON files by dumping the contents to a timestamped file in a secure folder.
    """

    try:
 
        # Check if the directory exists before proceeding
        if os.path.exists(DESKTOP_DUMP_PATH):

            with open(file_path, 'r') as corrupted_file:
                corrupted_content = corrupted_file.read()
    
            # Generate a timestamped filename for the dump
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            dump_file_path = os.path.join(dump_path, f"corrupted_{timestamp}.txt")
    
            # Save the corrupted content to the dump file
            with open(dump_file_path, 'w') as dump_file:
                if corrupted_content:
                    dump_file.write(corrupted_content)
    
            print(f"[INFO] Corrupted JSON content saved to: {dump_file_path}")
    
    except Exception as e:
        print(f"[ERROR] Failed to handle corrupted JSON file: {e}")
        capture_and_copy_traceback()



def is_serializable(value):
    """
    Check if a value is serializable to JSON.
    Returns True if it is, False otherwise.
    """
    try:
        json.dumps(value)
        return True
    except (TypeError, OverflowError):
        return False


def check_disk_space_at_startup():


    try:
        import psutil
    except ModuleNotFoundError:
        print_color("AW", "\npsutil module not found. Please install dependencies in Preferences.")
        return True

    disk_space = psutil.disk_usage('/').free

    threshold = 20 * 1024 * 1024

    return disk_space >= threshold

  
def save_properties_to_json(properties_to_save):
    if not check_disk_space_at_startup():
        print("\nNot enough disk space to save properties.")
        return

    global JSON_FILE_PATH

    try:
        with open(JSON_FILE_PATH, 'r') as json_file:
            try:
                existing_data = json.load(json_file)
            except json.JSONDecodeError as e:
                print("[WARNING] Corruption detected in JSON file.")
                handle_corrupted_json(JSON_FILE_PATH, DESKTOP_DUMP_PATH)
                existing_data = {}  # Reset to empty dict to prevent data loss

    except FileNotFoundError:
        existing_data = {}  # If the file doesn't exist, create an empty dict
        with open(JSON_FILE_PATH, 'w') as json_file:
            json.dump(existing_data, json_file)

    # Serialize CollectionProperty (e.g., ActionFileItems)
    for key, value in properties_to_save.items():
        if isinstance(value, bpy.types.bpy_prop_collection):
            # Convert the collection to a list of dictionaries
            serialized_collection = []
            for item in value:
                serialized_collection.append(item.as_dict())  # Ensure item has as_dict() or equivalent
            existing_data[key] = serialized_collection
        elif is_serializable(value):
            existing_data[key] = value
        else:
            print(f"[WARNING] Skipping non-serializable property: {key}, Type: {type(value)}")

    # Step 3: Write the updated data back to the JSON file
    try:
        if existing_data:
            with open(JSON_FILE_PATH, 'w') as json_file:
                json.dump(existing_data, json_file, indent=4)

    except Exception as e:
        print(f"Error saving properties to JSON:\n")
        capture_and_copy_traceback()




def reload_properties_from_json():
    global JSON_FILE_PATH
    global HANDLE_FLOAT_VECTOR
    # Get add-on preferences manager for checking add-on properties
    manager = bpy.context.preferences.addons[__name__].preferences.Prop

    # Manager diversion list (specific properties to be saved as manager properties)
    manager_diversion_list = ["fast"]

    # Check if the file exists
    if not os.path.exists(JSON_FILE_PATH):
        print_color("AW", f"\nJSON file {JSON_FILE_PATH} not found so creating it.")
        with open(JSON_FILE_PATH, 'w') as json_file:
            json_file.write('{}')
        return

    try:
        with open(JSON_FILE_PATH, 'r') as json_file:
            saved_properties = json.load(json_file)
            
            try:

                # Iterate through the saved properties and apply them to the scene or preferences
                for prop, value in saved_properties.items():
                    # HANDLE_FLOAT_VECTOR: Special handling for float vector properties (RGB/RGBA)
                    if HANDLE_FLOAT_VECTOR and isinstance(value, list):
        
        
                        try:
                            # Determine expected length by checking the length of the saved value.
                            expected_length = len(value)
                     
        
                            # Proceed only if the value has either 3 or 4 elements.
                            if expected_length in [3, 4]:
                                # Round the values to 3 decimal places.
                                rounded_value = [round(val, 3) for val in value]
                          
        
                                # Apply the rounded value to the property.
                                if hasattr(bpy.context.scene, prop):
                                    setattr(bpy.context.scene, prop, rounded_value)
                                 
                                elif hasattr(manager, prop):
                                    setattr(manager, prop, rounded_value)
    
                        except Exception as e:
                            print(f"[ERROR] Error restoring float vector for {prop}: {e}")
                            capture_and_copy_traceback()
                

                    elif isinstance(value, list):
                        if hasattr(manager, prop) and isinstance(getattr(manager, prop), bpy.types.bpy_prop_collection):
                            # Clear the existing collection
                            collection = getattr(manager, prop)
                            collection.clear()
        
                            # Recreate the collection items
                            for item_data in value:
                                new_item = collection.add()
                                for attr, attr_value in item_data.items():
                                    setattr(new_item, attr, attr_value)
                    else:
                        # Check if the property is in the manager_diversion_list
                        if prop in manager_diversion_list:
                            # Directly save it as a manager property
                            setattr(manager, prop, value)
                        elif hasattr(bpy.context.scene, prop):
                            # Set scene property if found
                            setattr(bpy.context.scene, prop, value)
                        elif manager and hasattr(manager, prop):
                            # Set add-on preference property
                            setattr(manager, prop, value)
            except TypeError as e:
                # Broadly catch errors with "enum" in their description
                if "enum" in str(e).lower():
                    print_color("AW", "\nEnum-related error while setting property, no big deal.")
                else:
                    raise  # Re-raise other TypeErrors
            except Exception as e:
                print_color("AW", "\nError while reloading properties from JSON. Likely nothing.")
                capture_and_copy_traceback()

    
        print_color("AG", f"\nProperties successfully reloaded from JSON.")

    except Exception as e:
        print_color("AR", f"\nError loading properties from JSON:\n")
        capture_and_copy_traceback()

#tv

TEST_MODE = 0


previous_values_dict = {}
global_props = []
# Global dictionary to store current property values
current_prop_values = {}

# Function to periodically update current property values
def update_current_values():
    global current_prop_values
    scene = bpy.context.scene
    # Loop through each property in the previous_values_scene and update its stored value
    for prop in previous_values_scene:
        if hasattr(scene, prop):
            current_prop_values[prop] = getattr(scene, prop)
            # print(f"\n🚀 {prop}: {current_prop_values[prop]}")





# Function to reset properties if they differ from the stored values
def reset_properties():
    global current_prop_values
    scene = bpy.context.scene

    for prop, stored_value in current_prop_values.items():
        if hasattr(scene, prop):
            try:
                current_value = getattr(scene, prop)
                if current_value != stored_value:
                    setattr(scene, prop, stored_value)
            except ReferenceError as e:
                # Skip properties causing reference errors
                print(f"Skipping reset for property '{prop}': {e}")


@persistent
def undo_post_handler(dummy):
 
    reset_properties()

@persistent
def redo_post_handler(dummy):
    reset_properties()


# Exception list: Properties to skip
exception_list = [
    # This property isn't in the previous value list just leaving this here as a placeholder so I could use this exception list if necessary
    "gpt_current_iteration",

]

def test_values(source, prop_dict, changes_accumulator):
    
    scn = bpy.context.scene
    update_current_values()
    global previous_values_dict
    global TEST_MODE
    current_values = {}
    properties_to_save = {}

    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop

    except KeyError as e:
        return

    if not manager.new_addition:
        TEST_MODE = 0
    try:
        for prop, _ in prop_dict.items():
       
            if prop in exception_list:
                if TEST_MODE:
                    print(f"Skipping property: {prop}")
                continue

            if prop == 'addons_status':
                # Assuming 'addons_status' should be handled differently if needed
                continue

            if TEST_MODE:
                if prop != 'collect_error_message_only':
    
                    
                    continue

            
            if prop not in previous_values_dict:
                previous_values_dict[prop] = {'previous_value': None}


            current_value = None

            if hasattr(source, prop):
                
                
                current_value = getattr(source, prop, None)
             
                # Check if the current value is a float vector and handle its length
                if HANDLE_FLOAT_VECTOR and isinstance(current_value, bpy.types.bpy_prop_array):
                    # Derive the expected length based on the existing property
                    current_prop = [getattr(source, prop)[i] for i in range(4)] if hasattr(source, prop) else None
                    if current_prop:
                        expected_length = len(current_prop)
       
                    else:
                        expected_length = 3  # Default to 3 if unable to derive

                    # Adjust the current value based on its length
                    current_value = [current_value[i] for i in range(expected_length)]

                if TEST_MODE:
                    print(f"{prop} Previous value: {previous_values_dict[prop].get('previous_value', None)}")
                    print(f"{prop} Current value: {current_value}")

                prev_value = previous_values_dict[prop].get('previous_value', None)

                try:
                    if current_value is not None and prev_value != current_value:

                        
                        changes_accumulator.append((prop, prev_value, current_value))
                        if TEST_MODE:
                            print(f"\n🚀 Property changed: {prop}")
                            print(f"Appended to changes_accumulator: {changes_accumulator[-1]}")

                        # Update the previous value in the previous_values_dict correctly
                        previous_values_dict[prop]['previous_value'] = current_value
                        if TEST_MODE:
                            print(f"Updated previous_values_dict[{prop}] to {current_value}")

                        if prev_value is not None:
                            manager.save_pref = True
                    
                            properties_to_save[prop] = current_value
                                                  
                            if properties_to_save:
        
                                save_properties_to_json(properties_to_save)       
                                bpy.ops.fast.info('INVOKE_DEFAULT', message=f"✔️ Saved {prop}", duration=1)
                                
                    

                except KeyboardInterrupt:
                    if TEST_MODE:
                        print("\n❌ KeyboardInterrupt detected, exiting function.")
                    return
                except Exception as e:
                    if TEST_MODE:
                        print(f"\n❌ Exception occurred while processing property {prop}: {e}")
                        capture_and_copy_traceback()
            else:
                if TEST_MODE:
                    print(f"Property {prop} Source {source} does not exist.")  # Log that the property does not exist
    
    except KeyboardInterrupt:
        print("\n❌ KeyboardInterrupt detected, exiting function.")
    except Exception as e:
        capture_and_copy_traceback()







def test_values_function():
    global global_props
    delay = 0.5
    scn = bpy.context.scene

    try:

        try:
            manager = bpy.context.preferences.addons[__name__].preferences.Prop
        except KeyError as e:
            #print("Manager error.")
            return


        # Check file size and adjust return value based on size thresholds
        file_path = bpy.data.filepath
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            if file_size > 1 * 1024 * 1024 * 1024:  # Over 1 GB
                delay = 2
            elif file_size > 500 * 1024 * 1024:  # Over 500 MB
                delay = 1


        if manager.autogpt_processing == 'Initializing' or manager.autogpt_processing == 'Analyzing' or manager.autogpt_processing == 'Waiting for Input':
            # This way the token sliders work right and we're just appending a placeholder so definitely it'll save after Autonomous GPT-4 is done running
            global_props.append('placeholder')

        else:
            changes_accumulator = []  # Accumulate changes here
            test_values(manager, gpt_props, changes_accumulator)
            test_values(manager, previous_values, changes_accumulator)
            test_values(manager, previous_values_addons_and_settings, changes_accumulator)
            test_values(manager, new_properties, changes_accumulator)
            test_values(bpy.context.scene, previous_values_scene, changes_accumulator)
        return delay 
        
    except Exception as e:
        capture_and_copy_traceback()
        print("\nAttempted to bypass exception access crash...")
        return delay




last_mod_time_0 = None
last_mod_time_1 = None
user_command_file_path = os.path.join(os.path.expanduser('~'), "Documents", "FAST Settings", "AGPT-4 Instructions", "user-command.txt")
last_mod_time_2 = None
user_instruction_set_file_path = os.path.join(os.path.expanduser('~'), "Documents", "FAST Settings", "AGPT-4 Instructions", "user-instruction-sets.txt")
last_mod_time_3 = None
data_file_path = os.path.join(os.path.expanduser('~'), "Documents", "FAST Settings", "AGPT-4 Data", "data.txt")
last_mod_time_4 = None
log_file_path = os.path.join(bpy.utils.user_resource('SCRIPTS'), 'addons', 'blender_ai_thats_error_proof', 'data', 'autogpt', 'BSE', "BSE_current_line.txt")
execution_count_6 = 0
print_new_line_for_autogpt = False
last_mod_time_5 = None
api_key_file_path = os.path.join(os.path.expanduser('~'), 'Documents', 'FAST Settings', 'api_key.csv')
temp_api_key = ""
iteration_counter = 0

        
def save_user_preferences():
 
    global last_mod_time_0
    global last_mod_time_1
    global user_command_file_path
    global last_mod_time_2
    global user_instruction_set_file_path
    global last_mod_time_3
    global user_master_goal_file_path
    global last_mod_time_4
    global log_file_path
    global last_mod_time_5
    global api_key_file_path
    global print_new_line_for_autogpt
    global iteration_counter
    global temp_api_key
    scn = bpy.context.scene
    try:
        try:
            manager = bpy.context.preferences.addons[__name__].preferences.Prop
        except Exception as e:
            return


        # Get the manager and Blender preferences
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        prefs = bpy.context.preferences

        if manager.save_pref == True:


            try:
      
                gpt_daz_block_save_user_preferences()
                if not print_new_line_for_autogpt:
            
                    print_new_line_for_autogpt = True

            except Exception as e:
                capture_and_copy_traceback()

                print(f"An error occurred, likely as no user preferences have been saved, no big deal: {e}")
                manager.save_pref = False
            manager.save_pref = False
   


        if manager.was_restarted_enable_pref:
            manager.was_restarted_enable_pref = False

        

 
        all_active = all(kmi.active for _, kmi in fastmenu_keymaps)
        
        # Ensure the directory exists
        directory = os.path.dirname(user_command_file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("\nDirectory created at:", directory)
        
        # Ensure the file exists or create it if it doesn't
        if not os.path.exists(user_command_file_path):
            with open(user_command_file_path, 'w') as file:
                file.write("")
        
        

        try:
            mod_time = os.path.getmtime(user_command_file_path)
            if last_mod_time_0 is None or mod_time > last_mod_time_0:
                last_mod_time_0 = mod_time
   
                
                # If the file exists, append the keyword and update the manager property
                if os.path.exists(user_command_file_path):
            
                    with open(user_command_file_path, 'r') as file:
                        original_content = file.read()
        
                    # Update the Blender property
                    manager.gpt_user_command = original_content
                    my_redraw()

        
        except FileNotFoundError:
            # This block may be redundant now since the file is created if not found
            pass

        try:
            mod_time = os.path.getmtime(user_command_file_path)
            if last_mod_time_1 is None or mod_time > last_mod_time_1:
                last_mod_time_1 = mod_time
   
                
                # If the file exists, append the keyword and update the manager property
                if os.path.exists(user_command_file_path):
            
                    with open(user_command_file_path, 'r') as file:
                        original_content = file.read()
        
                    # Update the Blender property
                    manager.gpt_user_command = original_content
                    my_redraw()

        
        except FileNotFoundError:
            # This block may be redundant now since the file is created if not found
            pass

        # Ensure the directory exists
        directory = os.path.dirname(user_instruction_set_file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("\nDirectory created at:", directory)
        
        # Ensure the file exists or create it if it doesn't
        if not os.path.exists(user_instruction_set_file_path):
            with open(user_instruction_set_file_path, 'w') as file:
                file.write("")


        # Check the file modification time
        try:
            mod_time = os.path.getmtime(user_instruction_set_file_path)
            if last_mod_time_2 is None or mod_time > last_mod_time_2:
                last_mod_time_2 = mod_time
                if os.path.exists(user_instruction_set_file_path):
                    with open(user_instruction_set_file_path, 'r') as file:
                        content = file.read()
                        # Update the Blender property
                        manager.gpt_user_instruction_set= content
                        my_redraw()
               
        except FileNotFoundError:
            pass
    
  

        # Ensure the directory exists
        directory = os.path.dirname(data_file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("\nDirectory created at:", directory)
        
        # Ensure the file exists or create it if it doesn't
        if not os.path.exists(data_file_path):
            with open(data_file_path, 'w') as file:
                file.write("")
    

        try:
 
            # Ensure the file exists before doing anything else
            if not os.path.exists(api_key_file_path):
                with open(api_key_file_path, 'w') as file:
                    file.write("\n")  # Write a blank line to the file
                    
            mod_time = os.path.getmtime(api_key_file_path)
            if last_mod_time_5 is None or mod_time > last_mod_time_5:
                last_mod_time_5 = mod_time
        
                # Try to read the API key from the file if it exists
                if os.path.exists(api_key_file_path):
                    with open(api_key_file_path, 'r') as file:
                        lines = file.readlines()
                        
                        # Check for null characters in the lines
                        if any('\x00' in line for line in lines):
                            print("\nDetected an issue with the saved API key file. Fixing it now.")
        
                            # Check if there is an API key in the scene
                            if hasattr(scn, 'api_key') and scn.api_key:
                                print("\nUsing your saved API key to fix the file.")
                                with open(api_key_file_path, 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow(['API Key', scn.api_key])
                            else:
                                print("\nCould not find a saved API key. Starting fresh.")
                                with open(api_key_file_path, 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow(['API Key', ""])
                            return  2.0

                        # Continue processing valid file content
                        temp_api_key = None  # Initialize temp_api_key to None
                        if lines:  # If there's at least one line
                            try:
                                temp_api_key = lines[0].strip().split(',')[1]  # Attempt to extract the API key
                            except IndexError:
                                print("\nThe saved API key file is not formatted correctly. Fixing it now.")
                                temp_api_key = None  # Reset temp_api_key if IndexError occurs
        
                        # If temp_api_key is None, check the scene property
                        if temp_api_key:
                            #print("\nFound your saved API key and keeping it available.")
                            scn.api_key = temp_api_key
                        else:
                            if hasattr(scn, 'api_key') and scn.api_key:
                                #print("\nUsing your previously saved API key.")
                                temp_api_key = scn.api_key
        
                        my_redraw()
        
        except FileNotFoundError:
            # If the file is missing, skip any actions until it’s created
            print("\nWe couldn't find your saved API key file, but we'll create it when you set one.")
            pass
    
        return 2.0

    except Exception as e:
        print(f"*error in save_user_preferences*: \n")
        capture_and_copy_traceback()

        
        
        return 2.0




  

try:
    tooltip_descriptions = {
        "use_o1_mini_model": {
            "concise": "Enables the O1 model. Verbose tool-tip available",
            "verbose": ("Enable/Disable usage of the latest O1 model for script generation only.\n\n"
                        "Requests to fix code will automatically use the GPT 4o model.\n\n"
                        "The O1 model is highly adept at reasoning and provides an improved script output")
        },
    
        "ambient_noise_duration_prop": {
            "concise": "Duration Google analyzes ambient noise for better speech recognition. Verbose tool-tip available",
            "verbose": (
                "Duration (in seconds) that Google analyzes ambient noise before processing speech.\n\n"
                "This is used to improve speech recognition or transcribe an audio file more accurately.\n\n"
                "Strengthening the Voice Recognition:\n\n"
                "1. Low Microphone Volume: Ensure the microphone volume is at an optimum level.\n\n"
                "2. Ambient Noise: If in a noisy environment, increase the ambient noise slider until speech is clear.\n\n"
                "3. When adjusting ambient, be aware that fan noise can significantly impact accuracy.\n\n"
                "4. Network Issues: Requires an internet connection to Google. Poor connection might result in errors.\n\n"
                "5. Speech Clarity: Please speak clearly. Muffled or slurred speech might not be recognized properly.\n\n"
                "6. Language: En-US only. Speak another language? Click 'Report Issues'. We'll upgrade ASAP."
            )
        },

        # "gpt_script_is_over_200_lines": {
        #     "concise": "Manages error handling for scripts over 200 lines. Verbose tool-tip available",
        #     "verbose": (
        #         "[Not a user property please do not change. Shown here for info only.]\n\n"
        #         "This feature will be enabled automatically when a script exceeds 200 lines.\n\n"
        #         "When active, it allows the system to isolate the function that has an error,\n\n"
        #         "along with any required code, and attempt to fix just that section. You may\n\n"
        #         "see this property appear in either the text editor panel or the viewport\n\n"
        #         "panel, depending on where you are working with the script.\n\n"
        #         "If you input a long script in either location, the system will handle longer\n\n"
        #         "scripts by isolating functions and focusing on specific error corrections.\n\n"
        #         "The process should be quicker since only small sections are processed, but it\n\n"
        #         "will require you to run the script again for each subsequent error fix.\n\n"
        #         "If you prefer to avoid this property activating, reduce the script size to\n\n"
        #         "under 200 lines. For seasoned developers, you might consider removing non-\n\n"
        #         "essential functions temporarily, then adding them back one by one as needed.\n\n"
        #         "When a script exceeds 200 lines, the complexity increases, making it more\n\n"
        #         "challenging for GPT to process, which is why this feature is essential.\n\n"
        #         "This is a part of our ongoing efforts to optimize for large codebases, and\n\n"
        #         "we are working to refine this process further to ensure a smoother experience.\n\n"
        #         "For now, this feature will help streamline the correction of large scripts,\n\n"
        #         "and we appreciate your patience as we continue to improve this system."
        #     )
        # },
        

        "auto_save_disk_warning_threshold": {
            "concise": "Threshold for disk space warning during auto-save. Verbose tool-tip available",
            "verbose": (
                "GB point at which you'll receive audio notification.\n\n"
                "Disk warning interval is the same as the INTERVAL above.\n\n"
                "Disk warning cannot be deactivated"
            )
        },
        "gpt_show_add_example_prompt": {
            "concise": "Enables prompt to add examples/send errors if hit 'Max Iterations'. Verbose tool-tip available",
            "verbose": (
                "When enabled, prompts you to add a new code example to the AGPT-4 'examples.txt' file,\n\n"
                "if reach 'Max Iterations' and if AGPT-4 was stuck on same error multiple iterations.\n\n"
                "If you choose add example, ADDON/data/autogpt/examples.txt will open, allowing,\n\n"
                "you to add your code example(s). Once complete, you will then be asked if you,\n\n"
                "wish to continue. Upon confirmation, 'Create Add-On Examples' oper. will run,\n\n"
                "which generates the 'add_on_examples.txt' file AGPT-4 uses while generating/fixing.\n\n"
                "You get option to send error details by mail so we can fix, if this is checked"
            )
        },


        
        "auto_save_toggle": {
            "concise": "Toggles FAST auto-save for your current file. Verbose tool-tip available",
            "verbose": (
                "Auto-saves the current file.\n\n"
                "* Preferences on this panel are auto-saved.\n\n"
                "* Well documented...read all tool tips.\n\n"
                "Make sure to turn on DISK SPACE WARNING on the panel below.\n\n"
                "* FAST Auto-save doesn't require the typical shutdown of Blender....\n\n"
                "   While testing FAST religiously, we ALWAYS terminate the Blender process,\n\n"
                "* to test its fortitude during unexpected crashes.\n\n"
                "1. This is all you need for SERIOUS DATA PROTECTION!!\n\n"
                "2. If saved, uses the current file name, else 'scratch.blend' on the Desktop.\n\n"
                "3. Any missed saves, click Report Issues in preferences! (We never get any!)"
            )
        },
    
        "enter_material_preview_mode": {
            "concise": "Enters Material Preview mode when clicking Advanced Local Mode. Verbose tool-tip available",
            "verbose": (
                "This option switches the display mode to Material Preview when clicking Advanced Local Mode.\n\n"
                "It provides a streamlined environment for material adjustments"
            )
        },

        "add_blue_cube": {
            "concise": "Adds blue-colored cube when using the Blender Dark 2 theme. Verbose tool-tip available",
            "verbose": (
                "When enabled, automatically changes the default cube’s color to a pleasing blue,\n\n"
                "upon starting Blender if the 'Blender Dark Two' theme is installed"
            )
        },
        "exit_to_solid_mode": {
            "concise": "Exits to Solid Mode when leaving Advanced Local Mode. Verbose tool-tip available",
            "verbose": (
                "When exiting Local Mode, this option switches the display to Solid Mode.\n\n"
                "This only occurs if the user was previously in Material Preview mode"
            )
        },
        "auto_save_interval": {
            "concise": "Auto-save interval in seconds. Verbose tool-tip available",
            "verbose": (
                "Set the interval in seconds for FAST Auto-save.\n\n"
                "* 60 seconds minimum is recommended.\n\n"
                "* 10 seconds is safe for small files.\n\n"
                "* 59 seconds and below may cause erratic mouse movements in larger files"
            )
        },
    
    
        "diffeomorphic_camera_x_offset": {
            "concise": "The X offset of the camera used during import. Verbose tool-tip available",
            "verbose": (
                "The X offset value determines the horizontal shift of the camera used during the character import process.\n\n"
                "Adjust this value to fine-tune the camera's position for proper framing of imported assets"
            )
        },
        "diffeomorphic_camera_y_offset": {
            "concise": "The Y offset of the camera used during import. Verbose tool-tip available",
            "verbose": (
                "The Y offset value determines the vertical shift of the camera during the character import process.\n\n"
                "Adjust this value to control the height position of the camera for imported models"
            )
        },
        "diffeomorphic_skin_color": {
            "concise": "Sets the Daz skin material color. Verbose tool-tip available",
            "verbose": (
                "This option defines the RGBA color for the Daz skin material applied during character import.\n\n"
                "It supports custom colors, allowing you to specify the tone and transparency of the skin material"
            )
        },
        "diffeomorphic_clothes_color": {
            "concise": "Sets the Daz clothes material color. Verbose tool-tip available",
            "verbose": (
                "This option defines the RGBA color for the Daz clothes material used during import.\n\n"
                "Customizable color options allow you to adjust the clothes' appearance on imported characters"
            )
        },
        "diffeomorphic_material_method": {
            "concise": "Choose the material method for Daz imports. Verbose tool-tip available",
            "verbose": (
                "Select the appropriate material method for imported Daz assets.\n\n"
                "Available options include standard BSDF, Extended Principled, and Single Principled shaders, each with different features"
            )
        },
        "diffeomorphic_use_replace_slots": {
            "concise": "Replace material slots during import. Verbose tool-tip available",
            "verbose": (
                "When enabled, existing material slots in the scene will be replaced with the first materials during the Daz import.\n\n"
                "This option ensures that imported materials take precedence over existing materials"
            )
        },
        "diffeomorphic_use_add_slots": {
            "concise": "Add material slots during import. Verbose tool-tip available",
            "verbose": (
                "When enabled, extra material slots will be added after the existing material slots for the imported assets.\n\n"
                "This is useful when you need to retain previous material setups while adding new ones"
            )
        },
        "diffeomorphic_use_match_names": {
            "concise": "Match material names when importing. Verbose tool-tip available",
            "verbose": (
                "Enabling this option ensures that the imported materials' names are matched with existing ones during the import process.\n\n"
                "This is useful for keeping consistent naming conventions in your scene"
            )
        },
 
        "diffeomorphic_import_action": {
            "concise": "Imports an action with the Daz character. Verbose tool-tip available",
            "verbose": (
                "Import an action when you import a Daz character.\n\n"
                "Check VISEMES to import MIMIC animation.\n\n"
                "Please note that MIMIC animation can only be created in Daz Studio 32-bit.\n\n"
                "When creating a text file to accompany your audio file, ensure that it is named identically and contains a verbatim transcription of the spoken text.\n\n"
                "Punctuation is not required.\n\n"
                "If a character speaks a number, write out the number in word form rather than using digits"
            )
        },
        "diffeomorphic_disable_hair": {
            "concise": "Disables high-poly hair during Daz character import. Verbose tool-tip available",
            "verbose": (
                "If enabled, hair objects with polygons exceeding 26,090 will be hidden in the viewport at import.\n\n"
                "This is useful for animating without Blender hanging.\n\n"
                "1. Add high-poly hair in DAZ, parent it, and hide it before saving.\n\n"
                "2. Import the character into Blender and click DISABLE HAIR.\n\n"
                "3. Click MONITOR to animate without high-poly hair visible.\n\n"
                "4. Enable high-poly hair to render.\n\n"
                "Alternatively, duplicate the hair, convert it to mesh, and decimate with Planar (default) before applying"
            )
        },

        "button_spacing": {
            "concise": "Adjusts topbar button spacing to prevent overlap w/ topbar tabs. Verbose tool-tip available",
            "verbose": (
                "We've been working to get the button spacing right for the mode topbar buttons and,\n\n"
                "now this setting adjusts dynamically based on monitor resolution and scale so the,\n\n"
                "topbar buttons don't overlap topbar tabs.\n\n"
                "If you notice that the button spacing doesn't match at a certain resolution, you can manually,\n\n"
                "adjust this slider. Once set, the updated value will auto save to FAST Settings/data points.json and,\n\n"
                "be used to keep the topbar buttons at your setting.\n\n"
                "For best results, simply tweak the slider when neccessary and you won't,\n\n"
                "have to worry about it again for this resolution"
            ),
        },
        

        "left_padding": {
            "concise": "Sets the left padding for non-silent sections. Verbose tool-tip available",
            "verbose": (
                "Amount of time (in seconds) to keep before the start of a non-silent section.\n\n"
                "Drag the slider to the left to adjust. If markers created after removing silence overlap other markers, "
                "undo the changes and reduce the padding"
            )
        },
        "right_padding": {
            "concise": "Sets the right padding for non-silent sections. Verbose tool-tip available",
            "verbose": (
                "Amount of time (in seconds) to keep after the end of a non-silent section.\n\n"
                "Drag the slider to the right to adjust. If markers created after removing silence overlap others, "
                "undo the changes and reduce the padding"
            )
        },
        
        "gpt_use_beep": {
            "concise": "Toggle beep for Autonomous GPT-4. Verbose tool-tip available",
            "verbose": ("Enable/Disable BEEP for Autonomous GPT-4 operator.\n\n"
                        "Don't hear beep?? Turn up System Sounds in your OS"
            )
        },
        
        "use_beep": {
            "concise": "Enable/Disable beep for all operators. Verbose tool-tip available",
            "verbose": ("Enable/Disable BEEP for all operators that use.\n\n"
                        "Some operators use beep functionality to alert you,\n"
                        "but do so as a secondary measure only.\n\n"
                        "Beep settings are on the FAST AUDIO panel.\n\n"
                        "Don't hear beep?? Turn up System Sounds in your OS"
            )
        },
    
        "auto_save_disk_warning_threshold": {
            "concise": "Sets the disk space threshold for warning. Verbose tool-tip available",
            "verbose": (
                "Sets the threshold (in GB) at which you'll receive an audio notification.\n\n"
                "The disk warning interval is the same as the auto-save interval set above.\n\n"
                "Note: The disk warning cannot be deactivated and is hard-coded for system safety"
            )
        },
    
        "daz_studio_content_library_one": {
            "concise": "First Daz Studio content library path. Verbose tool-tip available",
            "verbose": ("The paths where your Daz Studio assets are kept and are used,\n\n"
                        "when FAST interfaces with Diffeomorphic during asset auto-import.\n\n"
                        "Add up to 3 content library paths for asset import.\n\n"
                        "These paths are temporary during asset import.\n\n"
                        "Editing EVEE.json file updates these path boxes.\n\n"
                        "See the ERROR + SCAN PATHS tool-tip above for more information.")
        },
        
        "daz_studio_content_library_two": {
            "concise": "Second Daz Studio content library path. Verbose tool-tip available",
            "verbose": ("The paths where your Daz Studio assets are kept and are used,\n\n"
                        "when FAST interfaces with Diffeomorphic during asset auto-import.\n\n"
                        "Add up to 3 content library paths for asset import.\n\n"
                        "These paths are temporary during asset import.\n\n"
                        "Editing EVEE.json file updates these path boxes.\n\n"
                        "See the ERROR + SCAN PATHS tool-tip above for more information.")
        },
        
        "daz_studio_content_library_three": {
            "concise": "Third Daz Studio content library path. Verbose tool-tip available",
            "verbose": ("The paths where your Daz Studio assets are kept and are used,\n\n"
                        "when FAST interfaces with Diffeomorphic during asset auto-import.\n\n"
                        "Add up to 3 content library paths for asset import.\n\n"
                        "These paths are temporary during asset import.\n\n"
                        "Editing EVEE.json file updates these path boxes.\n\n"
                        "See the ERROR + SCAN PATHS tool-tip above for more information.")
        },
        
        
        "audio_device": {
            "concise": "Select audio device for startup. Verbose tool-tip available",
            "verbose": ("Choose which startup preferences you want automatically enabled.\n\nAre you using 'OpenAL' and getting no audio out of speaker??\n\nJust switch to 'WASAPI' and switch back to 'OpenAL'...it works!\n\nThis is exactly what the audio fix below does (it auto-runs at startup.)\n\nNote: If you change audio device in the OS you need to,\n\nrestart Blender to hear audio from that device.\n\nNote: I set ''OpenAL' default because it's high performance in big scenes.\n\nNote: Can't enable audio device that's not available on your OS\n\nCurrent Audio Device")
        },
    
        "fast_button_use_beep": {
            "concise": "Enable beep for fast button. Verbose tool-tip available",
            "verbose": ("Toggle to enable/disable beep sound for the fast button.\n\n"
                        "Use this setting to hear a confirmation beep when interacting.")
        },
        
        "use_beep_local_global": {
            "concise": "Enable beep for local/global mode switch. Verbose tool-tip available",
            "verbose": ("Toggle beep for when switching between local and global modes.\n\n"
                        "Beep only sounds when button is clicked, to avoid constant alerts.")
        },
        
        "api_key": {
            "concise": "Enter your OpenAI API key. Verbose tool-tip available",
            "verbose": ("Enter your OpenAI API key for GPT functionality.\n\n"
                        "If an API key error occurs at startup, delete the key file and restart Blender.\n\n"
                        "'Documents/FAST Settings/api_key.csv'")
        },
        
        "diffeomorphic_use_only_selected": {
            "concise": "Only merge armatures that are children of selected armature. Verbose tool-tip available",
            "verbose": (
                "When importing a Daz character, only merge armatures that are children of selected armature"
            )
        },
        
        "gpt_choose_to_take_snapshot": {
            "concise": "Takes a screenshot of your screen instead of using a custom image. Verbose tool-tip available",
            "verbose": (
                "Check this property to take a screenshot of your entire screen instead of,\n\n"
                "using an image that you supplied in the 'Node Image Path' box"
            )
        },
        "gpt_data_limit": {
            "concise": "Sets the data limit for GPT usage, affects token cost. Verbose tool-tip available",
            "verbose": (
                "Default value is 5000 characters. Increase it if you need to, but realize,\n\n"
                "that this could increase token usage quite a bit. So if you do increase it past,\n\n"
                "5000, which is already pretty high, then keep looking at your credit usage on the website,\n\n"
                "and see how much it costs you every time you run it with that amount of data"
            )
        },
        "gpt_random_user_command": {
            "concise": "Generates a random command for testing AGPT-4. Verbose tool-tip available",
            "verbose": (
                "Allows you to generate a random user command when you run AGPT-4 from this panel.\n\n"
                "Don't worry, it won't overwrite your original user command in file,\n\n"
                "but you'll see random user command in the console when you run the operator.\n\n"
                "Turns on standard 'Boost' (costs < $0.01), for you, to verify cmd w/ Blender manual.\n\n"
                "Automatically unlinks any added code files, as not necessary, when generating a random command.\n\n"
                "We use this for internal testing, but you could also use it if you just want,\n\n"
                "to play around with the features and you don't know what to write for a user command.\n\n"
                "Note: It will overwrite user command in your file as soon as the operator starts.\n\n"
                "The testing system is so optimized, all we really do is check this and run AGPT-4 and fix issues.\n\n"
                "If you get bored/have extra time, You can run AGPT-4 w rand cmd on til hit maximum iterations with no fix,\n\n"
                "& use the instructions that come up to create an instruction set and send it...that'll make everybody's Day!\n\n"
                "If you do, do 🙂 that, thank you! Please make sure to include the error code with the set...& thx again!!! 🙂👍"
            )
        },
        "gpt_model_secondary": {
            "concise": "Switch from GPT-4o to the cheaper o3-mini for helper functions. Verbose tool-tip available",
            "verbose": (
                "🚀 OpenAI recently launched the o3-mini model, offering a cheaper alternative to GPT-4o.\n\n"
                "💡 This setting allows you to switch from the default GPT-4o model to o3-mini.\n\n"
                "🔄 The functions affected by this setting are specialized helper functions.\n\n"
                "📌 These functions either pre-process code before the main assistant handles it,\n\n"
                "or fix potential issues after code is generated.\n\n"
                "🔧 **Functions Affected:**\n\n"
                "- `extract_error_messages`\n\n"
                "- `check_and_fix_file_paths`\n\n"
                "- `analyze_smtp_and_modules`\n\n"
                "- `add_calls_and_verify_object`\n\n"
                "⚡ **Execution Frequency:**\n\n"
                "- All four functions run **once** when this system starts.\n\n"
                "- The following two run **every iteration** when a script is generated:\n\n"
                "  ➤ `analyze_smtp_and_modules`\n\n"
                "  ➤ `add_calls_and_verify_object`\n\n"
                "💰 **Cost Savings:**\n\n"
                "- Switching to `o3-mini` saves money per input/output token.\n\n"
                "- Cost efficiency increases significantly for long-running processes.\n\n"
                "- Example: If your script runs for five iterations, you save even more.\n\n"
                "⚠️ **Why it's NOT the Default:**\n\n"
                "- The o3-mini model is **untested** in this workflow.\n\n"
                "- If errors occur, you can report them or switch back to GPT-4o.\n\n"
                "🛠 **If you see function-related errors in the console,**\n\n"
                "they likely originate from this setting"
            )
        },
        "gpt_edit_user_command_prompt": {
            "concise": "Adds prompt for editing user commands in the console. Verbose tool-tip available",
            "verbose": (
                "Check this to regain the prompt to edit your user command in the console.\n\n"
                "The prompt was added to the console initially because the user command is so important.\n\n"
                "If you toggle this off, please remember to enable it before running AGPT-4.\n\n"
                "When you confirm your prompt, if you had 'Boost User Command' or 'Advanced Boost User Command' enabled,\n\n"
                "the prompt is auto saved to 'user_command.txt' to minimize chance of having to boost again.\n\n"
                "Note: Always shown in AGPT-4 [Text Editor] as it's vital you verify user command is fix request"
            )
        },
        "gpt_show_verify_example_prompt": {
            "concise": "Shows verify prompt to pause AGPT-4 for verifying or removing an example. Verbose tool-tip available",
            "verbose": (
                "Toggle this on to show verify prompt that pauses the operation of the AGPT-4 script generator.\n\n"
                "When an example is provided, at AGPT-4 startup, this prompt allows you to verify or remove the example"
            )
        },

        "gpt_send_anonymous_data": {
            "concise": "Sends anonymous error data to GitHub for debugging. Verbose tool-tip available",
            "verbose": (
                "Enable this option to send the red error section (only) to our public GitHub repository if the\n\n"
                "Autonomous GPT-4 functionality encounters the same error for every iteration.\n\n"
                "This helps us identify and address issues, such as missing login credentials for the SMTPLIB library,\n\n"
                "incorrect file paths being added, or access denied errors or other unforeseen errors"
            )
        },
        "gpt_file_permission_fixer_path": {
            "concise": "Path used for fixing file permission errors in scripts. Verbose tool-tip available",
            "verbose": (
                "This path is used when fixing FILE PERMISSION errors in file paths within your generated scripts.\n\n"
                "If the path causing the error is for non-critical data like saving renders or writing log files,\n\n"
                "it will be replaced with this path. The default path is set to a folder on your desktop named 'AGPT-4'.\n\n"
                "This path is hard-coded and cannot be changed. It is provided for reference only"
            )
        },
    
        "gpt_smtp_lib_app_password": {
            "concise": "Enter your SMTP app password for sending emails with SMTPLIB. Verbose tool-tip available",
            "verbose": (
                "This is your SMTP app password. You only need to provide this if you are intending to ask,\n\n"
                "AGPT-4 to generate code that uses the SMTPLIB library to send emails (e.g., through Gmail).\n\n"
                "The username will be your email address (e.g., your_email@gmail.com).\n\n"
                "To generate an app password for Gmail, follow these steps:\n\n"
                "1. Go to your Google Account.\n"
                "2. Select 'Security'.\n"
                "3. Under 'Signing in to Google', select 'App Passwords'.\n"
                "4. Sign in...At the bottom, choose 'Select app' and 'Select device' and choose the appropriate options.\n"
                "5. Follow the instructions to generate the app password.\n\n"
                "If you don't know what the SMTPLIB library is, you don't need to worry about this setting"
            )
        },
        "gpt_smtp_lib_server": {
            "concise": "Enter your email provider's SMTP server, e.g., 'smtp.gmail.com' for Gmail. Verbose tool-tip available",
            "verbose": (
                "This is the SMTP server for your email provider. For Gmail, this should be 'smtp.gmail.com'.\n\n"
                "Ensure the SMTP server matches your email provider's settings"
            )
        },
    
        "gpt_confirm_data": {
            "concise": "Automatically confirms data for you instead of showing a dialog. Verbose tool-tip available",
            "verbose": (
                "This replaces the data confirmation section that showed up in the console.\n\n"
                "If checked it will automatically confirm yes for you,\n\n"
                "if unchecked the confirmation dialog will show up as normal.\n\n"
                "If using 'Pull SE & BSE Examples' button to generate an example,\n\n"
                "this is toggled off just so we could be sure that you meant to send bone or node data"
            )
        },
        "gpt_boost_user_command": {
            "concise": "Boosts your command using added code for precision. Verbose tool-tip available",
            "verbose": (
                "Checked: Autonomous GPT-4 analyzes request, code you may've added + Blender 4.3 manual to,\n\n"
                "refine your request. Doesn't alter your initial goal but provides a detailed command that,\n\n"
                "matches your intended purpose. Ideal for solving complex issues with greater precision.\n\n"
                "Hint: Boosted command is auto-added to user command file.\n\n"
                "Hint: 'user-command-backup.txt' is created before boost, next to 'user-command.txt'.\n\n"
                "Turning on 'Boost User Command' ensures your command is verified step-by-step\n\n"
                "against the Blender manual, confirming correct terminology and actions.\n\n"
                "This also helps the assistant send relevant instructions to guide script\n\n"
                "generation according to best practices in Blender. By boosting, the assistant\n\n"
                "can filter and prioritize instructions more effectively, as it uses your\n\n"
                "optimized command to choose what’s essential.\n\n"
                "Note: The assistant reviews those specific inst. sets + relevant user inst. sets,\n\n"
                "from 'FAST Settings/AGPT-4 Instructions/script-gen-instruction-sets.txt' for any\n\n"
                "additional guidance.\n\n"
                "Since we can’t send all instructions at once without risking irrelevant info,\n\n"
                "the assistant focuses only on what’s necc. and boosting command helps with that"
            )
        },
        
        "gpt_advanced_boost_user_command": {
            "concise": "Uses the advanced GPT-4o model for more accurate command boosting. Verbose tool-tip available",
            "verbose": (
                "Check to use the advanced GPT-4o model for boosting user command.\n\n"
                "When checked it also looks up the API which will improve your script.\n\n"
                "Standard boost uses the GPT-4o mini model, this uses the GPT-4o model.\n\n"
                "Costs more but some e.g. scripts for modeling, may require it to be successful"
            )
        },
    
    

    
        "gpt_confirm_object_is_selected": {
            "concise": "Confirms that required objects are selected before running the script. Verbose tool-tip available",
            "verbose": (
                "This replaces the object reference section that showed up in the console.\n\n"
                "This property is toggled off when the operator finishes or Blender is restarted, so it's important to check each time.\n\n"
                "Checklist:\n"
                "1. Are objects needed by the script?\n"
                "2. Are the objects selected?\n"
                "3. If no, select the objects, then check this property.\n\n"
                "Confirmation Information:\n"
                "1. If you check this, a reference will be added and the current file will be used.\n"
                "2. If you check this, the objects will be referenced for you in the user command (internally) without changing the file.\n"
                "3. If you check this, your Blender file containing the objects will be used for error tests.\n\n"
                "Note: If providing bone data, the rig must be selected"
            )
        },
    
        "bse_search_term": {
            "concise": "Search for terms on Blender Stack Exchange. Verbose tool-tip available",
            "verbose": (
                "Enter a search term to look up on Blender Stack Exchange.\n\n"
                "This is a precursor to AGPT-4's Auto-BSE lookup feature (providing here until implemented)"
            )
        },
    
    
        "gpt_find_code_examples": {
            "concise": "Finds code examples based on your boosted user command. Verbose tool-tip available",
            "verbose": (
                "When enabled, this retrieves a relevant code example at startup to help generate your script.\n"
                "This is absolutely vital for success and costs $0.10 per run.\n\n"
                "To work, it needs to boost your user command first, which adds less than $0.01,\n"
                "as we use the cheaper GPT-4o Mini model for boosting, as it gives solid results.\n\n"
                "This setting only applies to the initial lookup when starting a script.\n"
                "During error fix iterations (which default to five), code examples are always retrieved,\n"
                "but those use GPT-4o Mini automatically and are not affected by this setting.\n\n"
                "We leave this as an option to turn off if needed, mainly for testing errors outside\n"
                "of the example retrieval functionality, but we strongly recommend keeping it on."
            )
        },


        "gpt_extra_data_for_find_code_examples": {
            "concise": "Adds precise API and operator calls to your boosted command for improved example lookup. Verbose tool-tip available",
            "verbose": (
                "When checked, if 'Find Code Examples' is also checked, the boosted prompt is re-analyzed.\n\n"
                "The exact, specific API or operator calls are added to every line.\n\n"
                "This improves the example lookup by ensuring precise search terms.\n\n"
                "The boosted feature is enhanced as the assistant will know the exact operators, functions, variables, and properties to use.\n\n"
                "Note: OpenAI's model knowledge only goes back to October 2023, so recent API verification is required.\n\n"
                "This feature costs approximately $0.10 more, and it runs regardless of whether boost or advanced boost is turned on"
            )
        },
        "gpt_show_lookups": {
            "concise": "Shows printed output of API, manual, and code lookups. Verbose tool-tip available",
            "verbose": (
                "Turn this property on to show API, manual, and code lookup printed output.\n\n"
                "Otherwise, they aren't printed, though they are still generated and given to 'Autonomous GPT-4'.\n\n"
                "You can turn this on at any time while your code is processing"
            )
        },
        "show_se_content": {
            "concise": "Shows extra text in the scanned Blender/Stack Exchange questions. Verbose tool-tip available",
            "verbose": (
                "Shows extra text in the Blender/Stack Exchange questions we're scanning.\n\n"
                "You can turn this on at any time while your code is processing"
            )
        },
        "gpt_show_cost": {
            "concise": "Shows token usage details in the console. Verbose tool-tip available",
            "verbose": (
                "Shows the token printouts in the console so you can see token usage per function.\n\n"
                "You can turn this on at any time while your code is processing"
            )
        },
        "gpt_4o_mini_input_token_count": {
            "concise": "Displays the GPT-4 mini input token count used, priced at $0.15 per million. Verbose tool-tip available",
            "verbose": (
                "Retrieves the total GPT-4 mini input token count, priced at $0.15 per 1 million tokens,\n\n"
                "and displays it on the panel.\n\n"
                "Not a settable property (this value is displayed this way to make it look nice on the panel)"
            )
        },
        "gpt_4o_mini_output_token_count": {
            "concise": "Displays the GPT-4 mini output token count, priced at $0.60 per million. Verbose tool-tip available",
            "verbose": (
                "Retrieves the total GPT-4 mini output token count, priced at $0.60 per 1 million tokens,\n\n"
                "and displays it on the panel.\n\n"
                "Not a settable property (this value is displayed this way to make it look nice on the panel)"
            )
        },
        "gpt_4o_mini_total_token_count": {
            "concise": "Displays the total GPT-4 mini token count (input and output combined). Verbose tool-tip available",
            "verbose": (
                "Retrieves the total GPT-4 mini token count, the sum of both input and output tokens across all runs,\n\n"
                "and displays it on the panel.\n\n"
                "Not a settable property (this value is displayed this way to make it look nice on the panel)"
            )
        },
        "gpt_4o_input_token_count": {
            "concise": "Displays the GPT-4o input token count, priced at $2.50 per million. Verbose tool-tip available",
            "verbose": (
                "Retrieves the total GPT-4o input token count, priced at $2.50 per 1 million tokens,\n\n"
                "and displays it on the panel.\n\n"
                "Not a settable property (this value is displayed this way to make it look nice on the panel)"
            )
        },
        "gpt_4o_output_token_count": {
            "concise": "Displays the GPT-4o output token count, priced at $10.00 per million. Verbose tool-tip available",
            "verbose": (
                "Retrieves the total GPT-4o output token count, priced at $10.00 per 1 million tokens,\n\n"
                "and displays it on the panel.\n\n"
                "Not a settable property (this value is displayed this way to make it look nice on the panel)"
            )
        },
        "gpt_4o_total_token_count": {
            "concise": "Displays the total GPT-4o token count (input and output combined). Verbose tool-tip available",
            "verbose": (
                "Retrieves the total GPT-4o token count, the sum of both input and output tokens across all runs,\n\n"
                "and displays it on the panel.\n\n"
                "Not a settable property (this value is displayed this way to make it look nice on the panel)"
            )
        },
        "gpt_o3_mini_input_token_count": {
            "concise": "Displays the o3 mini input token count, priced at $1.10 per million. Verbose tool-tip available",
            "verbose": (
                "Retrieves the total GPT o3 mini input token count.\n\n"
                "This is the count of input tokens used, priced at $1.10 per 1 million tokens.\n\n"
                "This value is automatically updated to display on the panel.\n\n"
                "Not a settable property (it's displayed this way to make it look nice on the panel)"
            )
        },
        "gpt_o3_mini_output_token_count": {
            "concise": "Displays the GPT o3 mini output token count, priced at $4.40 per million. Verbose tool-tip available",
            "verbose": (
                "Retrieves the total GPT o3 mini output token count.\n\n"
                "This is the count of output tokens generated by the model, priced at $4.40 per 1 million tokens.\n\n"
                "This value is automatically updated to display on the panel.\n\n"
                "Not a settable property (it's displayed this way to make it look nice on the panel)"
            )
        },
        "gpt_o3_mini_total_token_count": {
            "concise": "Displays the total GPT o3 mini token count (input and output combined). Verbose tool-tip available",
            "verbose": (
                "Retrieves the total GPT o3 mini token count.\n\n"
                "This is the sum total of both input and output tokens used across all runs.\n\n"
                "This value is automatically updated to display on the panel.\n\n"
                "Not a settable property (it's displayed this way to make it look nice on the panel)"
            )
        },
        "gpt_o1_mini_input_token_count": {
            "concise": "Displays the GPT o1 mini input token count, priced at $1.10 per million. Verbose tool-tip available",
            "verbose": (
                "Retrieves the total GPT o1 mini input token count.\n\n"
                "This is the count of input tokens used, priced at $1.10 per 1 million tokens.\n\n"
                "This value is automatically updated to display on the panel.\n\n"
                "Not a settable property (it's displayed this way to make it look nice on the panel)"
            )
        },
        "gpt_o1_mini_output_token_count": {
            "concise": "Displays the GPT o1 mini output token count, priced at $4.40 per million. Verbose tool-tip available",
            "verbose": (
                "Retrieves the total GPT o1 mini output token count.\n\n"
                "This is the count of output tokens generated by the model, priced at $4.40 per 1 million tokens.\n\n"
                "This value is automatically updated to display on the panel.\n\n"
                "Not a settable property (it's displayed this way to make it look nice on the panel)"
            )
        },
        "gpt_o1_mini_total_token_count": {
            "concise": "Displays the total GPT o1 mini token count (input and output combined). Verbose tool-tip available",
            "verbose": (
                "Retrieves the total GPT o1 mini token count.\n\n"
                "This is the sum total of both input and output tokens used across all runs.\n\n"
                "This value is automatically updated to display on the panel.\n\n"
                "Not a settable property (it's displayed this way to make it look nice on the panel)"
            )
        },
    
    
        "gpt_pause_before_fixing_errors": {
            "concise": "Pauses before fixing code errors, allowing manual edits between iterations. Verbose tool-tip available",
            "verbose": (
                "This pauses after the error is generated before attempting to fix the code each iteration,\n\n"
                "allowing you to make a quick edit to the code to help it get past an error.\n\n"
                "If you edit code, only replace items, do not add new ones; otherwise, it will not work.\n\n"
                "Autonomous GPT-4 cannot hold the intended change in memory if there isn't an item to recognize and replace each iteration.\n\n"
                "This functionality is new and will improve.\n\n"
                "You can untick this property at any time, and it will be recognized by Autonomous GPT-4.\n\n"
                "Filepath to add edits: 'FAST Settings/AGPT-4 Script Testing/modified_user_script.py'.\n\n"
                "This file is updated each iteration with your generated code plus extra code added for testing"
            )
        },
    
        "gpt_run_final_script": {
            "concise": "Runs the final generated script after processing. Verbose tool-tip available",
            "verbose": (
                "Controls whether to run the final script at the end of processing.\n\n"
                "When enabled, the script that was generated and refined through the iterations\n\n"
                "will be executed, resulting in visible changes in the viewport, such as creating objects\n\n"
                "or applying transformations based on the script's commands.\n\n"
                "Disable this if you plan to work on your scene while the script is being created,\n\n"
                "or if you're unsure whether the results of the script might cause unintended effects in your scene"
            )
        },

        "gpt_current_iteration": {
            "concise": "Displays the current iteration on the panel. Verbose tool-tip available",
            "verbose": (
                "A property that shows the current iteration on the panel.\n\n"
                "This is not settable (It just doesn't look good as a label).\n\n"
                "You can view the progress of script generation or error checking iterations here"
            )
        },
        "gpt_use_beep": {
            "concise": "Enables a beep sound for the Autonomous GPT-4 operator. Verbose tool-tip available",
            "verbose": (
                "Enable or disable the BEEP for the Autonomous GPT-4 operator.\n\n"
                "If you don't hear the beep, check and turn up System Sounds in your OS settings"
            )
        },
        "gpt_operator_name": {
            "concise": "Specifies the operator to run at startup, useful for testing. Verbose tool-tip available",
            "verbose": (
                "Run 'bpy.ops.fast.auto_gpt_assistant()' or another Blender operator at startup.\n\n"
                "This is primarily used for testing, but you may find it useful too.\n\n"
                "Make sure to add the command to 'Command Override'.\n\n"
                "NOTE: Unrelated console errors can block this from working"
            )
        },
        "gpt_run_on_selected_objects": {
            "concise": "Runs the generated script on the selected object(s). Verbose tool-tip available",
            "verbose": (
                "If this boolean property is selected, then GPT will apply your script request to the selected object(s).\n\n"
                "Make sure to also reference the object by name, including proper capitalization, in your script generation request"
            )
        },
        "gpt_added_code": {
            "concise": "Specifies the path to additional code for GPT to reference or fix. Verbose tool-tip available",
            "verbose": (
                "Specify the path to a file containing additional code for GPT to reference or fix.\n\n"
                "Use the keyword 'fix code' in your query when you add Python code here"
            )
        },
        "gpt_show_code": {
            "concise": "Toggles code visibility in the console. Verbose tool-tip available",
            "verbose": (
                "Toggles the visibility of all code in the console.\n\n"
                "We're working to improve this functionality and make it more user-friendly.\n\n"
                "If you're not a coder, you can turn this off and read messages to understand what's happening instead.\n\n"
                "However, sometimes it's important to see the code to troubleshoot issues.\n\n"
                "You can turn this on at any time while your code is processing"
            )
        },
        "gpt_error_check_timeout": {
            "concise": "Adjusts the timeout before Blender quits after a subprocess execution. Verbose tool-tip available",
            "verbose": (
                "Autonomous GPT-4 scripts are tested in a Blender subprocess.\n\n"
                "Adjust the time Blender waits before quitting after running in a subprocess.\n\n"
                "This is a delay to ensure your script has enough time to finish executing.\n\n"
                "A minimum of 15 seconds is hard-coded for safety.\n\n"
                "If Blender doesn't fully start before quitting in 10 + (this value) seconds, increase the timeout.\n\n"
                "This helps ensure error messages are fully captured.\n\n"
                "To monitor this, check the 'Error Check in Foreground Mode' property and rerun the operator"
            )
        },
        "gpt_main_assistant_temperature": {
            "concise": "Adjusts the balance between creativity and reliability in AI responses. Verbose tool-tip available",
            "verbose": (
                "You can change this property, but it will be reverted at Blender startup.\n\n"
                "These settings are critical to the system running well, and we've found success with these values.\n\n"
                "Setting the 'temperature' influences the balance between creativity and reliability in AI responses.\n\n"
                "Lower values lead to more reliable, less diverse outputs, while higher values allow for more creativity,\n\n"
                "but possibly riskier results.\n\n"
                "If changing this value resolves an issue, please report your findings so we can improve the default settings"
            )
        },
        "gpt_main_assistant_top_p": {
            "concise": "Controls nucleus sampling to influence the diversity of AI responses. Verbose tool-tip available",
            "verbose": (
                "You can change this property, but it will be reverted at Blender startup.\n\n"
                "These settings are critical to the system running well, and we've found success with these values.\n\n"
                "Setting 'top_p' controls the nucleus sampling for AI responses.\n\n"
                "Lower values consider only the most probable outputs, leading to more focused, reliable results.\n\n"
                "Higher values allow for broader outputs, fostering diversity and creativity.\n\n"
                "If changing this value resolves an issue, please report your findings so we can improve the default settings"
            )
        },
        "gpt_advanced_api_or_manual_or_fast_decider": {
            "concise": "Uses the advanced GPT-4o model to decide whether to send API, manual, or add-on info. Verbose tool-tip available",
            "verbose": (
                "Check this to use the advanced GPT-4o model to decide whether to send API lookups, manual lookups,\n\n"
                "or add-on lookup information to GPT.\n\n"
                "We only send one of the four options each iteration to avoid overwhelming GPT with too much data.\n\n"
                "This costs around $0.03 per use, while the standard GPT-4 mini model costs about $0.01.\n\n"
                "Run Autonomous GPT-4 to see the decision-making process in the console, then check this box to compare.\n\n"
                "Note: This setting doesn't apply when using the 'blender-question' keyword"
            )
        },
        # "azure_enable_rest_keyframes": {
        #     "concise": "Adds rest keyframes to silent sections of the animation. Verbose tool-tip available",
        #     "verbose": (
        #         "Adds rest keyframes to the start and end of silent sections, determined by the 'Silence Threshold'.\n\n"
        #         "This only applies if there are no rest pose keyframes on the frame immediately before or after that frame"
        #     )
        # },
        "azure_add_markers": {
            "concise": "Adds phoneme markers for better animation visualization. Verbose tool-tip available",
            "verbose": (
                "Add phoneme markers at the frame of added poses to help better visualize the animation.\n\n"
                "When checked, the singular add keyframe buttons are also affected for intuitive use"
            )
        },
        "azure_silence_thresh_rms": {
            "concise": "Sets the silence threshold for adding rest keyframes. Verbose tool-tip available.",
            "verbose": (
                "Determines silent portions of your audio where rest keyframes are added at the start and end.\n\n"
                "For use with the phonetic setting, where the mouth may remain open after saying words.\n\n"
                "When you run the operator with the 'Add Rest Keyframes' option enabled, the script evaluates\n"
                "your audio to identify silent sections. These are determined based on this 'Silence Threshold' value (RMS).\n\n"
                "For each silent section derived, the 'white text' section in the console will display:\n"
                "  - Start and End Frames of the section.\n"
                "  - RMS Values for Each Slice within the silent section, providing a numerical representation of\n"
                "    the waveform.\n"
                "  - Lowest RMS in the Section, helping you understand the quietest part.\n\n"
                "The RMS values printed in the console represent slices of audio within the section. These values\n"
                "are listed in order of their position in the section. For example, if the section spans frames 27\n"
                "to 29 and includes ten RMS values, each number represents the sound level of a specific slice in\n"
                "that section, starting from the first slice to the last.\n\n"
                "Higher RMS values indicate more sound, while lower values (e.g., around 20) suggest little to no sound.\n\n"
                "Steps to refine the silence threshold:\n\n"
                "1. **Detect Missing Silent Sections**: If a section you believe should be silent is not detected,\n"
                "   you won't see any output for that section in the console. To resolve this, raise the threshold by an\n"
                "   arbitrary value, such as 50, and rerun the operator. This helps overshoot the silence detection.\n\n"
                "2. **Undo and Adjust**: After running the operator, undo the action by clicking the 'Undo' button on the\n"
                "   top bar until the audio strip and keyframes disappear. This action won't reset the property value.\n"
                "   You can then modify the threshold and rerun the operator. Alternatively, you can set the property\n"
                "   first and undo afterward—the order does not matter.\n\n"
                "3. **Eliminate Unwanted Sections**: Once you have overshot, or to eliminate sections with unwanted sounds,\n"
                "   in the first place you can use the console output to identify RMS values within those sections,\n"
                "   and lower the threshold slightly below the lowest RMS value\n"
                "   representing unwanted sound. Rerun the operator and repeat until only the intended sections remain.\n\n"
                "4. **Iterative Refinement**: By running, adjusting, and rerunning the operator, you can precisely control\n"
                "   which sections qualify as silent. Over time, this approach allows you to find the ideal RMS threshold\n"
                "   dependent on the way your specific audio clips are generated\n\n"
                "This process ensures a practical and iterative way to refine silence detection, giving you full control\n"
                "over what qualifies as silent sections. By combining overshooting, undoing, and eliminating, you can\n"
                "quickly achieve optimal results without relying on external tools or guesswork."
            )
        },
        "use_beep_local_global": {
            "concise": "Toggles beep sound when switching modes. Verbose tool-tip available",
            "verbose": (
                "Toggle to disable the beep sound that occurs when you switch modes.\n\n"
                "The beep only sounds when you click the button, which may become annoying if frequent"
            )
        },
        "disable_render_and_window": {
            "concise": "Toggles rendering of the viewport and preview window display. Verbose tool-tip available",
            "verbose": (
                "Enable to render the viewport and show a preview in a separate window.\n\n"
                "Disable this if the window doesn’t come to the foreground or if you encounter camera misalignment in large scenes"
            )
        },
        "key_saved_clip_for_reimport_clip": {
            "concise": "Stores the file path of the last used clip for reimporting. Verbose tool-tip available",
            "verbose": (
                "Stores the file path of the last used clip for reimporting.\n\n"
                "The file path will remain set after restarting Blender"
            )
        },
        "window_offset_x": {
            "concise": "Adjusts horizontal placement (in pixels) of centered windows. Verbose tool-tip available",
            "verbose": (
                "Adjust the horizontal placement (in pixels) of all centered windows.\n\n"
                "Only affects windows opened from the FAST Preferences header button"
            )
        },
        "window_offset_y": {
            "concise": "Adjusts vertical placement (in pixels) of centered windows. Verbose tool-tip available",
            "verbose": (
                "Adjust the vertical placement (in pixels) of centered windows.\n\n"
                "Only affects windows opened from the FAST Preferences header"
            )
        },
    
        "daz_import_obj_color": {
            "concise": "Sets the viewport color for the imported OBJ. Verbose tool-tip available",
            "verbose": (
                "Choose the viewport color for the imported OBJ.\n\n"
                "Note: This setting does not affect Daz Studio re-import"
            )
        },
        
        "azure_silence_length": {
            "concise": "Sets the min. silence length (in frames) to add extra 'rest' keyframes. Verbose tool-tip available.",
            "verbose": (
                "Determines the minimum length of silence (in frames) where additional 'rest'\n\n"
                "keyframes will be added automatically during lip-sync processing.\n\n"
                
                "**Why Add Rest Keyframes?**\n\n"
                
                "Azure Lip Sync does not always insert 'rest' keyframes accurately, which can\n\n"
                "cause the mouth to remain open or blend awkwardly between phonemes.\n\n"
                
                "Adding these extra 'rest' keyframes ensures the character's mouth closes properly\n\n"
                "during silent sections, enhancing the overall quality of the animation.\n\n"
        
                "**How It Works:**\n\n"
                
                "- If using the **Azure for Shape Keys** button, a 'rest' keyframe is added\n\n"
                "at both the start and end of silence sections exceeding the set frame length.\n\n"
                
                "- If using the **Azure for Grease Pencil** button, a 'rest' keyframe is added\n\n"
                "only at the start of the silent section since Grease Pencil frames are instant.\n\n"
        
                "**Important Notes:**\n\n"
                
                "- Designed for the **Azure Phonetic** setting for English speech.\n\n"
                "- Results may vary with the **PocketSphinx** mode, which suits more abstract\n\n"
                "or pitch-shifted voices and non-English speech patterns.\n\n"
                
                "- This feature is part of an ongoing improvement but has shown noticeable\n\n"
                "improvements in most lip-sync results when tested.\n\n"
    
            )
        },
        
                
                  
        "add_viewport_color": {
            "concise": "Adds color to the imported Daz OBJ. Verbose tool-tip available",
            "verbose": (
                "Choose to add color to the imported Daz OBJ.\n\n"
                "Changes viewport color setting at base of materials tab"
            )
        },
        "procedural_crowds_location": {
            "concise": "Sets the file path for the Procedural Crowds ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the Procedural Crowds ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
        "transportation_location": {
            "concise": "Sets the file path for the Transportation ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the Transportation ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
        "faceit_location": {
            "concise": "Sets the file path for the FACEIT ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the FACEIT ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
        "arkit_blendshape_helper_location": {
            "concise": "Sets the file path for ARKit Blendshape Helper. Verbose tool-tip available",
            "verbose": (
                "Set the path to the ARKit Blendshape Helper.\n\n"
                "This preference is saved in 'Documents/FAST Settings'"
            )
        },
        "furnishing_location": {
            "concise": "Sets the file path for the Ultimate Furniture Pack ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the Ultimate Furniture Pack ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
        "animation_layers_location": {
            "concise": "Sets the file path for the Animation Layers ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the Animation Layers ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
        "auto_rig_pro_location": {
            "concise": "Sets the file path for the Auto-Rig Pro ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the Auto-Rig Pro ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
        "auto_rig_pro_library_location": {
            "concise": "Sets the file path for the Auto-Rig Pro Library ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the Auto-Rig Pro Library ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
        "extreme_pbr_location": {
            "concise": "Sets the file path for the Extreme PBR ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the Extreme PBR ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
        "hdri_maker_location": {
            "concise": "Sets the file path for the HDRI Maker ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the HDRI Maker ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
        "ev_express_location": {
            "concise": "Sets the file path for the EV Express ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the EV Express ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
        "fast_mixamo_location": {
            "concise": "Sets the file path for the Mixamo ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the Mixamo ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
        "nview_location": {
            "concise": "Sets the file path for the N-View ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the N-View ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },

        "light_coll_contents_enum": {
            "concise": "Choose a collection to edit all lights within. If one light is selected, only it is adjusted. Verbose tool-tip available",
            "verbose": (
                "Choose a collection to edit all lights within. If one light is selected, only it is adjusted. Verbose tool-tip available\n\n"
                "This preference is saved in 'Documents/FAST Settings' on successful installation"
            )
        },
        "poliigon_location": {
            "concise": "Sets the file path for the Poliigon ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the Poliigon ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
        "rig_gns_pro_location": {
            "concise": "Sets the file path for the Rig-GNS ZIP file. Verbose tool-tip available",
            "verbose": (
                "Set the path to the Rig-GNS ZIP file.\n\n"
                "Button at the top will keep it installed and enabled.\n\n"
                "This preference is saved here and in 'Documents/FAST Settings' on successful installation"
            )
        },
    
        "render_viewport_overlays": {
            "concise": "Viewport overlays will be invisible when rendering if lighted. Verbose tool-tip available",
            "verbose": (
                "Turns on/off viewport overlays when rendering the output image or animation,\n\n"
                "while your overlays in the viewport remain intact, providing an unobstructed preview.\n\n"
                "Lighted means you will not see overlays in render, unlighted means you will."
            ),
        },

        "include_fast_startup_backup": {
            "concise": "Includes FAST Startup Backup directory in deletion. Verbose tool-tip available",
            "verbose": (
                "Include the FAST Startup Backup directory in the deletion process.\n\n"
                "This will NOT include any 'startup.blend' backups located in 'config' directory.\n\n"
                "This option is unchecked by default to ensure backups are available"
            )
        },
    
        "adv_local_keep_armature": {
            "concise": "Keeps armatures when entering advanced local mode. Verbose tool-tip available",
            "verbose": (
                "Choose to keep armatures when entering advanced local mode.\n\n"
                "For example, when selecting a character's body mesh that is parented to an armature"
            )
        },
    
        "auto_save_startup_file": {
            "concise": "Toggles automatic startup file saving during regular auto-save. Verbose tool-tip available",
            "verbose": (
                "Automatically auto-saves a startup file with your normal auto-save process.\n\n"
                "This option is especially useful for users needing the bookmarking feature for large files.\n\n"
                "Enabling this ensures that a startup file is saved during each auto-save, improving backup reliability on large projects"
            )
        },
    
        "auto_save_file": {
            "concise": "Enables or disables automatic saving of the main file. Verbose tool-tip available",
            "verbose": (
                "Selecting this option causes your main file to get saved during the auto-save procedure.\n\n"
                "If unchecked, the file will not be saved during auto-save or at startup,\n\n"
                "but all other checked actions on the panel will still be evaluated"
            )
        },
        "auto_save_bookmark_file": {
            "concise": "Enables an automatic file bookmarking system. Verbose tool-tip available",
            "verbose": (
                "A really awesome file bookmarking system...\n\n"
                "Saves the startup file and main file with every change, regardless of the panel interval setting.\n\n"
                "Necessary for creating a bookmark of your current scene state.\n\n"
                "Will only save the startup file if your current file size is less than 100 MB.\n\n"
                "This is currently in testing, and I'll increase the limit past 100 MB if it is safe"
            )
        },
        "auto_save_increment": {
            "concise": "Auto-saves with a timestamp and adds incremented filenames. Verbose tool-tip available",
            "verbose": (
                "Generates new file name each save and saves to,\n\n'FAST Auto-saves' folder in current or custom directory.\n\nAdds a tag to incremented file (e.g., [File]_FAST_1, [File]_FAST_2, etc.)...\n\nSo you know it was saved with the INCREMENT feature.\n\nThis is different from SAVE ON STARTUP which also increments,\n\nbut it saves with this naming convention (e.g., scratch_1, scratch_2, etc.)\n\nand also SAVE ON STARTUP saves only once at startup"
            )
        },
        "auto_save_increment_backup": {
            "concise": "Creates a backup of incremented files on startup. Verbose tool-tip available",
            "verbose": (
                "Creates another backup in 'Documents/FAST Increment Backup' on startup,\n\nif INCREMENT enabled, so when open up file and edit it the original is safe here.\n\nElse, as make changes if INCREMENT is on, could lose access to the original.\n\nNote: Duplicate file names get overwritten to save on disk space.\n\nBlender now has 'Revert' feature on 'File Menu' which is easier to use.\n\nI will leave this here as a fail safe, better to have two options, in case one fails"
            )
        },
        "auto_save_delete_old_versions": {
            "concise": "Deletes older saved versions when new ones are created. Verbose tool-tip available",
            "verbose": (
                "Manages files in the 'FAST Auto-saves' folder, requiring INCREMENT to be enabled.\n\n"
                "Keeps only the recent files based on the number you set in KEEP, and deletes older ones.\n\n"
                "Warning: This can result in losing existing files, so review the folder first to understand the impact.\n\n"
                "To prevent data loss, set SAVE VERSIONS in Blender's Preferences under 'SAVE & LOAD' to 1 or higher"
            )
        },
        "auto_save_file_size_warning": {
            "concise": "Monitors file size for sudden reductions during auto-save. Verbose tool-tip available",
            "verbose": (
                "Monitors Blender project file size on auto-save.\n\n"
                "If the file size drops drastically, it may indicate data corruption.\n\n"
                "Critical when DELETE OLD VERSIONS and INCREMENT are active, as,\n\n"
                "older versions may get deleted, leaving only the corrupted file"
            )
        },
        "auto_save_file_size_warning_threshold": {
            "concise": "Sets the percentage threshold for file size reduction warnings. Verbose tool-tip available",
            "verbose": (
                "Sets the percentage threshold for file size reduction that will trigger a warning.\n\nExample: Set 25% threshold to get alerts if your file size drops below 75%"
            )
        },

        "auto_save_interval": {
            "concise": "Time interval (in seconds) for auto-save. Verbose tool-tip available",
            "verbose": (
                "Specifies the time interval in seconds for auto-saving files.\n\n"
                "Recommended intervals: 60 seconds minimum is safe; shorter intervals may cause erratic mouse movements in larger files"
            )
        },
        "is_dirty": {
            "concise": "Auto-saves only when unsaved changes are detected. Verbose tool-tip available",
            "verbose": (
                "Only auto-save every 'n' seconds if unsaved changes are detected.\n\n"
                "This improves performance and reduces the number of saved files.\n\n"
                "This setting also applies to saving preferences and scripts"
            )
        },
    
        "auto_save_delete_temp": {
            "concise": "Deletes temporary files to free up disk space. Verbose tool-tip available.",
            "verbose": (
                "Deletes unneeded temporary files specific to each OS on disk space warning.\n\n"
                "- **Windows:** Cleans files in `AppData/Local/Temp`, a location for temp files.\n"
                "- **Mac:** Cleans files in `/var/folders/`, commonly used for temporary app data.\n"
                "- **Linux:** Cleans files in `/tmp/`, a shared directory for temp files..\n\n"
                "It does not delete any Blender-related files, only temp files."
            )
        },

        "auto_save_splash_screen": {
            "concise": "Displays a splash screen on startup for FAST Auto-save. Verbose tool-tip available",
            "verbose": (
                "Displays a splash screen on startup.\n\n"
                "Click button (timeline, dope sheet, graph editor, sequencer) to re-open splash screen"
            )
        },
        "save_on_startup": {
            "concise": "Automatically saves on startup as scratch.blend. Verbose tool-tip available",
            "verbose": (
                "Automatically saves on Blender startup as scratch.blend.\n\nUses the 'INCREMENT' naming style for a one-time save (e.g., scratch_FAST_1).\n\nDoesn't activate continuous INCREMENT or produce multiple versions.\n\nUniquely named files retain their original name upon auto-save.\n\nFiles are saved in 'FAST Auto-saves' folder on Desktop.\n\nCombine with SPLASH SCREEN for easy file retrieval"
            )
        },
    
        "overlays_prop": {
            "concise": "Toggles overlays during Transform XYZ operations. Verbose tool-tip available",
            "verbose": (
                "Toggles overlays during the Transform XYZ operations.\n\n"
                "Overlays remain active when moving lights, cameras, or empties to maintain visibility"
            )
        },
        "diffeomorphic_shell_method_geometry_nodes": {
            "concise": "Sets shell method to 'Geometry Nodes' for characters like L4N4. Verbose tool-tip available",
            "verbose": (
                "Sets the shell method to 'Geometry Nodes' for imported characters like L4N4 to improve their visual quality.\n\n"
                "This setting is experimental and may produce different results with various models"
            )
        },
        "hide_scene_objects": {
            "concise": "Automatically hides all objects in the Blender scene, including the default cube. Verbose tool-tip available",
            "verbose": (
                "Automatically hides all objects in the Blender scene, including the default cube, when importing Daz characters.\n\n"
                "This feature saves the visibility state of each object before hiding them.\n\n"
                "The saved states allow you to restore original visibility of all objects,\n\n"
                "Use the 'Restore Hidden Objects' button to revert all objects back to their visibility state.\n\n"
                "If the restore button doesn't work, click undo to revert and rerun the operator\n\n"
                "that started the disabling, without this enabled.\n\n"
                "This functionality relies on a scene property to store the state of objects.\n\n"
                "When disabling objects, the scene property is reset and filled with the objects being disabled.\n\n"
                "When restoring, all objects are re-enabled and the scene property is deleted.\n\n"
                "or safety, when disabling objects, if the scene property already exists,\n\n"
                "all objects are automatically re-enabled before immediately being disabled again,\n\n"
                "so that the property gets reset properly"
            )
        },

        "gpt_hide_scene_objects": {
            "concise": "Automatically hides all objects in the Blender scene. Verbose tool-tip available",
            "verbose": (
                "Automatically hides all objects in the Blender scene.\n\n"
                "This feature saves the visibility state of each object before hiding them.\n\n"
                "The saved states allow you to restore original visibility of all obj, only during the same session.\n\n"
                "The visibility states are stored temporarily and will be reset at Blender startup.\n\n"
                "Use the 'Restore Hidden Objects' button to revert to original state.\n\n"
                "Note: Only works on viewport panel version not in text editor version"
            )
        },
        "diffeomorphic_units": {
            "concise": "Imports FACE UNITS morphs for advanced facial animation. Verbose tool-tip available",
            "verbose": (
                "FACE UNITS morphs allow for advanced shaping and posing of a character's face.\n\n"
                "These morphs enable highly customizable facial animations"
            )
        },
        "diffeomorphic_expressions": {
            "concise": "Imports EXPRESSION morphs for facial animations. Verbose tool-tip available",
            "verbose": (
                "EXPRESSION morphs allow for advanced shaping and posing of facial expressions,\n\n"
                "enabling more detailed and expressive character animations"
            )
        },
        "diffeomorphic_visemes": {
            "concise": "Imports VISEMES morphs for lip-sync animations. Verbose tool-tip available",
            "verbose": (
                "VISEMES morphs are used to add MIMIC Pose Presets and create other lip-sync animations.\n\n"
                "Import these when using MIMIC Lip Sync animation, particularly for Genesis 8 or earlier characters"
            )
        },
        "diffeomorphic_body": {
            "concise": "Imports BODY morphs for character body animation. Verbose tool-tip available",
            "verbose": (
                "BODY morphs are used for advanced shaping and posing of a character's body,\n\n"
                "allowing for more flexibility in character animations"
            )
        },
        "diffeomorphic_facs": {
            "concise": "Imports FACS morphs for natural facial expressions. Verbose tool-tip available",
            "verbose": (
                "FACS morphs are based on the Facial Action Coding System and allow for more natural and diverse facial expressions.\n\n"
                "These are recommended for Genesis 8.1 characters using MIMIC Lip Sync animation"
            )
        },
        "diffeomorphic_facs_details": {
            "concise": "Imports FACS Details for facial animation. Verbose tool-tip available",
            "verbose": (
                "FACS DETAILS provide a standard set of facial details using FACS morphs.\n\n"
                "These details enhance facial animations for characters using FACS"
            )
        },
        "diffeomorphic_facs_expressions": {
            "concise": "Imports FACS EXPRESSIONS for facial animation. Verbose tool-tip available",
            "verbose": (
                "FACS EXPRESSIONS are a standard set of facial expressions using FACS morphs.\n\n"
                "They allow for a broader range of facial expressions for characters"
            )
        },

        "use_feminine": {
            "concise": "Choose to use feminine morphs when importing Genesis 9 characters. Verbose tool-tip available",
            "verbose": (
                "Choose to use feminine morphs when importing Genesis 9 characters from DAZ Studio.\n\n"
                "This setting ensures all feminine-specific morphs are included in the imported model"
            )
        },
        "use_masculine": {
            "concise": "Choose to use masculine morphs when importing Genesis 9 characters. Verbose tool-tip available",
            "verbose": (
                "Choose to use masculine morphs when importing Genesis 9 characters from DAZ Studio.\n\n"
                "This setting ensures all masculine-specific morphs are included in the imported model"
            )
        },

        "diffeomorphic_action_name": {
            "concise": "Specifies the action name used during import. Verbose tool-tip available",
            "verbose": (
                "Specifies the action name used by the IMPORT ACTION functionality.\n\n"
                "The default name is 'Action', and you must press Enter after entering the name"
            )
        },
    
        "diffeomorphic_add_audio": {
            "concise": "Adds audio to the Daz character. Verbose tool-tip available",
            "verbose": (
                "Adds audio to the Daz character, placing the file in the 'FAST/daz_studio_save/audio' directory.\n\n"
                "Ensure the audio is added correctly at the frame set for the first frame of the animation"
            )
        },
    
    
        "diffeomorphic_merge_non_conforming": {
            "concise": "Specifies how to merge non-conforming bones. Verbose tool-tip available",
            "verbose": (
                "Specifies the method used to merge non-conforming bones during character import.\n\n"
                "'NEVER' doesn't merge any bones, 'Face Controls' merges only face controls, and 'ALWAYS' merges all bones"
            )
        },
    
        "diffeomorphic_fit_meshes": {
            "concise": "Specifies the method for fitting meshes to morphs. Verbose tool-tip available",
            "verbose": (
                "Specifies the method for fitting meshes to morphs during import.\n\n"
                "'DBZ FILE' is preferred for characters, while 'SHARED' and 'UNIQUE' are for props and environments"
            )
        },
        "debug": {
            "concise": "Enables debug mode for material and normal map display. Verbose tool-tip available",
            "verbose": (
                "Enables debug mode for displaying detailed console information about 'Activate Diffuse' and 'Activate Normals'.\n\n"
                "Warning: Detailed console output could crash Blender when entering 'Material Preview' or 'Render' modes"
            )
        },
        "transform_nudge_prop": {
            "concise": "Ultra-precise nudge value for Transform XYZ operations. Verbose tool-tip available",
            "verbose": (
                "Ultra-precise nudge value for Transform XYZ operations.\n\n"
                "Use the mouse scroll wheel after invoking to nudge.\n\n"
                "If no movement, scroll up as nudge might be set too fine"
            )
        },
    
        "optimized_map": {
            "concise": "Optimizes normal maps for faster animation rendering. Verbose tool-tip available",
            "verbose": (
                "Choose whether to optimize Normal Maps using the FAST button.\n\n"
                "Can provide much faster animation in render mode, depending on the\n\n"
                "number of objects with normal maps connected to your character\n\n"
                "that also have an Armature modifier.\n\n"
                "If, when importing Daz Studio character, you encounter pink textures,\n\n"
                "try disabling this option and then reimporting your character.\n\n"
                "If this resolves the issue, reimport with this setting off,\n\n"
                "then go to the material tab for the affected material.\n\n"
                "Select the 'Normal' button on the left pane to rest texture"
            )
        },
    
        "auto_mode": {
            "concise": "Auto-activates diffuse image texture nodes for new models. Verbose tool-tip available",
            "verbose": (
                "Choose whether diffuse image texture nodes should be activated automatically,\n\nwhen a new material or model is brought into the active scene.\n\nIf seeing many material related console errors,\n\nconsider turning off AUTO MODE temporarily.\n\nThis is usually indicative of errors in materials in your Scene,\n\nThough it is verbose, as to WARNINGS, these are not intrinsic AUTO MODE errors"
            )
        },

        "enable_pref": {
            "concise": "Enables Blender's default add-ons and preferences. Verbose tool-tip available",
            "verbose": (
                "Enables Blender's default add-ons and common preferences.\n\n"
                "This includes setting 'Undo Steps' to 64, which improves stability in larger scenes"
            )
        },

        "new_workspace": {
            "concise": "Creates a new workspace when using the FAST button. Verbose tool-tip available",
            "verbose": (
                "Creates a new duplicate Layout workspace when clicking the FAST button.\n\n"
                "This helps improve viewport performance in large scenes"
            )
        },
    
    
        "diffeomorphic_load_fast_setting": {
            "concise": "Load the best settings for most Daz imports. Verbose tool-tip available",
            "verbose": (
                "Load the best Diffeomorphic settings that work for most characters.\n\n"
                "Uncheck if you would like to set your own settings in the Daz Setup panel in Global Settings.\n\n"
                "If you check Load Settings, the settings in EVEE.json in fast_diffeomorphic_settings folder\n"
                "are temporarily loaded when a character is imported with the monitor functionality and will be\n"
                "reverted to whatever settings you had before once the character has been imported"
            )
        },
        "gpt_keyword": {
            "concise": "Choose a keyword for AGPT-4 instructions. Verbose tool-tip available",
            "verbose": (
                "Select a keyword to provide AGPT-4 with proper instructions.\n\n"
                "The keyword will be auto-added to your user command file for future use.\n\n"
                "Make sure you're spelling the keyword correctly when adding manual instructions to the command file"
            )
        },


        "GPTScriptFileIndex": {
            "concise": "Selects the script file index from available AGPT-4 scripts. Verbose tool-tip available",
            "verbose": (
                "Only script files are displayed in this list; other folders/files are skipped.\n\n"
                "Default File Descriptions:\n\n"
                "- unlink: unlinks the current script from AGPT-4.\n\n"
                "- main_file.py: Main file for adding code to the AGPT-4 operator.\n\n"
                "- fixed_code.py: Latest fixed code from each iteration is saved here."

            )
        },
    

    
        "pull_se_examples_iterations": {
            "concise": "Set the number of Stack Exchange search iterations. Verbose tool-tip available",
            "verbose": (
                "Sets the number of Stack Exchange search iterations, higher produce better results.\n\n"
                "Minimum recommendation: 10 for standard Python, 50 for Blender Python.\n\n"
                "You can adjust this value live on the panel during execution; if lowered,\n\n"
                "the search will stop once it reaches the new target iteration"
            )
        },

        "gpt_extra_data_for_find_code_examples": {
            "concise": "Add precise API calls for better example search. Verbose tool-tip available",
            "verbose": (
                "Adds precise API and operator calls to your boosted command for improved example lookup.\n\n"
                "This feature enhances the example search by ensuring specific API or operator terms are used"
            )
        },
    

    
        "daz_studio_error_scan_paths": {
            "concise": "Sets the paths for error and scan files in Daz importer. Verbose tool-tip available",
            "verbose": (
                "The 3 ERROR & SCAN files in Diffeomorphic GLOBAL SETTINGS on Daz Setup panel.\n\n"
                "'daz_importer_errors.txt', 'Scanned Daz Database', 'import_daz_scanned_absolute_paths.json'\n\n"
                "Are saved to the selected path. These are temporary paths used by ADDON during asset import.\n\n"
                "Editing FAST/Diffeomorphic_SETTINGS/EVEE.json file updates these path boxes.\n\n"
                "Ensure the 3 ERROR & SCAN paths all use the same directory.\n\n"
                "Restart Blender if paths are changed from files, but no restart is needed if changed in Blender.\n\n"
                "If mistakes occur, copy & rename Factory Settings.JSON to EVEE.JSON & restart Blender"
            )
        },
    
    
        "daz_studio_extra_setup": {
            "concise": "Automates extra setup in Daz Studio. Verbose tool-tip available",
            "verbose": "Also switch into Material Preview and turn off Overlays & turn on Transparency."
        },

        "diffeomorphic_first_frame": {
            "concise": "Set the first frame for action import. Verbose tool-tip available",
            "verbose": "Choose the first frame of animation from your Pose Preset file for import.\nThe first frame sets the starting point and can affect the overall timing."
        },
        "diffeomorphic_last_frame": {
            "concise": "Set the last frame for action import. Verbose tool-tip available",
            "verbose": "Choose the last frame of animation from your Pose Preset file for import.\nThe last frame defines the end of the animation, ensuring proper keyframe alignment."
        },

        "diffeomorphic_fps": {
            "concise": "Set FPS for action import. Verbose tool-tip available",
            "verbose": (
                "This should match the FPS (frames per second) your scene was set to when saved in Daz Studio.\n\n"
                "Automatically updates the scene's FPS when this slider is moved"
            )
        },
        "file_state": {
            "concise": "Indicates the file's save state with icons or theme colors. Verbose tool-tip available",
            "verbose": (
                "Changes Icon or Theme Colors to indicate file state.\n\n"
                "1. BLUE: File is saved.\n\n"
                "2. GREEN: File is unsaved.\n\n"
                "3. RED: File is unnamed & unsaved"
            )
        },
    
        "show_active_auto_viewport": {
            "concise": "Auto-focus on active objects in the viewport. Verbose tool-tip available",
            "verbose": (
                "Automatically focus on the active object in the viewport when selected in the outliner.\n\n"
                "Use this mindfully as it will frame selected objects in the viewport"
            )
        },
        "show_active_auto_outliner": {
            "concise": "Focuses the outliner on the active object when selected. Verbose tool-tip available",
            "verbose": (
                "Automatically shifts the outliner view to highlight and center the active object when it is selected\n\n"
                "in the viewport, ensuring that users can easily locate the object in complex scenes."
            )
        },
        "gpt_max_iterations": {
            "concise": "Sets the number of iterations for GPT-4 processing. Verbose tool-tip available",
            "verbose": (
                "This controls how many times Autonomous GPT-4 processes your code to fix errors.\n\n"
                "Increase if close to max iterations or to avoid token expenditure"
            )
        },


        "gpt_keyword": {
            "concise": "Selects a keyword to provide AGPT-4 with proper instructions. Verbose tool-tip available",
            "verbose": (
                "Choose a keyword for AGPT-4 instructions. The keyword is automatically added to the user command file.\n\n"
                "Ensure proper spelling when adding manual instruction sets"
            )
        },
        "diffeomorphic_load_fast_settings": {
            "concise": "Load optimal Diffeomorphic settings for character import. Verbose tool-tip available",
            "verbose": (
                "Load the best Diffeomorphic settings that work for most characters.\n\n"
                "Uncheck if you would like to set your own settings in the Daz Setup panel in Global Settings.\n\n"
                "If you check Load Settings, the settings in EVEE.json in fast_diffeomorphic_settings folder\n\n"
                "are temporarily loaded when a character is imported with the monitor functionality and will be\n\n"
                "reverted to whatever settings you had before once the character has been imported"
            )
        },
    
        "auto_save_keep_versions": {
            "concise": "Sets the number of old versions to keep",
            "verbose": (
                "* Specify the number of old versions to retain.\n\n"
                "* Older versions beyond this number will be deleted.\n\n"
                "* Default is 5, but it has been raised to 10 to avoid data loss in case of file issues"
            )
        },

 
}

except Exception as e:
    print(f"Error in loading tooltip_descriptions dictionary: \n")
    capture_and_copy_traceback()





# Property descriptions (verbose and concise)
VERBOSE_TOOLTIP = (
    "You can change this property, but it will be reverted at Blender startup.\n\n"
    "These settings are integral to the system running well & we've had luck with these settings.\n\n"
    "Setting the 'top_p' parameter controls the nucleus sampling for AI responses.\n\n"
    "When lower, the model considers only the most probable outputs, leading to more reliable and focused responses.\n\n"
    "When higher, it allows for a broader range of outputs, fostering more diversity and creativity.\n\n"
    "We've chosen this default value because we have found this setting to be the most effective.\n\n"
    "If you encounter an issue and changing this value resolves it, please report the issue,\n\n"
    "with your findings so we can improve the default settings for specific circumstances."
)

CONCISE_TOOLTIP = "Set the 'top_p' parameter to control nucleus sampling for AI responses."

def tooltip_update_timer():

    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
    except KeyError as e:

        return
    # Check if the tooltip_update_timer already has the last state stored
    if hasattr(tooltip_update_timer, "last_verbose_tooltip_state"):
        # Compare the stored state with the current manager's verbose_tooltips
        if tooltip_update_timer.last_verbose_tooltip_state == manager.verbose_tooltips:
            return 1.0  # No changes, call again in 1 second

    # Define the operations to be executed
    def update_tooltips_and_redraw():
        bpy.ops.fast.update_tooltips()
        my_redraw()

    # Check the autogpt_processing property
    if manager.autogpt_processing in ('Initializing', 'Analyzing', 'Waiting for Input', 'SE') or manager.se_fix_code:
        main_thread(update_tooltips_and_redraw)  # Run in main thread
    else:
        update_tooltips_and_redraw()  # Run as normal in the current thread

    # Store the current state
    tooltip_update_timer.last_verbose_tooltip_state = manager.verbose_tooltips

    return 1.0  # Call again in 1 second

class FAST_OT_UpdateTooltipsOperator(bpy.types.Operator):
    bl_idname = "fast.update_tooltips"
    bl_label = "Update Tooltips"

    def execute(self, context):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        scene = bpy.context.scene # added
        try:
    
            # Re-define the property for each tooltip
            for prop_name, descriptions in tooltip_descriptions.items():
                current_description = descriptions["verbose"] if manager.verbose_tooltips else descriptions["concise"]

    
                # Check the property name and re-assign it with the updated description
                if prop_name == "use_o1_mini_model":
                    bpy.types.Scene.use_o1_mini_model = bpy.props.BoolProperty(
                        name="Use O1 Mini Model",
                        description=current_description,
                        default=False
                    )
    
                elif prop_name == "auto_save_toggle":
                    bpy.types.Scene.auto_save_toggle = bpy.props.BoolProperty(
                        name="Auto Save Toggle",
                        description=current_description,  # Uses current_description for verbose description
                        default=True  # Set the appropriate default value
                    )
                    
                elif prop_name == "auto_save_interval":
                    bpy.types.Scene.auto_save_interval = bpy.props.IntProperty(
                        name="Auto Save Counter",
                        description=current_description,
                        default=60,
                        min=10,
                        max=600,
                    )
                
                elif prop_name == "auto_save_keep_versions":
                    bpy.types.Scene.auto_save_keep_versions = bpy.props.IntProperty(
                        name="Keep Versions #",
                        description=current_description,
                        default=5,
                        min=1,
                        max=100,
                    )
    
                elif prop_name == "enter_material_preview_mode":
                    bpy.types.Scene.enter_material_preview_mode = bpy.props.BoolProperty(
                        name="Enter Material Preview",
                        description=current_description,
                        default=False,
                    )
                elif prop_name == "add_blue_cube":
                    bpy.types.Scene.add_blue_cube = bpy.props.BoolProperty(
                        name="Add Blue Cube",
                        default=True,
                        description=current_description,
                    )
    
                elif prop_name == "exit_to_solid_mode":
                    bpy.types.Scene.exit_to_solid_mode = bpy.props.BoolProperty(
                        name="Exit to Solid Mode",
                        description=current_description,
                        default=True,
                    )
                
                
                elif prop_name == "diffeomorphic_disable_hair":
                    bpy.types.Scene.diffeomorphic_disable_hair = bpy.props.BoolProperty(
                        name="Disable High-Poly Hair",
                        description=current_description,
                        default=False,
                    )
    
    
                elif prop_name == "gpt_choose_to_take_snapshot":
                    bpy.types.Scene.gpt_choose_to_take_snapshot = bpy.props.BoolProperty(
                        name="GPT Choose to Take Snapshot",
                        description=current_description,        
                        default=True
                    )
                    
                elif prop_name == "gpt_data_limit":
                    bpy.types.Scene.gpt_data_limit = bpy.props.IntProperty(
                        name="GPT Data Limit",
                        description=current_description,
                        default=5000,
                        min=1,
                        max=20000,
                    )
    
                # Elif blocks with current_description
                elif prop_name == "diffeomorphic_camera_x_offset":
                    bpy.types.Scene.diffeomorphic_camera_x_offset = bpy.props.FloatProperty(
                        name="Camera X Offset",
                        description=current_description,
                        default=0.01,
                    )
                
                elif prop_name == "diffeomorphic_camera_y_offset":
                    bpy.types.Scene.diffeomorphic_camera_y_offset = bpy.props.FloatProperty(
                        name="Camera Y Offset",
                        description=current_description,
                        default=0.87,
                    )
                
                elif prop_name == "diffeomorphic_skin_color":
                    bpy.types.Scene.diffeomorphic_skin_color = bpy.props.FloatVectorProperty(
                        name="Daz Skin Color",
                        description=current_description,
                        subtype="COLOR",
                        size=4,
                        min=0.0,
                        max=1.0,
                        default=(0.600, 0.400, 0.250, 1.0),
                    )
                
                elif prop_name == "diffeomorphic_clothes_color":
                    bpy.types.Scene.diffeomorphic_clothes_color = bpy.props.FloatVectorProperty(
                        name="Daz Clothes Color",
                        description=current_description,
                        subtype="COLOR",
                        size=4,
                        min=0.0,
                        max=1.0,
                        default=(0.090, 0.010, 0.015, 1.0),
                    )

                
                elif prop_name == "diffeomorphic_use_replace_slots":
                    bpy.types.Scene.diffeomorphic_use_replace_slots = bpy.props.BoolProperty(
                        name="Replace Material Slots",
                        description=current_description,
                        default=True,
                    )
                
                elif prop_name == "diffeomorphic_use_add_slots":
                    bpy.types.Scene.diffeomorphic_use_add_slots = bpy.props.BoolProperty(
                        name="Add Material Slots",
                        description=current_description,
                        default=False,
                    )
                
                elif prop_name == "diffeomorphic_use_match_names":
                    bpy.types.Scene.diffeomorphic_use_match_names = bpy.props.BoolProperty(
                        name="Match Material Names",
                        description=current_description,
                        default=True,
                    )
                
    
                elif prop_name == "gpt_edit_user_command_prompt":
                    bpy.types.Scene.gpt_edit_user_command_prompt = bpy.props.BoolProperty(
                        name="Show Edit User Command Prompt",
                        description=current_description,        
                        default=False
                    )
    
                elif prop_name == "gpt_show_verify_example_prompt":
                    bpy.types.Scene.gpt_show_verify_example_prompt = bpy.props.BoolProperty(
                        name="GPT Verify or Remove Example",
                        description=current_description,        
                        default=False
                    )
                           
                elif prop_name == "gpt_file_permission_fixer_path":
                    bpy.types.Scene.gpt_file_permission_fixer_path = bpy.props.StringProperty(
                        name="File Permission Fixer Path",
                        description=current_description,
                        default="os.path.join(os.path.expanduser('~'), 'Desktop', 'AGPT-4')",
                        maxlen=1024,
                        subtype='FILE_PATH',
                        update=update_gpt_file_permission_fixer_path
                    )
    
    
    
                elif prop_name == "gpt_smtp_lib_app_password":
                    bpy.types.Scene.gpt_smtp_lib_app_password = StringProperty(
                        name="SMTP App Password",
                        description=current_description,
                        default="",
                        subtype='PASSWORD'
                    )
    
                elif prop_name == "gpt_smtp_lib_server":
                    bpy.types.Scene.gpt_smtp_lib_server = StringProperty(
                        name="SMTP Server",
                        description=current_description,
                        default="smtp.gmail.com",
                    
                    )
    
                elif prop_name == "gpt_confirm_object_is_selected":
                    bpy.types.Scene.gpt_confirm_object_is_selected = bpy.props.BoolProperty(
                        name="Confirm Object Is Selected",
                        description=current_description,
                        default=False
                    )
    
                elif prop_name == "gpt_confirm_data":
                    bpy.types.Scene.gpt_confirm_data = bpy.props.BoolProperty(
                        name="Confirm Object Is Selected",
                        description=current_description,
                        default=False
                    )
    
                elif prop_name == "gpt_boost_user_command":
                    bpy.types.Scene.gpt_boost_user_command = BoolProperty(
                        name="Boost User Command",
                        
                        description=current_description,
    
                        default=True,
                        update=update_gpt_boost_user_command
                    )
                        
                elif prop_name == "auto_save_startup_file":
                    bpy.types.Scene.auto_save_startup_file = bpy.props.BoolProperty(
                        name="FAST Auto-save Startup File",
                        description=current_description,
                        default=False,
                    )
    
                elif prop_name == "gpt_advanced_boost_user_command":
                    bpy.types.Scene.gpt_advanced_boost_user_command = bpy.props.BoolProperty(
                        name="Use Advanced Model for Boost User Command",
                        description=current_description,
                        default=False, 
                        update=update_gpt_advanced_boost_user_command
                    )
    
                elif prop_name == "pull_se_examples_iterations":
                    bpy.types.Scene.pull_se_examples_iterations = bpy.props.IntProperty(
                        name="SE Search Iterations",
                        description=current_description,
                        default=50,
                        min=1,
                        max=200,
                    )

                elif prop_name == "ambient_noise_duration_prop":
                    bpy.types.Scene.ambient_noise_duration_prop = bpy.props.FloatProperty(
                        name="Ambient Noise Duration",
                        description=current_description,  # Use dynamic description
                        default=0.25,
                        min=0.00,
                        max=5.0,
                    )
                elif prop_name == "bse_search_term":
                    bpy.types.Scene.bse_search_term = bpy.props.StringProperty(
                        name="BSE Search Term",
                        description=current_description,
                        default=""
                    )
    
                elif prop_name == "gpt_find_code_examples":
                    bpy.types.Scene.gpt_find_code_examples = bpy.props.BoolProperty(
                        name="Find Examples",
                        description=current_description,        
                        default=True,
                    )
    
                elif prop_name == "gpt_extra_data_for_find_code_examples":
                    bpy.types.Scene.gpt_extra_data_for_find_code_examples = bpy.props.BoolProperty(
                        name="Extra Data for Find Code Examples",
                        description=current_description,        
                        default=True,
                    )
    
                elif prop_name == "gpt_show_lookups":
                    bpy.types.Scene.gpt_show_lookups = bpy.props.BoolProperty(
                        name="Show Lookups",
                        description=current_description,
                        default=True
                    )
    
                elif prop_name == "show_se_content":
                    bpy.types.Scene.show_se_content = bpy.props.BoolProperty(
                        name="Show Body Content",
                        description=current_description,
                        default=False
                    )
    
                elif prop_name == "gpt_show_cost":
                    bpy.types.Scene.gpt_show_cost = bpy.props.BoolProperty(
                        name="Show Tokens",
                        description=current_description,
                        default=False
                    )
    
                elif prop_name == "gpt_4o_mini_input_token_count":
                    bpy.types.Scene.gpt_4o_mini_input_token_count = bpy.props.IntProperty(
                        name="GPT 4o mini Input Token Count",
                        description=current_description,
                        default=0
                    )
    
                elif prop_name == "gpt_4o_mini_output_token_count":
                    bpy.types.Scene.gpt_4o_mini_output_token_count = bpy.props.IntProperty(
                        name="GPT 4o mini Output Token Count",
                        description=current_description,
                        default=0
                    )
    
                elif prop_name == "gpt_4o_mini_total_token_count":
                    bpy.types.Scene.gpt_4o_mini_total_token_count = bpy.props.IntProperty(
                        name="Total GPT 4o mini Token Count",
                        description=current_description,
                        default=0
                    )
    
                elif prop_name == "gpt_4o_input_token_count":
                    bpy.types.Scene.gpt_4o_input_token_count = bpy.props.FloatProperty(
                        name="GPT 4o Input Token Count",
                        description=current_description,
                        default=0,
    
                    )
    
                elif prop_name == "gpt_4o_output_token_count":
                    bpy.types.Scene.gpt_4o_output_token_count = bpy.props.FloatProperty(
                        name="GPT 4o Output Token Count",
                        description=current_description,
                        default=0,
    
                    )
    
                elif prop_name == "gpt_o3_mini_input_token_count":
                    bpy.types.Scene.gpt_o3_mini_input_token_count = bpy.props.FloatProperty(
                        name="GPT o3 mini Input Token Count",
                        description=current_description,
                        default=0,
    
                    )
    
                elif prop_name == "gpt_o3_mini_output_token_count":
                    bpy.types.Scene.gpt_o3_mini_output_token_count = bpy.props.FloatProperty(
                        name="GPT o3 mini Output Token Count",
                        description=current_description,
                        default=0,
    
                    )

                elif prop_name == "gpt_o3_mini_total_token_count":
                    bpy.types.Scene.gpt_o3_mini_total_token_count = bpy.props.IntProperty(
                        name="Total GPT o3 mini Token Count",
                        description=current_description,
                        default=0
                    )

                elif prop_name == "gpt_4o_total_token_count":
                    bpy.types.Scene.gpt_4o_total_token_count = bpy.props.FloatProperty(
                        name="Total GPT 4o Token Count",
                        description=current_description,
                        default=0,
    
                    )
    
                elif prop_name == "gpt_o1_mini_input_token_count":
                    bpy.types.Scene.gpt_o1_mini_input_token_count = bpy.props.IntProperty(
                        name="GPT o1 mini Input Token Count",
                        description=current_description,
                        default=0
                    )
    
                elif prop_name == "gpt_o1_mini_output_token_count":
                    bpy.types.Scene.gpt_o1_mini_output_token_count = bpy.props.IntProperty(
                        name="GPT o1 mini Output Token Count",
                        description=current_description,
                        default=0
                    )
    
                elif prop_name == "gpt_o1_mini_total_token_count":
                    bpy.types.Scene.gpt_o1_mini_total_token_count = bpy.props.IntProperty(
                        name="Total GPT o1 mini Token Count",
                        description=current_description,
                        default=0
                    )
    
    
    
                elif prop_name == "gpt_pause_before_fixing_errors":
                    bpy.types.Scene.gpt_pause_before_fixing_errors = bpy.props.BoolProperty(
                        name="Pause Before Fixing Errors",
                        description=current_description,
                        default=False
                    )
    
                elif prop_name == "gpt_run_final_script":
                    bpy.types.Scene.gpt_run_final_script = bpy.props.BoolProperty(
                        name="GPT Run Final Script",
                        description=current_description,
                        default=True)
    
    
                elif prop_name == "gpt_current_iteration":
                    bpy.types.Scene.gpt_current_iteration = bpy.props.IntProperty(
                        name="GPT Current Iteration",
                        description=current_description,
                        default=0,
                        min=0,  # Minimum value
                        max=20
                    )
                elif prop_name == "gpt_model_secondary":
                    bpy.types.Scene.gpt_model_secondary = bpy.props.EnumProperty(
                        name="GPT Model (Secondary)",
                        items=[
                            ("gpt-4o", "gpt-4o", "GPT-4o: First Choice. Latest flagship model, it's the best and cheapest"),
                            ("o3-mini", "o3-mini", "o3-mini: Latest miniature version of the o3 model, optimized for reasoning tasks in coding, mathematics, and science."),
                        ],
                        default="gpt-4o",
                        description=current_description,
                    )
                elif prop_name == "gpt_use_beep":
                    bpy.types.Scene.gpt_use_beep = bpy.props.BoolProperty(
                        name="Use Beep",
                        description=current_description,
                        default=True,
                    )
    
                elif prop_name == "gpt_operator_name":
                    bpy.types.Scene.gpt_operator_name = bpy.props.StringProperty(
                        name="Operator Name",
                        description=current_description,
                        default="bpy.ops.fast.auto_gpt_assistant()"
                    )
    
                # Add the elif condition for the property
                elif prop_name == "auto_save_disk_warning_threshold":
                    bpy.types.Scene.auto_save_disk_warning_threshold = bpy.props.IntProperty(
                        name="Disk Space Warning Threshold",
                        description=current_description,  # Assuming current_description holds the full description
                        default=3,
                        min=1,
                        max=100,
                    )
                
                
                elif prop_name == "render_viewport_overlays":
                    bpy.types.Scene.render_viewport_overlays = bpy.props.BoolProperty(
                        name="Render Viewport Overlays",
                        description=current_description,
                        default=True,
                    )
                elif prop_name == "gpt_run_on_selected_objects":
                    bpy.types.Scene.gpt_run_on_selected_objects = bpy.props.BoolProperty(
                        name="Run on Selected Object",
                        description=current_description,
                        default=False
                    )
    
                elif prop_name == "gpt_added_code":
                    bpy.types.Scene.gpt_added_code = bpy.props.StringProperty(
                        name="Additional Code Path",
                        description=current_description,
                        subtype='FILE_PATH',
                        default=""
    
                    )
    
                elif prop_name == "GPTScriptFileIndex":
                    bpy.types.Scene.GPTScriptFileIndex = bpy.props.IntProperty(
                        name="Selected Script File Index",
                        description=current_description,
                        update=update_gpt_script_file_index,
                    )
    
                elif prop_name == "gpt_show_code":
                    bpy.types.Scene.gpt_show_code = bpy.props.BoolProperty(
                        name="Show Code",
                        description=current_description,
                        default=True
                    )
    
                elif prop_name == "gpt_error_check_timeout":
                    bpy.types.Scene.gpt_error_check_timeout = bpy.props.IntProperty(
                        name="Blender Quit Timeout",
                        description=current_description,
                        default=15,
                        min=15,
                        max=120,
                    )
                    
                    
                elif prop_name == "gpt_max_iterations":
                    bpy.types.Scene.gpt_max_iterations = bpy.props.IntProperty(
                        name="GPT Iteration Count",
                        description=current_description,
                        default=5,
                        min=0,
                        max=50,
                        update=update_gpt_max_iterations
                    )
                    
    
                elif prop_name == "gpt_main_assistant_temperature":
                    bpy.types.Scene.gpt_main_assistant_temperature = bpy.props.FloatProperty(
                        name="Main GPT Assistant Temperature",
                        description=current_description,
                        default=0.1,
                        step=1,
                        min=0.0,
                        max=1.0
                    )
    
                elif prop_name == "gpt_main_assistant_top_p":
                    bpy.types.Scene.gpt_main_assistant_top_p = bpy.props.FloatProperty(
                        name="Main GPT Assistant Top_p",
                        description=current_description,
                        default=0.2,
                        step=1,
                        min=0.0,
                        max=1.0
                    )
    
                elif prop_name == "gpt_advanced_api_or_manual_or_fast_decider":
                    bpy.types.Scene.gpt_advanced_api_or_manual_or_fast_decider = bpy.props.BoolProperty(
                        name="Use Advanced Model for API/Add-on/Manual Decider",
                        description=current_description,
                        default=False
                    )
                elif prop_name == "api_key":
                    bpy.types.Scene.api_key = bpy.props.StringProperty(
                        name="API Key",
                        description=current_description,
                        default="",
                        # subtype='PASSWORD',
                        update=update_api_key
                    )

    
                elif prop_name == "azure_add_markers":
                    bpy.types.Scene.azure_add_markers = bpy.props.BoolProperty(
                        name="Add Rest Markers",
                        description=current_description,
                        default=True
                    )
    
                elif prop_name == "azure_silence_thresh_rms":
                    bpy.types.Scene.azure_silence_thresh_rms = bpy.props.FloatProperty(
                        name="Azure Silence Threshold (RMS)",
                        description=current_description,
                        default=186.70,
                        min=0.0,
                        max=2959.00,
                    )




                elif prop_name == "use_beep_local_global":
                    bpy.types.Scene.use_beep_local_global = bpy.props.BoolProperty(
    
                        name = "Use Beep...Local or Global Mode",
                        description=current_description,
    
                        default = True
                    )
    
                elif prop_name == "disable_render_and_window":
                    bpy.types.Scene.disable_render_and_window = bpy.props.BoolProperty(
                        name="Disable Render & Window",
                        description=current_description,
                        default=True
                    )
    
                elif prop_name == "key_saved_clip_for_reimport_clip":
                    bpy.types.Scene.key_saved_clip_for_reimport_clip = bpy.props.StringProperty(
                        name="Saved Clip for Redo",
                        description=current_description,
                        default="",
                        subtype='FILE_PATH'
                    )
                    
                elif prop_name == "window_offset_x":
                    bpy.types.Scene.window_offset_x = bpy.props.IntProperty(
                        name="Window X Offset",
                        description=current_description,
                        default=-120,
                        min=-10000,
                        max=10000,
                    )
                    
                elif prop_name == "window_offset_y":
                    bpy.types.Scene.window_offset_y = bpy.props.IntProperty(
                        name="Window Y Offset",
                        description=current_description,
                        default=0,
                        min=-10000,
                        max=10000,
                    )
    
                elif prop_name == "left_padding":
                    bpy.types.Scene.left_padding = bpy.props.FloatProperty(
                        name="Left Padding",
                        default=0.01,
                        min=-10.0,
                        max=10.0,
                        step=1.0,
                        description=current_description,
    
                    )
                    
                elif prop_name == "right_padding":
                    bpy.types.Scene.right_padding = bpy.props.FloatProperty(
                        name="Right Padding",
                        default=0.15,
                        min=-10.0,
                        max=10.0,
                        step=1.0,
                        description=current_description,
    
                    )
                elif prop_name == "daz_import_obj_color":
                    
                    bpy.types.Scene.daz_import_obj_color = bpy.props.FloatVectorProperty(
                        name="",
                        description=current_description,
    
                        subtype="COLOR",
                        size=4,
                        default=(1.0, 1.0, 1.0, 1.0),
                        min=0.0,
                        max=1.0,
                    )
    
                elif prop_name == "add_viewport_color":
                    bpy.types.Scene.add_viewport_color = bpy.props.BoolProperty(
                        name="Color DAZ Morph",
                        description=current_description,
                        default=False, 
                    )
    

                elif prop_name == "include_fast_startup_backup":
                    bpy.types.Scene.include_fast_startup_backup = bpy.props.BoolProperty(
                        name="Include Startup Backup",
                        description=current_description,
                        default=True,
                    )
    
                # ✅ Proper `elif` Handling Section for Dynamic Property Assignment
                elif prop_name == "azure_silence_length":
                    bpy.types.Scene.azure_silence_length = bpy.props.IntProperty(
                        name="Azure Minimum Silence Length",
                        description=current_description,  # Consistent with your example
                        default=1,
                        min=1,
                        max=1000,
                        step=1
                    )
                
                elif prop_name == "adv_local_keep_armature":
                    bpy.types.Scene.adv_local_keep_armature = bpy.props.BoolProperty(
                        name="Local Armature",
                        default=False,
                        description=current_description,
    
                    )
    
                elif prop_name == "auto_save_file":
                    bpy.types.Scene.auto_save_file = bpy.props.BoolProperty(
                        name="FAST Auto-save Save File",
                        description=current_description,
                        default=True,
                    )
    
                elif prop_name == "auto_save_bookmark_file":
                    bpy.types.Scene.auto_save_bookmark_file = bpy.props.BoolProperty(
                        name="FAST Auto-save Startup File",
                        description=current_description,
                        default=False, 
                    )
    
                elif prop_name == "auto_save_increment":
                    bpy.types.Scene.auto_save_increment = bpy.props.BoolProperty(
                        name="Auto-save with Timestamp",
                        description=current_description,
                        default=True,
                    )
    
                elif prop_name == "auto_save_increment_backup":
                    bpy.types.Scene.auto_save_increment_backup = bpy.props.BoolProperty(
                        name="Auto Save Increment on Startup",
                        description=current_description,
                        default=True,
                    )
    
                elif prop_name == "auto_save_delete_old_versions":
                    bpy.types.Scene.auto_save_delete_old_versions = bpy.props.BoolProperty(
                        name="Choose to Delete Old Versions",
                        description=current_description,
                        default=True,
                    )
    
                elif prop_name == "auto_save_file_size_warning":
                    bpy.types.Scene.auto_save_file_size_warning = bpy.props.BoolProperty(
                        name="Auto-Save File Size Warning",
                        description=current_description,
                        default=False, 
                    )
    
                elif prop_name == "auto_save_file_size_warning_threshold":
                    bpy.types.Scene.auto_save_file_size_warning_threshold = bpy.props.FloatProperty(
                        name="File Size Reduction Threshold",
                        description=current_description,
    
                        min=0.0,
                        max=100.00,
                        default=50.0,
                        subtype="PERCENTAGE",
                    )
    
                elif prop_name == "gpt_random_user_command":
                    bpy.types.Scene.gpt_random_user_command = bpy.props.BoolProperty(
                        name="GPT Random User Command (Internal Testing)",
                        description=current_description,
                        default=False,
                        update=update_gpt_random_user_command,
                    )
                elif prop_name == "is_dirty":
                    bpy.types.Scene.is_dirty = bpy.props.BoolProperty(
                        name="Auto-save Only on Unsaved Changes",
                        description=current_description,
                        default=True,
                    )
    
    
    
                elif prop_name == "auto_save_delete_temp":
                    bpy.types.Scene.auto_save_delete_temp = bpy.props.BoolProperty(
                        name="Auto Save Delete Temp",
                        description=current_description,
                        default=False, 
                    )
    
                elif prop_name == "auto_save_splash_screen":
                    bpy.types.Scene.auto_save_splash_screen = bpy.props.BoolProperty(
                        name="FAST Auto-save Splash Screen",
                        description=current_description,
                        default=True,
                    )
    
                elif prop_name == "save_on_startup":
                    bpy.types.Scene.save_on_startup = bpy.props.BoolProperty(
                        name="Save on Startup",
                        description=current_description,
                        default=True,
                    )

    
                elif prop_name == "overlays_prop":
                    bpy.types.Scene.overlays_prop = bpy.props.BoolProperty(
                        name="Transform Overlays Decider",
                        description=current_description,
                        default=False, 
                    )

                elif prop_name == "fast_button_use_beep":
                    bpy.types.Scene.fast_button_use_beep = bpy.props.BoolProperty(
                        name="Fast Button Use Beep",
                        description=current_description, 
                        default=True,
                    )
                elif prop_name == "button_spacing":
                    bpy.types.Scene.button_spacing = bpy.props.FloatProperty(
                        name="Button Spacing",
                        description=current_description, 
                        default=spacing,  # Dynamic value from calculate_spacing_timer
                        min=0,
                        max=max_spacing,  # Dynamic max value
                        step=1.0,
                    )

    
                elif prop_name == "debug":
                    bpy.types.Scene.debug = bpy.props.BoolProperty(
                        name="Debug mode",
                        description=current_description,
                        default=False, 
                    )
    
                elif prop_name == "transform_nudge_prop":
                    bpy.types.Scene.transform_nudge_prop = bpy.props.FloatProperty(
                        name="Transform Nudge",
                        description=current_description,
                        default=0.1,
                        min=0.00000001,
                        max=1.0,  # Increase the maximum value to 1.0
                        step=0.01,
                        subtype="NONE",
                    )
    
                elif prop_name == "optimized_map":
                    bpy.types.Scene.optimized_map = bpy.props.BoolProperty(
                        name="Optimize Normal Map",
                        description=current_description,
                        default=True,
                        
                    )
    
                elif prop_name == "auto_mode":
                    bpy.types.Scene.auto_mode = bpy.props.BoolProperty(
                        name="Auto Mode",
                        description=current_description,
                        default=True,
                    )

                elif prop_name == "gpt_show_add_example_prompt":
                    bpy.types.Scene.gpt_show_add_example_prompt = bpy.props.BoolProperty(
                        name="Add Example Prompt",
                        description=current_description,
                        default=False,
                    )
    
                elif prop_name == "enable_pref":
                    bpy.types.Scene.enable_pref = bpy.props.BoolProperty(
                        name="Enable Preferences",
                        description=current_description,
                        default=True,
                    )
    
                elif prop_name == "new_workspace":
                    bpy.types.Scene.new_workspace = bpy.props.BoolProperty(
                        name="New Workspace",
                        description=current_description,
                        default=True,
                    )
    
                elif prop_name == "use_beep":
                    bpy.types.Scene.use_beep = bpy.props.BoolProperty(
                        name="Use Beep",
                        description=current_description,
                        default=True,
                    )
    
        except Exception as e:
            print(f"❌ Exception occurred while processing tooltip descriptions:")
            print(f"   Prop Name: {prop_name}")
            print(f"   Descriptions: {descriptions}")
            print(f"   Tooltip Descriptions Item: {tooltip_descriptions.get(prop_name)}")
            print(f"   Error: {e}")
            capture_and_copy_traceback()

        return {'FINISHED'}




# Redraw function to update Blender UI
def my_redraw():
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type in {"VIEW_3D"}:
                area.tag_redraw()

class FAST_OT_restart_blender_menu(bpy.types.Operator):

    bl_idname = "fast.restart_blender_menu"
    bl_label = "Restart Blender"
    bl_description = "Saves file & restarts Blender without any dialogs. This is tested and safe."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        

        try:
            # Call your custom restart function here
            bpy.ops.fast.restart_blender(show_message=False, save_file_before_restart=True)

        except Exception as e:
            print("")
            self.report({"ERROR"}, f"Error restarting Blender: {e}")
            capture_and_copy_traceback()
            return {'CANCELLED'}

        return {'FINISHED'}

menus_to_extend = [
    'OUTLINER_MT_collection',
    'OUTLINER_MT_object',
    'OUTLINER_MT_context_menu',
    'VIEW3D_MT_edit_mesh_context_menu',
    'VIEW3D_MT_pose_context_menu',
    "VIEW3D_MT_object_context_menu",
    'GRAPH_MT_context_menu',
    'SEQUENCER_MT_context_menu',
    'DOPESHEET_MT_context_menu',
    "NODE_MT_context_menu",
    "TEXT_MT_context_menu"
]

def draw_switch_fast_menu(self, context):
    

    manager = bpy.context.preferences.addons[__name__].preferences.Prop

    # Check the current state of the fast_menu property
    if manager.fast_menu:
        menu_text = "Blender Menu"  # When fast_menu is True
    else:
        menu_text = "Fast Menu"  # When fast_menu is False

    layout = self.layout
    layout.separator()

    if manager.disable_restart_blender:
        layout.operator("fast.restart_blender_menu", text='Restart Blender')
        layout.separator()
    if manager.disable_save_startup:
        layout.operator("fast.save_and_backup_startup_file", text="Save Startup File", emboss=True)
        
    if manager.disable_delete_startup:
        layout.operator("fast.delete_and_backup_startup_file", text="Delete Startup File", emboss=True)
        layout.separator()
  

    if manager.disable_show_console:
        layout.operator("fast.show_console", text="Console", emboss=True)
        layout.separator()
    if manager.disable_n_panel:
        layout.operator("fast.toggle_n_panel", text="N-Panel", emboss=True)
        layout.separator()
    if manager.disable_verbose_tool_tips:
        layout.operator("fast.toggle_verbose_tooltips", text="Verbose Tool-tips", emboss=True)
        layout.separator()

def register_km_menus():
    

    global menus_to_extend
    for menu_id in menus_to_extend:
        if hasattr(bpy.types, menu_id):
            menu_class = getattr(bpy.types, menu_id)
            menu_class.append(draw_switch_fast_menu)
        else:
            print(f"Menu {menu_id} not found for registration.")

def unregister_km_menus():
    

    global menus_to_extend
    for menu_id in menus_to_extend:
        if hasattr(bpy.types, menu_id):
            menu_class = getattr(bpy.types, menu_id)
            menu_class.remove(draw_switch_fast_menu)
        else:
            print(f"Menu {menu_id} not found for unregistration.")

def in_tenth_of_a_second():
    scn = bpy.context.scene


    
    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop


        manager.gpt_last_examples_vector_store_id = retrieve_vector_store_id()


        if manager.bse_fix_code or manager.se_fix_code:

            scn.gpt_edit_user_command_prompt = manager.gpt_temp_edit_user_command_prompt
            scn.gpt_confirm_object_is_selected = manager.gpt_temp_confirm_object_is_selected
            scn.gpt_boost_user_command = manager.gpt_temp_boost_user_command
            scn.gpt_find_code_examples = manager.gpt_temp_find_code_examples
            scn.gpt_run_final_script = manager.gpt_temp_run_final_script
            scn.gpt_random_user_command = manager.gpt_temp_random_user_command
        

        if manager.bse_fix_code:
            manager.bse_fix_code = False
        
        if manager.se_fix_code:
            manager.se_fix_code = False


        manager.gpt_use_current_file_for_error_check = False
        scn.gpt_main_assistant_temperature = 0.1
        scn.gpt_main_assistant_top_p = 0.2
 

        scn.gpt_4o_total_token_count = 0
        scn.gpt_4o_input_token_count = 0
        scn.gpt_4o_output_token_count = 0
        scn.gpt_4o_mini_total_token_count = 0
        scn.gpt_4o_mini_input_token_count = 0
        scn.gpt_4o_mini_output_token_count = 0
        scn.gpt_o1_mini_input_token_count = 0
        scn.gpt_o1_mini_output_token_count = 0
        scn.gpt_o1_mini_total_token_count = 0
        scn.gpt_o3_mini_input_token_count = 0
        scn.gpt_o3_mini_output_token_count = 0
        scn.gpt_o3_mini_total_token_count = 0
        manager.gpt_4o_total_cost = 0
        manager.gpt_4o_mini_total_cost = 0
        manager.gpt_o1_mini_total_cost = 0
        scn.gpt_current_iteration = 0           
        log_autogpt_state("0")

    except Exception as e:
        capture_and_copy_traceback()
        pass


def register():
    
    
    
    global block_register
    if block_register:
        return


    import bpy
    import bpy.utils.previews
    
    # stdout_capture = io.StringIO()
    
    # with redirect_stdout(stdout_capture):
    

    
        # try:
        #     bpy.utils.register_class(FAST_Properties)
        # except ValueError:
        #     pass

    
        # try:
        #     bpy.utils.register_class(FAST_Preferences)
        # except ValueError:
        #     pass

        # try:
        #     bpy.utils.register_class(GPTScriptFileItem)
        # except ValueError:
        #     pass


    try:
        bpy.utils.register_class(FAST_OT_hide_console)
    except ValueError:
        capture_and_copy_traceback()
    
    try:
        bpy.utils.register_class(FAST_OT_show_console)
    except ValueError:
        capture_and_copy_traceback()
    
    try:
        bpy.utils.register_class(FAST_OT_show_console_helper)
    except ValueError:
        capture_and_copy_traceback()
    
    try:
        bpy.utils.register_class(FAST_OT_close_windows_safely)
    except ValueError:
        capture_and_copy_traceback()
    
    try:
        bpy.utils.register_class(FAST_OT_confirm_and_restart_blender)
    except ValueError:
        capture_and_copy_traceback()
    
    try:
        bpy.utils.register_class(FAST_OT_restart_blender)
    except ValueError:
        capture_and_copy_traceback()
    
    try:
        bpy.utils.register_class(check_dependencies)
    except ValueError:
        capture_and_copy_traceback()
    
    try:
        bpy.utils.register_class(install_dependencies)
    except ValueError:
        capture_and_copy_traceback()
    

    

    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
    except KeyError as e:
        #print("Manager error.")
        capture_and_copy_traceback()
        return



    manager.register_done = False
    manager.register_done_n_panel = False
    manager.register_done_gpt = False
    try:
        load_icons()
    except:
        print("Internal: likely error in register function")
        pass


    bpy.app.timers.register(run_second, persistent=True, first_interval=5.0)


    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except ValueError as e:
            # print(f"Warning: {cls.__name__} could not be registered: {e}")
            print(f"Warning: class could not be registered...check file.", cls)
            return

    bpy.types.Scene.api_key = bpy.props.StringProperty(
        name="API Key",
        description=tooltip_descriptions["api_key"]["concise"],
        default="",
        # subtype='PASSWORD',
        update=update_api_key,
    )   

    bpy.types.Scene.gpt_choose_to_take_snapshot = bpy.props.BoolProperty(
        name="GPT Choose to Take Snapshot",
        description=tooltip_descriptions["gpt_choose_to_take_snapshot"]["concise"],  
        default=True,
    )
    bpy.types.Scene.gpt_show_verify_example_prompt = bpy.props.BoolProperty(
        name="GPT Verify or Remove Example",
        description=tooltip_descriptions["gpt_show_verify_example_prompt"]["concise"],  
        default=False,
    )
    bpy.types.Scene.gpt_data_limit = bpy.props.IntProperty(
        name="GPT Data Limit",
        description=tooltip_descriptions["gpt_data_limit"]["concise"],  
        default=5000,
        min=1,
        max=20000,
    )
    
    bpy.types.Scene.gpt_random_user_command = bpy.props.BoolProperty(
        name="GPT Random User Command (Internal Testing)",
        description=tooltip_descriptions["gpt_random_user_command"]["concise"],  
        default=True,
    )
    
    bpy.types.Scene.gpt_edit_user_command_prompt = bpy.props.BoolProperty(
        name="Show Edit User Command Prompt",
        description=tooltip_descriptions["gpt_edit_user_command_prompt"]["concise"],  
        default=True,
    )
    bpy.types.Scene.ambient_noise_duration_prop = bpy.props.FloatProperty(
        name="Ambient Noise Duration",
        default=0.25,
        min=0.00,
        max=5.0,
        description=tooltip_descriptions["ambient_noise_duration_prop"]["concise"],
    )
    bpy.types.Scene.pull_se_examples_iterations = bpy.props.IntProperty(
        name="SE Search Iterations",
        description=tooltip_descriptions["pull_se_examples_iterations"]["concise"],
        default=50,
        min=1,
        max=200,
    )

    bpy.types.Scene.gpt_send_anonymous_data = bpy.props.BoolProperty(
        name="Send Anonymous Error Data",
        description=tooltip_descriptions["gpt_send_anonymous_data"]["concise"],  
        default=False,
    )
    
    bpy.types.Scene.gpt_file_permission_fixer_path = bpy.props.StringProperty(
        name="File Permission Fixer Path",
        description=tooltip_descriptions["gpt_file_permission_fixer_path"]["concise"],  
        default="",
        update=update_gpt_file_permission_fixer_path
    )
    

    bpy.types.Scene.gpt_smtp_lib_app_password = bpy.props.StringProperty(
        name="SMTP App Password",
        description=tooltip_descriptions["gpt_smtp_lib_app_password"]["concise"],  
        default="",
        subtype='PASSWORD'
    )
    
    bpy.types.Scene.gpt_smtp_lib_server = bpy.props.StringProperty(
        name="SMTP Server",
        description=tooltip_descriptions["gpt_smtp_lib_server"]["concise"],  
        default="smtp.gmail.com",
    )
    
    bpy.types.Scene.gpt_confirm_object_is_selected = bpy.props.BoolProperty(
        name="Confirm Object Is Selected",
        description=tooltip_descriptions["gpt_confirm_object_is_selected"]["concise"],  
        default=False,
    )
    
    bpy.types.Scene.gpt_confirm_data = bpy.props.BoolProperty(
        name="Confirm Data",
        description=tooltip_descriptions["gpt_confirm_data"]["concise"],  
        default=False,
    )
    
    bpy.types.Scene.gpt_boost_user_command = bpy.props.BoolProperty(
        name="Boost User Command",
        description=tooltip_descriptions["gpt_boost_user_command"]["concise"],  
        default=True,
        update=update_gpt_boost_user_command
    )
    bpy.types.Scene.gpt_model_secondary = bpy.props.EnumProperty(
        name="GPT Model (Secondary)",
        items=[
            ("gpt-4o", "gpt-4o", "GPT-4o: First Choice. Latest flagship model, it's the best and cheapest"),
            ("o3-mini", "o3-mini", "o3-mini: Latest miniature version of the o3 model, optimized for reasoning tasks in coding, mathematics, and science."),
        ],
        default="gpt-4o",
        description=tooltip_descriptions["gpt_model_secondary"]["concise"], 
    )
    bpy.types.Scene.gpt_advanced_boost_user_command = bpy.props.BoolProperty(
        name="Use Advanced Model for Boost User Command",
        description=tooltip_descriptions["gpt_advanced_boost_user_command"]["concise"],  
        default=True,
        update=update_gpt_advanced_boost_user_command
    )
    
    bpy.types.Scene.bse_search_term = bpy.props.StringProperty(
        name="BSE Search Term",
        description=tooltip_descriptions["bse_search_term"]["concise"],  
        default="",
    )

    
    bpy.types.Scene.gpt_find_code_examples = bpy.props.BoolProperty(
        name="Find Examples",
        description=tooltip_descriptions["gpt_find_code_examples"]["concise"],  
        default=True,
    )
    
    bpy.types.Scene.gpt_show_lookups = bpy.props.BoolProperty(
        name="Show Lookups",
        description=tooltip_descriptions["gpt_show_lookups"]["concise"],  
        default=True,
    )
    
    bpy.types.Scene.show_se_content = bpy.props.BoolProperty(
        name="Show Body Content",
        description=tooltip_descriptions["show_se_content"]["concise"],  
        default=False,
    )
    bpy.types.Scene.gpt_max_iterations = bpy.props.IntProperty(
        name="GPT Iteration Count",
        description=tooltip_descriptions["gpt_max_iterations"]["concise"],
        default=5,
        min=0,
        max=50,
    )
    bpy.types.Scene.gpt_show_cost = bpy.props.BoolProperty(
        name="Show Tokens",
        description=tooltip_descriptions["gpt_show_cost"]["concise"],  
        default=False,
    )
    
    bpy.types.Scene.gpt_4o_mini_input_token_count = bpy.props.IntProperty(
        name="GPT 4o mini Input Token Count",
        description=tooltip_descriptions["gpt_4o_mini_input_token_count"]["concise"],  
        default=0,
    )
    
    bpy.types.Scene.gpt_4o_mini_output_token_count = bpy.props.IntProperty(
        name="GPT 4o mini Output Token Count",
        description=tooltip_descriptions["gpt_4o_mini_output_token_count"]["concise"],  
        default=0,
    )
    
    bpy.types.Scene.gpt_4o_mini_total_token_count = bpy.props.IntProperty(
        name="Total GPT 4o mini Token Count",
        description=tooltip_descriptions["gpt_4o_mini_total_token_count"]["concise"],  
        default=0,
    )
    
    bpy.types.Scene.gpt_4o_input_token_count = bpy.props.FloatProperty(
        name="GPT 4o Input Token Count",
        description=tooltip_descriptions["gpt_4o_input_token_count"]["concise"],  
        default=0,
    )
    
    bpy.types.Scene.gpt_4o_output_token_count = bpy.props.FloatProperty(
        name="GPT o3 mini Output Token Count",
        description=tooltip_descriptions["gpt_4o_output_token_count"]["concise"],  
        default=0,
    )
    
    bpy.types.Scene.gpt_o3_mini_input_token_count = bpy.props.FloatProperty(
        name="GPT o3 mini Input Token Count",
        description=tooltip_descriptions["gpt_o3_mini_input_token_count"]["concise"],  
        default=0,
    )
    
    bpy.types.Scene.gpt_o3_mini_output_token_count = bpy.props.FloatProperty(
        name="GPT 4o Output Token Count",
        description=tooltip_descriptions["gpt_o3_mini_output_token_count"]["concise"],  
        default=0,
    )
    bpy.types.Scene.gpt_o3_mini_total_token_count = bpy.props.IntProperty(
        name="Total GPT o3 mini Token Count",
        description=tooltip_descriptions["gpt_o3_mini_total_token_count"]["concise"],  
        default=0,
    )
    
    bpy.types.Scene.gpt_4o_total_token_count = bpy.props.FloatProperty(
        name="Total GPT 4o Token Count",
        description=tooltip_descriptions["gpt_4o_total_token_count"]["concise"],  
        default=0,
    )
    
    bpy.types.Scene.gpt_o1_mini_input_token_count = bpy.props.IntProperty(
        name="GPT o1 mini Input Token Count",
        description=tooltip_descriptions["gpt_o1_mini_input_token_count"]["concise"],  
        default=0,
    )
    
    bpy.types.Scene.gpt_o1_mini_output_token_count = bpy.props.IntProperty(
        name="GPT o1 mini Output Token Count",
        description=tooltip_descriptions["gpt_o1_mini_output_token_count"]["concise"],  
        default=0,
    )
    
    bpy.types.Scene.gpt_o1_mini_total_token_count = bpy.props.IntProperty(
        name="Total GPT o1 mini Token Count",
        description=tooltip_descriptions["gpt_o1_mini_total_token_count"]["concise"],  
        default=0,
    )
    

    bpy.types.Scene.gpt_pause_before_fixing_errors = bpy.props.BoolProperty(
        name="Pause Before Fixing Errors",
        description=tooltip_descriptions["gpt_pause_before_fixing_errors"]["concise"],  
        default=False,
    )
    


    bpy.types.Scene.gpt_run_final_script = bpy.props.BoolProperty(
        name="GPT Run Final Script",
        description=tooltip_descriptions["gpt_run_final_script"]["concise"],  
        default=True,
    )
    
    bpy.types.Scene.gpt_current_iteration = bpy.props.IntProperty(
        name="GPT Current Iteration",
        description=tooltip_descriptions["gpt_current_iteration"]["concise"],  
        default=0,
        min=0,
        max=20,
    )
    
    bpy.types.Scene.gpt_use_beep = bpy.props.BoolProperty(
        name="Use Beep",
        description=tooltip_descriptions["gpt_use_beep"]["concise"],  
        default=True,
    )

    bpy.types.Scene.gpt_operator_name = bpy.props.StringProperty(
        name="Operator Name",
        description=tooltip_descriptions["gpt_operator_name"]["concise"],  
        default="bpy.ops.fast.auto_gpt_assistant()",
    )
    
    bpy.types.Scene.gpt_run_on_selected_objects = bpy.props.BoolProperty(
        name="Run on Selected Object",
        description=tooltip_descriptions["gpt_run_on_selected_objects"]["concise"],  
        default=False,
    )
    
    bpy.types.Scene.gpt_added_code = bpy.props.StringProperty(
        name="Additional Code Path",
        description=tooltip_descriptions["gpt_added_code"]["concise"],  
        default="",
        subtype='FILE_PATH',
    )
    
    bpy.types.Scene.gpt_show_code = bpy.props.BoolProperty(
        name="Show Code",
        description=tooltip_descriptions["gpt_show_code"]["concise"],  
        default=True,
    )
    
    bpy.types.Scene.gpt_error_check_timeout = bpy.props.IntProperty(
        name="Blender Quit Timeout",
        description=tooltip_descriptions["gpt_error_check_timeout"]["concise"],  
        default=15,
        min=15,
        max=120,
    )
    
    bpy.types.Scene.gpt_main_assistant_temperature = bpy.props.FloatProperty(
        name="Main GPT Assistant Temperature",
        description=tooltip_descriptions["gpt_main_assistant_temperature"]["concise"],  
        default=0.1,
        step=1,
        min=0.0,
        max=1.0,
    )
    
    bpy.types.Scene.gpt_main_assistant_top_p = bpy.props.FloatProperty(
        name="Main GPT Assistant Top_p",
        description=tooltip_descriptions["gpt_main_assistant_top_p"]["concise"],  
        default=0.2,
        step=1,
        min=0.0,
        max=1.0,
    )

    bpy.types.Scene.gpt_show_add_example_prompt = bpy.props.BoolProperty(
        name="Add Example Prompt",
        description=tooltip_descriptions["gpt_show_add_example_prompt"]["concise"],  
        default=False,
    )

    bpy.types.Scene.gpt_advanced_api_or_manual_or_fast_decider = bpy.props.BoolProperty(
        name="Use Advanced Model for API/Add-on/Manual Decider",
        description=tooltip_descriptions["gpt_advanced_api_or_manual_or_fast_decider"]["concise"],  
        default=False,
    )
    
    bpy.types.Scene.hide_scene_objects = bpy.props.BoolProperty(
        name="Hide Objects",
        description=tooltip_descriptions["hide_scene_objects"]["concise"],  
        default=True,
    )
    bpy.types.Scene.gpt_hide_scene_objects = bpy.props.BoolProperty(
        name="Hide Objects",
        description=tooltip_descriptions["gpt_hide_scene_objects"]["concise"],  
        default=True,
    )

    bpy.types.Scene.gpt_main_assistant_temperature = bpy.props.FloatProperty(
        name="Main GPT Assistant Temperature",
        description=tooltip_descriptions["gpt_main_assistant_temperature"]["concise"],
        default=0.1,
        min=0.0,
        max=1.0
    )
    
    bpy.types.Scene.gpt_main_assistant_top_p = bpy.props.FloatProperty(
        name="Main GPT Assistant Top_p",
        description=tooltip_descriptions["gpt_main_assistant_top_p"]["concise"],
        default=0.2,
        min=0.0,
        max=1.0
    )

    bpy.types.Scene.GPTScriptFileIndex = bpy.props.IntProperty(
        name="Selected Script File Index",
        description=tooltip_descriptions["GPTScriptFileIndex"]["concise"],
        update=update_gpt_script_file_index,
    )
        
    bpy.types.Scene.gpt_max_iterations = bpy.props.IntProperty(
        name="GPT Iteration Count",
        description=tooltip_descriptions["gpt_max_iterations"]["concise"],
        default=5,
        min=0,
        max=50,
        update=update_gpt_max_iterations,
    )


    bpy.utils.register_class(BLENDER_AI_PT_Panel_1)
    bpy.utils.register_class(BLENDER_AI_PT_Panel_2)
    bpy.utils.register_class(BLENDER_AI_PT_Panel_3)
    register_km_menus()
    bpy.types.Scene.fast = PointerProperty(type=FAST_Properties)



    

    tfp = os.path.join(os.path.expanduser("~"), "Desktop", "OBS", ".COMMERCIAL")

    if os.path.exists(tfp):

        manager.new_addition = True

       
        manager.gpt_do_not_save_userpref_while_running = False


    else:
        manager.new_addition = False
        manager.gpt_do_not_save_userpref_while_running = False

    bpy.app.timers.register(tooltip_update_timer, persistent=True)

    manager.autogpt_processing = 'Autonomous GPT-4'
    manager.gpt_main_processing_status = False
    manager.gpt_cancel_op = False
    manager.gpt_input_waiting = False
    manager.bse_scan_cancel_op = False

    manager.web_search_light_button = False
    manager.se_pull_cancel_op = False
    manager.allow_auto_gpt_assistant = False

    manager.gpt_final_print_string = "{}"
    manager.gpt_file_path_notification = False
    manager.gpt_first_code = ""
    manager.gpt_using_data = False
    manager.se_boosted_user_command = ""
    manager.print_example_message = False
    manager.ran_checker_from_outside_main_code = False
    manager.gpt_q_run = False
    manager.te_script_not_tested = False
    manager.gpt_img_run = False
    if manager.is_restarting:
        manager.is_restarting = False
        clear_console()

    manager.te_current_text_block_name = ""
    manager.gpt_error_mssg_list = ""

    if manager.se_changed_values:

        manager.gpt_run_lookups = manager.gpt_temp_run_lookups
        
        manager.se_changed_values = False   

        save_user_pref_block_info()

    manager.console_window_handle = 0
    bpy.app.timers.register(in_tenth_of_a_second, first_interval=0.1)


    

    bpy.types.WindowManager.fast = PointerProperty(type=FAST_Properties)

    bpy.context.window_manager.fast.module_name = 'blender_ai_thats_error_proof'

    bpy.app.handlers.load_post.append(enable_pref)

    # bpy.app.timers.register(gpt_enable_pref)
    bpy.app.timers.register(save_user_preferences, persistent=True, first_interval=15)
    bpy.app.timers.register(test_values_function, persistent=True)
    bpy.app.timers.register((scene_sync), persistent=True)

    bpy.app.timers.register(execute_queued_functions)

    bpy.app.timers.register(run_once_on_install, first_interval=0.1)

    try:
        bpy.utils.register_class(FAST_OT_UpdateTooltipsOperator)
    except Exception:
        pass


    # Register the scene property with the verbose tooltip by default
    bpy.types.Scene.gpt_main_assistant_top_p = bpy.props.FloatProperty(
        name="Main GPT Assistant Top_p",
        description=VERBOSE_TOOLTIP,  # Start with verbose by default
        default=0.2,
        step=1,
        min=0.0,
        max=1.0,
    )
    bpy.app.timers.register(lambda: (reload_properties_from_json(), None)[1], first_interval=1.0)
    all_active = all(kmi.active for _, kmi in fastmenu_keymaps)
    manager.register_done_n_panel = True



def unregister():

    try:

        for cls in reversed(classes):
            try:
                bpy.utils.unregister_class(cls)
            except RuntimeError:
                pass

        # unregister all keymaps
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
        addon_keymaps.clear()
        fastmenu_keymaps.clear()
        del bpy.types.Scene.fast


        if hasattr(bpy.utils, "unregister_class"):
    

            bpy.utils.unregister_class(BLENDER_AI_PT_Panel_1)
            bpy.utils.unregister_class(BLENDER_AI_PT_Panel_2)
            bpy.utils.unregister_class(BLENDER_AI_PT_Panel_3)
            unregister_km_menus()

        if hasattr(bpy.app.timers, "tooltip_update_timer"):
            bpy.app.timers.unregister(tooltip_update_timer)

        try:
            unload_icons()
        except:
            pass
    
        try:
            bpy.app.timers.unregister(run_second)
        except:
            pass
    

      
        bpy.utils.unregister_class(GPTScriptFileItem)
        bpy.utils.unregister_class(FAST_Properties)
        bpy.utils.unregister_class(FAST_Preferences)
        bpy.utils.unregister_class(FAST_OT_hide_console)
        bpy.utils.unregister_class(FAST_OT_show_console)
        bpy.utils.unregister_class(FAST_OT_show_console_helper)
        bpy.utils.unregister_class(FAST_OT_close_windows_safely)
        bpy.utils.unregister_class(FAST_OT_confirm_and_restart_blender)
        bpy.utils.unregister_class(FAST_OT_restart_blender)
        bpy.utils.unregister_class(FAST_OT_info)
        bpy.utils.unregister_class(check_dependencies)
        bpy.utils.unregister_class(install_dependencies)

        try:
            bpy.utils.unregister_class(FAST_OT_check_addon_version_op_1,)
        except ValueError:
            capture_and_copy_traceback()

        try:
            bpy.utils.unregister_class(FAST_OT_install_fast)
        except ValueError:
            capture_and_copy_traceback()
        

    
        del bpy.types.WindowManager.fast

    
        if hasattr(bpy.app.timers, "run_once_on_install"):
            bpy.app.timers.unregister(bpy.app.timers.run_once_on_install)
    

        # if hasattr(bpy.app.handlers.load_post, "gpt_enable_pref"):
        #     bpy.app.handlers.load_post.remove(gpt_enable_pref)


        if hasattr(bpy.app.handlers.load_post, "enable_pref"):
            bpy.app.handlers.load_post.remove(enable_pref)
            
        if bpy.app.timers.is_registered(in_tenth_of_a_second):
            bpy.app.timers.unregister(in_tenth_of_a_second)

        if hasattr(bpy.app.timers, "save_user_preferences"):
            bpy.app.timers.unregister(save_user_preferences)
        
        if hasattr(bpy.app.timers, "test_values_function"):
            bpy.app.timers.unregister(test_values_function)

        if hasattr(bpy.app.timers, "scene_sync"):
            bpy.app.timers.unregister(scene_sync)


        if bpy.app.timers.is_registered(execute_queued_functions):
            bpy.app.timers.unregister(execute_queued_functions)

        try:
            bpy.utils.unregister_class(FAST_OT_UpdateTooltipsOperator)
        except Exception:
            pass


        del bpy.types.Scene.gpt_main_assistant_top_p
    



    except Exception as e:

        capture_and_copy_traceback()
        
        print_color("AR", "\nThere was an issue disabling the add-on. Please restart Blender.")    



classes = (
    FAST_OT_toggle_verbose_tooltips,
    FAST_OT_toggle_n_panel,
    FAST_OT_delete_pip_cache,
    FAST_OT_DiffeomorphicRestoreHiddenObjects,
    FAST_UL_script_files,
    FAST_OT_restart_blender_menu,
    FAST_OT_gpt_save_theme,
    FAST_OT_get_tutorial_transcript,
    FAST_OT_get_node_image_data,
    FAST_OT_open_node_image,
    FAST_OT_open_blender_intro_tutorial,
    FAST_OT_pull_se_or_bse_example,
    FAST_OT_pull_se_or_bse_example_helper,
    FAST_OT_pull_se_or_bse_example_tester,
    FAST_OT_light_scene,
    FAST_OT_gpt_delete_asset_init,
    FAST_OT_gpt_delete_asset,
    FAST_OT_code_and_command_to_clipboard,
    FAST_OT_auto_gpt_assistant,
    FAST_OT_auto_gpt_questions,
    FAST_OT_text_auto_gpt_assistant,
    FAST_OT_auto_gpt_modal_operator,
    FAST_OT_Open_OpenAICredits_Website,
    FAST_OT_open_openai_api_key_website,
    FAST_OT_Open_CopyQ_Website,
    FAST_OT_open_blender_api,
    FAST_OT_auto_gpt_assistant_info,
    FAST_OT_auto_gpt_question_info,
    FAST_OT_gpt_user_command_info,
    FAST_OT_gpt_user_instruction_set_info,
    FAST_OT_gpt_added_code_info,
    FAST_OT_auto_gpt_extra_info_1,
    FAST_OT_auto_gpt_extra_info_2,
    FAST_OT_auto_gpt_info_3,
    FAST_OT_open_gpt_model_pricing_info,
    FAST_OT_send_bone_data_to_file,
    FAST_OT_EditUserInstructionSets,
    FAST_OT_TextEditUserInstructionSets,
    FAST_OT_EditUserCommand,
    FAST_OT_added_code_operator,
    FAST_OT_open_file_in_editor,
    FAST_OT_open_examples,
    FAST_OT_create_addon_examples,
    FAST_OT_scan_fix_blender_stack_exchange_script,
    FAST_OT_view_scanned_bse_example,
    FAST_OT_open_data_file,
    FAST_OT_OpenStandardPythonFileOperator,
    FAST_OT_default_standard_python_theme,
    FAST_OT_take_script_result_snapshot,
    FAST_OT_text_run_script,
    FAST_OT_CopyLatestBackupUserCommand,
    FAST_OT_open_popover,
    FAST_OT_open_user_command_backup_folder,
    FAST_OT_AddFixUserCommand,
    FAST_OT_pull_se_or_bse_example_test,
    FAST_OT_pull_se_or_bse_example_helper_test,
    FAST_OT_Open_OpenAIAPIKeys_Website,
    FAST_OT_Text_To_Image,
    FAST_OT_Open_Image,
    FAST_OT_save_and_backup_startup_file_append,
    FAST_OT_save_and_backup_startup_file,
    FAST_OT_delete_and_backup_startup_file,
    FAST_OT_fast_issues,
)
