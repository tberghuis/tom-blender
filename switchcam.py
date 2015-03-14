bl_info = {
	"name": "switch cam and change background image",
	"category": "Object",
}

import bpy

class ChangeBackgroundImage(bpy.types.Operator):
	"""switch cam and change background image"""
	bl_idname = "object.change_background_image"
	bl_label = "switch cam"	
	bl_options = {'REGISTER', 'UNDO'}  

	def execute(self, context):		
		scene = bpy.context.scene
		currentcam = bpy.context.scene.camera
		setcam = False

		for ob in scene.objects:
			if ob.type == 'CAMERA':
				if ob == currentcam:
					setcam = True
				elif setcam:
					bpy.context.scene.camera = ob
					break

		if currentcam == bpy.context.scene.camera:		
			for ob in scene.objects:
				if ob.type == 'CAMERA':
					bpy.context.scene.camera = ob
					break

		for area in bpy.context.screen.areas:
			if area.type == 'VIEW_3D':
				space_data = area.spaces.active
				for i, bg in enumerate(space_data.background_images):
					if bg.image.name == bpy.context.scene.camera.name:
						bg.show_background_image = True
					else:
						bg.show_background_image = False

		return {'FINISHED'}			

def register():
	bpy.utils.register_class(ChangeBackgroundImage)


def unregister():
	bpy.utils.unregister_class(ChangeBackgroundImage)

if __name__ == "__main__":
	register()		