# Node Split

- Node name : 'Split'
- bl_idname : [CompositorNodeSplit](https://docs.blender.org/api/current/bpy.types.CompositorNodeSplit.html)


``` python
Split(image=None, image_1=None, axis='X', factor=50, tag_need_exec=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- image : None
- image_1 : None
- axis : 'X'
- factor : 50
- tag_need_exec : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, image=None, image_1=None, axis='X', factor=50, tag_need_exec=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'CompositorNodeSplit', node_label=node_label, node_color=node_color, **kwargs)

    self.axis            = axis
    self.factor          = factor
    self.tag_need_exec   = tag_need_exec
    self.image           = image
    self.image_1         = image_1
```
