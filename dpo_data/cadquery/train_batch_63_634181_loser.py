import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().rect(68,196).push([(-8.5,0)]).rect(49,26,mode='s').finalize().extrude(200)