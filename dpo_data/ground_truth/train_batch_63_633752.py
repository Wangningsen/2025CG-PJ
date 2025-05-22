import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-54,-12),(-45,-12)).segment((-45,-8)).segment((45,-8)).segment((45,-12)).segment((54,-12)).arc((0,12),(-54,-12)).assemble().finalize().extrude(200)