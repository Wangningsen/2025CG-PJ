import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().segment((31,-33),(59,-100)).segment((99,-83)).segment((55,21)).arc((-93,53),(31,-33)).assemble().finalize().extrude(25)