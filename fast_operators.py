
#test
import bpy
import os
import sys
import glob
from contextlib import redirect_stdout

lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
if lib_path not in sys.path:
    sys.path.append(lib_path)

main_sys_paths = sys.path 

import platform
import subprocess
import importlib
from .fast_global import *
from .fast_global import capture_and_copy_traceback
try:
    if platform.system() == "Windows":
        # Check if "lib" path is in sys.path
        lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
        if lib_path not in sys.path:
            sys.path.append(lib_path)


        import psutil

        # Remove "lib" after import to avoid redundancy
        if lib_path in sys.path:
            sys.path = [path for path in sys.path if path != os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")]

  

    elif platform.system() in ["Darwin", "Linux"]:  # macOS or Linux
        # Check if "lib" path is in sys.path and remove it
        lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
        if lib_path in sys.path:
            sys.path = [path for path in sys.path if path != os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")]

   

        # Add "lib2" to sys.path if not already there
        lib2_path = os.path.join(os.path.dirname(__file__), "lib2")
        if lib2_path not in sys.path:
            sys.path.append(lib2_path)
      

        import psutil

        # Remove "lib2" after import
        if lib2_path in sys.path:
            sys.path = [path for path in sys.path if path != os.path.join(os.path.dirname(__file__), "lib2")]

        # print(f"{platform.system()}: Removed {lib2_path} from sys.path")

except ModuleNotFoundError as e:
    pass


lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
if lib_path not in sys.path:
    sys.path.append(lib_path)

lib3_path = os.path.join(os.path.dirname(__file__), "lib3")
if lib3_path not in sys.path:
    sys.path.append(lib3_path)




try:
    # Detect platform and modify paths only for Windows
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

    if platform.system() == "Darwin":
        import objc

    import pywinctl as gw
    # print("\npywinctl imported successfully!")

    # # Programmatically check where it's being imported from
    # pywinctl_spec = importlib.util.find_spec("pywinctl")
    # if pywinctl_spec is not None and pywinctl_spec.origin:
    #     print(f"'pywinctl' is being imported from: {pywinctl_spec.origin}")
    # else:
    #     print("Unable to determine the import path for 'pywinctl'.")

except ModuleNotFoundError as e:

    pywinctl_spec = importlib.util.find_spec("pywinctl")
    if pywinctl_spec is not None:
        print_color("AR", f"\n'pywinctl' was found at: {pywinctl_spec.origin}")
    else:
        print_color("AR", f"\nFailed to locate 'pywinctl' in the current environment.")



import shutil
import platform
import subprocess
import re
import time
import zipfile
import json
import ctypes
import importlib
import inspect
import traceback
import requests
import warnings
import stat
from bpy.props import StringProperty, BoolProperty
from bpy.types import Operator
import asyncio
import functools
try:
    import aiohttp
except ModuleNotFoundError:
    aiohttp = None

import addon_utils
from datetime import datetime

from .fast_icons import *



from . import __name__


class FAST_OT_info(bpy.types.Operator):
    bl_idname = "fast.info"
    bl_label = "Extended Info Display"
    message: bpy.props.StringProperty(default="Extended information message.")
    duration: bpy.props.IntProperty(default=10, description="Duration in seconds")
    flag: bpy.props.BoolProperty(default=False)  # Control flag to determine whether to print immediately and finish

    _timer = None
    _start_time = 0
    _iterations = 0
    _interval = 3

    def execute(self, context):
        if self.flag:
            self.report({'INFO'}, self.message)
            return {'FINISHED'}
        else:
            self._start_time = time.time()
            self._iterations = 0

            # Start a new thread for the timer logic
            self.thread = threading.Thread(target=self.timer_thread, args=(context,))
            self.thread.start()
            
            return {'RUNNING_MODAL'}

    def timer_thread(self, context):
        while True:
            elapsed_time = time.time() - self._start_time
            if elapsed_time >= self._interval * self._iterations:
                bpy.app.timers.register(functools.partial(self.report_message, context), first_interval=0.1)
                self._iterations += 1

            if elapsed_time >= self.duration:
                bpy.app.timers.register(functools.partial(self.finish_operator, context), first_interval=0.1)
                break

            time.sleep(0.1)

    def report_message(self, context):
        self.report({'INFO'}, self.message)

    def finish_operator(self, context):
        try:
            self.report({'INFO'}, self.message)
            self.cancel(context)
        except:
            caller_info = inspect.stack()[1]  # Get information about the caller
            calling_line = caller_info.lineno  # Line number where print_color was called 
            print(f"\nInvalid info call...called from line: {calling_line}")  # Print the line number after the output
        
        return None

    def modal(self, context, event):
        if self.flag:
            self.report({'INFO'}, self.message)
            self.cancel(context)
            return {'FINISHED'}

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        if self.flag:
            self.report({'INFO'}, self.message)
            return {'FINISHED'}
        else:
            self._start_time = time.time()
            self._iterations = 0
            self._timer = context.window_manager.event_timer_add(0.1, window=context.window)
            context.window_manager.modal_handler_add(self)
            self.execute(context)
            return {'RUNNING_MODAL'}

    def cancel(self, context):
        if self._timer:
            self.thread.join()
            context.window_manager.event_timer_remove(self._timer)
            
        return None

class FAST_OT_toggle_verbose_tooltips(bpy.types.Operator):
    bl_idname = "fast.toggle_verbose_tooltips"
    bl_label = "Toggle Verbose Tooltips"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def description(cls, context, event):

        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        if manager.verbose_tooltips:
            return (
                "A way to make those big tool-tips smaller.\n\n"
                "We have documentation built into the tool tips!\n\n"
                "See it works by toggling and looking at this tool-tip"
            )
        else:
            return "Toggle between one & multi-line tool-tips"

    def execute(self, context):
        scn = bpy.context.scene

        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        manager.verbose_tooltips = not manager.verbose_tooltips
        # Check the current state and report accordingly
        if manager.verbose_tooltips:
            print("")
            self.report({"INFO"}, "Verbose Tooltips are ON")
            print("")
        else:
            print("")
            self.report({"INFO"}, "Concise Tooltips are ON")
            print("")
        return {"FINISHED"}


def try_delete_item(item_path, retries=3, delay=1):
    """
    Try to delete a file or directory.

    :param item_path: Path to the file or directory to delete.
    :param retries: Number of times to retry deletion.
    :param delay: Time (in seconds) to wait between retries.
    """
    for attempt in range(retries):
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
                return True
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                return True
        except PermissionError as e:
            print(f"PermissionError while trying to delete {item_path}: {e}")

            # If directory, try deleting files inside individually
            if os.path.isdir(item_path):
                for file_inside in os.listdir(item_path):
                    try_delete_item(os.path.join(item_path, file_inside))
        except Exception as e:
            print(f"Error while trying to delete {item_path}:\n")

            capture_and_copy_traceback()

            
        # If the max number of attempts hasn't been reached, wait and then try again
        if attempt < retries - 1:
            time.sleep(delay)

    print(f"Failed to delete {item_path} after {retries} attempts.")
    return False




class FAST_OT_google_voice_search(bpy.types.Operator):
    bl_idname = "fast.google_voice_search"
    bl_label = "Google Operator Search"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def description(cls, context, event):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        if manager.verbose_tooltips:
            return (
                "Click button, wait for the beep, and speak your phrase. Blender will search for it.\n\n"
                "For multiple operations, use this operator and rerun easily via RE-RUN VIA F3 button.\n\n"
                "Sound feature is Windows and Mac only. Put in feature request I will add your OS.\n\n"
                "Strengthening the Voice Recognition:\n\n"
                "1. Low Microphone Volume: Ensure the microphone volume is at an optimum level.\n\n"
                "2. Ambient Noise: If noisy environment, increase ambient noise slider on 'FAST Google' panel, until heard clearly.\n\n"
                "3. Network Issues: This operator requires internet connection to Google. Poor connection might result in errors.\n\n"
                "4. Speech Clarity: Ensure spoken words are clear. Muffled or slurred speech might not be recognized correctly.\n\n"
                "5. Language and Accent: This is set to en-US. If have a different accent, click REPORT ISSUES and I'll upgrade ASAP"
            )
        else:
            return "Voice-activated F3 search tool for Blender using Google's voice recognition. Verbose tool-tip available"

    # operator status
    listeningStart = False
    listeningCompleted = False
    finished = False
    # user feedback
    cancel_request = False
    # recorded audio
    audio = None
    # threads
    t1 = None
    # time
    time_start = 0.0
    total_time = 0.0

    def execute(self, context):
        global listeningActive
        try:
            if not listeningActive:
                try:
                    manager = bpy.context.preferences.addons[__name__].preferences.Prop
                except:
                    self.report({"INFO"}, "Could not find installed addon, re-enable the addon."
                    )
                    return {"CANCELLED"}

                wm = context.window_manager

                timeout_duration = manager.timeout_duration_prop

                self.timer = wm.event_timer_add(0.013333, window=context.window)
                wm.modal_handler_add(self)
                return {"RUNNING_MODAL"}
            else:
                return {"CANCELLED"}
        finally:
            listeningActive = False

    def listen_to_mic(self, r, mic, timeout_duration, use_beep):
        global listeningActive
        self.listeningStart = True
        listeningActive = True
        # print('thread start')
        # print('Microphone listening start')

        print(use_beep)
        # play beep sound to indicate start of speech recognition
        if use_beep:
            beep()

        with mic as source:
            try:
                self.audio = r.listen(
                    source, timeout=timeout_duration
                )  # set timeout to 5 seconds
            except sr.UnknownValueError:
                
                self.cancel_request = True
                self.report(
                    {"INFO"}, "Google Speech Recognition could not understand audio"
                )
            except sr.RequestError as e:
                
                self.cancel_request = True
                self.report(
                    {"INFO"},
                    "Could not request results from Google Speech Recognition service; {0}".format(
                        e
                    ),
                )
            except sr.WaitTimeoutError:
                
                if not self.cancel_request:
                    self.report({"INFO"}, "Timeout error waiting for listening to start."
                    )
                self.cancel_request = True
            except ModuleNotFoundError:
                
                self.cancel_request = True
                self.report(
                    {"INFO"},
                    "Install Speech Recognition by clicking Install Dependencies in F.A.S.T. preferences.",
                )

            self.listeningCompleted = True
            listeningActive = False
            # print('audio listening failed')

            # self.report({'ERROR'}, "Microphone input level too low")
        # print('thread finished')

    def modal(self, context, event):
        global listeningActive



        if event.type in {"ESC", "LEFTMOUSE", "RIGHTMOUSE"}:
            if not self.cancel_request:
                # print('cancel request')
                self.cancel_request = True

        if not self.listeningStart:
            self.listeningStart = True
            self.time_start = time.time()
            global sr

            manager = bpy.context.preferences.addons[__name__].preferences.Prop
            ambient_duration = manager.ambient_noise_duration_prop
            timeout_duration = manager.timeout_duration_prop
            use_beep = manager.use_beep

            # have a worst case timeout duration?
            if timeout_duration == 0 or timeout_duration > 10:
                timeout_duration = 10

            try:
                import requests

                requests.head("http://www.google.com/", timeout=5)
            except requests.ConnectionError:
                self.report({"INFO"}, "Please connect to the internet.")
                listeningActive = False
                return {"CANCELLED"}

            try:
                # initialize recognizer
                r = sr.Recognizer()
                mic = sr.Microphone()
            except:
                # print('except')
                self.report({"ERROR"}, "speechrecognition module dependency not found: Ensure you have installed dependencies in F.A.S.T. preferences.")
                listeningActive = False
                return {"CANCELLED"}

            # check if microphone still connected
            if mic.list_microphone_names() == []:
                self.report({"ERROR"}, "No microphone detected")
                listeningActive = False
                return {"CANCELLED"}

            # optimise microphone sensitivity
            with mic as source:
                r.adjust_for_ambient_noise(source, duration=ambient_duration)

            # invoke search menu
            bpy.ops.wm.search_menu("INVOKE_DEFAULT")

            # create and launch listener thread
            self.t1 = threading.Thread(
                target=self.listen_to_mic, args=(r, mic, timeout_duration, use_beep)
            )
            self.t1.start()

        if self.listeningCompleted and not self.cancel_request:
            self.t1.join()
            # print('thread join')

            r = sr.Recognizer()
            mic = sr.Microphone()
            try:
                text = r.recognize_google(self.audio, language="en-US", show_all=False)
            except:
                text = ""
                # print('Google Speech Recognition could not interpret audio')
                self.report(
                    {"INFO"}, "Google Speech Recognition could not interpret audio"
                )

            if len(text) == 0:
                self.report(
                    {"INFO"}, "No text was interpreted from the audio recording."
                )
                # print('no text was interpreted from the audio recording')
            else:
                # print(f"Recognized speech: {text}")
                # Mimic keyboard input after recognized speech
                pyautogui.typewrite(text)

            self.modal_finished = True
            # bpy.context.window_manager.progress_end()
            return {"FINISHED"}

        if self.listeningCompleted and self.cancel_request:
            self.t1.join()
            listeningActive = False
            return {"CANCELLED"}

        if self.listeningCompleted and self.modal_finished:
            # self.t1.join()
            # print('operator finished_3')
            # print('')
            # wm.progress_end()
            listeningActive = False
            return {"FINISHED"}

        return {"PASS_THROUGH"}






class FAST_OT_ToggleAllButtons(bpy.types.Operator):
    """Disables all the buttons in FAST PREFERENCES, And as a result on the interface as well."""

    bl_idname = "fast_preferences.toggle_all_buttons"
    bl_label = "Toggle All Buttons"

    def execute(self, context):
        manager = context.preferences.addons[__name__].preferences.Prop
        if manager.Toggle == True:
            manager.fast_save_file_text = False
            manager.show_extras = False
            manager.show_console_text = False
            manager.text_toggle_comment = False
            manager.show_gpt_operator = False
            manager.text_indent = False
            manager.text_unindent = False
            manager.text_cut = False
            manager.text_copy = False
            manager.text_paste = False
            manager.text_select_all = False
            manager.text_print = False
            manager.added_code_operator = False
            manager.edit_user_command = False
            manager.edit_user_instruction_set = False
            manager.autogpt_assistant = False
            manager.fast_bookmarks = False
            manager.adjust_transform_nudge = False
            manager.show_splash_screen = False
            manager.play_timeline_overlays_prop = False
            manager.fast_button = False
            # manager.delete_hierarchy = False
            manager.select_objects = False
            manager.restart_blender_prop = False
            manager.restart_blender_prop_no_save = False
            manager.use_only_selected_keyframe_handles = False
            manager.use_only_selected_curve_keyframes = False
            manager.render_viewport = False
            manager.jump_count = False
            manager.auto_mode = False
            manager.show_buttons = False
            manager.show_panel_buttons = False
            manager.show_preferences = False
            manager.clean_up = False
            manager.enable_pref = False
            manager.new_workspace = False
            manager.fast_menu = False

            manager.set_frame = False
            manager.skip_frames = False
            manager.frame_jump = False
            manager.jump_count_1 = False
            manager.jump_count_5 = False
            manager.jump_count_10 = False
            manager.jump_count_15 = False
            manager.jump_count_all = False
            manager.keyframe_jump = False
            manager.open_keyframe = False
            manager.delete_keyframes = False
            manager.play_timeline = False

            manager.advanced_local_mode = False
            manager.add_camera_at_view = False
            manager.temp_auto_key_frame = False
            manager.toggle_n_panel = False
            manager.show_active = False
            manager.save_and_enter_material_preview_mode = False
            manager.cycle_cameras = False
            manager.set_keying_settings = False
            manager.full_screen = False
            manager.switch_object = False
            manager.switch_edit = False
            manager.switch_pose = False
            manager.switch_sculpt = False
            manager.switch_vertex_paint = False
            manager.switch_weight_paint = False
            manager.switch_texture_paint = False
            manager.show_overlays = False
            manager.toggle_xray = False
            manager.switch_solid = False
            manager.switch_preview = False
            manager.switch_render = False
            manager.toggle_wireframe = False

            manager.undo_redo = False
            manager.set_keys = False
            manager.current_frame = False
            manager.childless_empties = False
            manager.frame_nodes = False
            manager.google_voice_text = False
            manager.google_voice_search = False
            manager.add_audio_video = False
            manager.add_audio_video_t = False
            manager.split_clip = False
            manager.delete_clip = False

            manager.to_timeline_s = False
            manager.to_timeline_ne = False
            manager.to_timeline_ds = False
            manager.to_timeline_ge = False

            manager.to_sequencer_t = False
            manager.to_sequencer_ne = False
            manager.to_sequencer_ds = False
            manager.to_sequencer_ge = False

            manager.to_shader_editor_t = False
            manager.to_shader_editor_s = False
            manager.to_shader_editor_ne = False
            manager.to_shader_editor_ds = False
            manager.to_shader_editor_ge = False

            manager.to_dope_sheet_t = False
            manager.to_dope_sheet_ne = False
            manager.to_dope_sheet_s = False
            manager.to_dope_sheet_ds = False
            manager.to_dope_sheet_ge = False

            manager.to_graph_editor_t = False
            manager.to_graph_editor_ds = False
            manager.to_graph_editor_s = False
            manager.to_graph_editor_ne = False

            manager.empty_func = False
            manager.my_class = False
            manager.diffeomorphic = False
            # manager.save_startup_file = False
            # manager.delete_startup_file = False
            manager.show_console = False
            manager.show_gizmo = False
            manager.fast_panel_addon = False
            manager.fast_panel_animation_1 = False
            manager.fast_panel_animation_2 = False
            manager.fast_panel_append = False
            manager.fast_panel_audio = False
            manager.fast_panel_auto_save = False
            manager.fast_panel_bp = False
            manager.fast_panel_daz_studio_1 = False
            manager.fast_panel_daz_studio_2 = False
            manager.fast_panel_daz_studio_3 = False
            manager.fast_panel_daz_studio_4 = False
            manager.empty_prop = False
            manager.fast_panel_et = False
            manager.fast_panel_google = False
            manager.fast_auto_gpt_panel_main_1 = False
            manager.fast_auto_gpt_panel_main_2 = False
            manager.fast_auto_gpt_panel_main_3 = False
            manager.fast_panel_key = False
            manager.fast_panel_ml = False
            manager.fast_panel_nudge_transform = False
            manager.fast_panel_os = False
            manager.fast_panel_rhubarb = False
            manager.fast_panel_speech_bubble = False
            manager.fast_panel_theme_1 = False
            manager.fast_panel_theme_2 = False
            manager.fast_save_file = False

            manager.Toggle = False

        elif manager.Toggle == False:
            manager.fast_save_file_text = True
            manager.show_extras = True
            manager.show_console_text = True
            manager.text_toggle_comment = True
            manager.show_gpt_operator = True
            manager.text_indent = True
            manager.text_unindent = True
            manager.text_cut = True
            manager.text_copy = True
            manager.text_paste = True
            manager.text_select_all = True
            manager.text_print = True
            manager.added_code_operator = True
            manager.edit_user_command = True
            manager.edit_user_instruction_set = True
            manager.autogpt_assistant = True
            manager.fast_bookmarks = True
            manager.adjust_transform_nudge = True
            manager.show_splash_screen = True
            manager.play_timeline_overlays_prop = True
            manager.fast_button = True
            # manager.delete_hierarchy = True
            manager.select_objects = True
            manager.restart_blender_prop = True
            manager.restart_blender_prop_no_save = True
            manager.use_only_selected_keyframe_handles = True
            manager.use_only_selected_curve_keyframes = True
            manager.render_viewport = True
            manager.jump_count = True
            manager.auto_mode = True
            manager.show_buttons = True
            manager.show_panel_buttons = True
            manager.show_preferences = True
            manager.clean_up = True
            manager.enable_pref = True
            manager.new_workspace = True
            manager.fast_menu = True

            manager.set_frame = True
            manager.skip_frames = True
            manager.frame_jump = True
            manager.jump_count_1 = True
            manager.jump_count_5 = True
            manager.jump_count_10 = True
            manager.jump_count_15 = True
            manager.jump_count_all = True
            manager.keyframe_jump = True
            manager.open_keyframe = True
            manager.delete_keyframes = True
            manager.play_timeline = True

            manager.advanced_local_mode = True
            manager.add_camera_at_view = True
            manager.temp_auto_key_frame = True
            manager.toggle_n_panel = True
            manager.show_active = True
            manager.save_and_enter_material_preview_mode = True
            manager.cycle_cameras = True
            manager.set_keying_settings = True
            manager.full_screen = True
            manager.switch_object = True
            manager.switch_edit = True
            manager.switch_pose = True
            manager.switch_sculpt = True
            manager.switch_vertex_paint = True
            manager.switch_weight_paint = True
            manager.switch_texture_paint = True
            manager.show_overlays = True
            manager.toggle_xray = True
            manager.switch_solid = True
            manager.switch_preview = True
            manager.switch_render = True
            manager.toggle_wireframe = True

            manager.undo_redo = True
            manager.set_keys = True
            manager.current_frame = True
            manager.childless_empties = True
            manager.frame_nodes = True
            manager.google_voice_text = True
            manager.google_voice_search = True
            manager.add_audio_video = True
            manager.add_audio_video_t = True
            manager.split_clip = True
            manager.delete_clip = True

            manager.to_timeline_s = True
            manager.to_timeline_ne = True
            manager.to_timeline_ds = True
            manager.to_timeline_ge = True

            manager.to_sequencer_t = True
            manager.to_sequencer_ne = True
            manager.to_sequencer_ds = True
            manager.to_sequencer_ge = True

            manager.to_shader_editor_t = True
            manager.to_shader_editor_s = True
            manager.to_shader_editor_ne = True
            manager.to_shader_editor_ds = True
            manager.to_shader_editor_ge = True

            manager.to_dope_sheet_t = True
            manager.to_dope_sheet_ne = True
            manager.to_dope_sheet_s = True
            manager.to_dope_sheet_ds = True
            manager.to_dope_sheet_ge = True

            manager.to_graph_editor_t = True
            manager.to_graph_editor_ds = True
            manager.to_graph_editor_s = True
            manager.to_graph_editor_ne = True

            manager.empty_func = True
            manager.my_class = True
            manager.diffeomorphic = True
            # manager.save_startup_file = True
            # manager.delete_startup_file = True
            manager.show_console = True
            manager.show_gizmo = True
            manager.fast_panel_addon = True
            manager.fast_panel_animation_1 = True
            manager.fast_panel_animation_2 = True
            manager.fast_panel_append = True
            manager.fast_panel_audio = True
            manager.fast_panel_auto_save = True
            manager.fast_panel_bp = True
            manager.fast_panel_daz_studio_1 = True
            manager.fast_panel_daz_studio_2 = True
            manager.fast_panel_daz_studio_3 = True
            manager.fast_panel_daz_studio_4 = True
            manager.empty_prop = True
            manager.fast_panel_et = True
            manager.fast_panel_google = True
            manager.fast_auto_gpt_panel_main_1 = True
            manager.fast_auto_gpt_panel_main_2 = True
            manager.fast_auto_gpt_panel_main_3 = True
            manager.fast_panel_key = True
            manager.fast_panel_ml = True
            manager.fast_panel_nudge_transform = True
            manager.fast_panel_os = True
            manager.fast_panel_rhubarb = True
            manager.fast_panel_speech_bubble = True
            manager.fast_panel_theme_1 = True
            manager.fast_panel_theme_2 = True
            manager.fast_save_file = True

            manager.Toggle = True

        # # this sets manager.fast_menu to correct value
        # bpy.ops.fast_operators.toggle_fast_menu()

        if manager.fast_menu:
            for km, kmi in fastmenu_keymaps:
                kmi.active = True
                
        else:
            for km, kmi in fastmenu_keymaps:
                kmi.active = False
                

        bpy.context.preferences.active_section = bpy.context.preferences.active_section

        return {"FINISHED"}

  

class MAC_LINUX_ERROR_OT_notification(bpy.types.Operator):
    bl_idname = "mac_linux.error_notification"
    bl_label = "Mac/Linux Error Notification"
    bl_options = {"REGISTER", "UNDO"}

    message_1: bpy.props.StringProperty(
        default="Sorry, an error occurred while bringing,"
    )
    message_2: bpy.props.StringProperty(
        default="the Blender console to the foreground."
    )
    message_3: bpy.props.StringProperty(
        default="Click REPORT ISSUES, & I'll fix ASAP!!!"
    )

    def execute(self, context):
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=220)

    def draw(self, context):
        layout = self.layout
        box = layout.box()

        row1 = box.row()
        row1.label(text=self.message_1)

        row2 = box.row()
        row2.label(text=self.message_2)

        row3 = box.row()
        row3.label(text=self.message_3)


def count_blender_instances():
    """Counts the number of Blender instances running on the system."""

    if platform.system() == "Windows":
        # Windows-specific implementation
        try:
            process_name = "blender.exe"
            result = subprocess.check_output(["tasklist"], shell=True)
            return result.decode().count(process_name)
        except subprocess.CalledProcessError as e:
            print("Error counting Blender instances on Windows:", e)
            return 0

    elif platform.system() == "Darwin":
        # macOS-specific implementation
        try:
            process_name = "blender"
            result = subprocess.check_output(["ps", "-ax"], universal_newlines=True)
            return result.count(process_name)
        except subprocess.CalledProcessError as e:
            print("Error counting Blender instances on macOS:", e)
            return 0

    elif platform.system() == "Linux":
        # Linux-specific implementation
        try:
            process_name = "blender"
            result = subprocess.check_output(["ps", "-e"], universal_newlines=True)
            return result.count(process_name)
        except subprocess.CalledProcessError as e:
            print("Error counting Blender instances on Linux:", e)
            return 0

    else:
        print("Unsupported platform.")
        return 0


console_window_handle = None
class FAST_OT_show_console_helper(bpy.types.Operator):
    bl_idname = "fast.show_console_helper"
    bl_label = "Show Console Helper"
    bl_description = "Helper to obtain and store the Blender console window handle"

    def execute(self, context):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        scn = bpy.context.scene
        try:


            import re
            
            def check_blender_foreground():
                try:
                    # Get the currently active window
                    active_window = gw.getActiveWindow()
                    if not active_window:
                        print("No active window found.")
                        return False, False, False, None
            
                    # Get the title of the active window
                    window_title = active_window.title
       
            
                    # Match specific Blender or console window patterns
                    blender_console_pattern = re.compile(r'Blender \(\d+\)')
                    is_specific_blender = bool(
                        re.match(r'^Blender 4\.3$', window_title) or
                        blender_console_pattern.search(window_title)
                    )

            
                    # Check for Blender executable and command prompt (cmd.exe)
                    is_blender_exe = "blender.exe" in window_title.lower()
       
            
                    is_cmd_exe = "cmd.exe" in window_title.lower()
           
            
                    # # Return results
                    # Return results
                    # Return results
                    hwnd = active_window.getHandle()
          
                    return is_specific_blender, is_blender_exe, is_cmd_exe, hwnd
            
                except Exception as e:
                    print(f"Error checking foreground window:\n{e}")
                    capture_and_copy_traceback()
                    return False, False, False, None
    
            
    
            #This is the old one I commented this out on May 4th and added the new one with the range 
            # def toggle_console_and_check(original_handle=None):
            #     while True:
            #         bpy.ops.wm.console_toggle()
            #         # time.sleep(0.25)  # Wait for the window to change
            #         is_specific_blender, is_blender_exe, is_cmd_exe, new_handle = check_blender_foreground()
    
            #         # If the original handle is set and a new window with "Blender" appears
            #         if original_handle and (is_specific_blender or is_blender_exe or is_cmd_exe) != original_handle:
            #             return new_handle
    
            #         # If no specific window at startup, find any Blender window
            #         if not original_handle and (is_specific_blender or is_blender_exe or is_cmd_exe):
            #             return new_handle
            def toggle_console_and_check(original_handle=None):
                max_attempts = 10
                for attempt in range(max_attempts):
                    bpy.ops.wm.console_toggle()
                    time.sleep(0.25)  # Optional: Wait for the window to change
                    is_specific_blender, is_blender_exe, is_cmd_exe, new_handle = check_blender_foreground()
                    # If the original handle is set and a new window with "Blender" appears
                    if original_handle and (is_specific_blender or is_blender_exe or is_cmd_exe) != original_handle:
                        return new_handle
    
                    # If no specific window at startup, find any Blender window
                    if not original_handle and (is_specific_blender or is_blender_exe or is_cmd_exe):
                        return new_handle
                # If no console window is found after maximum attempts, report and cancel
                self.report({'INFO'}, "No console window available after multiple attempts.")
                return None
    
    
            is_specific_blender, is_blender_exe, is_cmd_exe, original_handle = check_blender_foreground()
    
            new_handle = None
            if is_specific_blender:
                # If specific Blender window is in the foreground at startup, toggle until new handle found
                new_handle = toggle_console_and_check(original_handle=original_handle)
            else:
                # If no specific Blender window, toggle until any Blender window found
                new_handle = toggle_console_and_check()
    
            if new_handle:

            
                if isinstance(new_handle, int):
                    # Use raw hwnd directly
                    manager.console_window_handle = new_handle
      
                elif hasattr(new_handle, "getHandle"):
                    # Use pywinctl's getHandle method
                    manager.console_window_handle = new_handle.getHandle()
                
                else:
             
                    self.report({'ERROR'}, "New handle is invalid or incompatible.")
                    return {'CANCELLED'}
            else:
  
                self.report({'ERROR'}, "No new window handle found.")
                return {'CANCELLED'}

    
        except Exception as e:
            
            print("")
            self.report({"ERROR"}, f"Error bringing console to foreground:\n")
            capture_and_copy_traceback()
            return {"CANCELLED"}

        return {'FINISHED'}




# Global variable to track initialization
is_initialized = False
#asc
class FAST_OT_show_console(bpy.types.Operator):
    bl_idname = "fast.show_console"
    bl_label = "Show Console"
    bl_description = "Bring Blender console window to foreground"

    def execute(self, context):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        scn = bpy.context.scene
        console_window = 0


        os_type = platform.system()

        if os_type == "Windows":
            pass

        elif os_type == "Darwin" or os_type == "Linux":
            # For macOS and Linux, return a cancellation message
            self.report({'INFO'}, "Sorry, this functionality isn't supported on your operating system currently.")
            self.report({'INFO'}, "Please click 'Report Issues' and request an upgrade or new feature.")
            return {'CANCELLED'}
        else:
            self.report({'ERROR'}, f"Unsupported OS: {os_type}")
            return {'CANCELLED'}



        try:
    
            global is_initialized
            
            # Check if already initialized
            if not is_initialized:
                bpy.ops.fast.show_console_helper()
                is_initialized = True      
            
            manager_handle=int(manager.console_window_handle)
            # print("\n🚀 Console Handle:", manager_handle)

            windows = gw.getAllWindows()

            for win in windows:
                if win._hWnd == manager_handle:
                    console_window = win
                    break

            if console_window:
                # Activate, show, and restore the window
                try:
                    time.sleep(0.1)
                    console_window.activate()
                    console_window.show()
                    console_window.restore()
                    
                except:
                    pass

                ctypes.windll.user32.SetWindowPos(manager_handle, -1, 0, 0, 0, 0, 3)
                
                return {"FINISHED"}
            else:
                print("")
                self.report({"WARNING"}, "Console window not found.")
                return {"CANCELLED"}
  
        except Exception as e:
            capture_and_copy_traceback()
            print("")
            self.report({"ERROR"}, f"Error bringing console to foreground:\n")
            capture_and_copy_traceback()
            return {"CANCELLED"}

        







class FAST_OT_hide_console(bpy.types.Operator):
    bl_idname = "fast.hide_console"
    bl_label = "Hide Blender Console Window"
    bl_description = "Hide the Blender console window"

    def execute(self, context):
        try:
            # Retrieve the handle from the stored value
            manager = bpy.context.preferences.addons[__name__].preferences.Prop
            handle = int(manager.console_window_handle)
            
            # Define constant for the minimize action
            SW_MINIMIZE = 6

            # Minimize the console window
            ctypes.windll.user32.ShowWindow(handle, SW_MINIMIZE)

        except Exception as e:
            capture_and_copy_traceback()

            
            self.report(
                {"ERROR"},
                "An error occurred while trying to hide the console: {}".format(e),
            )
            return {"CANCELLED"}

        return {"FINISHED"}


# UNCOMMENT BEFORE UPLOADING #
def my_download_version_folder(version_folder_url, target_dir):
    try:

        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        scn = bpy.context.scene
        
    except KeyError as e:
        
        return


    try:
        #test
        version_folder_url = "https://fast-blender-add-ons.com/update_version_and_ui_3/"

        cache_buster = str(int(time.time()))
        url_with_cache_buster = f"{version_folder_url}?cb={cache_buster}"
        
        target_file_path = os.path.join(target_dir, "update_version_and_ui_3.zip")
        
        # Start time
        start_time = datetime.now()


        

        
        # Request to download the file
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache'
        }
        try:
            response = requests.get(url_with_cache_buster, headers=headers, stream=True, timeout=2)
            response.raise_for_status() 
            
        except requests.exceptions.Timeout:
            return  
    
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 404:
                print_color("AR", "\nUpdate feature is temporarily offline as we upload latest version.")
                manager.update_available = False
            else:
                print_color("AR", f"\nAn HTTP error occurred: {http_err}")
                capture_and_copy_traceback()
                manager.update_available = False
            return
        except requests.exceptions.RequestException as e:
            print_color("AR", f"\nAn error occurred while downloading updates.\n\nLikely, there is no connection to the internet.\n")
            capture_and_copy_traceback()
            manager.update_available = False
            return
        except zipfile.BadZipFile:
            print_color("AR", "Error: The downloaded file is not a valid zip file.")
            manager.update_available = False
            return
        except Exception as e:
            print_color("AR", f"An unexpected error occurred.")
            capture_and_copy_traceback()
            manager.update_available = False
            return

        # Save the downloaded file
        with open(target_file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Print completion details
        end_time = datetime.now()
      
        duration = (end_time - start_time).total_seconds()
        #print(f"Download completed successfully in {duration:.2f} seconds.")
        #print(f"File saved to: {target_file_path}")



        # Unzip the downloaded file
        with zipfile.ZipFile(target_file_path, 'r') as zip_ref:
            zip_ref.extractall(target_dir)
        #print("Files extracted.")

        # Check for the existence of 'ui.txt'
        ui_text_file = os.path.join(target_dir, "update_version_and_ui_3", "ui.txt")

        if not ui_text_file:
            print("UI text file not found after extraction.")
            manager.update_available = False
            return

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading:\n")
        capture_and_copy_traceback()
        if not manager.internet_connection_printed:
            print_color("AR", "\nAn error occurred while downloading. Please check your Internet connection and try again.")
            show_console_ste()
            
            manager.internet_connection_printed = True
        manager.update_available = False
        return {"CANCELLED"}
    except zipfile.BadZipFile:
        print("Downloaded file is not a valid zip file.\n")
        capture_and_copy_traceback()
        manager.update_available = False
        return {"CANCELLED"}
    except Exception as e:
        print(f"An unexpected error occurred:\n")
        capture_and_copy_traceback()
        manager.update_available = False
        return {"CANCELLED"}
  
    new_target_dir = os.path.join(target_dir, "update_version_and_ui_3")

 

    with open(ui_text_file, "r") as update_info_file:
        manager.fast_update_info = update_info_file.read()


    downloaded_version = get_update_version(new_target_dir)



    if downloaded_version:
        version = get_current_version()

        downloaded_version = downloaded_version.strip()
        version = version.strip()

        if downloaded_version <= version:
         
            manager.fast = 0
            my_redraw()

            if (manager.autogpt_processing != 'Initializing' and 
                manager.autogpt_processing != 'Analyzing' and 
                manager.autogpt_processing != 'Waiting for Input' and
                manager.autogpt_processing != 'SE'):
                print_color("AG", "\nVersion ", new_line=False)
                print_color("AO", downloaded_version, new_line=False)
                print_color("AG", " is current, your up to date!")

            manager.update_available = False
            
        elif downloaded_version > version:

            if (manager.autogpt_processing != 'Initializing' and 
                manager.autogpt_processing != 'Analyzing' and 
                manager.autogpt_processing != 'Waiting for Input'):
                print_color("AW", "\nVersion ", new_line=False)
                print_color("AO", downloaded_version, new_line=False)
                print_color("AW", " update available.")
            manager.downloaded_version = downloaded_version
            manager.update_available = True
            manager.fast = 1
            my_redraw()
    
    manager.fast_prev_version_number = get_previous_version()

    if manager.fast_prev_version_number != "None":
        manager.revert_fast = True
    else:
        manager.revert_fast = False

    manager.fast_target_dir = target_dir
    

    zip_file_path = os.path.join(target_dir, "update_version_and_ui_3.zip")

    if os.path.exists(zip_file_path):

        os.remove(zip_file_path)

    save_user_pref_block_info()










class FAST_OT_check_addon_version_op_1(bpy.types.Operator):
    """Check for latest B.A.I.T.E.P. updates"""

    bl_idname = "fast.check_addon_version_op_1"
    bl_label = "Check Addon Version"
    string: bpy.props.StringProperty(default="")
    wrap: bpy.props.BoolProperty(default=False)
    width: bpy.props.IntProperty(default=183)
    offset_x: bpy.props.IntProperty(default=0)
    offset_y: bpy.props.IntProperty(default=0)

    def execute(self, context):
        
        try:
            bpy.ops.fast.install_fast()
            return {"FINISHED"}
        except Exception as e:
            self.report({"ERROR"}, "Error checking for updates. Details: " + str(e))
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
                manager.update_available = False

    def invoke(self, context, event):
        manager = None

        try:
            try:
                manager = bpy.context.preferences.addons[__name__].preferences.Prop
                scn = bpy.context.scene
            except KeyError as e:
                self.report({"ERROR"}, "Manager or Scene error: " + str(e))
                return {"CANCELLED"}
            # see why this isn't working
            manager.fast = 2
            my_redraw()
            manager.fast_version = get_current_version()
        
            result = fast_connection_checker()
            if not result:
    
                msg = "No Internet connection detected. Could not check for updates."
                print_color("AR", "\n", msg)
                return {'CANCELLED'}

      
            
            manager.download_version_folder_var = False
            manager.fast_prev_version_number = "None"


            target_dir = os.path.join(tempfile.gettempdir(), ".temp")
            if os.path.exists(target_dir):
                shutil.rmtree(target_dir)

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            version_folder_url = None
            thread = threading.Thread(
                target=my_download_version_folder, args=(version_folder_url, target_dir)
            )
            thread.start()
            thread.join()
            
            try:
        
                if manager.update_available:
                    
                        
                    manager = bpy.context.preferences.addons[__name__].preferences.Prop
                    scn = bpy.context.scene
                    for area in context.screen.areas:
              
                        if area.type == "VIEW_3D":
                            
                            for region in area.regions:
                       
                                if region.type == "WINDOW":
                                    
                                    try:
                                        screen_size = pyautogui.size()
                                     
                                    except Exception as e:
                                        return {'CANCELLED'}

            
                                        # If pyautogui is not installed, use the dimensions of the 3D View region
                                        region = [r for r in area.regions if r.type == "WINDOW"][0]
                                        screen_size = type("Size", (object,), {"width": region.width, "height": region.height})()
                                        # Report to the user that pyautogui is not installed
                                        self.report({"INFO"}, "PyAutoGUI is not installed. Defaulting to 3D Viewport size.")
                                        print("Error: ", str(e))
            
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
                                    self.string = f"Version {manager.downloaded_version} is now available!\nClick 'OK' to install it right now!"
                                    
                                    # The message box will now appear where the cursor was warped to
                                    return context.window_manager.invoke_props_dialog(self, width=self.width)
                # else:
                #     pass
            except Exception as e:
                self.report({"ERROR"}, "No update currently available")
                capture_and_copy_traceback()
                return {"CANCELLED"}

                

            manager.download_version_folder_var = True
            
            return {"FINISHED"}

        
        except Exception as e:
            pass

            if manager is not None:
                manager.download_version_folder_var = False
            self.report({"ERROR"}, "Error checking for updates. Details: " + str(e))
            return {"CANCELLED"}



def try_delete_item(item_path, retries=3, delay=1):
    """
    Try to delete a file or directory.

    :param item_path: Path to the file or directory to delete.
    :param retries: Number of times to retry deletion.
    :param delay: Time (in seconds) to wait between retries.
    """
    for attempt in range(retries):
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
                return True
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                return True
        except PermissionError as e:
            print(f"PermissionError while trying to delete {item_path}: {e}")

            # If directory, try deleting files inside individually
            if os.path.isdir(item_path):
                for file_inside in os.listdir(item_path):
                    try_delete_item(os.path.join(item_path, file_inside))
        except Exception as e:
            print(f"Error while trying to delete {item_path}:\n")
            capture_and_copy_traceback()

            

        # If the max number of attempts hasn't been reached, wait and then try again
        if attempt < retries - 1:
            time.sleep(delay)

    print(f"Failed to delete {item_path} after {retries} attempts.")
    return False


def delete_except_lib():
    # Access the manager property
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    # Set the update_in_progress flag to True
    manager.update_in_progress = True

    try:
        # Path to the B.A.I.T.E.P. directory
        fast_dir = os.path.join(bpy.utils.user_resource("SCRIPTS"), "addons", "blender_ai_thats_error_proof")

        # Paths for exclusions
        logs = os.path.join(fast_dir, "logs")

        exclusions = [
            os.path.join(fast_dir, "lib"),
    
            logs,
        ]

        # Check if B.A.I.T.E.P. directory exists
        if not os.path.exists(fast_dir):
            print(f"The B.A.I.T.E.P. directory {fast_dir} does not exist.")
            return

        # Traverse each item in the B.A.I.T.E.P. directory
        for item in os.listdir(fast_dir):
            item_path = os.path.join(fast_dir, item)

            # If the item is a directory and not in exclusions, attempt to delete it
            if os.path.isdir(item_path) and item_path not in exclusions:
                print(f"Attempting to delete directory: {item_path}")
                try_delete_item(item_path)

            # If the item is a file, attempt to delete it
            elif os.path.isfile(item_path):
                print(f"Attempting to delete file: {item_path}")
                try_delete_item(item_path)

    except Exception as e:
        

        print(f"An error occurred during the delete process:\n")
        capture_and_copy_traceback()
    finally:
        
        manager.update_in_progress = False


def backup_to_temp():

    base_path = os.path.join(os.path.expanduser('~'), "Documents", "FAST Settings", "AGPT-4 Examples")
    addon_path = os.path.join(bpy.utils.user_resource("SCRIPTS"), "addons", "blender_ai_thats_error_proof")

    examples_txt_path = os.path.join(base_path, "examples.txt")
    addon_examples_txt_path = os.path.join(base_path, "addon_examples.txt")
    temp_dir = tempfile.gettempdir()
    temp_examples_txt_path = os.path.join(temp_dir, "examples.txt")
    temp_addon_examples_txt_path = os.path.join(temp_dir, "addon_examples.txt")




    # Backup examples.txt
    if os.path.exists(examples_txt_path):
        print_color("AR", "\nexamples.txt", new_line=False)
        print_color("AG", " exists at:\n")
        print_color("AR", f"{examples_txt_path}")
        try:
            shutil.copy2(examples_txt_path, temp_examples_txt_path)
            if os.path.exists(temp_examples_txt_path):
                print_color("AR", "\nexamples.txt", new_line=False)
                print_color("AG", " backed up to:\n")
                print_color("AR", f"{temp_examples_txt_path}")
        except Exception as e:
            capture_and_copy_traceback()
            print_color("AG", "\nFailed to backup ", new_line=False)
            print_color("AR", "examples.txt", new_line=False)
            print_color("AG", ": ")
            print_color("AR", f"{e}")
    else:
        print_color("AR", "\nexamples.txt", new_line=False)
        print_color("AG", " doesn't exist at:\n")
        print_color("AR", f"{examples_txt_path}")

    # Backup addon_examples.txt
    if os.path.exists(addon_examples_txt_path):
        print_color("AR", "\naddon_examples.txt", new_line=False)
        print_color("AG", " exists at:\n")
        print_color("AR", f"{addon_examples_txt_path}")
        try:
            shutil.copy2(addon_examples_txt_path, temp_addon_examples_txt_path)
            if os.path.exists(temp_addon_examples_txt_path):
                print_color("AR", "\naddon_examples.txt", new_line=False)
                print_color("AG", " backed up to:\n")
                print_color("AR", f"{temp_addon_examples_txt_path}")
        except Exception as e:
            capture_and_copy_traceback()
            print_color("AG", "\nFailed to backup ", new_line=False)
            print_color("AR", "addon_examples.txt", new_line=False)
            print_color("AG", ": ")
            print_color("AR", f"{e}")
    else:
        print_color("AR", "\naddon_examples.txt", new_line=False)
        print_color("AG", " doesn't exist at:\n")
        print_color("AR", f"{addon_examples_txt_path}")


            
                

def restore_from_temp():
    
    base_path = os.path.join(os.path.expanduser('~'), "Documents", "FAST Settings", "AGPT-4 Examples")
    addon_path = os.path.join(bpy.utils.user_resource("SCRIPTS"), "addons", "blender_ai_thats_error_proof")

    examples_txt_path = os.path.join(base_path, "examples.txt")
    addon_examples_txt_path = os.path.join(base_path, "addon_examples.txt")

    temp_dir = tempfile.gettempdir()

    temp_examples_txt_path = os.path.join(temp_dir, "examples.txt")
    temp_addon_examples_txt_path = os.path.join(temp_dir, "addon_examples.txt")


   
    

    # Restore examples.txt
    if os.path.exists(temp_examples_txt_path):
        print_color("AR", "\nexamples.txt", new_line=False)
        print_color("AG", " exists at:\n")
        print_color("AR", f"{temp_examples_txt_path}")
        try:
            shutil.copy2(temp_examples_txt_path, examples_txt_path)
            if os.path.exists(examples_txt_path):
                print_color("AR", "\nexamples.txt", new_line=False)
                print_color("AG", " restored to:\n")
                print_color("AR", f"{examples_txt_path}")
        except Exception as e:
            capture_and_copy_traceback()
            print_color("AG", "\nFailed to restore ", new_line=False)
            print_color("AR", "examples.txt", new_line=False)
            print_color("AG", ": ")
            print_color("AR", f"{e}")
    else:
        print_color("AR", "\nexamples.txt", new_line=False)
        print_color("AG", " doesn't exist in the temp directory:\n")
        print_color("AR", f"{temp_examples_txt_path}")

    # Restore addon_examples.txt
    if os.path.exists(temp_addon_examples_txt_path):
        print_color("AR", "\naddon_examples.txt", new_line=False)
        print_color("AG", " exists at:\n")
        print_color("AR", f"{temp_addon_examples_txt_path}")
        try:
            shutil.copy2(temp_addon_examples_txt_path, addon_examples_txt_path)
            if os.path.exists(addon_examples_txt_path):
                print_color("AR", "\naddon_examples.txt", new_line=False)
                print_color("AG", " restored to:\n")
                print_color("AR", f"{addon_examples_txt_path}")
        except Exception as e:
            capture_and_copy_traceback()
            print_color("AG", "\nFailed to restore ", new_line=False)
            print_color("AR", "addon_examples.txt", new_line=False)
            print_color("AG", ": ")
            print_color("AR", f"{e}")
    else:
        print_color("AR", "\naddon_examples.txt", new_line=False)
        print_color("AG", " doesn't exist in the temp directory:\n")
        print_color("AR", f"{temp_addon_examples_txt_path}")

    
    if os.path.exists(temp_examples_txt_path):
        os.remove(temp_examples_txt_path)
    
    if os.path.exists(temp_addon_examples_txt_path):
        os.remove(temp_addon_examples_txt_path)
    



















































# def download_folder_alternative(url, target_dir):
#     try:

#         # Send a request to download the file from the provided URL
#         response = requests.get(url, stream=True)
#         response.raise_for_status()  # Check for any HTTP errors
        
#         # Define the target file path
#         target_file_path = os.path.join(target_dir, "downloaded_file.zip")
        
#         # Write the content to a file
#         with open(target_file_path, 'wb') as file:
#             for chunk in response.iter_content(chunk_size=8192):
#                 if chunk:  # filter out keep-alive new chunks
#                     file.write(chunk)
        

        
#         # # Remove the ZIP file after extraction
#         # os.remove(target_file_path)
#         # print("Download and extraction completed successfully.")
    
#     except Exception as e:
#         print(f"An error occurred: {e}")











































def download_folder_alternative(url, target_dir):
    try:

        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for any HTTP errors
        print_color("AW", "\nRequest successful. Downloading the file in chunks...")

        # Define the target file path
        target_file_path = os.path.join(target_dir, "baitep_uncompiled_version_for_update.zip")
        print_color("AW", f"\nTarget file path:\n\n{target_file_path}\n")
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0

        # Write the content to a file
        with open(target_file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    file.write(chunk)
                    downloaded_size += len(chunk)
                    progress_percentage = (downloaded_size / total_size) * 100 if total_size > 0 else 0
                    
                    print(f"Downloaded {downloaded_size} of {total_size} bytes ({progress_percentage:.2f}% complete)", end='\r', flush=True)



        print(f"\n\nDownload complete. File saved to:\n\n{target_file_path}")
    
    except requests.exceptions.RequestException as e:
        print_color


def backup_addon(addon_path):
    """Backs up the specified add-on directory, excluding the lib folder."""
    print_color("AR", "\nDo you want to make a backup of your current add-on install directory before you start?")
    print_color("AG", "\nThis will exclude the LIB folder to save time.")

    
    while True:
        print_color("AW", "\nProceed with backup? (Y/N): ")
        show_console_ste()
        user_input = getch().strip().upper()

        if user_input == 'Y':  # Check if the response is uppercase 'Y'
            backup_dir = Path(tempfile.gettempdir()) / "BAITEP_backup"
            backup_dir.mkdir(parents=True, exist_ok=True)
            
            for item in Path(addon_path).iterdir():
                if item.name.lower() == 'lib': 
                    continue
                if item.is_dir():
                    shutil.copytree(item, backup_dir / item.name, dirs_exist_ok=True)
                else:
                    shutil.copy2(item, backup_dir / item.name)
            print_color("AG", f"\nBackup completed successfully to {backup_dir}")
            break  # Exit the loop after successful operation
        elif user_input == 'N':
            print_color("AR", "\nBackup skipped by the user.")
            break  # Exit the loop if user chooses not to back up
        else:
            print_color("AR", "\nWrong input. Please try again. Enter 'Y' for yes or 'N' for no.")

def check_disk_space():
    try:
        import psutil
    except ModuleNotFoundError:
        print_color("AR", "\npsutil module not found. Please install dependencies in Preferences.")
        return True

    # Check available disk space on the root directory
    disk_space = psutil.disk_usage('/').free  # Change '/' to any other directory if needed

    # Set the threshold to 10 gigabytes (10 * 1024 * 1024 * 1024 bytes)
    threshold = 1.35 * 1024 * 1024 * 1024  # 10 GB
    # Print out the available disk space and the threshold for debugging purposes
    print_color("AG", f"\nAvailable disk space: {disk_space / (1024 * 1024 * 1024):.2f} GB")
    print_color("AR", f"\nRequired disk space: {threshold / (1024 * 1024 * 1024):.2f} GB")
    
    # Check if there is enough space, else cancel
    if disk_space < threshold:
        print_color("AR", "\nInsufficient disk space. You need at least 1.35GB of free space.")
        print_color("AG", "\nPlease free up some space and restart Blender to try again.")
        return False
    
    return True
    
# Function to save a file in the temp directory
def save_temp_file():
    temp_dir = tempfile.gettempdir()  # Get the temp directory
    temp_file_path = os.path.join(temp_dir, "restart_trigger.tmp")
    
    # Create an empty file
    with open(temp_file_path, "w") as f:
        pass  # We don't need to write any data, just create the file
    
    return temp_file_path

# Function to check if the temp file exists
def check_temp_file():
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, "restart_trigger.tmp")
    
    return os.path.exists(temp_file_path)

    
def execute_func():

    manager = bpy.context.preferences.addons[__name__].preferences.Prop

    try:
        time.sleep(3)
        print_color("AW", "\nBlender is usable while installing.")

        
        if not check_disk_space():
            return None
        
        # # Replace the input statement with print_color and getch_input
        # print_color("AW", "\nAre you sure you want to proceed? (Y/N): ")
        # response = getch().strip().upper()
        
        # # Check the user's response with uppercase check
        # if response == 'Y':  # Uppercase check
        #     pass  # Do nothing if the response is 'Y'
        # elif response == 'N':  # Check if the user pressed 'N'
        #     print_color("AR", "\nOperation cancelled by the user.")  # Print a line if the response is 'N'
        # else:
        #     print_color("AR", "\nInvalid input. Please enter 'Y' for Yes or 'N' for No.")



        version_folder_url = "https://fast-blender-add-ons.com/wp-content/uploads/baitep_uncompiled_version_for_update.zip"
        target_dir = os.path.join(tempfile.gettempdir(), ".temp")

        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)
        os.makedirs(target_dir)
    
        # os.makedirs(target_dir, exist_ok=True)

        try:
            import gdown

            addon_dir = os.path.join(bpy.utils.user_resource("SCRIPTS"), "addons")
            fast_dir = os.path.join(addon_dir, "blender_ai_thats_error_proof")
            backup_addon(fast_dir)

            backup_to_temp()

            print_color("AR", "\nCommencing the B.A.I.T.E.P. update process, progress is shown in the console.", new_line=True)
            print_color("AR", "\nIn case of an interruption, restart Blender and re-initiate the update.", new_line=True)

            download_folder_alternative(version_folder_url, target_dir)

            print_color("AG", "\nVersion folder has been downloaded.\n")
        except ImportError:
            pass
        except Exception as e:
            capture_and_copy_traceback()

            print_color("AR", f"An error occurred while downloading: {e}")

        if manager.fast == 1:
            # Set the prev_version_dir path inside the Documents folder
            prev_version_dir = documents_dir / "baitep_prev_version"
            if os.path.exists(prev_version_dir):
                shutil.rmtree(prev_version_dir)
            os.makedirs(prev_version_dir, exist_ok=True)

            # Create a ZipFile object
            current_version = get_current_version()
            # print_color("AW", current_version, type(current_version))
            current_version = current_version.replace(".", "_")
            final_zip_path = os.path.join(
                prev_version_dir, f"baitep_prev_version_{current_version}.zip"
            )

            fast_zip_path = os.path.join(
                fast_dir, f"baitep_prev_version_{current_version}.zip"
            )
            # Get the Blender version string
            blender_version = bpy.app.version_string[
                :3
            ]  # Extracting the first three characters for the Blender version

            if sys.platform == "win32":
                before_scripts_dir = os.path.join(
                    os.getenv("APPDATA"),
                    "Blender Foundation",
                    "Blender",
                    blender_version,
                )
            elif sys.platform == "darwin":  # For macOS
                before_scripts_dir = os.path.join(
                    os.path.expanduser("~"),
                    "Library",
                    "Application Support",
                    "Blender",
                    blender_version,
                )
            else:
                before_scripts_dir = os.path.join(
                    os.path.expanduser("~"), ".config", "blender", blender_version
                )

            # Delete existing zip file in prev_version_dir if it exists
            if os.path.exists(final_zip_path):
                os.remove(final_zip_path)
            if os.path.exists(fast_zip_path):
                os.remove(fast_zip_path)
            pycache_dir = os.path.join(fast_dir, "__pycache__")
            if os.path.exists(pycache_dir):
                shutil.rmtree(pycache_dir)
            with zipfile.ZipFile(final_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                # Zip the files from directory
                total_files = sum([len(files) for r, d, files in os.walk(fast_dir)])
                print_color("AW", "Total files: ", total_files)  # print out total files

                for foldername, subfolders, filenames in os.walk(fast_dir):
                    for filename in filenames:
                        # Create the complete filepath of the file in directory
                        filePath = os.path.join(foldername, filename)
                        file_path_components = filePath.split(os.sep)
                        if "lib" in file_path_components or "lib2" in file_path_components or "lib3" in file_path_components:
            
                            continue

                        # Add file to zip
                        try:
                            zipf.write(
                                filePath, os.path.relpath(filePath, fast_dir)
                            )
                        except FileNotFoundError:
                            print_color("AR", f"File not found: {filePath}. Skipping...")
                            continue
                        relative_path = os.path.relpath(
                            filePath, start=before_scripts_dir
                        )
                        print_color("AW", f"Zipping: {relative_path}")

                zipf.close()  # ensure the file is closed
                time.sleep(1)  # not generally recommended, but can sometimes help

                if os.path.exists(final_zip_path):
                    manager.fast_prev_version_number = get_previous_version()
                    

            # Save the version of the current Blender
            current_version_number = get_current_version()

            print_color("AW", f"\nCurrent B.A.I.T.E.P. add-on version: {current_version_number}")
            print_color("AW", f"\nPrevious B.A.I.T.E.P. add-on version: {manager.fast_prev_version_number}")

            
            print_color("AW", "")

            # Use glob to directly get the zip files matching the naming convention
            zip_files = glob.glob(os.path.join(target_dir, "baitep_uncompiled_version_for_update.zip"))

            # If you just want the first match (assuming there's only one zip file following this convention):
            if zip_files:
                latest_zip_file = zip_files[0]
            else:
                # Handle the case where no matching .zip files were found
                print_color("AR", "No .zip files were found.")
                return None

            print_color("AW", "zip_files:", zip_files, "\n")
            print_color("AW", "latest_zip_file:", latest_zip_file, "\n")
            if not latest_zip_file:
                print_color("AR", "No .zip files were found.")
                return None

            # Move the first .zip file found to the add-on directory
            shutil.copy(latest_zip_file, os.path.join(addon_dir, "baitep.zip"))

            downloaded_file_path = os.path.join(addon_dir, "baitep.zip")
            print_color("AW", "Update file moved:\n", downloaded_file_path)

            if not os.path.exists(downloaded_file_path):
                print_color("AR", f"Error: The file {downloaded_file_path} does not exist.")
                return None

            try:
                install_fast("baitep.zip")
                remove_file("baitep.zip")
                # print_color("AW", "manager.fast:", manager.fast)
                # shutil.rmtree(target_dir)
            except Exception as e:
                

                print_color("AR", f"Error during B.A.I.T.E.P. installation:\n")
                capture_and_copy_traceback()

                manager.fast = 1
                my_redraw()
                return None
        else:
            print_color("AW", "\nB.A.I.T.E.P. is up to date.")

        return None
    except Exception as e:
        capture_and_copy_traceback()

        print_color("AR", traceback.format_exc())  # Print traceback information
 
        return None

def install_fast(filename):
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    print_color("AW", "\nInstalling B.A.I.T.E.P.!!...\n")
    addon_dir = os.path.join(bpy.utils.user_resource("SCRIPTS"), "addons")

    # List of directories to remove
    dirs_to_remove = [
        os.path.join(addon_dir, "blender_ai_thats_error_proof", "icons"),  # Add any future folders here
    ]

    print_color("AW", 
        "Directories to remove:\n", dirs_to_remove
    )  # Print the list of directories

    # Remove directories in dirs_to_remove if they exist
    for dir_to_remove in dirs_to_remove:
        print_color("AW", 
            f"\nChecking directory:\n{dir_to_remove}"
        )  # Print the directory being checked
        if os.path.exists(dir_to_remove):
            print_color("AW", 
                f"\nDirectory exists:\n{dir_to_remove}"
            )  # Print if the directory exists
            try:
                shutil.rmtree(dir_to_remove)
                print_color("AW", f"\nRemoved directory:\n{dir_to_remove}"
                )  # Print if the directory was removed successfully
            except Exception as e:
                capture_and_copy_traceback()

                print_color("AR", f"\nError while removing directory:\n{dir_to_remove}"
                )  # Print if there was an error
                print_color("AR", traceback.format_exc())  # Print traceback information
        else:
            print_color("AR", f"\nDirectory does not exist:\n{dir_to_remove}"
            )  # Print if the directory does not exist

    delete_except_lib()

    addon_path = os.path.join(addon_dir, filename)
    with zipfile.ZipFile(addon_path, "r") as zip_ref:
        zip_ref.extractall(addon_dir)
        copy_failed = True # Flag for failed copy

        # Set this to the path just before "scripts"
        blender_version = bpy.app.version_string[
            :3
        ]  # Extracting the first three characters for the Blender version
       


        if sys.platform == "win32":
            before_scripts_dir = os.path.join(
                os.getenv("APPDATA"),
                "Blender Foundation",
                "Blender",
                blender_version,
            )
        elif sys.platform == "darwin":  # For macOS
            before_scripts_dir = os.path.join(
                os.path.expanduser("~"),
                "Library",
                "Application Support",
                "Blender",
                blender_version,
            )
        else:
            before_scripts_dir = os.path.join(
                os.path.expanduser("~"), ".config", "blender", blender_version
            )

        for file in zip_ref.namelist():
            target_path = os.path.join(addon_dir, file)
            if os.path.exists(target_path):
                relative_path = os.path.relpath(
                    target_path, start=before_scripts_dir
                )
                print_color("AW", f"{relative_path}\n")
                manager.fast = 0
                manager.revert_fast = True
                my_redraw()
            else:
                print_color("AR", f"Failed to copy: {target_path}")
                manager.fast = 1
                manager.revert_fast = False
                
                my_redraw()

                copy_failed = False  # Set flag to True if copy failed

        if copy_failed:
            restore_from_temp()
            print_color("AR", "\nAddon installed successfully...")
            print_color("AB", "\nNote: Only tested on Blender 4.3...")
            print_color("AR", "\nPlease restart Blender manually.")
            print_color("AG", "\nManual restart is necc. so Blender's usable during updating.")
            print_color("AG", "\nWe will re-add automatic restart soon.")
            # Just throw a conditional and save preferences so when a property your property is ticked it runs the restart operation and sets it to false didn't add it now so we could test it a few times 
                        

        
        

class FAST_OT_install_fast(bpy.types.Operator):
    """Installs the latest B.A.I.T.E.P. update"""
    bl_idname = "fast.install_fast"
    bl_label = "Install/Uninstall B.A.I.T.E.P."

    def execute(self, context):
        global is_update_finished
        show_console_ste()

        thread = threading.Thread(target=execute_func)
        thread.start()  # Start the thread

            
        return {"FINISHED"}











class FAST_OT_delete_pip_cache(bpy.types.Operator):
    """Deletes the PIP cache folder.\n\nIf installing dependencies fails for any reason,\n\nclick this button, and try again"""

    bl_idname = "fast.delete_pip_cache"
    bl_label = "Delete PIP Cache"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        # Determine the cache path based on OS
        if os.name == "nt":  # Windows
            cache_path = os.path.join(
                os.path.expanduser("~"), "AppData", "Local", "pip", "Cache"
            )
        else:  # macOS and Linux
            cache_path = os.path.join(os.path.expanduser("~"), ".cache", "pip")

        # Check if the cache path exists, and if it does, remove it
        if os.path.exists(cache_path):
            shutil.rmtree(cache_path)
            self.report({"INFO"}, "PIP Cache deleted successfully!")

        else:
            self.report({"WARNING"}, "PIP Cache directory not found!")

        return {"FINISHED"}






# Define a dictionary to map color names to color codes
color_codes = {
    "black": "\x1b[30m",
    "red": "\x1b[31m",
    "green": "\x1b[32m",
    "yellow": "\x1b[33m",
    "blue": "\x1b[34m",
    "magenta": "\x1b[35m",
    "cyan": "\x1b[36m",
    "white": "\x1b[37m",
    "reset": "\x1b[0m",
}


libraries = [
    ("requests", "requests", ""),
    ("pyperclip", "pyperclip", ""),
    ("pyautogui", "PyAutoGUI", ""),
    ("psutil", "psutil", ""), 
    ("openai", "openai", ""),
    ("bs4", "beautifulsoup4", ""),  # for bs4 (BeautifulSoup)
    ("tiktoken", "tiktoken", ""),
    ("speech_recognition", "SpeechRecognition", ""),  # for speech_recognition
    ("pygments", "pygments", ""),
    ("aiohttp", "aiohttp", ""),
    ("ffmpeg", "ffmpeg", ""),
    ("pydub", "pydub", ""),
    ("pytube", "pytube", ""),
    ("youtube_transcript_api", "youtube-transcript-api", ""),
    ("PIL", "pillow", ""),  # Added
    ("pywinctl", "pywinctl", ""),  # Added
    ("dateutil", "python-dateutil", ""),  # Added
    ("pydantic", "pydantic", ""),  # Added
    ("instructor", "instructor", ""),  # Added

]

# Windows-specific packages
if platform.system() == "Windows":
    libraries.extend([
        ("pyaudio", "pyaudio", ""),
        ("pywin32", "pywin32", ""),
        ("pypiwin32", "pypiwin32", ""),
        ("pywinctl", "pywinctl", ""),

    ])

# Mac-specific packages
elif platform.system() == "Darwin":
    libraries.extend([
        ("pywinctl", "pywinctl", "")
    ])

# Linux-specific packages
elif platform.system() == "Linux":
    libraries.extend([
        ("pywinctl", "pywinctl", "")
    ])

available_libraries = [lib[0] for lib in libraries]
available_libraries_str = "\n     - ".join(available_libraries)





def get_package_metadata(package_name, pip_name, target_directory):
    start_time = time.time()  # Start time

    def read_metadata_from_dist_info(dist_info_dir):
        metadata = {}
        metadata_file = os.path.join(dist_info_dir, "METADATA")

        with open(metadata_file, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    if ": " in line:
                        key, value = line.strip().split(": ", 1)
                        metadata[key] = value
                    else:
                        metadata[line.strip()] = None
                except:
                    pass
        return metadata

    try:
        backup_path = sys.path

        sys.path = []
        sys.path.append(target_directory)

        try:
            sys.path.append(os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages", "win32"))
            sys.path.append(os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages", "win32", "lib"))
            sys.path.append(os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages", "pywin32_system32"))

        except Exception as e:
            capture_and_copy_traceback()
            print(f"Error adding pywin32 paths to sys.path: {e}")

        # Original library dictionary
        names = [
            # ("cv2", "opencv-python", "opencv_python"),
            ("youtube_transcript_api", "youtube-transcript-api", "youtube_transcript_api"),
            ("googlesearch", "googlesearch-python", "googlesearch_python"),
            ("github", "PyGithub", "PyGithub"),
            ("PIL", "pillow", "Pillow"),
            # ("pyaudio", "pyaudio", "PyAudio"),  # Conditional addition handled below
            ("pywinctl", "pywinctl", "PyWinCtl"),
            ("pygments[windows-terminal]", "pygments", "pygments"),
            # ("chromedriver_autoinstaller", "chromedriver-autoinstaller", "chromedriver-autoinstaller"),
        ]
        
        # Adding pyaudio conditionally for Linux or Windows platforms
        if platform.system() in ["Linux", "Windows"]:
            names.append(("pyaudio", "pyaudio", "PyAudio"))

        for name_tuple in names:
            if name_tuple[0] == package_name:
                dist_info_name = name_tuple[2] + "-"
                break
        else:
            dist_info_name = pip_name + "-"

        try:
            for item in os.listdir(target_directory):
                if dist_info_name in item and "dist-info" in item:
                    dist_info_dir = os.path.join(target_directory, item)
                    data = read_metadata_from_dist_info(dist_info_dir)
                    package_found = True
            if data:
                metadata = {
                    "Name": data.get("Name"),
                    "Version": data.get("Version"),
                    "Location": target_directory,
                }
        except:
            package_found = False

        if package_name in sys.modules:
            pass
        else:
            if package_name in ["pywin32", "pypiwin32", "pywinctl"]:
                # Existing Windows-specific logic remains unchanged
                if platform.system() == "Windows":
                    
                    new_test_name = "win32con"
                    package = __import__(new_test_name)
                
                
                # Linux-specific setup
                elif platform.system() == "Linux":
                    try:
                        import pywinctl
                
                    except Exception as e:
                        if package_name in ["pywinctl"]:
                            pass
                
                # macOS-specific setup
                elif platform.system() == "Darwin":
                    try:
                        import pywinctl
                
                    except Exception as e:
                        
                        pass
                
                else:
                    print(f"Unsupported platform: {platform.system()}")
            else:
                try:
                    sys.path = [target_directory]
                    package = __import__(package_name)

                except AttributeError as e:
                    if "'polars' has no attribute '_cpu_check'" in str(e):
                        # Handle the specific error, e.g., log it or notify the user
                        print("Polars module is not properly initialized.\nThis happens when we update OpenAI due to interrelated dependencies.\nIt is not an issue.")
                    else:
                        # Re-raise the exception if it's not the expected one
                        raise
                
                except:
                    sys.path = main_sys_paths
                    package = __import__(package_name)
              

            try:
                package_location = inspect.getfile(package)
            except:
                package_location = None

        try:
            if not metadata:
                metadata = {
                    "Name": str(package_name),
                    "Version": getattr(package, "__version__", ""),
                    "Location": package_location,
                }
        except:
            metadata = None

        sys.path = backup_path

        return metadata, package_found

    except ImportError as e:
        # print_color("AR", f"\nGet package metadata error:")
        # traceback.print_exc()
        return None, None
    

    except Exception as e:
        if "sqlite3" in str(e):
            print("LanceDB issue: Missing 'sqlite3' module, likely a shared dependency error.")
            return None, None
        elif "'polars' has no attribute '_cpu_check'" in str(e):
            print("Polars issue: '_cpu_check' error detected, likely due to shared dependency conflicts.")
            return None, None
        elif 'pygments' in str(e) and pip_name == "icecream":
            print_color("AR", "\nNote: Icecream uses the pygments library, so it is looking for pygments also.")
        else:
            print_color("AR", f"ERROR: {str(e)}")
            traceback.print_exc()
        return None, None

    finally:
        sys.path = backup_path

        end_time = time.time()  # End time
        total_time = end_time - start_time  # Calculate total time
  
tensorflow_flag = False

def import_special(lib_name):
    """
    Import a library from a specific 'lib' directory, ensuring it does not 
    import from any other location. Restores sys.path after the import.
    If an error occurs, it raises the exception to the calling function.
    """
    lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
    original_sys_path = sys.path.copy()  # Backup the current sys.path

    try:
        # Clear sys.path and append only the lib_path
        sys.path.clear()
        sys.path.append(lib_path)
        
        # # Dynamically import the library
        # print(f"Attempting to import {lib_name} from {lib_path}...")
        imported_lib = __import__(lib_name)
        # print(f"Successfully imported {lib_name} from {imported_lib.__file__}")
        
        # Return the imported library for use
        return imported_lib
    except Exception as e:
        # # Make the error loud and clear
        # print(f"Error occurred while importing {lib_name}: {e}")
        raise  # Raise the exception to the caller
    finally:
        # Restore the original sys.path
        sys.path = original_sys_path

import site
import sys

def print_site_packages_info():
    print("Standard site-packages paths:")
    for path in site.getsitepackages():
        print(f"  {path}")

    print("\nUser site-packages path:")
    print(f"  {site.getusersitepackages()}")

    print("\nCurrent sys.path entries:")
    for path in sys.path:
        print(f"  {path}")


# This is a duplicate of the one from the INIT file it's gotta be here because otherwise we risk a circular import to get it here

def check_for_updates():

    try:
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
    except:
        return

    if manager.tfe_startup_check_counter >= 1:  # Check on every startup it's fast because we're using the website for download
        try:
            manager.tfe_startup_check_counter = 0  
            
            # bpy.ops.fast.check_addon_version_op_1("INVOKE_DEFAULT", string=msg)
    
            bpy.ops.fast.check_addon_version_op_1("INVOKE_DEFAULT")
    
        except Exception as e:
            capture_and_copy_traceback()
    else:
        manager.tfe_startup_check_counter += 1

def reset_timer(new_interval):
    """Deregister the current timer and register a new one with a different interval."""
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    current_time = time.time()

    # Check if less than 10 seconds have passed since the start time
    if current_time - manager.timer_start_time < 10.0:
        # Check if the timer is registered
        if bpy.app.timers.is_registered(check_for_updates):
            bpy.app.timers.unregister(check_for_updates)  # Unregister the timer
            if not bpy.app.timers.is_registered(check_for_updates):
                bpy.app.timers.register(check_for_updates, first_interval=new_interval)
            # print(f"Timer reset to {new_interval} seconds.")
        # else:
            # print("Timer 'check_for_updates' is not currently registered.")

    # else:
        # print("Timer reset skipped; less than 10 seconds since the last reset.")

    # Update the timer start time
    manager.timer_start_time = current_time




not_installed_libraries = []

async def fetch_latest_openai_version():
    
    """Asynchronously fetch the latest OpenAI version using aiohttp."""
    if aiohttp is None:
        if os.path.exists(os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")):
            print_color("AR", f"\nThe aiohttp library is not installed. Please restart Blender to initiate install of it.")
        return None
    try:
        url = "https://pypi.org/pypi/openai/json"
        timeout = aiohttp.ClientTimeout(total=2)  # Set a 10-second timeout
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['info']['version']
                else:
                    return None
    except (aiohttp.ClientError, asyncio.TimeoutError) as e:
        print_color("AR", f"\nFailed to retrieve latest OpenAI version from website.")
        return None

async def check_and_update_openai():
    """Checks for OpenAI package updates and cleans up old installations if an update is needed."""
    lib_folder = os.path.join(os.path.dirname(__file__), "lib", 'Python311', 'site-packages')

    openai_path = os.path.join(lib_folder, 'openai')
    dist_info_paths = glob.glob(os.path.join(lib_folder, 'openai-*.dist-info'))
    latest_version = None
    global not_installed_libraries

    try:
        import importlib.metadata
        current_version = importlib.metadata.version('openai')
    except importlib.metadata.PackageNotFoundError:
        current_version = None

    try:
        latest_version = await fetch_latest_openai_version()
    except Exception as e:
        capture_and_copy_traceback()
        pass

    if latest_version and current_version != latest_version:
        # print(f"\n🚀 current_version: {current_version}")
        # print(f"\n🚀 latest_version: {latest_version}")
   
        if os.path.exists(openai_path) or any(os.path.exists(p) for p in dist_info_paths):
            print(f"\nUpdating OpenAI from version {current_version} to {latest_version}")
            if os.path.exists(openai_path):
                shutil.rmtree(openai_path, ignore_errors=True)
                print(f"\nRemoved directory: {openai_path}")
            for path in dist_info_paths:
                if os.path.exists(path):
                    shutil.rmtree(path, ignore_errors=True)
                    print(f"\nRemoved directory: {path}")
            print("\nOld version of OpenAI removed.")

            if not_installed_libraries is None:  # Reinitialize if it was cleared
                not_installed_libraries = []

            not_installed_libraries.append(("openai", "openai", ""))  # Add OpenAI directly to list
       
        else:
            print_color("AR", f"\nNo OpenAI directories found.")
    elif latest_version == current_version:
        print_color("AG", "\nOpenAI is up-to-date.")

    return not_installed_libraries


# Global variable to control Keras import status
keras_imported = False

def test_libraries():
    
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
   

    import os
    folder_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
    lib_folder = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")  # Path to lib folder


    global libraries
    global not_installed_libraries
    global keras_imported


    if not_installed_libraries is None:
        not_installed_libraries = []
    original_sys_path = None

    original_sys_path = sys.path
    sys.path = []
    sys.path.append(folder_path)


    def print_successful_import(lib, pip_name, version):
        if pip_name:
            # print(f"\n🚀 pip_name: {pip_name}")
            print_color("AW", "Successfully imported ", new_line=False)
            # time.sleep(0.01)  # Small delay
            print_color("AB", pip_name, new_line=False)
            # time.sleep(0.01)  # Small delay
            if version:
                print_color("AR", f" {version}", new_line=False)
                # time.sleep(0.01)  # Small delay
            
            print_color("AW", "!")
   
 
    # if manager.restarting_blender:
        
        # manager.restarting_blender = False
        # save_user_pref_block_info()
        # print("\nRestarting Blender so skipping testing libraries.")
        # # Can't do this you have to put another conditional somewhere because this block testing libraries and the standard time. I bet it's something to do with restart after install while you put this in here so just add one of those restart after startup conditionals
        # return

    for lib, pip_name, version in libraries:


  

        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        manager.block_save_pref = True



        # if lib == "kivy":
        #     try:
        #         import logging
        #         logging.basicConfig(level=logging.CRITICAL)
                
        #         # Set specific modules to a lower log level
        #         logging.getLogger('kivy').setLevel(logging.CRITICAL)
        #         logging.getLogger('urllib3').setLevel(logging.CRITICAL)
        #         logging.getLogger('trimesh').setLevel(logging.CRITICAL)
                
        #         # import getopt
        #         # from kivy.app import App
        #         # from kivy.uix.button import Button

        #         print_successful_import(lib, pip_name, version)
        #     except ImportError as e:
        #         print_color("AR", "Failed to import ", new_line=False)
        #         print_color("AG", pip_name, "...")
        #         not_installed_libraries.append((lib, pip_name, version))
        #         capture_and_copy_traceback()
        #     continue


  
        try:
            if lib == "phidata":
                try:
                    from phi.assistant import Assistant
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue

            # if lib == "whisper-mic":
            #     try:
            #         from whisper_mic import WhisperMic
            #         print_successful_import(lib, pip_name, version)
            #     except ImportError as e:
            #         print_color("AR", "Failed to import ", new_line=False)
            #         print_color("AG", pip_name, "...")
            #         not_installed_libraries.append((lib, pip_name, version))
            #         traceback.print_exc()
            #     continue

            elif lib == "chromedriver-autoinstaller":
                # try:
                #     import chromedriver_autoinstaller
                #     print_successful_import(lib, pip_name, version)
                # except ImportError as e:
                #     print_color("AR", "Failed to import ", new_line=False)
                #     print_color("AG", pip_name, "...")
                #     not_installed_libraries.append((lib, pip_name, version))
                continue

                
            elif lib == "tf-keras":
         
                try:
                    if manager.test_tensorflow:
                        keras_path = os.path.join(
                            bpy.utils.user_resource('SCRIPTS'), 
                            'addons', 
                            'FAST', 
                            'lib', 
                            'Python311', 
                            'site-packages', 
                            'tf_keras'
                        )
                        
                        if not os.path.exists(keras_path):
                            print_color("AR", "Failed to import ", new_line=False)
                            print_color("AG", pip_name, "...")
                            not_installed_libraries.append((lib, pip_name, version))
        
                        else:
                            print_successful_import(lib, pip_name, version)
                    else:
                        print_color("AG", "Not testing 'TF-KERAS' as 'Test Tensorflow' is not enabled.")
                except ImportError as e:
                    traceback.print_exc()
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
                
            
            
            elif lib == "tensorflow":
             
                try:
                    if manager.test_tensorflow:

                  
                        keras_path = os.path.join("lib", "Python311", "site-packages", "tf_keras")
    
                        if os.path.exists(keras_path):
                            os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress INFO & WARNING
                            os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Suppress oneDNN warnings
                            os.environ['TF_USE_LEGACY_KERAS'] = '1'  # Ensure compatibility mode
                            warnings.filterwarnings("ignore", category=UserWarning, module="tf_keras")

                        import tensorflow as tf 
    
                        print_successful_import(lib, pip_name, version)
        
                    else:
                        print_color("AG", "Not testing 'TensorFlow' as 'Test Tensorflow' is not enabled.")            
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue

            
            # elif lib == "torch" and platform.system() == "Windows":
            #     # Backup original sys.path and limit to lib3 for importing
            #     lib_path = os.path.join(os.path.dirname(__file__), "lib3")
            #     original_sys_path = sys.path.copy()
            #     sys.path.clear()
            #     sys.path.append(lib_path)
               
            
            #     try:
            #         import Cython
            #         import torch
            #         print("✅ Torch imported successfully!")
            
            #     except ImportError as e:
            #         # pass
            #         print_color("AR", "Failed to import ", new_line=False)
            #         print_color("AG", pip_name, "...")
            #         not_installed_libraries.append((lib, pip_name, version))
            
            #     finally:
            #         # Restore sys.path back to original state
            #         sys.path.clear()
            #         sys.path.extend(original_sys_path)
            #         print("🔧 sys.path restored after import attempt.")
            
           

            elif lib == "transformers":
                try:
                    if manager.test_tensorflow:
                        import transformers
                        warnings.filterwarnings(
                            "ignore",
                            message="None of PyTorch, TensorFlow >= 2.0, or Flax have been found.*",
                            category=UserWarning,
                            module="transformers"
                        )
                        print_successful_import(lib, pip_name, version)
                    else:
                        print_color("AG", "Not testing 'Transformers' as 'Test Tensorflow' is not enabled.")
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
            
                continue


            elif lib == "pydub":
                try:
                    
                    warnings.filterwarnings("ignore", category=RuntimeWarning, module="pydub.utils")
                    import pydub
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue

            
            elif lib == "PyGithub":
                try:
                    from github import Github
              
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue  

            
            elif lib == "moviepy":
                try:
                    import moviepy
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                 
                continue
   
            
            elif lib == "pasta":
                try:
                    import pasta
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))

                continue

            elif lib == "ast_scope":
                try:
                    import ast_scope
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))

                continue
            elif lib == "PIL":
                try:
                    import PIL
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append(("PIL", "pillow", ""))
                continue
            elif lib == "azure-cognitiveservices-speech":
                try:
                    import azure.cognitiveservices.speech as speechsdk
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue      
            elif lib == "youtube-search-python":
                try:
                    from youtubesearchpython import VideosSearch
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:

                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
            

            elif lib == "googlesearch-python":
                try:
                    from googlesearch import search
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue


            elif lib == "youtube_dl":
                try:
                    import youtube_dl
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue

            elif lib == "send2trash":
                try:
                    from send2trash import send2trash
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                 
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
            
                    # Append the library to the not_installed_libraries list
                    not_installed_libraries.append((lib, pip_name, version))
    
                continue

            elif lib == "fitz":
                try:
                    import fitz
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue

            elif lib == "pygments[windows-terminal]":
                try:
                    import pygments
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue

            elif lib == "pydrive":
                try:
                    from pydrive.auth import GoogleAuth
                    from pydrive.drive import GoogleDrive
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue

            elif lib == "bs4":
                try:
                    from bs4 import BeautifulSoup
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "cv2":
                try:

                    import_special("cv2")

                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue

  
            elif lib == "ffmpeg":
                
                
                
                if platform.system() == "Darwin":  # macOS
                    path_to_ffmpeg = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages", "ffmpeg")
                elif platform.system() == "Linux":
                    path_to_ffmpeg = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages", "ffmpeg")
                elif platform.system() == "Windows":
                    path_to_ffmpeg = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages", "ffmpeg.exe")
           
                else:
                    print_color("AR", "Unsupported Operating System Detected!")
                    traceback.print_exc()
                    not_installed_libraries.append((lib, pip_name, version))
                    continue
            
                # Check if the path exists and is a file
                if os.path.exists(path_to_ffmpeg):
                    
                    print_successful_import(lib, pip_name, version)
                else:
                    
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
            
    
            elif lib == "gdown":
                try:
                    from gdown import download
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "psutil":
                try:
                    from psutil import cpu_percent
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "pyaudio" and platform.system() in ["Linux", "Windows"]:
                try:
                    from pyaudio import PyAudio
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
            
    
            elif lib == "pyautogui":
                try:
                    from pyautogui import moveTo
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "pyperclip":
                try:
                    import pyperclip
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
  
            elif lib == "speech_recognition":
                try:
                    import speech_recognition as sr
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue

            elif lib == "openai":
                if (lib, pip_name, version) in not_installed_libraries:
                    print_color("AR", "Ready to upgrade ", new_line=False)
                    print_color("AG", pip_name, "...")
                else:
                    try:
                        import openai
                        
         
                        print_successful_import(lib, pip_name, version)
                    except ImportError as e:
                        print_color("AR", "Failed to import ", new_line=False)
                       
                        print_color("AG", pip_name, "...")
                        not_installed_libraries.append((lib, pip_name, version))
                continue

            elif lib == "instructor":
                try:
                    from instructor import Instructor
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "tzdata":
                try:
                    import tzdata
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "dateutil":
                try:
                    from dateutil import parser
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "pytz":
                try:
                    import pytz
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "pydantic":
                try:
                    from pydantic import BaseModel
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "tiktoken":
                try:
                    from tiktoken import encoding_for_model
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "selenium":
                try:
                    from selenium import webdriver
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "vulture":
                try:
                    from vulture import Vulture
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "icecream":
                try:
                    from icecream import ic
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue

    
            elif lib == "aiohttp":
                try:
                    import aiohttp
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "aiofiles":
                try:
                    import aiofiles
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "lxml":
                try:
                    from lxml import etree
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "plotly":
                try:
                    from plotly import graph_objects as go
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue

            elif lib == "langchain":
                try:
                    import langchain
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "github":
                try:
                    from github import Github
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "pygit2":
                try:
                    import pygit2
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "importlib_metadata":
                try:
                    import importlib_metadata
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "astor":
                try:
                    import astor
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "pytube":
                try:
                    from pytube import YouTube
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "wget":
                try:
                    import wget
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "trimesh":
                try:
                    import trimesh
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "imageio":
                try:
                    import imageio
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "py7zr":
                try:
                    import py7zr
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    
            elif lib == "sounddevice":
                try:
                    import sounddevice as sd
                    print_successful_import(lib, pip_name, version)
                except ImportError as e:
                    print_color("AR", "Failed to import ", new_line=False)
                    print_color("AG", pip_name, "...")
                    not_installed_libraries.append((lib, pip_name, version))
                continue
    

            # elif lib == "PyInstaller":
            #     try:
            #      

            #         result = subprocess.run(["pyinstaller", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #         print(f"\n🚀 result: {result}")
            #         if result.returncode == 0:
            #             print_successful_import(lib, pip_name, version)
            #         else:
            #             raise ImportError("PyInstaller not available")
            #     except (ImportError, subprocess.CalledProcessError) as e:
            #         print_color("AR", "\nFailed to access PyInstaller ", new_line=False)
            #         print_color("AG", pip_name, "...")
            #         not_installed_libraries.append((lib, pip_name, version))
            #         capture_and_copy_traceback()
            #     continue

            else:
                if lib == "setuptools":
                
                    # Suppress Setuptools-specific warnings
                    warnings.filterwarnings(
                        "ignore",
                        message="Distutils was imported before Setuptools.*",
                        category=UserWarning,
                        module="_distutils_hack"
                    )
                    warnings.filterwarnings(
                        "ignore",
                        message="Setuptools is replacing distutils.*",
                        category=UserWarning,
                        module="_distutils_hack"
                    )

                package_metadata, package_found = get_package_metadata(
                    lib, pip_name, folder_path.lower()
                )
                try:
                    n = package_metadata["Name"]

                    package_location = package_metadata["Location"]

                    if package_metadata and not package_found:
                        print("Package not in fast/lib (imported from different directory):"
                        )
                        print("package_location:", package_location)
                        print("   lib_location :", folder_path.lower())
                        # install it in lib anyway?
                        not_installed_libraries.append((lib, pip_name, version))
                        
                    else:
                        print_successful_import(lib, pip_name, version)
                except:
                    raise ImportError(f"Failed to import {pip_name}.")
    
        except ImportError as e:
            not_installed_libraries.append((lib, pip_name, version))
        
            print_color("AR", "Failed to import ", new_line=False)
            print_color("AG", pip_name, "...")
        except:
            
            not_installed_libraries.append((lib, pip_name, version))
            
        # reset_timer(30)

    save_user_pref_block_info()
    
    sys.path = original_sys_path

    manager.register_done_bse = True
    manager.register_done_gpt = True
    return not_installed_libraries
    




def get_ffmpeg_url():
    if sys.platform.startswith("win"):
        return (
            "https://github.com/Pullusb/static_bin/raw/main/ffmpeg/windows/ffmpeg.exe"
        )
    elif sys.platform.startswith(("linux", "freebsd")):
        return "https://github.com/Pullusb/static_bin/raw/main/ffmpeg/linux/ffmpeg"
    else:  # Mac
        return "https://github.com/Pullusb/static_bin/raw/main/ffmpeg/mac/ffmpeg"



# # URL of the pypiwin32 wheel file
# pypiwin32_url = "https://files.pythonhosted.org/packages/d0/1b/2f292bbd742e369a100c91faa0483172cd91a1a422a6692055ac920946c5/pypiwin32-223-py3-none-any.whl"



def get_path_to_ffmpeg(folder_path):
    if sys.platform.startswith("win"):
        ffmpeg_filename = "ffmpeg.exe"
    else:
        ffmpeg_filename = "ffmpeg"
    path_to_ffmpeg = os.path.join(folder_path, ffmpeg_filename)
    path_to_ffmpeg = path_to_ffmpeg.replace("\\", "/")
    return path_to_ffmpeg




global_confirmation = False

class FAST_OT_FlashMessageBox(bpy.types.Operator):
    """Flash message box and wait for confirmation"""
    bl_idname = "fast.flash_message_box"
    bl_label = "Confirmation Required"
    bl_options = {'REGISTER'}

    string: bpy.props.StringProperty(default="")
    title: bpy.props.StringProperty(default="Missing Libraries")
    wrap: bpy.props.BoolProperty(default=True)
    width: bpy.props.IntProperty(default=194)

    offset_x: bpy.props.IntProperty(default=0)
    offset_y: bpy.props.IntProperty(default=0)
    use_popup: bpy.props.BoolProperty(default=False)


    def execute(self, context):

            
        try:
            import pywinctl
            show_console_ste()  # Call the function only if pywinctl imports successfully
        except ImportError:
            print_color("AR", f"\npywinctl not found. Could not show console.")

        manager = bpy.context.preferences.addons[__name__].preferences.Prop     
             
        bpy.ops.fast.info('INVOKE_DEFAULT', message="Initiating FAST library installation. If no libraries are installed this will take a while.", duration=10)
        bpy.app.timers.register(lambda: (initiate_install_dependencies(), None)[1], first_interval=0.1)
        manager.dependencies_installed = True
        if manager.startup_dependency_info:
            pass
            
        return {'FINISHED'}



    def invoke(self, context, event):
 
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        print_color("AR", f"\nWaiting for user input.")
        # beep()
        # for area in context.screen.areas:
        #     if area.type == "VIEW_3D":
        #         for region in area.regions:
        #             if region.type == "WINDOW":
        #                 try:
        #                     screen_size = pyautogui.size()
        #                 except Exception as e:
        #                     print_color("AR", f"\nDefaulting to Blender's screen size functionality for message box.")

        #                     # If pyautogui is not installed, use the dimensions of the 3D View region
        #                     region = [r for r in area.regions if r.type == "WINDOW"][0]
        #                     screen_size = type("Size", (object,), {"width": region.width, "height": region.height})()
        #                     # Report to the user that pyautogui is not installed
        #                     self.report({"INFO"}, "PyAutoGUI is not installed. Defaulting to 3D Viewport size.")
        #                     # print("Error: ", str(e))
        #                 break

        # screen_width, screen_height = (screen_size.width, screen_size.height)

        # # Calculate the center of the screen
        # screen_center_x = screen_width // 2

        # screen_center_y = screen_height // 2

        # # Calculate the starting X position for the message box to be centered
        # message_box_start_x = screen_center_x

        # # Apply offsets to fine-tune the position
        # final_x = message_box_start_x + manager.offset_x
  
        # final_y = screen_center_y + manager.offset_y

        #print("cursor warp is active")
        context.window.cursor_warp(-10000, -10000)
        

        if self.use_popup:
            return context.window_manager.invoke_popup(self, width=self.width)
        else:
            return context.window_manager.invoke_props_dialog(self, width=self.width)
   
#1

    def draw(self, context):
        layout = self.layout
        layout.label(text="Libraries need to be installed.")
        layout.label(text="Do you want to install them now?")



class install_dependencies(bpy.types.Operator):
    bl_idname = "module.install_dependencies"
    bl_label = "Install Dependencies"
    bl_description = (
        "Downloads and installs required Python packages for this add-on.\n\n"
        "Internet connection is required.\n\n"
        "Click, wait 20 minutes, come back to Blender...\n\n"
        "& everything should be installed.\n\n"
        "This process may take up to 20 minutes, but you'll see all the amazing libraries you'll have installed...\n\n"
        "Whenever you start up Blender and look at the console...\n\n"
        "\n\nThen you can use them in your scripts, with their import functions, in the 'Text Editor'!!"
    )
    bl_options = {"REGISTER", "INTERNAL"}

    original_sys_path = None
    libraries = libraries
    active = False
    message = bpy.props.StringProperty()
    thread_failed = False
    current_package_index = 0
    error_message = None
    flag = False
    flag2 = False
    dependencies_file: StringProperty(
        name="Dependencies File",
        description="Path to the file containing not installed libraries",
        default=""
    )
    # t1 = None
    not_installed_libraries = []
    successfully_installed_libraries = []
    pip_names_to_upgrade = ["pytube"]

    folder_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")

    def ensure_pip(self):
        print_color("AW", "Ensuring pip is installed and upgrading...")
        try:
            print("")
            subprocess.run([sys.executable, "-m", "pip", "--version"], check=True)
        except subprocess.CalledProcessError:
            import ensurepip

            lib_dir = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
            ensurepip.bootstrap(root=lib_dir)

            os.environ.pop("PIP_REQ_TRACKER", None)

        # Upgrade pip
        try:
            path = "--target=" + os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip", path], check=True)

            print("pip has been upgraded successfully.")
        except Exception as e:
            

            print(f"Error upgrading pip:\n")
            capture_and_copy_traceback()
        result = bpy.ops.fast.delete_pip_cache()

 
 

    def download_ffmpeg(self, url, dest, bar_size=50):
        try:
            print_color("GB", "Downloading ", new_line=False)
            print_color("AR", "FFMPEG", new_line=False)
            print_color("GB", "...", new_line=False)

            response = requests.get(url, stream=True)
            file_size = int(response.headers.get("Content-Length", 0))
            block_size = 1024
            num_bars = file_size // block_size

            with open(dest, "wb") as outfile:
                for i, data in enumerate(response.iter_content(block_size)):
                    # Print progress
                    percent_done = (i + 1) * 100 // num_bars
                    num_hashes = percent_done * bar_size // 100
                    bar = "#" * num_hashes + "-" * (bar_size - num_hashes)
                    sys.stdout.write(f"\r[{bar}] {percent_done}%")
                    sys.stdout.flush()
                    outfile.write(data)

            os.chmod(dest, os.stat(dest).st_mode | stat.S_IXUSR)

        except Exception as e:
            capture_and_copy_traceback()

            print("An error occurred during the download of ffmpeg:", str(e))
            return None
        return "FINISHED"

    @classmethod
    def is_running(cls):
        return cls.active

    def invoke(self, context, event):
        # self.confirm = 'NO'
        cls = self.__class__
        cls.current_package = 0

        # cls.abort = False
        self.original_sys_path = sys.path
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=400)

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        # text = "This operation will install dependencies using PIP, Continue?"
        text = (
            "\nInternet connection is required."
            "\nYou must restart Blender after install."
            "\nEstimated time for full installation: 5 minutes,"
            "\nThis operation will install dependencies in the FAST addon lib folder using PIP, Continue?"
        )
        wrap_text(
            col, string=text, text_length=(context.region.width / 6.5), center=True
        )
        # box = layout.box()
        col = box.column(align=True)
        wrap_text(
            col,
            string="Press ESC to return",
            text_length=(context.region.width / 6.5),
            center=True,
            icon="CANCEL",
        )

    # use these if you want to design custom class specific pop up functions
    def draw_popup(self, layout):
        layout.label(text="Info:")
        layout.label(text=self.message)

    def show_popup(self, message):
        self.message = message
        bpy.context.window_manager.popup_menu(
            self.draw_popup, title="Popup", icon="INFO"
        )

    def execute(self, context):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        scn = bpy.context.scene

    
        if os.path.exists(self.dependencies_file):
            with open(self.dependencies_file, "r") as file:
                self.not_installed_libraries = eval(file.read())
            # Delete the file after reading it
            os.remove(self.dependencies_file)
            print_color("AR", f"\nDeleted temp file: {self.dependencies_file}")
    

        if count_blender_instances() > 1:
            print_color("AR", f"\nMultiple Blender instances detected. Operation cancelled.")
            self.report({'INFO'}, msg)
            return {'CANCELLED'}

        result = fast_connection_checker()
        if not result:
            # manager.register_done = True
            msg = "No Internet connection detected. Could not install dependencies."
            self.report({'INFO'}, msg)
            return {'CANCELLED'}
        
        cls = self.__class__
        cls.active = True
        cls.thread_failed = False
        cls.last_index = -1
        cls.current_package_index = 0  # Index of the current library being processed
        cls.error_message = None
        # cls.progress_message = None



        try:
            preferences = bpy.context.preferences.addons[__package__].preferences
            manager = bpy.context.preferences.addons[__name__].preferences.Prop
            scn = bpy.context.scene
        except:
            cls.error_message = f"Manager Error: {str(e)}"
            self.end_modal(context)
            capture_and_copy_traceback()
            return {"CANCELLED"}




        # backup sys.path
        self.original_sys_path = sys.path

        print_color("AR", f"\nNot installed libraries: {self.not_installed_libraries}")
    
        if len(self.not_installed_libraries):
            print_color("AR", "\nSome libraries are not installed properly...")
            print_color("AG", "\nWe're installing them for you...")
            print_color("AB", "\nIf installation doesn't proceed, restart Blender...")
            print_color("AR", "\nThe process will commplete automatically after the restart...")
            print_color("AW", "") # Blank line
            
            self.ensure_pip()
    
        elif not self.not_installed_libraries:
            text = "Dependencies are already installed!"
            # draw_info(text, width=208)
            self.report({"INFO"}, text)
            return {"FINISHED"}
        else:
            print_color("AR", f"\nUnrecognized issue. Check install dependencies operator.")

        wm = context.window_manager
        timestep = 1 / 60
        self.timer = wm.event_timer_add(timestep, window=context.window)
        wm.modal_handler_add(self)
        bpy.ops.fast.info('INVOKE_DEFAULT', message="Dependencies are installing. Must wait until completes before using Blender.", duration=15)
        return {"RUNNING_MODAL"}

    def pip_package(self, lib, pip_name, version):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        cls = self.__class__
        cls.last_index = cls.current_package_index
        import os
        import sys
        path = "--target=" + os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
        # instead of this in thread, store errors then write after
        pip_errors_file = os.path.join(bpy.utils.script_path_user(), "addons", "blender_ai_thats_error_proof", "logs", 'PIP_dependency_errors.log')
        # Use try-except to catch any errors and write them to the file
        with open(pip_errors_file, 'w') as error_file:

            try:
                    
                full_pip_name = pip_name if not version else f"{pip_name}=={version}"
                print_color("AB", f"\nAttempting to install {pip_name}...")

                # cls.progress_message = f"Attempting to install: {pip_name}..."
    
                ffmpeg_url = get_ffmpeg_url()
            
                path_to_ffmpeg = get_path_to_ffmpeg(self.folder_path)
            
                if lib == "ffmpeg":
                    
                    # Special handling for FFmpeg, if it is not found
                    if not os.path.exists(path_to_ffmpeg) or not os.access(path_to_ffmpeg, os.X_OK):
                        print_color("AR", "\nFFmpeg was not found", new_line=False)
                        print_color("AG", "...Installing...", new_line=True)
                       
                        if platform.system() == "Darwin":  # macOS
                            
                            try:
                                # Ensure the parent directory exists
                                os.makedirs(os.path.dirname(path_to_ffmpeg), exist_ok=True)
                        
                                def download_ffmpeg_for_darwin():
                                    """Download FFmpeg on macOS using the requests library."""
                                    print(f"\n🚀 Starting FFmpeg download for Darwin (macOS).")
                                    
                                    try:
                                        # Get the FFmpeg download URL and destination path
                                        ffmpeg_url = get_ffmpeg_url()  # Ensure this function is defined and returns the correct URL
                                        path_to_ffmpeg = get_path_to_ffmpeg(self.folder_path)  # Ensure this is the intended destination
                                
                                        print(f"Downloading FFmpeg from: {ffmpeg_url}")
                                        print(f"Destination path: {path_to_ffmpeg}")
                                
                                        # Download the FFmpeg binary
                                        response = requests.get(ffmpeg_url, stream=True)
                                        response.raise_for_status()  # Automatically raises an error for non-2xx responses
                                
                                        with open(path_to_ffmpeg, "wb") as outfile:
                                            for chunk in response.iter_content(chunk_size=1024):
                                                if chunk:  # Filter out keep-alive chunks
                                                    outfile.write(chunk)
                                
                                        # Make the binary executable
                                        os.chmod(path_to_ffmpeg, os.stat(path_to_ffmpeg).st_mode | stat.S_IXUSR)
                                
                                        print_color("AG", f"FFmpeg downloaded and made executable at: {path_to_ffmpeg}.", new_line=True)
                                        return True  # Success
                                
                                    except Exception as e:
                                        print_color("RW", f"An error occurred while downloading FFmpeg: {str(e)}", new_line=True)
                                        traceback.print_exc()
                                        return False  # Failure

                                
     
                                if not download_ffmpeg_for_darwin():
                                    print("Failed to DL FFmpeg programmatically.")
                                    self.not_installed_libraries.append((lib, pip_name, version))
                                else:
                                    print("FFmpeg installed successfully.")
                                    self.successfully_installed_libraries.append((lib, pip_name, version))


                            except Exception as e:
                                print_color("RW", f"An error occurred during FFmpeg installation: {str(e)}", new_line=True)
                                self.not_installed_libraries.append((lib, pip_name, version))
                        
                        else:
                            # Default downloading and executable creation logic for other platforms
                            download_ffmpeg_result = self.download_ffmpeg(
                                ffmpeg_url, path_to_ffmpeg, bar_size=50
                            )
                
                            if download_ffmpeg_result is None:
                                print_color("AR", f"\nAn ffmpeg error occurred. Please connect to the Internet, restart Blender, and try again.")
                                self.not_installed_libraries.append((lib, pip_name, version))
                            elif (
                                download_ffmpeg_result
                                and os.path.exists(path_to_ffmpeg)
                                and os.access(path_to_ffmpeg, os.X_OK)
                            ):
                                print_color("AR", "\nFFmpeg ", new_line=False)
                                print_color("AG", "downloaded ", new_line=False)
                                print_color("AB", "successfully.", new_line=True)
                                print("")
                                cls.successfully_installed_libraries.append((lib, pip_name, version))
                            else:
                                print_color("AR", "FFmpeg download failed", new_line=True)
                                self.not_installed_libraries.append((lib, pip_name, version))
                
                            if not os.access(path_to_ffmpeg, os.X_OK):
                                try:
                                    os.chmod(
                                        path_to_ffmpeg,
                                        os.stat(path_to_ffmpeg).st_mode | stat.S_IXUSR,
                                    )
                                    print_color("GB", "ffmpeg made executable successfully.", new_line=True)
                                except:
                                    print_color("RW", "Failed to make ffmpeg executable.", new_line=True)
                                    self.not_installed_libraries.append((lib, pip_name, version))  # Add to not installed libraries
                    else:
                        print_color("AR", f"\nffmpeg installation already in lib")
                        self.successfully_installed_libraries.append((lib, pip_name, version))
                

                else:
                    if pip_name in self.pip_names_to_upgrade:
              
                        print_color("AG", f"\nUpgrading library: {pip_name}")
                        try:
                            subprocess.run(
                                [sys.executable, "-m", "pip", "install", full_pip_name, path, "--no-user"],
                                check=True,
                            )
                            
                            
                            print_color("AG", f"\nSuccessfully upgraded {pip_name}")
                            self.successfully_installed_libraries.append((lib, pip_name, version))
                        except Exception as e:
                            

                            print_color("AR", f"\nError upgrading {pip_name}:\n")
                            capture_and_copy_traceback()
                            self.not_installed_libraries.append((lib, pip_name, version))
                    else:

                        # General PIP Install Logic
                        if lib not in ["pywin32", "pypiwin32", "pywinctl", "pyaudio", "openai"]:  # Skip full installations handled separately
                            import sys
                            print_color("AG", f"\nInstalling library: {pip_name}\n")
                            try:
                                subprocess.run(
                                    [sys.executable, "-m", "pip", "install", full_pip_name, path, "--no-user"],
                                    check=True,
                                )
                                self.successfully_installed_libraries.append((lib, pip_name, version))
                            except Exception as e:
                                print_color("AR", f"\nError installing {pip_name}: {e}")
                                print_color("AR", f"\nAppending to not installed libraries list.")
                                traceback.print_exc()
                                self.not_installed_libraries.append((lib, pip_name, version))

                        system_platform = platform.system()
                    
                        if system_platform == "Windows":


                            # General PIP Install Logic
                            if lib in ["openai"]:  # Skip full installations handled separately
                                print_color("AG", f"\nUpgrading library: {pip_name}\n")
                                try:
                                    import sys, os

                                    # Save original sys.path and PYTHONUSERBASE
                                    original_sys_path = sys.path.copy()
                                    original_pythonuserbase = os.environ.get("PYTHONUSERBASE", "")

                                    lib_path = os.path.join(os.path.dirname(__file__), "lib")
            
                                    sys.path.clear()
                                    sys.path.append(lib_path)
                                    print(f"\n🚀 sys.path: {sys.path}")

                                    # Set PYTHONUSERBASE to the lib directory
                                    os.environ["PYTHONUSERBASE"] = lib_path

                                    # Perform the upgrade using --user and without --target
                                    subprocess.run(
                                        [sys.executable, "-m", "pip", "install", "--upgrade", full_pip_name, "--user"],
                                        check=True,
                                    )

                                    # Restore the original sys.path and PYTHONUSERBASE
                                    sys.path = original_sys_path
                                    os.environ["PYTHONUSERBASE"] = original_pythonuserbase

                                    self.successfully_installed_libraries.append((lib, pip_name, version))
                                except Exception as e:
                                    print_color("AR", f"\nError upgrading {pip_name}: {e}")
                                    print_color("AR", f"\nAppending to not installed libraries list.")
                                    self.not_installed_libraries.append((lib, pip_name, version))
                                    # Restore paths even in case of failure
                                    sys.path = original_sys_path
                                    os.environ["PYTHONUSERBASE"] = original_pythonuserbase

                        

                            if lib in ["pywin32", "pypiwin32", "pywinctl"]:
                                
                                print_color("AG", f"\nInstalling library: {pip_name}\n")
                                try:
                                    subprocess.run(
                                        [sys.executable, "-m", "pip", "install", full_pip_name, path, "--no-user"],
                                        check=True,
                                    )
                                    self.successfully_installed_libraries.append((lib, pip_name, version))
                                except Exception as e:
                                    print_color("AR", f"\nError installing {pip_name}: {e}")
                                    traceback.print_exc()
                                    print_color("AR", f"\nAppending to not installed libraries list.")
                                    self.not_installed_libraries.append((lib, pip_name, version))

                         
                                source_dir = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages", "pywin32_system32")
                                destination_dir = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages", "win32")

                
                        
                                if os.path.exists(destination_dir):
                                    dll_files = [f for f in os.listdir(source_dir) if f.endswith(".dll")]
                                    try:
                                        for dll_file in dll_files:
                                            source_path = os.path.join(source_dir, dll_file)
                                            destination_path = os.path.join(destination_dir, dll_file)
                                            shutil.copy(source_path, destination_path)
                                      
                                    except Exception as e:
                                        capture_and_copy_traceback()
                                        print_color("AR", f"\nError copying DLL files: {e}")
                        
                                    try:
                                        base_dir = os.path.dirname(__file__)
                                        sys.path.append(os.path.join(base_dir, "lib", "Python311", "site-packages", "win32"))
                                        sys.path.append(os.path.join(base_dir, "lib", "Python311", "site-packages", "win32", "lib"))
                                        sys.path.append(os.path.join(base_dir, "lib", "Python311", "site-packages", "pywin32_system32"))
                                        print_color("AB", f"\nDLL paths added to sys.path for {lib}")
                                    except Exception as e:
                                        capture_and_copy_traceback()
                                        print_color("AR", f"\nError adding DLL paths to sys.path for {lib}: {e}")
                                else:
                                    print_color("AR", f"\nwin32 path does not exist after install for {lib}")
                                    self.not_installed_libraries.append((lib, pip_name, version))

                            if lib in ["pyaudio"]:
                                
                                print_color("AG", f"\nInstalling library: {pip_name}\n")
                                try:
                                    subprocess.run(
                                        [sys.executable, "-m", "pip", "install", full_pip_name, path, "--no-user"],
                                        check=True,
                                    )
                                    self.successfully_installed_libraries.append((lib, pip_name, version))
                                except Exception as e:
                                    print_color("AR", f"\nError installing {pip_name}: {e}")
                                    traceback.print_exc()
                                    print_color("AR", f"\nAppending to not installed libraries list.")
                                    self.not_installed_libraries.append((lib, pip_name, version))

                            # if lib == "torch" or lib == "Cython":
                            #     # Set the LIB path to only use "lib3"
                            #     lib_path = os.path.join(os.path.dirname(__file__), "lib3")
                            #     os.makedirs(lib_path, exist_ok=True)  # Ensure lib3 exists
                            
                            #     # Backup original sys.path and temporarily limit to lib3
                            #     original_sys_path = sys.path.copy()
                            #     sys.path.clear()
                            #     sys.path.append(lib_path)
                           
                            
                            #     print_color("AG", f"\nInstalling library: {pip_name}\n")
                            #     try:
                            #         subprocess.run(
                            #             [sys.executable, "-m", "pip", "install", full_pip_name, path, "--no-user"],
                            #             check=True,
                            #         )
                            #         self.successfully_installed_libraries.append((lib, pip_name, version))
                            #     except Exception as e:
                            #         print_color("AR", f"\nError installing {pip_name}: {e}")
                            #         print_color("AR", f"\nAppending to not installed libraries list.")
                            #         self.not_installed_libraries.append((lib, pip_name, version))
                            
                            #     finally:
                            #         # Restore the original sys.path after installation
                            #         sys.path.clear()
                            #         sys.path.extend(original_sys_path)
                            #         print("\n🔧 sys.path restored after installation attempt.")
                            
                        
                        elif system_platform == "Linux":
                            if lib in ["pywinctl"]:

                                try:
                                    # Step 1: Update package lists
                                    print("Updating package lists...")
                                    subprocess.run(["sudo", "apt-get", "update"], check=True)
                        
                                    # Step 2: Install python-xlib for X11-based window management
                                    print("Installing python-xlib for pywinctl...")
                                    subprocess.run(["sudo", "apt-get", "install", "-y", "python3-xlib"], check=True)
                                    print("Successfully installed python-xlib.")
                        
                                    # Step 3: Install pywinctl using pip with --break-system-packages
                                    print("Installing pywinctl using pip...")
                                    subprocess.run([
                                        sys.executable, "-m", "pip", "install", "pywinctl", path, "--break-system-packages"
                                    ], check=True)
                                    print("Successfully installed pywinctl.")
                        
                                    # Step 4: Update the library path if needed (optional)
                                    sys.path.append(os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages"))
                                    print_color("AB", "\nPython paths updated for Linux.")
                        
                                    # Step 5: Mark library as successfully installed
                                    self.successfully_installed_libraries.append((lib, pip_name, version))
                                except Exception as e:
                                    print_color("AR", f"\nError installing {pip_name}: {e}")
                                    traceback.print_exc()
                                    print_color("AR", f"\nAppending to not installed libraries list.")
                                    self.not_installed_libraries.append((lib, pip_name, version))

                
       
                    
                            if lib == "pyaudio":
                                try:
                                    # Set environment variables for the build process
                                    import os
                                    os.environ["CFLAGS"] = "-I/usr/include/python3.11"
                                    os.environ["LDFLAGS"] = "-L/usr/lib/python3.11/config-3.11-x86_64-linux-gnu"
                        
                                    # Install pyaudio using Blender's Python
                                    print("Installing pyaudio for Blender's Python...")
                                    blender_python_path = os.path.join(os.path.dirname(sys.executable), "python3.11")
                                    subprocess.run([
                                        blender_python_path, "-m", "pip", "install", "pyaudio",
                                        path
                                    ], check=True)
                                    print("Successfully installed pyaudio for Blender's Python.")
                        
                                    # Append the library to the success list
                                    self.successfully_installed_libraries.append((lib, pip_name, version))
                                except Exception as e:
                                    print_color("AR", f"\nError installing {pip_name}: {e}")
                                    traceback.print_exc()
                                    print_color("AR", f"\nAppending to not installed libraries list.")
                                    self.not_installed_libraries.append((lib, pip_name, version))
                                
                
                                                    

                        elif system_platform == "Darwin":

                            if lib in ["openai"]:  # Skip full installations handled separately
                                print_color("AG", f"\nUpgrading library: {pip_name}\n")
                                try:
                                    import sys, os

                                    # Save original sys.path and PYTHONUSERBASE
                                    original_sys_path = sys.path.copy()
                                    original_pythonuserbase = os.environ.get("PYTHONUSERBASE", "")

                                    lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
            
                                    sys.path.clear()
                                    sys.path.append(lib_path)

                                    # Set PYTHONUSERBASE to the lib directory
                                    os.environ["PYTHONUSERBASE"] = lib_path

                                    # Perform the upgrade using --user and without --target
                                    subprocess.run(
                                        [sys.executable, "-m", "pip", "install", "--upgrade", full_pip_name, "--user"],
                                        check=True,
                                    )

                                    # Restore the original sys.path and PYTHONUSERBASE
                                    sys.path = original_sys_path
                                    os.environ["PYTHONUSERBASE"] = original_pythonuserbase

                                    self.successfully_installed_libraries.append((lib, pip_name, version))
                                except Exception as e:
                                    print_color("AR", f"\nError upgrading {pip_name}: {e}")
                                    print_color("AR", f"\nAppending to not installed libraries list.")
                                    self.not_installed_libraries.append((lib, pip_name, version))
                                    # Restore paths even in case of failure
                                    sys.path = original_sys_path
                                    os.environ["PYTHONUSERBASE"] = original_pythonuserbase



                            if lib == "pywinctl":
                                try:
                                    # Step 1: Install pyobjc dependency
                                    print("Installing pyobjc on macOS...")
                                    subprocess.run(
                                        [sys.executable, "-m", "pip", "install", "pyobjc", path],
                                        check=True
                                    )
                                    print("Successfully installed pyobjc.")
                        
                                    # Step 2: Install pywinctl
                                    print("Installing pywinctl on macOS...")
                                    subprocess.run(
                                        [sys.executable, "-m", "pip", "install", "pywinctl", path],
                                        check=True
                                    )
                                    print("Successfully installed pywinctl on macOS.")
                        
                                    # Verification Step: Check if pywinctl was successfully installed and print the installation path
                                    import importlib.util
                                    
                                    pywinctl_installed = importlib.util.find_spec("pywinctl")
                                    if pywinctl_installed:
                                        print("pywinctl verified as successfully installed.")
                                        print("pywinctl installed at:", pywinctl_installed.origin)
                                    else:
                                        print("pywinctl installation verification failed.")
                        
                                    # Step 3: Update Python paths if necessary
                                    lib_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
                                    if lib_path not in sys.path:
                                        sys.path.append(lib_path)
                                        print("Python path updated to include:", lib_path)
                        
                                    # Step 4: Handle permissions if applicable
                        
                                    # Mark library as successfully installed
                                    self.successfully_installed_libraries.append((lib, pip_name, version))
                        
                                except subprocess.CalledProcessError as e:
                                    # Handle errors during subprocess execution
                                    capture_and_copy_traceback()
                                    print(f"Error installing {lib} on macOS: {e}")
                                    self.not_installed_libraries.append((lib, pip_name, version))
                                except Exception as e:
                                    # Handle any other exceptions
                                    capture_and_copy_traceback()
                                    print(f"Unexpected error: {e}")
                                    self.not_installed_libraries.append((lib, pip_name, version))
                        

                            
                        
                            # if lib == "pyaudio":
                            #     try:
                            #         # Check if Homebrew is installed
                            #         brew_check = subprocess.run(["which", "brew"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            
                            #         if brew_check.returncode != 0:
                            #             print("Homebrew is not installed. Attempting to install Homebrew...")
                            #             subprocess.run(["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"], check=True)
                            #             print("Successfully installed Homebrew.")
                            
                            #         # Verify Homebrew installation before running diagnostics
                            #         brew_check = subprocess.run(["which", "brew"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            #         if brew_check.returncode == 0:
                            #             print("Running 'brew doctor' to check for Homebrew issues...")
                            #             subprocess.run(["brew", "doctor"], check=True)
                            
                            #         # Ensure Xcode Command Line Tools are installed
                            #         print("Checking for Xcode Command Line Tools...")
                            #         xcode_check = subprocess.run(["xcode-select", "-p"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            #         if xcode_check.returncode != 0:
                            #             print("Xcode Command Line Tools not found. Attempting to install...")
                            #             subprocess.run(["sudo", "xcode-select", "--install"], check=True)
                            #             print("Please complete the Xcode installation manually if prompted.")
                            
                            #         # Ensure Python development headers are available for Blender's Python
                            #         print("Checking for Python development headers...")
                            #         python_include_path = "/Applications/Blender.app/Contents/Resources/4.3/python/include/python3.11/Python.h"
                            #         if not os.path.exists(python_include_path):
                            #             print("Python development headers missing. Attempting to install...")
                            #             # Install Python dev tools for Blender's Python specifically
                            #             subprocess.run([
                            #                 "/Applications/Blender.app/Contents/Resources/4.3/python/bin/python3.11", 
                            #                 "-m", "pip", "install", "--upgrade", "python-dev-tools"
                            #             ], check=True)
                            #         else:
                            #             print("Python development headers already available.")
                            
                            #         # Ensure PortAudio is installed
                            #         print("Installing required PortAudio library via Homebrew...")
                            #         subprocess.run(["brew", "install", "portaudio"], check=True)
                            
                            #         # Set both static and dynamic environment variables for PyAudio compilation
                            #         try:
                            #             sdk_path = subprocess.check_output(["xcrun", "--show-sdk-path"]).decode().strip()
                            #             os.environ["CFLAGS"] = f"-I{sdk_path}/usr/include -I/usr/local/include"
                            #             os.environ["LDFLAGS"] = "-L/usr/local/lib"
                            #             print("Using dynamic SDK paths for PyAudio compilation.")
                            #         except subprocess.CalledProcessError:
                            #             os.environ["CFLAGS"] = "-I/usr/local/include"
                            #             os.environ["LDFLAGS"] = "-L/usr/local/lib"
                            #             print("Using default paths for PyAudio compilation.")
                            
                            #         # Attempt to install PyAudio using pip
                            #         print("Installing PyAudio using pip...")
                            #         subprocess.run([sys.executable, "-m", "pip", "install", "pyaudio", path], check=True)
                            #         print("Successfully installed PyAudio on macOS.")
                            
                            #     except subprocess.CalledProcessError as e:
                            #         print(f"Error installing PyAudio on macOS: {e}")
                            #         self.not_installed_libraries.append((lib, pip_name, version))
                            #     except Exception as e:
                            #         print(f"Unexpected error: {e}")
                            #         self.not_installed_libraries.append((lib, pip_name, version))
                            
                            

                            # # This is the installation procedure from the Mac tutorial on the medium website
                            # if lib == "pyaudio":
                            #     try:
                            #         # Step 1: Check if Homebrew is installed
                            #         print("Checking for Homebrew...")
                            #         brew_check = subprocess.run(["which", "brew"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            #         if brew_check.returncode != 0:
                            #             print("Homebrew is not installed. Installing Homebrew...")
                            #             subprocess.run(
                            #                 ["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"],
                            #                 check=True
                            #             )
                            #             print("Successfully installed Homebrew.")
                            
                            #         # Step 2: Verify Homebrew installation
                            #         print("Running 'brew doctor' to check for issues...")
                            #         subprocess.run(["brew", "doctor"], check=True)
                            
                            #         # Step 3: Ensure Xcode Command Line Tools are installed
                            #         print("Checking for Xcode Command Line Tools...")
                            #         xcode_check = subprocess.run(["xcode-select", "-p"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            #         if xcode_check.returncode != 0:
                            #             print("Xcode Command Line Tools not found. Installing...")
                            #             subprocess.run(["sudo", "xcode-select", "--install"], check=True)
                            #             print("Please complete the installation if prompted.")
                            
                            #         # Step 4: Check for Python development headers
                            #         print("Checking for Python development headers...")
                            #         python_include_path = "/Applications/Blender.app/Contents/Resources/4.3/python/include/python3.11/Python.h"
                            #         if not os.path.exists(python_include_path):
                            #             print("Python development headers missing. Installing python-dev-tools...")
                            #             subprocess.run(
                            #                 ["/Applications/Blender.app/Contents/Resources/4.3/python/bin/python3.11", "-m", "pip", "install", "--upgrade", "python-dev-tools"],
                            #                 check=True
                            #             )
                            #         else:
                            #             print("Python development headers already available.")
                            
                            #         # Step 5: Install PortAudio via Homebrew
                            #         print("Installing PortAudio via Homebrew...")
                            #         subprocess.run(["brew", "install", "portaudio"], check=True)
                            
                            #         # Step 6: Copy PortAudio headers and libraries for macOS compatibility
                            #         print("Copying PortAudio headers and libraries to system paths...")
                            #         subprocess.run(["sudo", "cp", "-r", "/opt/homebrew/Cellar/portaudio/19.7.0/include/*", "/usr/local/include"], check=True)
                            #         subprocess.run(["sudo", "cp", "-r", "/opt/homebrew/Cellar/portaudio/19.7.0/lib/*", "/usr/local/lib"], check=True)
                            
                            #         # Step 7: Set environment variables for PyAudio compilation
                            #         print("Setting environment variables for PyAudio compilation...")
                            #         sdk_path = subprocess.check_output(["xcrun", "--show-sdk-path"]).decode().strip()
                            #         os.environ["CFLAGS"] = f"-I{sdk_path}/usr/include -I/usr/local/include"
                            #         os.environ["LDFLAGS"] = "-L/usr/local/lib"
                            #         print("Environment variables set successfully.")
                            
                            #         # Step 8: Install PyAudio with the correct build options and target folder
                            #         print("Installing PyAudio using pip...")
                            #         subprocess.run([
                            #             sys.executable, "-m", "pip", "install", "pyaudio",
                            #             "--global-option=build_ext",
                            #             "--global-option=-I/usr/local/include",
                            #             "--global-option=-L/usr/local/lib",
                            #             path
                            #         ], check=True)
                            #         print("Successfully installed PyAudio.")
                            
                            #     except subprocess.CalledProcessError as e:
                            #         print(f"Error installing PyAudio: {e}")
                            #         self.not_installed_libraries.append((lib, "pyaudio", "latest"))
                            #     except Exception as e:
                            #         print(f"Unexpected error: {e}")
                            #         self.not_installed_libraries.append((lib, "pyaudio", "latest"))
                            

                print("")
            except Exception as e:
                capture_and_copy_traceback()

                self.not_installed_libraries.append((lib, pip_name, version))  # Add to not installed libraries
                text = f"Failed to install {pip_name}. Error: {str(e)}"
                
                print(text)
                cls.error_message = text
    
        cls.current_package_index = cls.current_package_index + 1


        


    def modal(self, context, event):
        cls = self.__class__
        
        if event.type == "TIMER":

            if cls.error_message:
                text = cls.error_message
                draw_error(text, "Error:", "ERROR")
                self.end_modal(context)
                return {"CANCELLED"}


            if cls.current_package_index < len(self.libraries):
                if cls.current_package_index != cls.last_index:
                    lib, pip_name, version = self.libraries[cls.current_package_index]
            
                    if (lib, pip_name, version) in self.not_installed_libraries:
                        print_color("AG", f"Installing package: {cls.current_package_index + 1} / {len(self.libraries)}")
            
                        if sys.platform == "darwin":

                            # This entire section was your code to accept the Pseudo password all you have to do is indent self P I P package after uncommenting it to reinstate that functionality
                            # manager = bpy.context.preferences.addons[__name__].preferences.Prop
            
                    
                            # if not manager.fast_sudo_password:
                            
                            #     # Start modal for sudo password and pass through
                            #     def start_modal():
                            #         # bpy.ops.fast.sudo_prompt_modal('INVOKE_DEFAULT')
                            #         return None  # Stop the timer after modal starts

                            #     if not self.flag:
                            #         self.flag = True
                            #         bpy.app.timers.register(start_modal, first_interval=0.1)

                            #     return {"PASS_THROUGH"}  # Wait until password is provided
                                
                            # else:
                            #     # If password is available, proceed with pip_package

                            self.pip_package(lib, pip_name, version)
                        else:
                            # For non-macOS platforms, proceed without sudo
                            self.pip_package(lib, pip_name, version)
   
                        # self.t1 = threading.Thread(target=self.pip_package, args=(lib, pip_name, version))

                        # self.t1.start()        

                    else:
                        cls.current_package_index = cls.current_package_index + 1
                        print_color(
                            "AG",
                            f"package: {pip_name} is already installed: {cls.current_package_index} / {len(self.libraries)}",
                        )

            else:
                if self.successfully_installed_libraries:
                    print_color("AW", "\nSuccessfully installed libraries:")
                    for i in self.successfully_installed_libraries:
                        print_color("AW", f"\n{i[0]}")
            
                # Perform the differential check with minimal code changes
                difference = [lib for lib in self.not_installed_libraries if lib not in self.successfully_installed_libraries]
            
                # If no difference, mark as successful and proceed as normal
                if not difference:
                    manager = bpy.context.preferences.addons[__name__].preferences.Prop
                    scn = bpy.context.scene
                    manager.dependencies_installed = True
                    manager.save_pref = True  
                    print_color("AR", "\nREADY ", new_line=False)
                    print_color("AG", "TO ", new_line=False)
                    print_color("AB", "RESTART ", new_line=False)
                    print_color("AR", "BLENDER")
                    print_color("AG", f"\nWaiting for user input in viewport.")
                    ask_to_restart_dependencies()
                else:
                    # If a difference is detected, warn the user but continue as you requested
                    print_color("AR", "INSTALLATION WARNING: A discrepancy was detected!")
                    print_color("AR", "The system is reporting a library installation issue.")
                    print_color("AR", "The affected library or libraries is printed below.")
                    print_color("AR", "Please report issue ASAP so we could fix this for you.")
        
                    
                    # Print the specific libraries that were reported as missing
                    for library in difference:
                        print_color("AR", f"- {library[0]} (PIP Name: {library[1]}, Version: {library[2]})")
            

                    self.end_modal(context)
                    return {"CANCELLED"}
            
                self.end_modal(context)
                return {"FINISHED"}
                                   
            # else:
            #     if self.successfully_installed_libraries:
            #         print_color("AW", "\nSuccessfully installed libraries:")
            #     for i in self.successfully_installed_libraries:

            #         print_color("AW", "\n", i[0])

            #     # print(f"\n🚀 Testing if installed list matches the original not installed list.")
            #     # print(f"\n🚀 set(self.not_installed_libraries): {set(self.not_installed_libraries)}")
            #     # print(f"\n🚀 set(self.successfully_installed_libraries): {set(self.successfully_installed_libraries)}")

            #     if set(self.successfully_installed_libraries) == set(self.not_installed_libraries):

            #         #123 sys.path.append(os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages"))
                    
            #         manager = bpy.context.preferences.addons[__name__].preferences.Prop
            #         scn = bpy.context.scene
            #         manager.dependencies_installed = True
            #         manager.save_pref = True  
            #         print_color("AR", "\nPLEASE ", new_line=False)
            #         print_color("AB", "RESTART ", new_line=False)
            #         print_color("AG", "BLENDER")
            #         ask_to_restart_dependencies()
            #     else:
     
            #         self.not_installed_libraries = list(set(self.not_installed_libraries))
        
            #         print_color("AR", "INSTALL DEPENDENCIES FAILED!")
            #         print("\nUnsuccessfully installed libraries:")

            #         for i in self.not_installed_libraries:
            #             print(f"\n🚀 i: {i}")

            #             if i not in self.successfully_installed_libraries:
            #                 print_color("AR", i[0])

            #         self.end_modal(context)
            #         return {"CANCELLED"}

            #     self.end_modal(context)

            #     return {"FINISHED"}

        return {"PASS_THROUGH"}

    def end_modal(self, context):
        cls = self.__class__
        if cls.error_message:
            bpy.context.preferences.addons[
                __name__
            ].preferences.install_error_msg = cls.error_message
        cls.active = False
        sys.path = self.original_sys_path

        # if self.t1 is not None and self.t1.is_alive():
        #     self.t1.join()
        
        #     print("The thread is still running so joined it.")
        # else:
        #     pass
        #     # print("The thread has finished.")
        
        return {"FINISHED"}






def threaded_check_dependencies():

    try:

        global not_installed_libraries
   
        get_elapsed_time()

        try:
            manager = bpy.context.preferences.addons[__name__].preferences.Prop
            scn = bpy.context.scene
        except KeyError:
            print("\nKeyError: returning from function.")
            return

        site_packages_path = os.path.join(os.path.dirname(__file__), "lib", "Python311", "site-packages")
        
        if not os.path.exists(site_packages_path):
            try:
                os.makedirs(site_packages_path)
                print_color("AG", f"\nCreated missing directory: {site_packages_path}")
            except Exception as e:
                print_color("AR", f"\nError creating directory: {e}")

           
        result = fast_connection_checker()
 
  
        if result:
            
            asyncio.run(check_and_update_openai())
        else:
            print_color("AR", "\nCannot update OpenAI. Please check Internet connection.")


        manager.fast_version = get_current_version()
        print_color("AR", "\nTHIS ", new_line=False)
        print_color("AG", "IS ", new_line=False)
        print_color("AB", "BLENDER A.I. ", new_line=False)
        print_color("AR", "VERSION ", new_line=False)
        print_color("AW", manager.fast_version)


        print_color("AG", "\nTESTING FAST DEPENDENCIES\n")
       
        time.sleep(0.5) #Added to see if this will prevent the need to refresh the console because sometimes when you drag your mouse over items in the console after startup it changes and this is where
        

        test_libraries()
        get_elapsed_time()

        try:
            # Handle missing dependencies
            if not_installed_libraries:
          
                instance_count = check_multiple_blender_instances_1()
                if instance_count > 1:
                    print_color("AR", "Multiple Blender instances detected.")
                    print_color("AR", "\nIt's likely another instance is already installing PIP libraries.")
                    print_color("AR", "\nTo avoid conflicts, PIP library installation will not proceed.")
                    
                    return  # Exit this function early to skip further processing
                
                # If only one instance, proceed with PIP library installation
                manager.dependencies_installed = False
            
                # Save not_installed_libraries to a temp file
                temp_file_path = os.path.join(tempfile.gettempdir(), "not_installed_libraries.txt")
                with open(temp_file_path, "w") as temp_file:
          
                    temp_file.write(str(not_installed_libraries)) 
                try:
                    bpy.utils.register_class(FAST_OT_FlashMessageBox)
                except ValueError:
                    capture_and_copy_traceback()

                def show_message_box():
                    """Function that shows the message box operator once"""
                    bpy.ops.fast.flash_message_box("INVOKE_DEFAULT")   

                if not manager.restart_after_enabling_addon:
                    bpy.app.timers.register(lambda: (show_message_box(), None)[1], first_interval=5.0)
       
        

        except Exception as e:
            print(f"An error occurred while handling missing dependencies: {e}")
            capture_and_copy_traceback()
            pass  # Continue executing code below
        
        return True


    except Exception as e:
        capture_and_copy_traceback()
        text = "An error occurred during the checking process. Check PIP_dependency_errors.log in /FAST/logs for details."
        print_color("AW", text)
        return False


not_installed_libraries = None
class check_dependencies(bpy.types.Operator):
    bl_idname = "module.check_dependencies"
    bl_label = "DEPENDENCIES"
    bl_description = "check dependencies are installed"
    bl_options = {"REGISTER", "INTERNAL"}

    active = False


    @classmethod
    def is_running(cls):
        return cls.active

    
    def execute(self, context):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        scn = bpy.context.scene

        get_elapsed_time()

        check_thread = threading.Thread(target=threaded_check_dependencies)
     
        check_thread.start()

    
        return {"FINISHED"}
    
    






class OperatorStatusPolling:
    """can use this class to check operator states"""

    install_dependencies_running = False


    @classmethod
    def poll(cls):
        if install_dependencies.is_running():
            cls.install_dependencies_running = True
        else:
            cls.install_dependencies_running = False

        if check_dependencies.is_running():
            cls.check_dependencies = True
        else:
            cls.check_dependencies = False




class FAST_OT_open_preferences_to_tab(bpy.types.Operator):
    """Open FAST Preferences on a specific tab"""
    bl_idname = "fast.open_preferences_to_tab"
    bl_label = "Open FAST Preferences"

    tab_name: bpy.props.StringProperty(default="UPDATES")  # Default tab

    def invoke(self, context, event):

        context.window.cursor_warp(0, 0)

        # Ensure the user preferences are displayed
        bpy.ops.screen.userpref_show('INVOKE_DEFAULT')


        context.preferences.active_section = 'ADDONS'
        context.window_manager.addon_search = "blender_ai_thats_error_proof"  # Replace "blender_ai_thats_error_proof" with your add-on's name
        bpy.ops.preferences.addon_expand(module="blender_ai_thats_error_proof")  # Replace "blender_ai_thats_error_proof" with your module name
        bpy.ops.preferences.addon_show(module="blender_ai_thats_error_proof")  # Replace "blender_ai_thats_error_proof" with your module name

        # Set the preferences tab if it exists
        preferences = bpy.context.preferences.addons.get("blender_ai_thats_error_proof")  # Replace "blender_ai_thats_error_proof" with your module name
        if preferences and hasattr(preferences.preferences, 'tabs'):
            preferences.preferences.tabs = self.tab_name



        return {'FINISHED'}




















    



def initiate_install_dependencies():
    try:
        # Path to the file containing not installed libraries
        temp_file_path = os.path.join(tempfile.gettempdir(), "not_installed_libraries.txt")
        
        # Call the operator and pass the file path
        bpy.ops.module.install_dependencies(dependencies_file=temp_file_path)
    except Exception as e:
        print(f"Error during initiate_install_dependencies: {e}")
        pass


check_thread = None

def check_dependencies_func_helper():       
    manager = bpy.context.preferences.addons[__name__].preferences.Prop   
    global check_thread
    try:

        
        result = bpy.ops.module.check_dependencies()

        if 'CANCELLED' in result:
            # Check for internet connection
            result = fast_connection_checker()
            
            if not result:
                msg = "No Internet connection detected. Can't test dependencies."
                manager.register_done_gpt = True
                
                print_color("AR", "\n", msg)
                return 
            else:
                print_color("AR", "\nDependencies test was canceled due to an internal issue.")
                return 



    except RuntimeError as e:
        capture_and_copy_traceback()
        return
    except Exception as e:
        capture_and_copy_traceback()
        return



def check_dependencies_func():
  
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
        
    try:
        check_dependencies_func_helper()
    except Exception as e:
        capture_and_copy_traceback()
        print("Failed to start check dependencies thread:", e)

    
    manager.register_done = True





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





class FAST_OT_save_and_backup_startup_file(bpy.types.Operator):
    bl_idname = "fast.save_and_backup_startup_file"
    bl_label = ""
    bl_description = "Saves and creates a backup of the Blender startup file."

    @classmethod
    def description(cls, context, event):

        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        if manager.verbose_tooltips:
            return (
                "Saves and backs up the Blender startup file, ensuring a safe recovery point.\n\n" 
                "Saves backups with incremented filenames in 'config' & 'Documents/FAST Startup Backup'"
            )
        else:
            return "Saves and backs up the Blender startup file. Verbose tooltip available"


    def execute(self, context):
        

        config_file_path = bpy.utils.user_resource("CONFIG")
        startup_file_path = os.path.join(config_file_path, "startup.blend")
        backup_folder_path = os.path.join(os.path.expanduser('~'), 'Documents', 'FAST Startup Backup')

        # Ensure the FAST Startup Backup folder exists
        if not os.path.exists(backup_folder_path):
            os.makedirs(backup_folder_path)

        def find_next_backup_number():
            

            i = 1
            while os.path.exists(os.path.join(config_file_path, f"startup.blend{i}")):
                i += 1
            return i

        # Backup process
        if os.path.exists(startup_file_path):
            try:
                backup_number = find_next_backup_number()
                backup_file_path = os.path.join(config_file_path, f"startup.blend{backup_number}")
                shutil.copy(startup_file_path, backup_file_path)

                # Also copy the backup to the FAST Startup Backup folder
                backup_file_fast_path = os.path.join(backup_folder_path, f"startup.blend{backup_number}")
                shutil.copy(backup_file_path, backup_file_fast_path)
                print("")
                bpy.ops.wm.save_homefile()
                print("")
                self.report({'INFO'}, "Startup file saved and backed up successfully.")
            except Exception as e:

                self.report({'ERROR'}, f"Error during backup: {str(e)}")
                return {'CANCELLED'}
        else:
            try:
                print("")
                bpy.ops.wm.save_homefile()
                print("")
                backup_number = find_next_backup_number()
                backup_file_path = os.path.join(config_file_path, f"startup.blend{backup_number}")
                shutil.copy(startup_file_path, backup_file_path)

                # Also copy the backup to the FAST Startup Backup folder
                backup_file_fast_path = os.path.join(backup_folder_path, f"startup.blend{backup_number}")
                shutil.copy(backup_file_path, backup_file_fast_path)
                print("")
                self.report({'INFO'}, "Startup file saved and backed up successfully.")
            except Exception as e:

                self.report({'ERROR'}, f"Error during backup: {str(e)}")
                return {'CANCELLED'}

        return {'FINISHED'}



class FAST_OT_save_and_backup_startup_file_append(bpy.types.Operator):
    bl_idname = "fast.save_and_backup_startup_file_append"
    bl_label = ""
    bl_description = "Saves and creates a backup of the Blender startup file in config dir."

    @classmethod
    def description(cls, context, event):

        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        if manager.verbose_tooltips:
            return (
                "Saves and backs up the Blender startup file, ensuring a safe recovery point.\n\n" 
                "Saves backups with incremented filenames in 'config' & 'Documents/FAST Startup Backup'.\n\n"
                "We placed this here because it's common to get crashes when running scripts.\n\n"
                "This helps us remember to save startup files after writing code and before running script.\n\n"
                "It can help you to do the same thing!\n\n"
                "Note: You need to stretch out the interface a bit to use this"
            )
        else:
            return "Backup startup file placed here so can remember before run script. Verbose tool-tip available"


    def execute(self, context):
        

        config_file_path = bpy.utils.user_resource("CONFIG")
        startup_file_path = os.path.join(config_file_path, "startup.blend")
        backup_folder_path = os.path.join(os.path.expanduser('~'), 'Documents', 'FAST Startup Backup')

        # Ensure the FAST Startup Backup folder exists
        if not os.path.exists(backup_folder_path):
            os.makedirs(backup_folder_path)

        def find_next_backup_number():
            

            i = 1
            while os.path.exists(os.path.join(config_file_path, f"startup.blend{i}")):
                i += 1
            return i

        # Backup process
        if os.path.exists(startup_file_path):
            try:
                backup_number = find_next_backup_number()
                backup_file_path = os.path.join(config_file_path, f"startup.blend{backup_number}")
                shutil.copy(startup_file_path, backup_file_path)

                # Also copy the backup to the FAST Startup Backup folder
                backup_file_fast_path = os.path.join(backup_folder_path, f"startup.blend{backup_number}")
                shutil.copy(backup_file_path, backup_file_fast_path)
                print("")
                bpy.ops.wm.save_homefile()
                print("")
                self.report({'INFO'}, "Startup file saved and backed up successfully.")
            except Exception as e:

                self.report({'ERROR'}, f"Error during backup: {str(e)}")
                return {'CANCELLED'}
        else:
            try:
                print("")
                bpy.ops.wm.save_homefile()
                print("")
                backup_number = find_next_backup_number()
                backup_file_path = os.path.join(config_file_path, f"startup.blend{backup_number}")
                shutil.copy(startup_file_path, backup_file_path)

                # Also copy the backup to the FAST Startup Backup folder
                backup_file_fast_path = os.path.join(backup_folder_path, f"startup.blend{backup_number}")
                shutil.copy(backup_file_path, backup_file_fast_path)
                print("")
                self.report({'INFO'}, "Startup file saved and backed up successfully.")
            except Exception as e:

                self.report({'ERROR'}, f"Error during backup: {str(e)}")
                return {'CANCELLED'}

        return {'FINISHED'}


    
class FAST_OT_delete_and_backup_startup_file(bpy.types.Operator):
    bl_idname = "fast.delete_and_backup_startup_file"
    bl_label = "Delete and Backup Startup File"
    bl_description = "Deletes and creates a backup of the Blender startup file in config dir."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        import os
        import shutil

        config_file_path = bpy.utils.user_resource("CONFIG")
        startup_file_path = os.path.join(config_file_path, "startup.blend")
        backup_folder_path = os.path.join(os.path.expanduser('~'), 'Documents', 'FAST Startup Backup')

        # Ensure the FAST Startup Backup folder exists
        if not os.path.exists(backup_folder_path):
            os.makedirs(backup_folder_path)

        def find_next_backup_number():
            i = 1
            while os.path.exists(os.path.join(config_file_path, f"startup.blend{i}")):
                i += 1
            return i

        # Check if the startup file exists
        if os.path.exists(startup_file_path):
            try:
                # Create a backup before deleting
                backup_number = find_next_backup_number()
                backup_file_path = os.path.join(config_file_path, f"startup.blend{backup_number}")
                shutil.copy(startup_file_path, backup_file_path)

                # Also copy the backup to the FAST Startup Backup folder
                backup_file_fast_path = os.path.join(backup_folder_path, f"startup.blend{backup_number}")
                shutil.copy(backup_file_path, backup_file_fast_path)

                # Delete the startup file
                os.remove(startup_file_path)
                self.report({"INFO"}, "Startup file backed up and deleted successfully.")
            except OSError as e:
                self.report({"ERROR"}, f"Error deleting the Startup file: {e}")
        else:
            self.report({"WARNING"}, "Startup file not found. No backup created.")

        return {"FINISHED"}




class FAST_OT_toggle_n_panel(bpy.types.Operator):
    """Toggle N-panel with a button so you don't have to go to press the key"""

    bl_idname = "fast.toggle_n_panel"
    bl_label = "Toggle N-Panel"

    def execute(self, context):

        # if not manager.register_done_bse:
        #     print("")
        #     self.report({'INFO'}, "Please wait for add-on to finish registering.")
        #     return {'CANCELLED'}  

        stdout_backup = sys.stdout
        
        
        with redirect_stdout(sys.stdout):
            try:
                # Access the addon manager to check if the registration is done
                manager = bpy.context.preferences.addons[__name__].preferences.Prop
                scn = bpy.context.scene
                if not manager.register_done_n_panel:
                    print("")
                    self.report({'INFO'}, "Please wait for add-on to finish registering.")
                    return {'CANCELLED'}  

                # Toggle the N-panel visibility in the 3D view area
                for area in context.screen.areas:
                    if area.type == "VIEW_3D":
                        with bpy.context.temp_override(area=area):
                            try:
                                bpy.ops.wm.context_toggle(data_path="space_data.show_region_ui")
                            except Exception as e:
                                print_color("AR", f"\nPlease ignore this error. It's not important but we can't hide it.")

            except Exception as e:
               print_color("AR", f"\nPlease ignore this error. It's not important but we can't hide it.")
               capture_and_copy_traceback()

        return {"FINISHED"}

