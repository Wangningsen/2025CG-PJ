import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.sketch().arc((15,9),(-13,-4),(16,4)).arc((13,6),(15,9)).assemble().push([(-2,-3)]).circle(7,mode='s').finalize().extrude(-92).union(w0.sketch().circle(74).push([(-18.5,58.5)]).rect(33,23,mode='s').finalize().extrude(108))