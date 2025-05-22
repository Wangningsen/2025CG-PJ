import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,59))
r=w0.sketch().circle(100).push([(-89,-30)]).circle(3,mode='s').push([(-3,4)]).circle(48,mode='s').finalize().extrude(-118)