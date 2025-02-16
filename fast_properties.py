

import bpy
import os
import sys
from pathlib import Path
from .fast_global import *
from .fast_keymaps import *
from datetime import datetime, timedelta

from bpy.props import (
    BoolProperty,
    IntProperty,
    FloatVectorProperty,
    StringProperty,
    FloatProperty,
    EnumProperty,
    CollectionProperty,
)




import requests

            
def update_gpt_node_image_path(self, context):

    scn = bpy.context.scene
    abs_path = bpy.path.abspath(self.gpt_node_image_path)
    if self.gpt_node_image_path != abs_path:
        self.gpt_node_image_path = abs_path

    # If gpt_node_image_path is set, set gpt_node_screenshot_path to False (or None)
    if self.gpt_node_image_path:
        self.gpt_node_screenshot_path = ""
    
        
def update_gpt_file_permission_fixer_path(self, context):

    scn = bpy.context.scene
    # Define the hard-coded path
    hard_coded_path = os.path.join(os.path.expanduser("~"), "Desktop", "AGPT-4")
    
    # Check if the path has been changed
    if self.gpt_file_permission_fixer_path != hard_coded_path:
        # Reset the path to the hard-coded value
        self.gpt_file_permission_fixer_path = hard_coded_path


def update_gpt_boost_user_command(self, context):
    scn = bpy.context.scene
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    if not scn.gpt_boost_user_command:
        # If boost is turned off, also turn off advanced boost
        if scn.gpt_advanced_boost_user_command:
            scn.gpt_advanced_boost_user_command = False
        my_redraw()

def update_gpt_advanced_boost_user_command(self, context):

    scn = bpy.context.scene
    if scn.gpt_advanced_boost_user_command and not scn.gpt_boost_user_command:
        # If advanced boost is turned on and boost is not on, turn on boost
        scn.gpt_boost_user_command = True
        my_redraw()


def update_bse_current_line(self, context):

    log_file_path = os.path.join(bpy.utils.user_resource('SCRIPTS'), 'addons', __name__, 'data', 'autogpt', 'BSE', "BSE_current_line.txt")
    with open(log_file_path, 'w', encoding='utf-8') as log_file:
        log_file.write(str(self.bse_current_line))
    


def update_gpt_blender_stack_exchange_tag(self, context):

    if self.gpt_blender_stack_exchange_tag != "#AutoGPT_Fix":
        bpy.ops.fast.info('INVOKE_DEFAULT', message="The tag cannot be changed. It has been reset to the default value. Please read tool-tip.", duration=1)
        self.gpt_blender_stack_exchange_tag = "#AutoGPT_Fix"



def update_gpt_max_iterations(self, context):

    scn = bpy.context.scene
    manager = bpy.context.preferences.addons[__name__].preferences.Prop
    
    if manager.autogpt_processing == 'Initializing' or manager.autogpt_processing == 'Analyzing' or manager.autogpt_processing == 'Waiting for Input' or manager.monitor_daz_studio_save_directory:
        return

    try:
        gpt_save_user_pref_block_info()
    except:
        pass





                
def update_api_key(self, context):
    import csv
    scn = bpy.context.scene
    # Define the file path for the API key file
    api_key_fp = os.path.join(os.path.expanduser('~'), 'Documents', 'FAST Settings', 'api_key.csv')

    # Check if the API key is being set or cleared
    if self.api_key:
   
        # Create the FAST Settings directory if it doesn't exist
        os.makedirs(os.path.dirname(api_key_fp), exist_ok=True)

        # Write the new API key to the file
        with open(api_key_fp, mode='w', newline='') as file:
            if self.api_key is not None:

                writer = csv.writer(file)
                # CSV with header
                writer.writerow(['API Key', self.api_key])
    


    else:
        pass

from . import __name__


class GPTScriptFileItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="Script Name")
    script_filepath: bpy.props.StringProperty(name="Script Filepath")


