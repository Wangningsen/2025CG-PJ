import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.sketch().segment((54,-84),(54,-33)).segment((94,-33)).arc((100,5),(90,43)).arc((86,67),(63,78)).arc((-100,6),(54,-84)).assemble().finalize().extrude(31)