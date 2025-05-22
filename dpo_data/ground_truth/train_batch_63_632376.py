import cadquery as cq
w0=cq.Workplane('YZ',origin=(-12,0,0))
w1=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.sketch().push([(-41,45)]).circle(11).push([(48,-4)]).circle(52).push([(48,-3.5)]).rect(18,87,mode='s').finalize().extrude(35).union(w1.sketch().arc((49,-23),(51,-23),(54,-22)).arc((51,-20),(49,-18)).close().assemble().finalize().extrude(-75))