import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-7))
r=w0.sketch().push([(-45,50)]).circle(50).push([(-33,-49)]).circle(51).push([(-33,-49.5)]).rect(74,67,mode='s').finalize().extrude(-22).union(w0.sketch().arc((51,-46),(91,-35),(79,5)).arc((22,3),(51,-46)).assemble().finalize().extrude(36))