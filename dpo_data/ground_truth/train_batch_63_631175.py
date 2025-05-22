import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().rect(100,154).push([(0,0.5)]).rect(64,45,mode='s').finalize().extrude(-200)