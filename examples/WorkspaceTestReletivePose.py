from libraries.vision.Workspace import Workspace

workspace = Workspace()


with open('workspace.json') as inputfile:
    workspace.from_json(inputfile.read())

position = workspace.get_pose(0.25, 0.25, 0.2)
print(position)
