from libraries.vision.Workspace import Workspace

workspace = Workspace()



with open('workspace.json') as inputfile:
    workspace.from_json(inputfile.read())

position, q = workspace.get_pose(50, 50, 0)
print(position)
print(q)