import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().rect(126,172).push([(-16.5,10.5)]).rect(77,59,mode='s').finalize().extrude(200)