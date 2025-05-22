import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,46,0))
w1=cq.Workplane('ZX',origin=(0,34,0))
r=w0.sketch().segment((37,-7),(41,-7)).segment((41,-2)).arc((100,46),(64,93)).segment((65,99)).segment((61,100)).segment((60,94)).arc((4,59),(37,1)).close().assemble().finalize().extrude(-92).union(w0.workplane(offset=-46/2).moveTo(-48.5,18).box(103,68,46)).union(w1.sketch().push([(-46,-44.5)]).rect(52,111).push([(-36.5,-25)]).rect(7,4,mode='s').finalize().extrude(-50))