class FAST_Properties(bpy.types.PropertyGroup):
    is_restarting: bpy.props.BoolProperty(name="Internal", default=False)
    collect_error_message_only: bpy.props.BoolProperty(
        name="Enable Anonymous Error Reporting",
        description=(
            "This property enables anonymous error data reporting.\n\n"
            "If enabled, the system captures error messages using the 'traceback' library.\n\n"
            "It sends only the full error message and line number to us, ensuring no sensitive data is included.\n\n"
            "The function handling this is located at the top of the FAST Global file, it's named 'capture_and_copy_traceback'.\n\n"
            "If an error occurs, the system will email the error details to us automatically,\n\n"
            "allowing us to test, fix, and send updates quickly.\n\n"
            "If this property is enabled, you do not need to manually report errors.\n\n"
            "By default, this property is disabled (False).\n\n"
            "If you enable it and see 'Error details sent successfully.' under an error message,\n\n"
            "you can relax as we are already working on a fix.\n\n"
            "If you do not see this message, click 'Report Issues' to notify us.\n\n"
            "On the FAST Messages panel, this setting can be toggled on at any time.\n\n"
            "This ensures you have control over whether error reporting is active.\n\n"
            "Please note: If you enable this property, errors will be emailed to us anonymously."
        ),
        default=False
    )
    run_it_first_2: bpy.props.BoolProperty(default=True)
    gpt_re_add_able_error: bpy.props.StringProperty(name="Internal", default="")
    gpt_q_run: bpy.props.BoolProperty(default=False)
    new_addition: bpy.props.BoolProperty(default=False)
    gpt_error_line: bpy.props.StringProperty(default="")
    verbose_tooltips: bpy.props.BoolProperty(
        name="Verbose Tooltip", description="Toggle tooltip verbosity for operator and property tool-tips.", default=False
    )
    sna_imprompt: bpy.props.StringProperty(
        name="Image Prompt",
        description="Enter the necessary prompt to create your image here",
        default="",
      
    )

    sna_serpenspathimg: bpy.props.StringProperty(
        name="Image Path",
        description="receives the path where your image is saved",
        default="",
      
    )

    sna_imprompt: bpy.props.StringProperty(
        name="Prompt",
        description="Image prompt for generation",
        default=""
    )
    
    sna_currentstatus: bpy.props.StringProperty(
        name="Current Status",
        description="Current status of the operation",
        default=""
    )

    sna_statusfloat: bpy.props.FloatProperty(
        name="Status Progress",
        description="Progress of the operation",
        default=0.0,
        min=0.0,
        max=1.0
    )
    
    sna_serpenspathimg: bpy.props.StringProperty(
        name="Generated Image Path",
        description="Path to the generated image",
        default=""
    )

    timeout_duration_prop: bpy.props.FloatProperty(
        name="Timeout Duration",
        default=5.0,
        min=0.01,
        max=5.0,
        description="Duration (in seconds) to speak your search term",
    )

    verbose_logging: bpy.props.BoolProperty(
    default=False,
    description="Enables verbose logging. When off, won't see API/manual lookups, code, and others. Developers turn this on."
    )

    new_section: bpy.props.BoolProperty(default=False)

    restarting_blender: bpy.props.BoolProperty(default=False)

    draw_open: bpy.props.BoolProperty(default=False)

    gpt_do_not_save_userpref_while_running: bpy.props.BoolProperty(
        default=False,
        description=(
            "Disable saving prefs while running AGPT-4. Not recommended under normal circumstances, "
            "as saving preferences ensures consistent behavior. However, this can be useful for creating,"
            "clean console outputs or demonstration videos."
        )
    )

    gpt_img_run: bpy.props.BoolProperty(
        default=False,
        description=(
            "Generates an image you describe in your user command and applies it to an image plane."
        )
    )

    semitones: bpy.props.IntProperty(
        name="Semitones",
        description="Pitch shift in semitones",
        default=0,
        min=-12,
        max=12,
        step=1,
    )

    gpt_random_user_command_line_count: bpy.props.IntProperty(
        name="Random Command Line Count",
        description="The max number of commands the random user command can have (influences script length.)",
        default=10,
        min=1,
        max=100
    )

    

    gpt_test_mode: bpy.props.BoolProperty(default=False)
    te_script_not_tested: bpy.props.BoolProperty(default=False)
    gpt_show_code_to_be_fixed: bpy.props.BoolProperty(default=False)
    

    new_addition: bpy.props.BoolProperty(default=False)

    gpt_do_not_save_userpref_while_running: bpy.props.BoolProperty(
        default=False,
        description=(
            "Disable saving prefs while running AGPT-4. Not recommended under normal circumstances, "
            "as saving preferences ensures consistent behavior. However, this can be useful for creating,"
            "clean console outputs or demonstration videos."
        )
    )

    gpt_img_run: bpy.props.BoolProperty(
        default=False,
        description=(
            "Generates an image you describe in your user command and applies it to an image plane."
        )
    )

    gpt_error_mssg_list: bpy.props.StringProperty(name="Temp User Command", description="Internal", default="")

    se_boosted_user_command: bpy.props.StringProperty(name="Internal", default="")

    print_example_message: bpy.props.BoolProperty(name="Internal", default=False)
    
    last_clip_name: bpy.props.StringProperty(name="Internal", default="")
    
    previous_file_id: bpy.props.StringProperty(name="Internal", default="")
    
    gpt_error_mssg_list: bpy.props.StringProperty(name="Temp User Command", description="Internal", default="")
    
    gpt_temp_edit_user_command_prompt: bpy.props.BoolProperty(name="Temp Edit User Command Prompt", description="Internal", default=False)
    
    gpt_temp_user_command: bpy.props.StringProperty(name="Temp User Command", description="Internal", default="")
    
    gpt_temp_confirm_object_is_selected: bpy.props.BoolProperty(name="Temp Confirm Object Is Selected", description="Internal", default=False)
    
    gpt_temp_boost_user_command: bpy.props.BoolProperty(name="Temp Boost User Command", description="Internal", default=False)
    
    gpt_temp_find_code_examples: bpy.props.BoolProperty(name="Temp Find Code Examples", description="Internal", default=False)
    
    gpt_temp_run_final_script: bpy.props.BoolProperty(name="Temp Run Final Script", description="Internal", default=False)
    
    gpt_temp_random_user_command: bpy.props.BoolProperty(name="Temp Random User Command", description="Internal", default=False)
    
    gpt_temp_run_lookups: bpy.props.BoolProperty(name="Temp Run Lookups", description="Internal", default=False)
    
    se_changed_values: bpy.props.BoolProperty(name="Internal", default=False)
    
    gpt_show_console_on_run: bpy.props.BoolProperty(name="Show Console on Run", default=True)
    
    full_error_message: bpy.props.StringProperty(name="Internal", default="")

    use_o1_mini_model: bpy.props.BoolProperty(
        name="Use O1 Mini Model",
        description="Enable/Disable usage of the latest O1 model for script generation only.\n\n"
                    "Requests to fixed code will automatically use the GPT 4o model.\n\n"
                    "The O1 model is highly adept at reasoning and provides an improved,\n\n"
                    "script output compared to previous models",
        default=True,
    )

    use_o1_model: bpy.props.BoolProperty(
        name="Use O1 Mini Model",
        description="Enable/Disable usage of the latest O1 model for script generation.\n\n"
                    "The O1 model is highly adept at reasoning and provides an improved "
                    "script output compared to previous models.",
        default=True,
    )

    gpt_beep_volume: bpy.props.FloatProperty(
        name="GPT Beep Volume",
        description="The volume of the beep sound",
        default=0.1,
        min=0.0,
        max=1.0,
    )

    gpt_show_cost: bpy.props.BoolProperty(
        name="Show Tokens",
        description=("Shows the token printouts in the console so you could see token usage per function. \n\nYou can turn this on at anytime while your code is processing"),
        default=False
    )

    beep_frequency: bpy.props.IntProperty(
        name="Fast Frequency",
        description="The frequency of the beep sound",
        default=963,
        min=1,
        max=2500,
    )

    beep_duration: bpy.props.IntProperty(
        name="Fast Duration",
        description="The duration of the beep sound in milliseconds",
        default=635,
        min=1,
        max=2500,
    )

    beep_volume: bpy.props.FloatProperty(
        name="Fast Volume",
        description="The volume of the beep sound (0.0 to 1.0)",
        default=0.1,
        min=0.0,
        max=1.0,
    )

    use_beep: bpy.props.BoolProperty(
        name="Use Beep",
        description="Enable/Disable BEEP for all operators that use.\n\nSome operators do use beep functionality to alert you,\n\nbut do so as a secondary measure only.\n\nBeep settings are on the FAST AUDIO panel\n\nDon't hear beep?? Turn up System Sounds in your OS",
        default=True,
    )
    
    restart_after_addons: bpy.props.BoolProperty(
        name="Restart Blender After Add-Ons",
        description="Setting a property to True to restart Blender after installing add-ons to improve window handling",
        default=False  
    )

    restart_after_addon_enabled: bpy.props.BoolProperty(
        name="Restart Blender After Addon Enabled",
        description="Setting a property to True to restart Blender after you enable addon to improve window handling",
        default=False  
    )

    restart_after_dependencies: bpy.props.BoolProperty(
        name="Restart Blender After Dependencies",
        description="Setting a property to True to restart Blender after installing dependencies to improve window handling",
        default=False  
    )

    restart_after_update: bpy.props.BoolProperty(
        name="Restart Blender After Update",
        description="Setting a property to True to restart Blender after installing update to improve window handling",
        default=False  
    )

    restart_after_key: bpy.props.BoolProperty(
        name="Restart Blender After Key",
        description="Setting a property to True to restart Blender after keying to improve window handling",
        default=False  
    )

    restart_after_verify: bpy.props.BoolProperty(
        name="Restart Blender After Verify",
        description="Setting a property to True to restart Blender after verifying to improve window handling",
        default=False  
    )

    gpt_visual_verification: bpy.props.BoolProperty(
        name="GPT Visual Verification",
        description="Enables GPT to take screenshots during the error checking process to verify operations visually.",
        default=True
    )



    test_tensorflow: bpy.props.BoolProperty(
        name="Import TensorFlow Library at Startup",
        description=(
            "With this selected, Tensorflow will be imported during Blender's startup.\n\n"
            "This ensures the Tensorflow library included with the add-on is ready for scripts.\n\n"
            "As TensorFlow can take 3-5 seconds to import, Leaving unchecked default allows for fast startups"
        ),
        default=False
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "test_tensorflow")

    toggle_pip_print_statements: bpy.props.BoolProperty(
        name="Toggle Pip Print Statements",
        description=("Turns off the print statements that shows which PIP libraries we import at startup"),
        default=False
    )

    handler_processing: bpy.props.BoolProperty(name="Internal", default=False)

    startup_done_1: bpy.props.BoolProperty(name="Internal", default=False)

    startup_done_2: bpy.props.BoolProperty(name="Internal", default=False)

    run_once_prop: bpy.props.BoolProperty(name="Internal", default=False)

    ran_checker_from_outside_main_code: bpy.props.BoolProperty(name="Internal", default=False)
    
    gpt_using_data: bpy.props.BoolProperty(name="Internal", default=False)

    gpt_choose_to_take_snapshot: bpy.props.BoolProperty(
        name="GPT Choose to Take Snapshot",
        description=(
            "Check this property to take a screenshot of your entire screen instead of,\n\n"
            "using an image that you supplied in the 'Node Image Path' box"
        ),
        default=True
    )

    gpt_data_limit: bpy.props.IntProperty(
        name="GPT Data Limit",
        description=
        "Default value is 5000 characters. Increase it if you need to, but realize,\n\n"
        "that this could increase token usage quite a bit. So if you do increase it past,\n\n"
        "5000, which is already pretty high, then keep looking at your credit usage on the website,\n\n"
        "and see how much it costs you every time you run it with that amount of data",
        default=5000,
        min=1,
        max=20000,
    )


    se_show_content: bpy.props.BoolProperty(
        name="Show Body Content",
        description=("Shows the body content of the Stack Exchange questions we're scanning.\n\nYou can turn this on at anytime while your code is processing"),
        default=True
    )
    gpt_show_tokens: bpy.props.BoolProperty(
        name="Show Tokens",
        description=("Shows the token printouts in the console so you could see token usage per function. \n\nYou can turn this on at anytime while your code is processing"),
        default=False
    )
    gpt_show_keyword_on_printout: bpy.props.BoolProperty(
        name="Show Keyword on User Command",
        description=("We remove it from user command console printout for decorative purposes, this will reverse that"),
        default=False
    )
    set_output_sound_file_level: bpy.props.FloatProperty(
        name="Set Output File Sound Level",
        description=
        "Automatically sets the volume of the clip after you get done recording",
        default=1.0,
        min=1.0,
        max=100.0,
    )

    force_solid_mode: bpy.props.BoolProperty(
        name="Force Solid Mode",
        description="If checked, forces solid mode whenever a scene is opened or restart feature is used",
        default=False  # You can change this to True if you want it enabled by default
    )

    disable_restart_blender: BoolProperty(
        name="Disable Restart Blender",
        description="Disable the Restart Blender option in the right-click context menu",
        default=True,
        
    )
    disable_save_startup: BoolProperty(
        name="Disable Save Startup File",
        description="Disable the Save Startup File option in the right-click context menu",
        default=True,
        
    )
    disable_delete_startup: BoolProperty(
        name="Disable Delete Startup File",
        description="Disable the Delete Startup File option in the right-click context menu",
        default=True,
        
    )

    # New Properties for Vernors Ginger Ale Section
    disable_show_console: BoolProperty(
        name="Disable Show Console",
        description="Disable the Show Console option in the right-click context menu",
        default=True,
    )
    
    disable_n_panel: BoolProperty(
        name="Disable N-Panel",
        description="Disable the N-Panel option in the right-click context menu",
        default=True,
    )
    
    disable_verbose_tool_tips: BoolProperty(
        name="Disable Verbose Tooltips",
        description="Disable the Verbose Tooltips option in the right-click context menu",
        default=True,
    )

    gpt_last_examples_vector_store_id: bpy.props.StringProperty(name="Internal", default="")

    gpt_first_code: bpy.props.StringProperty(name="Internal", default="")
        
    gpt_file_path_notification: bpy.props.BoolProperty(name="Internal", default=False)

    gpt_final_print_string: bpy.props.StringProperty(name="Internal", default="{}")

    fast_lines_of_code: bpy.props.StringProperty(name="Internal", default="7,197,771")

    alm_processing: bpy.props.BoolProperty(name="Internal", default=False)

    # alm_ready_for_undo: bpy.props.BoolProperty(name="Internal", default=False)

    inst_dependencies: bpy.props.BoolProperty(name="Internal", default=False)

    gpt_re_run_script_checker: bpy.props.BoolProperty(name="Internal", default=False)

    gpt_last_added_code_base_name: bpy.props.StringProperty(name="Internal", default="")

 

    gpt_choose_random_command_type: bpy.props.BoolProperty(
        name="GPT Random Command Type",
        description=(
            "Choose type, Blender or standard Python, of random user command."
        ),
        default=True
    )



    gpt_re_add_able_blender_output: bpy.props.StringProperty(name="Internal", default="")

    gpt_re_add_able_code: bpy.props.StringProperty(name="Internal", default="")

    gpt_set_panel_enable: bpy.props.BoolProperty(name="Internal", default=False)

    bmesh_register: bpy.props.BoolProperty(name="Internal", default=False)

    se_fix_code: bpy.props.BoolProperty(name="Internal", default=False)

    se_user_command_pass: bpy.props.StringProperty(name="Internal", default="")

    se_error_message_pass: bpy.props.StringProperty(name="Internal", default="")

    se_user_command: bpy.props.StringProperty(name="Internal", default="")

    allow_auto_gpt_assistant: bpy.props.BoolProperty(name="Internal", default=False)

    se_pull_cancel_op: bpy.props.BoolProperty(name="Cancel Pull Operation", default=False)

    updating_from_panel: bpy.props.BoolProperty(name="Cancel Pull Operation", default=False)

    gpt_edit_user_command_prompt: bpy.props.BoolProperty(
        name="Show Edit User Command Prompt",
        description=(
            "Check this to regain the prompt to edit your user command in the console.\n\n"
            "The prompt was added to the console in the 1st Place because the user command is so important.\n\n"
            "If you toggle this off please make sure to keep that in mind and check it before you run AGPT-4.\n\n"
            "It's in the checklist to serve as a visual reminder to check user command"
        ),
        default=False
    )

    gpt_send_anonymous_data: bpy.props.BoolProperty(
        name="Send Anonymous Error Data",
        description=(
            "Enable this option to send the red error section (only) to our public GitHub repository if the\n\n"
            "Autonomous GPT-4 functionality encounters the same error for every iteration.\n\n"
            "This helps us identify and address issues, such as missing login credentials for the SMTPLIB library,\n\n"
            "incorrect file paths being added, or access denied errors or other unforeseen errors.\n\n"
            "When enabled, this feature will automatically send the error message to a publicly accessible\n\n"
            "file on GitHub. No personal information, such as email addresses, is collected or transmitted.\n\n"
            "The data is used solely for improving the add-on's functionality and ensuring it performs\n\n"
            "smoothly for all users.\n\n"
            "We appreciate your help in making the Autonomous GPT-4 functionality more robust. You can view\n\n"
            "the collected error messages on our public GitHub repository to stay informed about the issues\n\n"
            "we are addressing.\n\n"
            "The function we use to collect data is at the top of the fast_global.py file in scripts/addons/FAST.\n\n"
            "You can inspect the function we use and search for the function name, which is 'append_error_to_github',\n\n"
            "in all the files in the add-on to inspect where it's used.\n\n"
            "Just so you know, we're being completely transparent in what we collect"
        ),
        default=False
    )

    image_save_index: bpy.props.IntProperty(
        name="Image Save Index",
        description="Tracks the index for saved images",
        default=1
    )
    register_done_bse: bpy.props.BoolProperty(name="Register Done N Panel", default=False)
    register_done_gpt: bpy.props.BoolProperty(name="Register Done GPT", default=False)
    
    copy_traceback: bpy.props.BoolProperty(
        name="Copy Traceback",
        description="Enable/Disable copying of traceback information to the clipboard on error",
        default=True, 
    )

    collect_error_message_only: bpy.props.BoolProperty(name="Register Done N Panel", default=False)
    
    play_error_sound: bpy.props.BoolProperty(
        name="Enable Error Sound",
        description="Enable this checkbox to get an audible warning when you encounter an error in the add-on.",
        default=False
    )

    restart_after_addon_enabled: bpy.props.BoolProperty(
        name="Restart Blender After Addon Enabled",
        description="Setting a property to True to restart Blender after you enable addon to improve window handling",
        default=False  
    )



    gpt_file_permission_fixer_path: bpy.props.StringProperty(
        name="File Permission Fixer Path",
        description=(
            "This path is used when fixing FILE PERMISSION errors in file paths within your generated scripts.\n\n"
            "If the path causing the error is for non-critical data like saving renders or writing log files,\n\n"
            "it will be replaced with this path. The default path is set to a folder on your desktop named 'AGPT-4'.\n\n"
            "This prop is shown for reference only, so you know what the code is doing, this path cannot be changed"
  
        ),
        default="os.path.join(os.path.expanduser('~'), 'Desktop', 'AGPT-4')",
        maxlen=1024,
        subtype='FILE_PATH',
        update=update_gpt_file_permission_fixer_path
    )

    gpt_smtp_lib_username: StringProperty(
        name="SMTP Username",
        description="This is your email address (e.g., your_email@gmail.com) that will be used for SMTP authentication.\n\n"
        "Refer to the 'App Password' tooltip for more information on what these properties are for",
        default="",
    )

    gpt_smtp_lib_app_password: StringProperty(
        name="SMTP App Password",
        description="This is your SMTP app password. You only need to provide this if you are intending to ask,\n\n" 
                    "AGPT-4 to generate code that uses the SMTPLIB library to send emails (e.g., through Gmail).\n\n" 
                    "The username will be your email address (e.g., your_email@gmail.com).\n\n" 
                    "To generate an app password for Gmail, follow these steps:\n\n"
                    "1. Go to your Google Account.\n"
                    "2. Select 'Security'.\n"
                    "3. Under 'Signing in to Google', select 'App Passwords'.\n"
                    "4. Sign in...At the bottom, choose 'Select app' and 'Select device' and choose the appropriate options.\n"
                    "5. Follow the instructions to generate the app password.\n\n"
                    "If you don't know what the SMTPLIB library is, you don't need to worry about this setting.\n\n"
                    "If these credentials are provided, you can request the Autonomous GPT-4 operator to generate scripts,\n\n" 
                    "for you that will send emails. For example, you could request a script to automatically send an email,\n\n"
                    "when a process is completed in Blender. Ensure your user command includes something like,\n\n" 
                    "'write a script that will use the SMTPLIB library to send an email' so the assistant understands your request",
        default="",
        subtype='PASSWORD'
    )
    
    gpt_smtp_lib_server: StringProperty(
        name="SMTP Server",
        description="This is the SMTP server for your email provider. For Gmail, this should be 'smtp.gmail.com'.\n\nEnsure the SMTP server matches your email provider's settings.",
        default="smtp.gmail.com",
       
    )

    gpt_node_image_path: StringProperty(
        name="Node Image Path",
        description="\nPath to the screenshot image or add your own image here.\n\n"
                    "Make sure the path is correctly specified to avoid errors during script execution.\n\n"
                    "The path to the screenshot is auto added here so can be opened with 'Open Image'",
        default="",
        maxlen=1024,
        subtype='FILE_PATH',
        update=update_gpt_node_image_path,
    )
    

    gpt_confirm_object_is_selected: bpy.props.BoolProperty(
        name="Confirm Object Is Selected",
        description="This replaces the object reference section that showed up in the console.\n\n"
            "This property is toggled off when operator finishes or restart Blender so important to check each time.\n\n"
            "Checklist:\n"
            "1. Are objects needed by the script?\n"
            "2. Are the objects selected?\n"
            "3. If no, select the objects, then check this property.\n\n"
            "Confirmation Information:\n"
            "1. If you check this, a reference will be added and the current file will be used.\n"
            "2. If you check this, the objects will be referenced for you in the user command (internally) without changing the file.\n"
            "3. If you check this, your Blender file containing the objects will be used for error tests.\n\n"
            "Note: If providing bone data, the rig must be selected",
        default=False
    )

    gpt_confirm_data: bpy.props.BoolProperty(
        name="Confirm Object Is Selected",
        description=("This replaces the data confirmation section that showed up in the console.\n\nIf checked it will automatically confirm yes for you,\n\nif unchecked the confirmation dialog will show up as normal.\n\nIf using 'Pull SE & BSE Examples' button to generate an example,\n\nthis is toggled off just so we could be sure that you meant to send bone or node data"
        ),
        default=False
    )

    gpt_boost_user_command: BoolProperty(
        name="Boost User Command",
        
        description="Checked: Autonomous GPT-4 analyzes request, added user instruction sets + Blender 4.3 manual to, \n\n"
                    "refine your request. Doesn't alter your initial goal but provides a detailed command that, \n\n"
                    "matches your intended purpose. Ideal for solving complex issues with greater precision. \n\n"
                    "You don't have to look up the manual to accomplish tasks in Blender! \n\n"
                    "Hint: Boosted command is auto-added to user command file. \n\n"
                    "Hint: 'user-command-backup.txt' is created before boost, next to 'user-command.txt'.",
        
        default=True,
        update=update_gpt_boost_user_command)
        
                    # Save as reminder to get this added
                    # "Note: If adding code in example file you got off Blender Stack Exchange for example,\n"
                    # "       when this is checked, it will pick that up and verify it for you against the Blender manual,\n"
                    # "       and output the new user command as a nicely verified set of instructions.\n"
                    # "       You can rerun Autonomous GPT-4 with those inst. & remove the code if script generation fails,\n"
                    # "       retrying that way may help as maybe manual verified inst. are better than poss. outdated code.\n\n"

    gpt_advanced_boost_user_command: bpy.props.BoolProperty(
        name="Use Advanced Model for Boost User Command",
        description="Check to use the advanced GPT-4o model for boosting user command.\n\n"
                    "When checked it also looks up the API which will improve your script.\n\n"
                    "Standard boost uses the GPT-4o mini model, this uses the GPT-4o model.\n\n"
                    "Costs more but some e.g. scripts for modeling, may require it to be successful",

        default=False,
        update=update_gpt_advanced_boost_user_command
    )


    pull_se_examples_iterations: bpy.props.IntProperty(
        name="SE Search Iterations",
        description="Number of iterations for searching Stack Exchange.\n\n"
            "Make sure to set this to a reasonable amount, or you risk not getting good example.\n\n"
            "For example, setting it to 10 may not find any good matches, whereas 100 ensures better results.\n\n"
            "The A.I. deciding if example pertains to user command needs enough iterations to find good examples.\n\n"
            "If unsure just leave at 50, better to spend 5 minutes here and have a better chance at a good script.\n\n"
            "I've got good standard Python examples set to 10...for Blender Python I set to 50 as BSE has less examples\n\n"
            "If you change your mind while the scanner is running you can change iterations and it'll recognize it in real time\n\n"
            "Note: We allow the slider to go down to one for tests but ten is the minimum recommended.",
        default=25,
        min=1,
        max=200,
    )
    bse_search_term: bpy.props.StringProperty(
        name="BSE Search Term",
        description="Enter a search term to look up on Blender Stack Exchange.\n\nA precursor to AGPT-4 Auto-BSE lookup (providing here until I get it implemented)",
        default=""
    )
    bse_search_result: bpy.props.StringProperty(
        name="BSE Search Result",
        description="Internal",
        default="",
        options={'HIDDEN', 'SKIP_SAVE'}
    )

    bse_search_light_button: bpy.props.BoolProperty(
        name="Internal",
        description="Internal",
        default=False
    )

    bse_accepted_answer_id: bpy.props.IntProperty(
        name="Accepted Answer ID",
        description="Internal",
        default=False
    )

    bse_current_line: IntProperty(
        name="BSE Current Line",
        description="Current line being processed in the BSE scan",
        default=0,
        min=0,
        max=300000,
        update=update_bse_current_line
    )

    bse_fix_code: bpy.props.BoolProperty(
        name="BSE Fix Code",
        description="Internal",
        default=False
    )

    bse_scan_cancel_op: bpy.props.BoolProperty(
        name="Cancel Scan Operation",
        description="Internal",
        default=False
    )

    gpt_allow_change_instruction_sets: bpy.props.BoolProperty(
        name="Allow Change Instruction Sets",
        description=(
            "\nPlease read all 'AGPT-4' documentation before you attempt the following...this includes reminder of key points\n\n"
            "When this feature is on, all inst set files in the 'AGPT-4 Instructions' directory, that are shipped with the add-on,\n\n" 
            "can be edited. Normally they cannot because they're set to be auto created/verified at Blender startup.\n\n"
            "E.G. If you make a mistake, turn this property off + restart Blender, and they'll all be regenerated.\n\n"
            "If the files get deleted, turning this property off/restarting Blender will regenerate them.\n\n"
            "It's recommended to be very careful because the inst sets are a culmination of 4 months of design.\n\n"
            "Pls read the 'Edit User Instruction Set' info + all other documentation before attempting edits.\n\n"
            "Even though you could edit the base instructions...for WRITE-CODE in 'AGPT-4 Instructions/script_generation',\n\n"
            "it's recommended to duplicate it per the instructions in 'Edit User Instruction Set' info button, which say, partly,\n\n"
            "....it's recommended to not change WRITE-CODE keyword...but make a derivative inst. set containing its contents ++\n\n"
            "other concise instructions you would like to add to it, as those inst are well made/will ensure new inst. set works.\n\n"
            "You can't create a derivative for ('fix-code, fix-py, standard-q, blender-q, fast-4-mini, fast-4),\n\n"
            "like you can with the WRITE-CODE keyword, the system will not recognize it, as it looks for those names directly.\n\n"
            "PROC-MAT, ANIM-INST, THEME-INST are already derivatives of WRITE-CODE(contain its instructions) edit them how you choose.\n\n"
            "If you remove any instruction from them they will not work as well, you can try to make them better but please be careful,\n\n"
            "e.g. change 1 inst of a set at a time, in response to an issue you're having, if change doesn't help, revert/try again.\n\n"
            "Note: Please do not change these file names: (write-code, write-py, fix-code, fix-py, standard-q, blender-q, fast-4-mini, fast-4).\n\n"
            "They are looked for by name by AGPT-4 so please only edit the contents of those files"
        ),
        default=False
    )

    gpt_blender_stack_exchange_title: StringProperty(
        name="Blender Stack Exchange Title",
        description="Title for Blender Stack Exchange 'Accepted Answer' code you retrieved from 'Scan BSE For Errors'.",
        default="",
    )
    gpt_blender_stack_exchange_tag: StringProperty(
        name="Blender Stack Exchange Tag",
        description="Tag to append to fixed scripts when added to local Blender Stack Exchange 'Posts.xml' file.\n\nThis tag cannot be changed, it's here so you know what to search for in the,\n\nfile to locate sections that have been changed.\n\n'Posts.xml' File Path: '\FAST\data\autogpt\BSE\Posts.xml'",
        default="#AutoGPT_Fix",
        update=update_gpt_blender_stack_exchange_tag
    )

    gpt_find_code_examples: bpy.props.BoolProperty(
        name="Find Examples",
        description="Find code examples from FAST Add-on by analyzing your user command.\n\nWhen requesting code on ChatGPT we always give it examples from our add-on,\n\nand as that works EXTREMELY WELL, we incorporated it into AGPT-4.\n\nThis costs $0.10 and it needs to boost your user command to work and that adds $0.10.\n\nThis works irrespective of the boost feature being on.\n\nWhy analyze boosted user command and not original user command??\n\nBecause when user command is boosted it's verified against the Blender 4.3 manual,\n\nand it's important when searching for examples to verify user command gives proper instr.\n\nif your user command is a request to fix code, you're provided code to fix is used,\n\nto create a boosted command for this feature",
        default=True,
    )

    gpt_optimize: bpy.props.BoolProperty(
        name="Optimize",
        description="Internal",
        default=False,
    )

    gpt_run_lookups: bpy.props.BoolProperty(
        name="Run Lookups",
        description="Internal.",
        default=True
    )

    gpt_show_lookups: bpy.props.BoolProperty(
        name="Show Lookups",
        description="Turn this property on to show API, Manual, & Code lookup printed output.\n\nOtherwise they aren't printed though still generated and given to 'Autonomous GPT-4'.\n\nYou can turn this on at anytime while your code is processing",
        default=True
    )

    gpt_optimize_set_internally: bpy.props.BoolProperty(
        name="Optimize Set Internally",
        description="Indicates that GPT Optimize was set to true internally.",
        default=False
    )
    
    gpt_o3_mini_total_cost: bpy.props.FloatProperty(
        name="GPT o3 Mini Total Cost",
        description="Calculated cost of GPT o3 Mini usage in dollars and cents.\n\nUpdated automatically.",
        default=0.0,
        precision=2,
    )

    gpt_4o_mini_total_cost: bpy.props.FloatProperty(
        name="GPT 4o Mini Total Cost",
        description="Calculated cost of GPT 4o Mini usage in dollars and cents.\n\nUpdated automatically.",
        default=0.0,
        precision=2,
    )
    gpt_4o_total_cost: bpy.props.FloatProperty(
        name="GPT 4o Total Cost",
        description="Calculated cost of GPT 4o usage in dollars and cents.\n\nUpdated automatically.",
        default=0.0,
        precision=2,
    )
    gpt_o3_mini_total_cost: bpy.props.FloatProperty(
        name="GPT o3 Mini Total Cost",
        description="Calculated cost of GPT o3 Mini usage in dollars and cents.\n\nUpdated automatically.",
        default=0.0,
        precision=2,
    )
    gpt_o1_mini_total_cost: bpy.props.FloatProperty(
        name="GPT o1 Mini Total Cost",
        description="Displays the total cost of GPT o1 Mini usage in dollars and cents, (auto updated based on usage)",  
        default=0.0,
    )
    gpt_verify_code_instructions: bpy.props.BoolProperty(
        name="Pause Before Fixing Errors",
        description="This pauses so you could verify fixes as far as not adhering to instructions.",
        default=True
    )

    gpt_pause_before_fixing_errors: bpy.props.BoolProperty(
        name="Pause Before Fixing Errors",
        description="This pauses after the error is generated before we try to fix the code each iteration,\n\nallowing you to make a quick edit to the code to help it get past an error.\n\nIf you edit code only replace items do not add, otherwise it will not work.\n\nAutonomous GPT-4 will not be able to hold the intended change in memory,\n\nif it doesn't have an item to recognize and replace each iteration.\n\nThis functionality is new and it will improve.\n\nYou can untick this property at any time, and it'll be recognized by Autonomous GPT-4.\n\nFilepath to add edits = 'FAST Settings\AGPT-4 Script Testing\modified_user_script.py'.\n\nThis file is updated each iteration with your, generated code plus extra code added for testing",
        default=False
    )
    
    gpt_use_current_file_for_error_check: bpy.props.BoolProperty(
        name="Save User File for Error Checking",
        description="Checked it saves the current Blender file to a temporary directory for error checking,\n\nUnchecked it uses the Blender default file for error checking.\n\nFile is saved to = '\AppData\Local\Temp\temp_blender_file.blend' (if you need to inspect it)\n\nAs this uses your current file for error checking, selecting any objects,\n\nthat you're asking the script to be written to interact with, will help in error checking process.\n\nThis is connected to a console message that will prompt you to select those object/s.\n\nDisable if using current file it's causing issues in error checking",
        default=False
    )

    gpt_relevant_bones: bpy.props.StringProperty(
        name="GPT Relevant Bones",
        description="Comma-separated list of relevant bone names",
        default="",

    )

    gpt_relevant_bone_frames: bpy.props.StringProperty(
        name="Relevant Bone Frames",
        description="\nComma-separated list of timeline frame numbers",
        default="",
    )

    GPTScriptFileItems: bpy.props.CollectionProperty(
        name="GPT Script Files",
        type=GPTScriptFileItem,  # Specify the correct type for the items in this collection
    )
    


    gpt_list_display_rows: bpy.props.IntProperty(
        name="Display Rows",
        description="Number of items to display in the list at once",
        default=5,
        min=1,
    )

    gpt_run_final_script: BoolProperty(
        name="GPT Run Final Script",
        description="Controls whether to run the final script at the end of processing.\n\nWhen enabled, the script that was generated and refined through the iterations,\n\nwill be executed, resulting in visible changes in the viewport,\n\nsuch as creating objects or applying transformations based on the script's commands.\n\nDisable this if you plan to work on your scene while the script is being created,\n\nor, if you're unsure if the results of script might cause unintended effects in your scene",
        default=True)

    tfe_pass_dependency_message: bpy.props.IntProperty(
        name="Pass dependency message",
        description="Passes the dependency message boolean to the threaded call for the check dependencies operator",
        default=0
    )

    tfe_pass_dependency_string: bpy.props.StringProperty(
        name="Pass dependency message",
        description="Passes the dependency message to the threaded call for the check dependencies operator",
        default=''
    )

    gpt_check_errors_using_default_addons: bpy.props.BoolProperty(
        name="Test Errors Using Default Add-ons",
        description="Disable this to test GPT-generated scripts with default Blender add-ons disabled.\n\n"
                    "To test scripts, Blender starts in Factory Startup Mode, ensuring clean settings.\n\n"
                    "If enabled, default add-ons that you had previously enabled will be re-enabled in this mode,\n\n"
                    "allowing the use of any operators or properties from them to be in your scripts without issue.\n\n"
                    "Allowing only default add-ons provides a stable environment for testing as Blender default add-ons,\n\n" 
                    "are quality checked so are strong enough to be enabled during an error checking subprocess.\n\n"
                    "Note: If requesting code that adds a 'Human Meta Rig' then this would need to checked, as otherwise,\n\n"
                    "you'll get errors in error checking process saying 'can't find: bpy.ops.object.armature_human_metarig_add()\n\n"
                    "If get issue related to this being checked, disable it, try the operation again, otherwise, just leave checked",
        default=True
    )

    gpt_current_iteration: bpy.props.IntProperty(
        name="GPT Max Iterations Panel",
        description="A property that shows the current iteration on the panel.\n\nUnsettable (Just doesn't look good as a label.)",
        default=0,
        min=0,  # Minimum value
        max=20
    )



    gpt_cancel_op: bpy.props.BoolProperty(
        name="Cancel Operation",
        description="Click this to cancel the operation, a bit of a unique method I know to cancel an operator...\n\nbut necessary, as this functionality uses well designed threading which requires a specific cancelation process...\n\n...and...if we made this a toggle button it would interrupt the design of the panel",
        default=False
    )

    gpt_input_waiting: bpy.props.BoolProperty(
        name="Cancel Operation",
        description="If there's a waiting input then switch to the console and press 'q'",
        default=False
    )

    gpt_show_file_confirmation: bpy.props.BoolProperty(
        name="Show File Confirmation",
        description="Check this to show the included file confirmation dialog in the console when run AGPT-4",
        default=False
    )
    
    gpt_clear_screen_on_run: bpy.props.BoolProperty(
        name="Clear Screen on Run",
        description="Clear console history at specific times for a nicer console interface.\n\nNote if you rely on console output, due to our consistent optimization/reordering,\n\nof features, relied on items could get inadvertently hidden when this is checked",
        default=False
    )
    
    gpt_auto_open_text_file: bpy.props.BoolProperty(
        name = "Auto Open Text File",
        description = "Allows the automatic opening of text file when you click 'Add Code Here'.",
        default = True  
    )
    
    
    gpt_run_script_at_end: bpy.props.BoolProperty(
        name="Run Script at End",
        description="Decide whether to run the script at the end or not",
        default=True  # Set the default value to False or True as needed
    )

    # Add the new properties for frequency, duration, and volume
    gpt_beep_frequency: bpy.props.IntProperty(
        name="Fast Frequency",
        description="The frequency of the beep sound",
        default=528,
        min=1,
        max=3000,
    )

    gpt_main_processing_status: bpy.props.BoolProperty(
        name="Main Processing Status",
        description="Indicates whether main processing is active",
        default=False
    )   

    gpt_use_beep: bpy.props.BoolProperty(
        name="Use Beep",
        description="Enable/Disable BEEP for Autonomous GPT-4 operator.\n\nDon't hear beep?? Turn up System Sounds in your OS",
        default=True,
    )

    gpt_operator_name: bpy.props.StringProperty(
        name="Operator Name",
        description="Run 'bpy.ops.fast.autogpt_assistant()' or other Blender operator at startup.\nWe use for testing but you may find it useful too.\nMake sure to add command to 'Command Override'.\nNOTE: Unrelated console errors can block this from working",
        default="bpy.ops.fast.autogpt_assistant()"
    )


    gpt_run_on_selected_objects: bpy.props.BoolProperty(
        name="Run on Selected Object",
        description="If this boolean property is selected, then GPT will apply your script request to this object.\nMake sure to also reference the object by name,\nincluding proper capitalization, in your script generation request",
        default=False
    )

    # gpt_selected_object_names: bpy.props.StringProperty(
    #     name="Selected Objects",
    #     description="If you wish Autonomous GPT-4 to write a script based on your current selection.\nMake sure to tell it exactly what to do to these objects in your script,\nand reference them in your command by the name you see in the 'Outliner' (proper casing).\nEditing text in panel box changes selection in viewport",
    #     default="",
    #     update=update_gpt_selected_object_names

    # )

    gpt_added_code: bpy.props.StringProperty(
        name="Additional Code Path",
        description="Specify path to a file containing additional code for GPT to reference or fix.\nUse keyword 'fix code' in your query when you add python code here",
        subtype='FILE_PATH',
        default=""

    )

    gpt_added_code_prop: bpy.props.BoolProperty(
        name="Added Code Prop",
        description="Internal prop to pass processing for an operation outside function level",
        default=False
    )

    gpt_show_code: bpy.props.BoolProperty(
        name="Show Code",
        description="Toggles the showing of all code in the console.\n\nWe're debating on how to make this functionality more user friendly so added this.\n\nIf you don't code, can turn off the code, and read messages to understand what's happening.\n\nBe aware sometimes it's vital to have this on in order to see what's happening.\n\nAs this improves we'll get closer and closer to making this a 1 click thing,\n\nthat just generates perfect code or auto fixes all code.\n\nYou can turn this on at anytime while your code is processing",
        default=True
    )

    # gpt_show_appended_instructions: bpy.props.BoolProperty(
    #     name="Show Appended Instructions",
    #     description="Show 'User Instruction Set' instructions in the console, e.g. 'write-code' instructions",
    #     default=False
    # )

    # gpt_show_appended_user_instruction_set: bpy.props.BoolProperty(
    #     name="Show Appended User Instruction Set",
    #     description="Show 'User Instruction Set' in the console",
    #     default=False
    # )

    gpt_mode_type: bpy.props.StringProperty(name="Mode Type")



    gpt_text_box_scale: bpy.props.FloatProperty(
        name="Text Box Height Scale",
        description="This is to scale both the 2 above text boxes height",
        default=1.0,  # Default scale is 1.0, adjust as needed
        min=1.0, max=3.0,  # Example range, adjust as needed
        step=0.01
    )

    gpt_full_text: bpy.props.StringProperty(
        name="GPT Full Text",
        description="Holds the content that the panel operator will use to copy user command and code to your clipboard.",
        # maxlen=2048,
        default="",
    )

    gpt_user_command: bpy.props.StringProperty(
        name="GPT User Command",
        description="Create a command override to automatically run 'Autonomous GPT-4' with specified command. Click Info Button=>",
        # maxlen=2048,
        default="",
     
    )

    # Updated tooltip for 'User Instruction Set' property with concise guidance and a streamlined example
    gpt_user_instruction_set: bpy.props.StringProperty(
        name="GPT User Instruction Set: (Will increases token usage if add too many.)",
        description="Create concise user instruction sets to enhance your Autonomous GPT-4 experience. Click Info Button=>",
        default="",
        
    )

    # Updated tooltip for 'User Instruction Set' property with concise guidance and a streamlined example
    gpt_data: bpy.props.StringProperty(
        name="GPT Data",
        description="Internal",
        default="",
        
    )

    gpt_hide_user_command_text: BoolProperty(
        name="Hide User Command",
        description="Hides the command text added from the panel to keep the UI uncluttered.",
        default=True,
    )

    gpt_hide_master_goal_text: BoolProperty(
        name="Hide User Command",
        description="Hides the command text added from the panel to keep the UI uncluttered.",
        default=True,
    )

    gpt_hide_user_instruction_set_text: BoolProperty(
        name="Hide User Instruction Set",
        description="Hides the instruction set text added from the panel for a cleaner UI experience.",
        default=True,
    )
    
    tfe_startup_check_counter: IntProperty(
        name="Startup Check Counter",
        description="Counts the number of Blender startups to trigger the check update functionality every five times. Resets after triggering.",
        default=1,
        min=1, 
        max=10
    )

    gpt_character_usage: bpy.props.IntProperty(
        name="GPT Character Usage",
        description="Character count as Autonomous GPT-4 runs have a 32768 character limit & adding instruction sets adds characters",
        default=0
    )

    gpt_error_check_timeout: bpy.props.IntProperty(
        name="Blender Quit Timeout",
        description=(
            "Autonomous GPT-4 scripts are tested in a Blender subprocess.\n\n"
            "Adjust the amount of time here Blender waits before quitting after running in a subprocess.\n\n"
            "This is a delay to ensure your script has enough time to finish executing.\n\n"
            "A minimum of 15 seconds is hard coded for safety.\n\n"
            "If you encounter issues with Blender not starting fully, increase this timeout.\n\n"
            "This helps to ensure that error messages are fully captured.\n\n"
            "To keep an eye on this, check the 'Error Check in Foreground Mode' property and rerun the operator.\n\n"
            "When 'TESTING IN FOREFROUND MODE' is printed in console's red error test section, Blender's starting then.\n\n"
            "If Blender doesn't start fully, before it quits in 10 + (this value) seconds, increase the quit timeout."
        ),
        default=15,
        min=15,
        max=120,
    )

    gpt_model: bpy.props.EnumProperty(
        name="GPT Model",
        items=[
            ("gpt-4o", "gpt-4o", "GPT-4o: First Choice. Latest flagship model, it's the best and cheapest"),
            ("o3-mini", "o3-mini", "o3-mini: Latest miniature version of the o3 model, optimized for reasoning tasks in coding, mathematics, and science."),
        ],
        default="gpt-4o",
        description="GPT-4o is the best-tested model and provides the most reliable results.\n\n"
                    "o3-mini can output extremely long scripts when given large instruction sets.\n\n"
                    "We tested this by running the 'Random User Command' function at the top of the panel,\n\n"
                    "setting the 'command_length' variable to 20, and it produced a 600+ line script.\n\n"
                    "Even though o3-mini is half the price of GPT-4o, running the 'Our Functionality'\n\n"
                    "(generator with automatic error fixing) in 5 iterations may cost the same as\n\n"
                    "using GPT-4o on a 300-line script. But we're still analyzing this and it actually may cost way more.\n\n"
                    "Monitor your OpenAI usage to avoid unexpected costs, especially for long scripts.\n\n"
                    "And use the o3-mini model at your own risk.\n\n"
                    "We're uploading the capability to use this despite the fact we haven't got a perfect result,\n\n" 
                    "with the script generator, as far as the error fixing being applied properly to it's output...\n\n"
                    "This is because outputting long scripts is still impressive,\n\n"
                    "and you could break its output down into 2 or 3 sections and use the text editor error,\n\n" 
                    "fixing functionality in order to fix it piece by piece manually (ask ChatGPT how to do this).\n\n"
                    "The verbose tooltip system in this add-on does **not** apply to this property.\n\n"
                    "It is important that you always see this information.\n"
    )


    gpt_advanced_api_or_manual_or_fast_decider: bpy.props.BoolProperty(
        name="Use Advanced Model for API/Add-on/Manual Decider",
        description="Check to use the advanced GPT-4o model for deciding whether to send API lookup, manual lookup, add-on lookup information or extra add-on lookup information to GPT.\n\nWe only send 1 of the 4 each iteration to avoid confusing it with too much data.\n\nThis costs around $0.03 per use, while the standard GPT-4 mini model costs about $0.01.\n\nRun Autonomous GPT-4 to see decision-making process in console, then check this box to compare.\n\nNote: This setting doesn't apply when using the blender-q or standard-q keywords",
        default=False
    )
    

    # Boolean property to choose whether to auto-add the command
    gpt_choose_auto_run_command: bpy.props.BoolProperty(
        name="GPT Choose Auto Add Command",
        description="Enable or disable automatic addition of GPT command",
        default=False  # Default value is False
    )
    
    autogpt_processing: bpy.props.StringProperty( 
        name="Is GPT Processing??",
        description="Indicates if GPT-4 processing is currently active",
        default='Autonomous GPT-4'
    )

    fast_auto_gpt_panel_main_1: bpy.props.BoolProperty(
        name="Autonomous GPT-4 Panel 1",
        description="Disable or enable the FAST AGPT-4 One panel",
        default=True,
    )

    fast_auto_gpt_panel_main_2: bpy.props.BoolProperty(
        name="Autonomous GPT-4 Panel 2",
        description="Disable or enable the FAST AGPT-4 Two panel",
        default=True,
    )

    fast_auto_gpt_panel_main_3: bpy.props.BoolProperty(
        name="Autonomous GPT-4 Panel 3",
        description="Disable or enable the FAST AGPT-4 Three panel",
        default=True,
    )

    edit_user_command: BoolProperty(
        name="Edit User Command",
        description="Allows editing of user commands",
        default=True
    )

    edit_user_instruction_set : BoolProperty(
        name="Edit User Instruction Sets",
        description="Enables editing of user instruction sets",
        default=True
    )
    
    autogpt_assistant: BoolProperty(
        name="Auto GPT Assistant",
        description="Toggle automatic GPT assistant functionality",
        default=True
    )

    openai_template_icon_scale: bpy.props.FloatProperty(
        description="Scale the template icon",
        name="OpenAI Icon Scale",
        default=8.0,
        min=0.00,
        max=8.00,
    )

    gpt_button_scale: bpy.props.FloatProperty(
        name="Button Height Scale 0",
        description="This is to scale the Blender A.I. panel buttons height",
        default=1.00,  # Default scale is 1.0, adjust as needed
        min=1.0, max=3.0,  # Example range, adjust as needed
        step=1
    )

    fast_save_file_text: BoolProperty(
        name="Best Blender Save Solution",
        description="Saves your file, saves your script, saves your preferences",
        default=True,
    )

    show_console_text: bpy.props.BoolProperty(
        name="Toggle Console",
        description="Toggle The Blender system console",
        default=True,
    )

    show_gpt_operator: bpy.props.BoolProperty(
        name="Show GPT Operator",
        description="Toggle to show or hide GPT Operator functionality",
        default=True 
    )

    text_toggle_comment: BoolProperty(
        name="Toggle Comment Custom",
        description="Toggle comment for the selected text",
        default=True,
    )

    text_indent: BoolProperty(
        name="Indent Text", description="Indent the selected text", default=True
    )

    text_unindent: BoolProperty(
        name="Unindent Text", description="Unindent the selected text", default=True
    )

    text_cut: BoolProperty(
        name="Cut Text", description="Cut the selected text", default=True
    )

    text_copy: BoolProperty(
        name="Copy Text", description="Copy the selected text", default=True
    )

    text_paste: BoolProperty(name="Paste Text", description="Paste text", default=True)

    text_select_all: BoolProperty(
        name="Select All Text", description="Select all the text", default=True
    )

    text_print: BoolProperty(
        name="Add Print Statement", description="Adds print statement around selected variable", default=True
    )

    print_extra_example_message: bpy.props.BoolProperty(name="Internal", default=False)
    
    startup_done: bpy.props.BoolProperty(name="Startup Done", default=False)

    startup_done_dependencies: bpy.props.BoolProperty(name="Startup Done Theme", default=False) 

    startup_done_1: bpy.props.BoolProperty(name="Internal", default=False)

    startup_done_2: bpy.props.BoolProperty(name="Internal", default=False)

    console_window_handle: bpy.props.IntProperty(
        name="Console Window Handle", default=0
    )

    
    save_pref: bpy.props.BoolProperty(
        name="Save User Preferences Modal Prop",
        description="Switch for save_user_preferences modal",
        default=False,
    )

    was_restarted_enable_pref: bpy.props.BoolProperty(
        name="Was Restarted Enable Pref",
        description="Flag to indicate if Blender was restarted using the FAST_OT_restart_blender operator.\n\nUsed to make sure enable_pref function is run",
        default=False,
    )

    print_enabled: bpy.props.BoolProperty(
        name="Print Enabled",
        description="Enable or disable printing cancelation logging information for 'Autonomous GPT-4'.",
        default=False,
    )
    
    startup_done: bpy.props.BoolProperty(name="Startup Done", default=False)

    startup_done_dependencies: bpy.props.BoolProperty(name="Startup Done Theme", default=False) 

    enable_done_1: bpy.props.BoolProperty(name="Enable Done 1", default=False)

    enable_done_2: bpy.props.BoolProperty(name="Enable Done 2", default=True)

    register_done: bpy.props.BoolProperty(name="Register Done", default=False)

    register_done_for_enable: bpy.props.BoolProperty(name="Register Done Enable", default=False)
    do_not_scroll: bpy.props.BoolProperty(name="Internal", default=False)
    start_time: bpy.props.FloatProperty(name="Start Time")
    end_time: bpy.props.FloatProperty(name="End Time")
    elapsed_time: bpy.props.StringProperty(name="Elapsed Time")
    restart_after_enabling_addon: bpy.props.BoolProperty(default=False)
    update_available: bpy.props.BoolProperty(
        name="Is update available",
        description="Result of the check add on version operator",
        default=False,
    )
    monitor_daz_studio_save_directory: BoolProperty(
        name="Monitor Daz Studio Save Directory [FAST] = [FAST INSTALL DIR]",
        description="Internal",
        default=False,

    )

    downloaded_version: bpy.props.StringProperty(
        name="Downloaded Version",
        description="The downloaded version of the addon or asset",
        default="",
    )
    
    fast: bpy.props.IntProperty(
        name="FAST Update", description="Shows the FAST update button"
    )   
    save_file_before_restart: bpy.props.BoolProperty(
        name="Save File Before Restart",
        description="Whether to save file before restart",
        default=False
    )

    show_restart_message: bpy.props.BoolProperty(
        name="Show Restart Message",
        description="Whether to show the restart message box",
        default=False
    )

    show_restart_message_no_save: bpy.props.BoolProperty(
        name="Show Restart Message No Save",
        description="Whether to show the restart message box",
        default=False
    )

    offset_x: bpy.props.IntProperty(
        name="Mesaage X Offset",
        description="Adjust horizontal placement (pixels) of all centered message boxes",
        default=-10000,
        min=-10000,
        max=10000,
    )
    
    offset_y: bpy.props.IntProperty(
        name="Message Y Offset",
        description="Adjust vertical placement (pixels) of centered message box",
        default=-10000,
        min=-10000,
        max=10000,
    )


    def update_fast_menu(self, context):
        if self.fast_menu:
            for km, kmi in fastmenu_keymaps:
                kmi.active = True
    
        else:
            for km, kmi in fastmenu_keymaps:
                kmi.active = False
                
    fast_menu: bpy.props.BoolProperty(
        name="Implements FAST Menu",
        description="FAST Stacked Context Menu",
        default=True,
        update=update_fast_menu,
    )


    restart_after_enabling_addons: bpy.props.BoolProperty(name="Internal", default=False)

    startup_dependency_info: bpy.props.BoolProperty(
        name="Starup Dependency Info",
        description="Enable or Disable the startup dependency check info box at startup",
        default=False,
    )

    restart_after_addons: bpy.props.BoolProperty(
        name="Restart Blender After Add-Ons",
        description="Setting a property to True to restart Blender after installing add-ons to improve window handling",
        default=False  # Default value is False, meaning Blender won't restart by default
    )

    preferences_window_handle: bpy.props.IntProperty(
        name="Preferences Window Handle", default=0
    )

    file_view_window_handle: bpy.props.IntProperty(
        name="File_View Window Handle", default=0
    )

    blender_main_window_handle: bpy.props.IntProperty(
        name="Blender Main Window Handle", default=0
    )

    adjustable_restart_delay: bpy.props.IntProperty(
        name="Adjustable Restart Delay",
        description="Increase the delay if restart functionality isn't working properly. Recommended increase: 2 or 3 seconds if issue.",
        default=1,  # Default delay set to 2 seconds
        min=1,
        max=5  
    )
    register_done_n_panel: bpy.props.BoolProperty(name="Register Done N Panel", default=False)
