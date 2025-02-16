

import bpy
import os
import sys
import webbrowser

lib_path = os.path.join(os.path.dirname(__file__), "lib")
if lib_path not in sys.path:
    sys.path.append(lib_path)

from .fast_global import *
from .fast_properties import FAST_Properties, GPTScriptFileItem
from .fast_icons import get_icon_id




def write_with_icons(layout, text, use_template_icon, scale):

    if "HORIZONTAL":
        layout = layout.row(align=True)
    else:
        layout = layout.column(align=True)

    for letter_or_number in text:
        if letter_or_number == "?":
            icon = "write_letter_or_number_question_mark"
        elif letter_or_number == ".":
            icon = "my_icon_letter_period"
        elif letter_or_number == "'":
            icon = "my_icon_letter_apostrophe"
        elif letter_or_number == "-":
            icon = "my_icon_letter_dash"
        elif letter_or_number == " ":
            icon = "letter_or_number_space"
        elif letter_or_number.isalpha():  # Checks if the character is alphabetic and converts to lowercase if true
            icon = "write_letter_or_number_" + letter_or_number.lower()
        else:  # Handles numbers and any other characters
            icon = "write_letter_or_number_" + letter_or_number

        if use_template_icon:
            layout.template_icon(icon_value=get_icon_id(icon), scale=scale)
        else:
            
            layout.label(icon_value=get_icon_id(icon))


    return layout

class FAST_OT_fast_issues(bpy.types.Operator):


    bl_idname = "fast.fast_issues"
    bl_label = "FAST ISSUES"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def description(cls, context, event):
        manager = bpy.context.preferences.addons['blender_ai_thats_error_proof'].preferences.Prop
        if manager.verbose_tooltips:
            return (
                "Opens FAST ISSUE FORM at fast-blender-add-ons.com.\n\n"
                "Paste full console output & name & email & phone number (we can call you.).\n\n"
                "ALL requests are handled immediately and fixes uploaded immediately.\n\n"
                "Don't be afraid to click 'Report Issues' if you notice something out of place,\n\n"
                "e.g. A poorly designed interface item, an error, something designed illogically.\n\n"
                "If you see something like that, we would love it if you would tell us as,\n\n"
                "The FAST Addon is gigantic :-D, and we do miss things from time to time :-D"
            )
        else:
            return "Opens FAST ISSUE FORM for reporting issues and getting e-mail/phone support"

    def execute(self, context):
        try:
          
            bpy.ops.fast.info('INVOKE_DEFAULT', message="Opening the web browser...", duration=1)
            webbrowser.open(
                "https://fast-blender-add-ons.com/support/"
            )
            try:
                from selenium.webdriver.common.keys import Keys
                html = driver.find_element_by_tag_name('html')
                html.send_keys(Keys.END)
            except:
                pass

        except Exception as e:
            capture_and_copy_traceback()

            # Print the traceback for debugging
            
            print("An error occurred while copying the console output and log file contents to the clipboard and appending to the FAST_AUTO_SAVE log file:", e)

        return {"FINISHED"}

from . import bl_info


class FAST_Preferences(bpy.types.AddonPreferences):

    bl_idname = "blender_ai_thats_error_proof" 

    Prop:bpy.props.PointerProperty(type=FAST_Properties)
    gpt:bpy.props.PointerProperty(type=GPTScriptFileItem)


    def draw(self, context):
        
        layout = self.layout
        manager = self.Prop

        col = layout.column(align=True)
        

                # Adding custom space using separators
        for _ in range(3):
            col.separator()
        row = col.row(align=True)
        row.alignment = 'CENTER'
        write_with_icons(row, "Blender A.I.", False, 1)

        for _ in range(3):
            col.separator()
    
        box = layout.box()
        marshmallow_peops = box.column_flow(columns=3, align=True)
        col = marshmallow_peops.column()
        col.label(text ="")
        
    
        row = marshmallow_peops.row()
        row.label(text = "Toggle Items On|Off", icon='TEXT', text_ctxt='label')

    
        # New Mount Dew Blast Section: Created for viewport related panels moved here
        mount_dew_blast = box.column_flow(columns=3, align=True)
        mount_dew_blast_row = mount_dew_blast.column()
        mount_dew_blast_row.prop(manager, "fast_auto_gpt_panel_main_1", text="Blender A.I. Panel 1", toggle=True, emboss=True)
        mount_dew_blast_row = mount_dew_blast.row()
        mount_dew_blast_row.prop(manager, "fast_auto_gpt_panel_main_2", text="Blender A.I. Panel 2", toggle=True, emboss=True)
        mount_dew_blast_row = mount_dew_blast.row()
        mount_dew_blast_row.prop(manager, "fast_auto_gpt_panel_main_3", text="Blender A.I. Panel 3", toggle=True, emboss=True)
         # Jolt Cola Section
        jolt_cola = box.column_flow(columns=3, align=True)
        jolt_cola_row = jolt_cola.column()
        jolt_cola_row.prop(manager, "disable_restart_blender", text="Restart Blender", toggle=True, emboss=True)
        jolt_cola_row = jolt_cola.row()
        jolt_cola_row.prop(manager, "disable_save_startup", text="Save Startup", toggle=True, emboss=True)
        jolt_cola_row = jolt_cola.row()
        jolt_cola_row.prop(manager, "disable_delete_startup", text="Delete Startup", toggle=True, emboss=True)
       
        vernors_ginger_ale = box.column_flow(columns=3, align=True)
        vernors_ginger_ale_row = vernors_ginger_ale.column()
        vernors_ginger_ale_row.prop(manager, "disable_show_console", text="Show Console", toggle=True, emboss=True)
        vernors_ginger_ale_row = vernors_ginger_ale.row()
        vernors_ginger_ale_row.prop(manager, "disable_n_panel", text="N-Panel", toggle=True, emboss=True)
        vernors_ginger_ale_row = vernors_ginger_ale.row()
        vernors_ginger_ale_row.prop(manager, "disable_verbose_tool_tips", text="Verbose Tool-tips", toggle=True, emboss=True)
       
        cherry_dr_pepper = box.column_flow(columns=3, align=True)
        
        # Empty row above (adds spacing)
        cherry_dr_pepper_row = cherry_dr_pepper.row()
        cherry_dr_pepper_row.label(text="")  # Just an empty label to maintain structure
        
        # Middle row with the Fast Issues operator
        cherry_dr_pepper_row = cherry_dr_pepper.row()
        cherry_dr_pepper_row.operator("fast.fast_issues", text="Report Issue", emboss=True, depress=True)
        
        # Empty row below (adds spacing)
        cherry_dr_pepper_row = cherry_dr_pepper.row()
        cherry_dr_pepper_row.label(text="")  # Another empty label for centering effect
        
    
filepath_list = {
        "geo": "//asset.obj",
        "anim": "//asset.fbx",
        "render": "//asset.exr"
}


