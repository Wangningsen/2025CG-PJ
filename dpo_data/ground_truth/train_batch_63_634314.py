import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-46,0))
r=w0.sketch().push([(-68.5,33.5)]).rect(63,93).push([(-68,34)]).circle(17,mode='s').reset().face(w0.sketch().arc((98,-36),(33,-52),(99,-40)).arc((95,-39),(98,-36)).assemble()).finalize().extrude(92)