import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().circle(55).push([(-45,17)]).circle(8,mode='s').finalize().extrude(200)