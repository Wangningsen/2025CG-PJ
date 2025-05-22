import cadquery as cq
w0=cq.Workplane('YZ',origin=(34,0,0))
r=w0.sketch().rect(20,200).push([(-5,49)]).circle(4,mode='s').finalize().extrude(-68)