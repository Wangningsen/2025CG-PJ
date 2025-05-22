import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().circle(29).push([(-3,12.5)]).rect(32,17,mode='s').finalize().extrude(200)