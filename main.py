import tkinter
import os
# Data

WINDOW_HEIGHT = 64*16
WINDOW_WIDTH = 64*24

WINDOW_NAME = "Plyformer"

ASSETS_FOLDER = os.getcwd() + "\\Assets"

# Images

IMAGES_CLOUD1 = f'{ASSETS_FOLDER}\\CLOUD1.png'
IMAGES_CLOUD2 = f'{ASSETS_FOLDER}\\CLOUD2.png'
IMAGES_CLOUD3 = f'{ASSETS_FOLDER}\\CLOUD3.png'
IMAGES_GROUND_FILL = f'{ASSETS_FOLDER}\\GROUND_FILL.png'
IMAGES_GROUND = f'{ASSETS_FOLDER}\\GROUND.png'
IMAGES_SKY_FILL = f'{ASSETS_FOLDER}\\SKY_FILL.png'

# Window

root = tkinter.Tk()
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.title = WINDOW_NAME
#:?  root.resizable = False

# Scene (Generalized Form: 24x12)

Current_Scene = [
    ["c1", "c2", "c3", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
    ["c3", "c2", "c1", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
    ["c3", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,],
]

# Renderer
def renderScene(scene):
        window = root
        for imageRow in scene:
            for value in imageRow:

                xPos = imageRow.index(value) #* 128 # Pixel Offset
                yPos = scene.index(imageRow) #* 128 # Pixel Offset

                placedImg = None

                if value == "c1":
                    placedImg = tkinter.PhotoImage(file=IMAGES_CLOUD1)
                    widget = tkinter.Label(window, image=placedImg)
                    widget.grid(row=yPos, column=xPos)
                    print(f'Success Rendering Image: {value} at ({xPos},{yPos} offsets.)')

                elif value == "c2":
                    placedImg = tkinter.PhotoImage(file=IMAGES_CLOUD2)
                    widget = tkinter.Label(window, image=placedImg)
                    widget.grid(row=yPos, column=xPos)
                    print(f'Success Rendering Image: {value} at ({xPos}, {yPos} offsets).')

                elif value == "c3":
                    placedImg = tkinter.PhotoImage(file=IMAGES_CLOUD3)
                    widget = tkinter.Label(window, image=placedImg)
                    widget.grid(row=yPos, column=xPos)
                    print(f'Success Rendering Image: {value} at ({xPos}, {yPos} offsets).')

                elif value == "gf":
                    placedImg = tkinter.PhotoImage(file=IMAGES_GROUND_FILL)
                    widget = tkinter.Label(window, image=placedImg)
                    widget.grid(row=yPos, column=xPos)
                    print(f'Success Rendering Image: {value} at ({xPos}, {yPos} offsets).')
                elif value == "gn":
                    placedImg = tkinter.PhotoImage(file=IMAGES_GROUND)
                    widget = tkinter.Label(window, image=placedImg)
                    widget.grid(row=yPos, column=xPos)
                    print(f'Success Rendering Image: {value} at ({xPos}, {yPos} offsets).')

                elif value == "sf":
                    placedImg = tkinter.PhotoImage(file=IMAGES_SKY_FILL)
                    widget = tkinter.Label(window, image=placedImg)
                    widget.grid(row=yPos, column=xPos)
                    print(f'Success Rendering Image: {value} at ({xPos}, {yPos} offsets).')

                else:
                    continue#print(f"ImageError: Renderer could not find specified image. ImageName: \"{value}\"")

#image = tkinter.PhotoImage(file=IMAGES_GROUND_FILL)
#w = tkinter.Label(root, image=image)

#w.grid(row=0, column=0)
renderScene(scene=Current_Scene)
placedImg = tkinter.PhotoImage(file=IMAGES_CLOUD1)
widget = tkinter.Label(root, image=placedImg)
widget.grid(row=1, column=2)
placedImg = tkinter.PhotoImage(file=IMAGES_CLOUD1)
widget = tkinter.Label(root, image=placedImg)
widget.grid(row=0, column=1)
root.mainloop()
