

import bpy

# note:
# keymaps stored in lists as [(km, kmi), (km, kmi)]

# all addon keymaps
addon_keymaps = []

# keymap lists
fastmenu_keymaps = []
# Global flag to track if the print statement has already been executed
printed_once = False

def disable_default_kmi(km=None, idname=None, retries=10):
    global printed_once  # Declare the flag as global to modify it inside the function
    wm = bpy.context.window_manager

    if not (km and idname) or retries < 1:
        return
    
    # Print statement only the first time
    if not printed_once:
        
        printed_once = True  # Set the flag to True after printing
    
    # The default keyconfig
    kc = wm.keyconfigs['Blender']
    for kmi in kc.keymaps[km].keymap_items:
        if kmi.idname == idname:
            # Only disable if the type is not MEDIA_PLAY or MEDIA_STOP
            if kmi.type not in ['MEDIA_PLAY', 'MEDIA_STOP']:
                kmi.active = False
             
    # Add some delay for retries
    bpy.app.timers.register(
        lambda: disable_default_kmi(km, idname, retries - 1),
        first_interval=5.1)


disable_default_kmi('Frames', 'screen.animation_play')



# startup keymaps only
# likely want keymaps in preferences for all features, even if disabled at startup
def initialise_keymaps(context):
    wm = context.window_manager
    kc = wm.keyconfigs.addon

    # register keymaps
    km = kc.keymaps.new(name='Object Mode', space_type='EMPTY', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km,kmi))

    # Register keymap for Edit Mesh Mode
    km = kc.keymaps.new(name='Mesh', space_type='EMPTY', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km, kmi))

    # Register keymap for Edit Curve Mode
    km = kc.keymaps.new(name='Curve', space_type='EMPTY', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km, kmi))

    # Register keymap for Edit Armature Mode
    km = kc.keymaps.new(name='Armature', space_type='EMPTY', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km, kmi))

    # Register keymap for Edit Metaball Mode
    km = kc.keymaps.new(name='Metaball', space_type='EMPTY', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km, kmi))

    # Register keymap for Edit Surface Mode
    km = kc.keymaps.new(name='Surface', space_type='EMPTY', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km, kmi))

    # Register keymap for Edit Lattice Mode
    km = kc.keymaps.new(name='Lattice', space_type='EMPTY', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km, kmi))
    
    km = kc.keymaps.new(name='Pose', space_type='EMPTY', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km,kmi))

    km = kc.keymaps.new(name='Sculpt', space_type='EMPTY', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km,kmi))

    km = kc.keymaps.new(name='Dopesheet', space_type='DOPESHEET_EDITOR', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km,kmi))

    # Keymap for playing timeline forward (space)
    kmi = km.keymap_items.new('fast.play_timeline_forward', 'SPACE', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    
    # Keymap for playing timeline reverse (SHIFT + CTRL + SPACE)
    kmi = km.keymap_items.new('fast.play_timeline_reverse', 'SPACE', 'PRESS', ctrl=True, shift=True)
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new("fast.toggle_frame_restore", 'F', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))

    km = kc.keymaps.new(name='Outliner', space_type='OUTLINER', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km,kmi))
 
    km = kc.keymaps.new(name='Text', space_type='TEXT_EDITOR', region_type='WINDOW')   
    
    kmi = km.keymap_items.new('fast.text_print', 'P', 'PRESS', ctrl=True, shift=False)
    addon_keymaps.append((km, kmi))
    
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km,kmi))

    km = kc.keymaps.new(name='Sequencer', space_type='SEQUENCE_EDITOR', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km,kmi))
    
    # Keymap for playing timeline forward (space)
    kmi = km.keymap_items.new('fast.play_timeline_forward', 'SPACE', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    
    # Keymap for playing timeline reverse (SHIFT + CTRL + SPACE)
    kmi = km.keymap_items.new('fast.play_timeline_reverse', 'SPACE', 'PRESS', ctrl=True, shift=True)
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new("fast.toggle_frame_restore", 'F', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))

    km = kc.keymaps.new(name='Graph Editor', space_type='GRAPH_EDITOR', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km,kmi))

    # Keymap for playing timeline forward (space)
    kmi = km.keymap_items.new('fast.play_timeline_forward', 'SPACE', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    
    # Keymap for playing timeline reverse (SHIFT + CTRL + SPACE)
    kmi = km.keymap_items.new('fast.play_timeline_reverse', 'SPACE', 'PRESS', ctrl=True, shift=True)
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new("fast.toggle_frame_restore", 'F', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))

    km = kc.keymaps.new(name='NLA Editor', space_type='NLA_EDITOR', region_type='WINDOW')

    # Keymap for playing timeline forward (space)
    kmi = km.keymap_items.new('fast.play_timeline_forward', 'SPACE', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    
    # Keymap for playing timeline reverse (SHIFT + CTRL + SPACE)
    kmi = km.keymap_items.new('fast.play_timeline_reverse', 'SPACE', 'PRESS', ctrl=True, shift=True)
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new("fast.toggle_frame_restore", 'F', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))

    km = kc.keymaps.new(name='Node Editor', space_type='NODE_EDITOR', region_type='WINDOW')
    kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
    fastmenu_keymaps.append((km,kmi))

    kmi = km.keymap_items.new("fast.toggle_frame_restore", 'F', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    
    km = kc.keymaps.new(name='Property Editor', space_type='PROPERTIES', region_type='WINDOW')
    
    # Keymap for playing timeline forward (space)
    kmi = km.keymap_items.new('fast.play_timeline_forward', 'SPACE', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    
    # Keymap for playing timeline reverse (SHIFT + CTRL + SPACE)
    kmi = km.keymap_items.new('fast.play_timeline_reverse', 'SPACE', 'PRESS', ctrl=True, shift=True)
    addon_keymaps.append((km, kmi))
    
    # Keymap for toggling frame restore
    kmi = km.keymap_items.new("fast.toggle_frame_restore", 'F', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D', region_type='WINDOW')
    
    # Keymap for playing timeline forward (space)
    kmi = km.keymap_items.new('fast.play_timeline_forward', 'SPACE', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    
    # Keymap for playing timeline reverse (SHIFT + CTRL + SPACE)
    kmi = km.keymap_items.new('fast.play_timeline_reverse', 'SPACE', 'PRESS', ctrl=True, shift=True)
    addon_keymaps.append((km, kmi))
    
    # Keymap for toggling frame restore
    kmi = km.keymap_items.new("fast.toggle_frame_restore", 'F', 'PRESS', ctrl=False, shift=False)
    addon_keymaps.append((km, kmi))
    
    for km, kmi in fastmenu_keymaps:
        addon_keymaps.append((km, kmi))

# import bpy
# import os
# from .fast_global import *
# from . import __name__, __package__
# from.fast_properties import FAST_Properties , theme_Properties
# from bpy.props import StringProperty, CollectionProperty
# #I used my own Android naming convention instead of, 
# #"layout" for the variables so is easier to organize.
# preferences = FAST_Properties()

# # Access the manager variable
# manager = preferences.Prop


# # note:
# # keymaps stored in lists as [(km, kmi), (km, kmi)]

# # all addon keymaps
# addon_keymaps = []

# # keymap lists
# fastmenu_keymaps = []


# # custom_menu_name = "OBJECT_MT_fast_menu"

# # startup keymaps only
# # likely want keymaps in preferences for all features, even if disabled at startup
# def initialise_keymaps(context):
#     wm = context.window_manager
#     kc = wm.keyconfigs.addon
#     manager = context.preferences.addons[__name__].preferences.Prop
#     # register keymaps
#     if manager.fast_menu_prop_om:    
#         km = kc.keymaps.new(name='Object Mode', space_type='EMPTY', region_type='WINDOW')
#         kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
#         fastmenu_keymaps.append((km,kmi))
#     if manager.fast_menu_prop_m:    
#         km = kc.keymaps.new(name='Mesh', space_type='EMPTY', region_type='WINDOW')
#         kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
#         fastmenu_keymaps.append((km,kmi))
#     if manager.fast_menu_prop_p:    
#         km = kc.keymaps.new(name='Pose', space_type='EMPTY', region_type='WINDOW')
#         kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
#         fastmenu_keymaps.append((km,kmi))
#     if manager.fast_menu_prop_ds:    
#         km = kc.keymaps.new(name='Dopesheet', space_type='DOPESHEET_EDITOR', region_type='WINDOW')
#         kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
#         fastmenu_keymaps.append((km,kmi))
#     if manager.fast_menu_prop_o:    
#         km = kc.keymaps.new(name='Outliner', space_type='OUTLINER', region_type='WINDOW')
#         kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
#         fastmenu_keymaps.append((km,kmi))
#     if manager.fast_menu_prop_te:    
#         km = kc.keymaps.new(name='Text', space_type='TEXT_EDITOR', region_type='WINDOW')
#         kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
#         fastmenu_keymaps.append((km,kmi))
#     if manager.fast_menu_prop_s:    
#         km = kc.keymaps.new(name='Sequencer', space_type='SEQUENCE_EDITOR', region_type='WINDOW')
#         kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
#         fastmenu_keymaps.append((km,kmi))
#     if manager.fast_menu_prop_ge:        
#         km = kc.keymaps.new(name='Graph Editor', space_type='GRAPH_EDITOR', region_type='WINDOW')
#         kmi = km.keymap_items.new("fast.fast_menu", 'RIGHTMOUSE', 'PRESS')
#         fastmenu_keymaps.append((km,kmi))

#     for km, kmi in fastmenu_keymaps:
#         addon_keymaps.append((km, kmi))        



###########################################################################
# API REFERENCE

### space types ###
'''
'EMPTY', 
'VIEW_3D', 
'IMAGE_EDITOR', 
'NODE_EDITOR', 
'SEQUENCE_EDITOR', 
'CLIP_EDITOR', 
'DOPESHEET_EDITOR', 
'GRAPH_EDITOR', 
'NLA_EDITOR', 
'TEXT_EDITOR', 
'CONSOLE', 
'INFO', 
'TOPBAR', 
'STATUSBAR', 
'OUTLINER', 
'PROPERTIES', 
'FILE_BROWSER', 
'SPREADSHEET', 
'PREFERENCES'
'''

### region types ###
'''
('WINDOW', 
'HEADER', 
'CHANNELS', 
'TEMPORARY', 
'UI', 
'TOOLS', 
'TOOL_PROPS', 
'PREVIEW', 
'HUD', 
'NAVIGATION_BAR', 
'EXECUTE', 
'FOOTER', 
'TOOL_HEADER', 
'XR')
'''


###################################################################################















# keymap functions

# returns the keydefs you want
# def get_keys(keymap_owner_key):
#     keylists = []
#     keylists.append(keydefs[keymap_owner_key])
#     return keylists

# # creates and registers a keymap based on given keydefs provided
# def register_keymaps(keylists):
#     wm = bpy.context.window_manager
#     kc = wm.keyconfigs.addon
#     keymaps = []

#     for keylist in keylists:
#         for item in keylist:
#             keymap = item.get("keymap")
#             space_type = item.get("space_type", "EMPTY")
#             region_type = item.get("region_type", "WINDOW")

#             if keymap:
#                 km = kc.keymaps.new(name=keymap, space_type=space_type, region_type=region_type)
#                 # print('keymap, space_type, region_type: ', keymap, space_type, region_type)

#                 if km:
#                     idname = item.get("idname")
#                     type = item.get("type")
#                     value = item.get("value")
#                     # print('idname, type, value: ', idname, type, value)
#                     shift = item.get("shift", False)
#                     ctrl = item.get("ctrl", False)
#                     alt = item.get("alt", False)
#                     oskey = item.get("oskey", False)

#                     kmi = km.keymap_items.new(idname, type, value, shift=shift, ctrl=ctrl, alt=alt, oskey=oskey)

#                     if kmi:
#                         properties = item.get("properties")

#                         if properties:
#                             for name, value in properties:
#                                 setattr(kmi.properties, name, value)
#                         # print("keymaps.append:", km, kmi)

#                         keymaps.append((km, kmi))
#     return keymaps

# def unregister_keymaps(keymaps):
#     for km, kmi in keymaps:
#         #print('deregistering keymap...')
#         km.keymap_items.remove(kmi)





# define keymaps here
# keydefs = {
#     "FastMenu": []
# }

# fast_menu_keydefs = [{
#     "label": "Object Fast Menu",                 # name of keymap in blender keymap preferences
#     "region_type": "WINDOW",                      # default is WINDOW 
#     "map_type": "MOUSE",                          # KEYBOARD, MOUSE
#     "keymap": "Object Mode",                      # Mesh, Object Mode, etc.
#     "idname": "fast.fast_menu",                    # operator_id to call on input event
#     "type": "RIGHTMOUSE",                         # QUOTE, RIGHTMOUSE, etc
#     "ctrl": False, 
#     "alt": False, 
#     "shift": False,                               # combination keys
#     "oskey": False,                                                
#     "value": "PRESS"
#     }]

# keydefs['FastMenu'] = fast_menu_keydefs




# # object
#                 {"label": "Object Fast Menu",                 # name of keymap in blender keymap preferences
#                 "region_type": "WINDOW",                      # default is WINDOW 
#                 "map_type": "MOUSE",                          # KEYBOARD, MOUSE
#                 "keymap": "Object Mode",                      # Mesh, Object Mode, etc.
#                 "idname": "fast.fast_menu",                    # operator_id to call on input event
#                 "type": "RIGHTMOUSE",                         # QUOTE, RIGHTMOUSE, etc
#                 "ctrl": False, 
#                 "alt": False, 
#                 "shift": False,                               # combination keys
#                 "oskey": False,                                                
#                 "value": "PRESS"
#                 },
#                 # mesh
#                 {"label": "Mesh Fast Menu",                   
#                 "region_type": "WINDOW",                      
#                 "map_type": "MOUSE",                          
#                 "keymap": "Mesh",                             
#                 "idname": "fast.fast_menu",                   
#                 "type": "RIGHTMOUSE",                         
#                 "ctrl": False, "alt": False, "shift": False,  
#                 "oskey": False,                                                
#                 "value": "PRESS"
#                 },
#                 # dopesheet
#                 {"label": "Dopesheet Fast Menu",              
#                 "region_type": "WINDOW",                      
#                 "space_type": "DOPESHEET_EDITOR",             
#                 "map_type": "MOUSE",                          
#                 "keymap": "Dopesheet",                        
#                 "idname": "fast.fast_menu",                    
#                 "type": "RIGHTMOUSE",                         
#                 "ctrl": False, "alt": False, "shift": False,  
#                 "oskey": False,                                                
#                 "value": "PRESS"
#                 },
#                 # outliner
#                 {"label": "Outliner Fast Menu",               
#                 "region_type": "WINDOW",                      
#                 "space_type": "OUTLINER",                     
#                 "map_type": "MOUSE",                          
#                 "keymap": "Outliner",                        
#                 "idname": "fast.fast_menu",                    
#                 "type": "RIGHTMOUSE",                         
#                 "ctrl": False, "alt": False, "shift": False,
#                 "oskey": False,                                                
#                 "value": "PRESS"
#                 },
#                 # text editor
#                 {"label": "Text Fast Menu",               
#                 "region_type": "WINDOW",                      
#                 "space_type": "TEXT_EDITOR",                     
#                 "map_type": "MOUSE",                          
#                 "keymap": "Text",                        
#                 "idname": "fast.fast_menu",                    
#                 "type": "RIGHTMOUSE",                         
#                 "ctrl": False, "alt": False, "shift": False,
#                 "oskey": False,                                                
#                 "value": "PRESS"
#                 }