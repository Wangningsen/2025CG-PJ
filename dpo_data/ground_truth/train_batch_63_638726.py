import cadquery as cq
w0=cq.Workplane('YZ',origin=(-93,0,0))
r=w0.sketch().circle(100).rect(32,100,mode='s').finalize().extrude(187)