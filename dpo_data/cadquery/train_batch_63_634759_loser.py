import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
w1=cq.Workplane('YZ',origin=(-21,0,0))
r=w0.sketch().arc((-4,85),(6,67),(15,48)).arc((10,67),(-4,85)).assemble().finalize().extrude(-15).union(w0.sketch().arc((51,-100),(54,-81),(51,-62)).close().assemble().finalize().extrude(27)).union(w1.sketch().push([(-51,35)]).rect(6,130).push([(-52,16)]).rect(2,4,mode='s').finalize().extrude(15))