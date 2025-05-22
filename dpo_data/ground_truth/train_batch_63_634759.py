import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
w1=cq.Workplane('YZ',origin=(21,0,0))
r=w0.sketch().segment((-4,85),(16,49)).arc((9,68),(-4,85)).assemble().finalize().extrude(13).union(w0.sketch().push([(-51,35)]).rect(6,130).push([(-53,18)]).rect(2,2,mode='s').finalize().extrude(15)).union(w1.sketch().arc((51,-100),(54,-81),(51,-62)).close().assemble().finalize().extrude(-26))