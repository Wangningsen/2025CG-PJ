import cadquery as cq
w0=cq.Workplane('YZ',origin=(-36,0,0))
r=w0.sketch().rect(122,200).push([(1,0)]).circle(14,mode='s').finalize().extrude(73)