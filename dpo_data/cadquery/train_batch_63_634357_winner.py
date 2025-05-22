import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().circle(72).reset().face(w0.sketch().segment((-39,49),(-14,11)).arc((-14,-12),(7,-21)).segment((32,-60)).segment((39,-55)).segment((14,-16)).arc((14,13),(-7,19)).segment((-32,59)).close().assemble(),mode='s').finalize().extrude(-200)