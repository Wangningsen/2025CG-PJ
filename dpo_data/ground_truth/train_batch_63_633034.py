import cadquery as cq
w0=cq.Workplane('YZ',origin=(56,0,0))
r=w0.sketch().rect(200,198).push([(-1,0)]).rect(94,198,mode='s').finalize().extrude(-112)