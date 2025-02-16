


import bpy.utils.previews
import bpy
import os
import traceback
from .fast_global import *


preview_collections = {}

def load_icons():
    try:

        pcoll = bpy.utils.previews.new()

        presets   = bpy.utils.user_resource('SCRIPTS')
        my_icons_dir = os.path.join(presets, 'addons', 'blender_ai_thats_error_proof', 'icons')

        pcoll.load("my_icon_1", os.path.join(my_icons_dir, "icon1.png"), 'IMAGE')
        pcoll.load("my_icon_2", os.path.join(my_icons_dir, "icon5.png"), 'IMAGE')
        pcoll.load("my_icon_3", os.path.join(my_icons_dir, "icon10.png"), 'IMAGE')
        pcoll.load("my_icon_4", os.path.join(my_icons_dir, "icon15.png"), 'IMAGE')
        pcoll.load("my_icon_5", os.path.join(my_icons_dir, "icon_all.png"), 'IMAGE')
        pcoll.load("my_icon_hash", os.path.join(my_icons_dir, "letter-hash.png"), 'IMAGE')
        pcoll.load("my_icon_print", os.path.join(my_icons_dir, "print.png"), 'IMAGE')
        pcoll.load("my_icon_file_red", os.path.join(my_icons_dir, "file-red.png"), 'IMAGE')
        pcoll.load("my_icon_file_green", os.path.join(my_icons_dir, "file-green.png"), 'IMAGE')
        pcoll.load("my_icon_file_blue", os.path.join(my_icons_dir, "file-blue.png"), 'IMAGE')
        pcoll.load("my_icon_file_gray", os.path.join(my_icons_dir, "file-gray-64.png"), 'IMAGE')
        pcoll.load("my_icon_folder", os.path.join(my_icons_dir, "folder.png"), 'IMAGE')
        pcoll.load("my_icon_folder_explorer", os.path.join(my_icons_dir, "folder_explorer.png"), 'IMAGE')
        pcoll.load("my_icon_web", os.path.join(my_icons_dir, "web.png"), 'IMAGE')
        pcoll.load("my_icon_asterix", os.path.join(my_icons_dir, "asterix.png"), 'IMAGE')
        pcoll.load("my_icon_m", os.path.join(my_icons_dir, "my_m.png"), 'IMAGE')
        pcoll.load("my_icon_reimport", os.path.join(my_icons_dir, "reimport.png"), 'IMAGE')
        pcoll.load("my_icon_daz_studio_template", os.path.join(my_icons_dir, ".daz_studio.png"), 'IMAGE')
        pcoll.load("my_icon_openai_template", os.path.join(my_icons_dir, ".openai.png"), 'IMAGE')
        pcoll.load("my_icon_openai_icon", os.path.join(my_icons_dir, ".openai_icon.png"), 'IMAGE')
        pcoll.load("my_icon_daz_studio_button", os.path.join(my_icons_dir, ".daz_studio_button.png"), 'IMAGE')
        pcoll.load("my_icon_right_arrow", os.path.join(my_icons_dir, "right_arrow.png"), 'IMAGE')
        pcoll.load("my_icon_right_arrow_2", os.path.join(my_icons_dir, "right_arrow_2.png"), 'IMAGE')
        pcoll.load("my_icon_connection", os.path.join(my_icons_dir, "connection.png"), 'IMAGE')
        pcoll.load("my_icon_extreme_pbr", os.path.join(my_icons_dir, ".extreme_pbr.png"), 'IMAGE')
        pcoll.load("my_icon_hdri_maker", os.path.join(my_icons_dir, ".hdri_maker.png"), 'IMAGE')
        pcoll.load("my_icon_rig_gns", os.path.join(my_icons_dir, ".rig_gns.png"), 'IMAGE')
        pcoll.load("my_icon_mixamo_com", os.path.join(my_icons_dir, ".mixamo_com.png"), 'IMAGE')
        pcoll.load("my_icon_mixamo_add_on", os.path.join(my_icons_dir, ".mixamo_add_on.png"), 'IMAGE')
        pcoll.load("my_icon_ev_express", os.path.join(my_icons_dir, ".ev_express.png"), 'IMAGE')
        pcoll.load("my_icon_replica", os.path.join(my_icons_dir, ".replica.png"), 'IMAGE')
        pcoll.load("my_icon_local", os.path.join(my_icons_dir, ".local.png"), 'IMAGE') 
        pcoll.load("my_icon_delete", os.path.join(my_icons_dir, "delete.png"), 'IMAGE')   
        pcoll.load("my_icon_render", os.path.join(my_icons_dir, ".render.png"), 'IMAGE')   
        # pcoll.load("my_icon_blender", os.path.join(my_icons_dir, "blender.png"), 'IMAGE')  
        pcoll.load("my_icon_transform", os.path.join(my_icons_dir, "transform.png"), 'IMAGE')  
        pcoll.load("my_icon_white_left_arrow", os.path.join(my_icons_dir, "white_left_arrow.png"), 'IMAGE')  
        pcoll.load("my_icon_white_right_arrow", os.path.join(my_icons_dir, "white_right_arrow.png"), 'IMAGE')
        pcoll.load("my_icon_mouse_2", os.path.join(my_icons_dir, ".mouse_2.png"), 'IMAGE')
        pcoll.load("my_icon_light_bulb", os.path.join(my_icons_dir, ".light_bulb.png"), 'IMAGE')
        pcoll.load("my_icon_youtube", os.path.join(my_icons_dir, "youtube.png"), 'IMAGE')
        pcoll.load("my_icon_fast_button", os.path.join(my_icons_dir, "fast_button.png"), 'IMAGE')
        pcoll.load("my_icon_restart", os.path.join(my_icons_dir, "restart.png"), 'IMAGE')
        pcoll.load("my_icon_console", os.path.join(my_icons_dir, "console.png"), 'IMAGE')
        pcoll.load("my_icon_restart_no_save", os.path.join(my_icons_dir, "restart_no_save.png"), 'IMAGE')
        pcoll.load("my_icon_google", os.path.join(my_icons_dir, "google.png"), 'IMAGE')
        pcoll.load("my_icon_fiverr", os.path.join(my_icons_dir, "fiverr.png"), 'IMAGE')
        pcoll.load("my_icon_timeline", os.path.join(my_icons_dir, ".timeline.png"), 'IMAGE')
        pcoll.load("my_icon_tria_left_blue", os.path.join(my_icons_dir, "tria_left_blue.png"), 'IMAGE')
        pcoll.load("my_icon_tria_right_blue", os.path.join(my_icons_dir, "tria_right_blue.png"), 'IMAGE')
        pcoll.load("my_icon_frame_set_start", os.path.join(my_icons_dir, "frame_set_start.png"), 'IMAGE')
        pcoll.load("my_icon_frame_set_end", os.path.join(my_icons_dir, "frame_set_end.png"), 'IMAGE')
        pcoll.load("my_icon_show_active", os.path.join(my_icons_dir, "show_active.png"), 'IMAGE')
        pcoll.load("my_icon_autogpt_assistant", os.path.join(my_icons_dir, "autogpt_assistant.png"), 'IMAGE')
        pcoll.load("my_icon_python", os.path.join(my_icons_dir, "python.png"), 'IMAGE')
        pcoll.load("my_icon_face", os.path.join(my_icons_dir, "happiness.png"), 'IMAGE')
        pcoll.load("my_icon_auto_gpt_assistant", os.path.join(my_icons_dir, "auto_gpt_assistant.png"), 'IMAGE')
        pcoll.load("my_icon_auto_gpt_assistant_2", os.path.join(my_icons_dir, "auto_gpt_assistant_2.png"), 'IMAGE')
        pcoll.load("my_icon_auto_gpt_assistant_3", os.path.join(my_icons_dir, "auto_gpt_assistant_3.png"), 'IMAGE')
        pcoll.load("my_icon_auto_gpt_assistant_4", os.path.join(my_icons_dir, "auto_gpt_assistant_4.png"), 'IMAGE')
        pcoll.load("my_icon_letter_period", os.path.join(my_icons_dir, "letter_period.png"), 'IMAGE')
        pcoll.load("my_icon_letter_apostrophe", os.path.join(my_icons_dir, "letter_apostrophe.png"), 'IMAGE')
        pcoll.load("my_icon_letter_dash", os.path.join(my_icons_dir, "letter_dash.png"), 'IMAGE')
