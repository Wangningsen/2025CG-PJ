import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().circle(81).push([(47,48)]).circle(4,mode='s').finalize().extrude(200)