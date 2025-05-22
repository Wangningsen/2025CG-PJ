import cadquery as cq
w0=cq.Workplane('YZ',origin=(15,0,0))
r=w0.sketch().segment((54,-84),(54,-33)).segment((95,-33)).arc((100,2),(90,37)).arc((86,66),(60,79)).arc((-100,3),(54,-84)).assemble().finalize().extrude(-30)