# icon_value=my_icon_face
# my_icon_face = get_icon_id("my_icon_face")

        # preview_collections["main"] = pcoll
        letters_and_numbers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        for letter_or_number in letters_and_numbers:
            # Check if the character is a letter and convert to lowercase, otherwise keep it as is
            if letter_or_number.isalpha():
                icon_name = f"write_letter_or_number_{letter_or_number.lower()}"
            else:
                icon_name = f"write_letter_or_number_{letter_or_number}"
            
            pcoll.load(icon_name, os.path.join(my_icons_dir, f"{icon_name}.png"), 'IMAGE')
        
        pcoll.load("letter_or_number_space", os.path.join(my_icons_dir, "letter_or_number_space.png"), 'IMAGE')
        
        preview_collections["main"] = pcoll
        

    except Exception as ex:
        print_color("AW", f"Error in load_icons:\n")
        capture_and_copy_traceback()



def unload_icons():

    for pcoll in preview_collections.values():
        try:
            bpy.utils.previews.remove(pcoll)
        except ResourceWarning as rw:
            pass  # Silently ignore the ResourceWarning
    preview_collections.clear()

def get_icon_id(icon_name):
    # Check if the icon exists in the collection and print a message if it does not
    icon = preview_collections["main"].get(icon_name)
    if icon is None:
        print(f"Icon not found: {icon_name}")
        return None

    return icon.icon_id
    


class FAST_OT_ReloadIcons(bpy.types.Operator):

    bl_idname = "fast.reload_icons"
    bl_label = "Reload Icons"
    bl_description = "Reloads FAST icons in case they're not displaying right due to Blender bug"

    @classmethod
    def description(cls, context, event):
        manager = bpy.context.preferences.addons[__name__].preferences.Prop
        if manager.verbose_tooltips:
            return ("Reloads FAST icons in case they're not displaying right due to Blender issue.\n\n"
                "You can also switch from one workspace and back to the original toggle icon reloading")
        else:
            return "Reloads FAST icons in case they're not displaying right due to Blender issue"
            
    def execute(self, context):

        
        try:
            unload_icons()  # Call your existing unload function
            load_icons()    # Call your existing load function
        except:
            pass

        return {'FINISHED'}
